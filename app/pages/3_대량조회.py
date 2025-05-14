import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# import sklearn
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier

st.title("📦 대량 이탈 예측 (사전 정의 파일 사용)")

# 1. 모델 불러오기
@st.cache_resource
def load_model():
    return joblib.load("../../notebooks/test/log_reg.pkl")

model = load_model()

# 2. CSV 파일 경로 직접 지정
csv_path = "../../notebooks/test/data/datasets.csv"

if not os.path.exists(csv_path):
    st.error(f"❌ 파일이 존재하지 않습니다: {csv_path}")
else:
    # 3. 파일 읽기
    df = pd.read_csv(csv_path)
    st.write("✅ 입력 데이터 미리보기", df.head())

    # 4. 예측 수행
    try:
        X = df.copy()
        y_prob = model.predict_proba(X)[:, 1]

        df["이탈 확률 (%)"] = (y_prob * 100).round(2)
        df["예측 결과"] = np.where(y_prob >= 0.5, "이탈 가능성 ↑", "잔류 가능성 ↑")

        st.success("✅ 예측 완료!")
        st.dataframe(df[["이탈 확률 (%)", "예측 결과"] + list(df.columns.difference(["이탈 확률 (%)", "예측 결과"]))])

        # 5. 다운로드
        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button("📥 예측 결과 다운로드", data=csv, file_name="predicted_attrition.csv", mime="text/csv")

    except Exception as e:
        st.error(f"❌ 예측 중 오류 발생: {e}")