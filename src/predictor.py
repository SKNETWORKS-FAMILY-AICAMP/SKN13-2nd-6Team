# 여기에 예측 모델 사용 method 작성
import shap
import pickle
import numpy as np
import pandas as pd

model_path = 'models/xgb.pkl'
feature_columns = [
    'Age', 'BusinessTravel', 'Department', 'Education',
    'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel', 'JobRole',
    'JobSatisfaction', 'MaritalStatus', 'NumCompaniesWorked', 'OverTime',
    'RelationshipSatisfaction', 'StockOptionLevel', 'WorkLifeBalance'
]

def prediction(*args):
    # 1. Load prediction model
    with open(model_path,'wb') as f:
        model = pickle.load(f)

    # 2. Predict stage
    X = pd.DataFrame(*args)
    y_proba = model.predict_proba(X)[:, 1]  # Yes일 확률

    # 3. SHAP값 계산
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    # 4. feature별 영향 정리
    shap_importance = pd.DataFrame({
        'Feature': feature_columns,
        'SHAP_Value': shap_values[0]
    }).sort_values(by='SHAP_Value', key=abs, ascending=False)

    # 5. Top 5 영향 피처 추출
    top5_features = shap_importance.head(5)['Feature'].tolist()

    return {
        "probability": float(y_proba),
        "shap_values": shap_importance.head(5).to_dict(orient='records'),
        "top5_features": top5_features
    }