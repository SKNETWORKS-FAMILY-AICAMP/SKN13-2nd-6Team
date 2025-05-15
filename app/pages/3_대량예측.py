# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import os
# from streamlit_extras.switch_page_button import switch_page

# # import sklearn
# # from sklearn.linear_model import LogisticRegression
# # from sklearn.ensemble import RandomForestClassifier

# st.title("📦 대량 이탈 예측 (사전 정의 파일 사용)")

# # 1. 모델 불러오기
# @st.cache_resource
# def load_model():
#     return joblib.load("../notebooks/test/log_reg.pkl")

# model = load_model()

# # 2. CSV 파일 경로 직접 지정
# csv_path = "../notebooks/test/data/datasets.csv"

# if not os.path.exists(csv_path):
#     st.error(f"❌ 파일이 존재하지 않습니다: {csv_path}")
# else:
#     # 3. 파일 읽기
#     df = pd.read_csv(csv_path)
#     st.write("✅ 입력 데이터 미리보기", df.head())

#     # 4. 예측 수행
#     try:
#         X = df.copy()
#         y_prob = model.predict_proba(X)[:, 1]

#         df["이탈 확률 (%)"] = (y_prob * 100).round(2)
#         df["예측 결과"] = np.where(y_prob >= 0.5, "이탈 가능성 ↑", "잔류 가능성 ↑")

#         st.success("✅ 예측 완료!")
#         st.dataframe(df[["이탈 확률 (%)", "예측 결과"] + list(df.columns.difference(["이탈 확률 (%)", "예측 결과"]))])

#         # 5. 다운로드
#         csv = df.to_csv(index=False).encode("utf-8-sig")
#         st.download_button("📥 예측 결과 다운로드", data=csv, file_name="predicted_attrition.csv", mime="text/csv")

#     except Exception as e:
#         st.error(f"❌ 예측 중 오류 발생: {e}")


# import streamlit as st
# import joblib
# import pandas as pd
# import numpy as np


# bundle = joblib.load("../notebooks/test/xgb.pkl")

# st.write("📦 모델 내용:")
# st.write(type(bundle))
# if isinstance(bundle, dict):
#     st.write("🔑 포함된 키:", list(bundle.keys()))



# st.title("📦 대량 이탈 예측")

# @st.cache_resource
# def load_model():
#     return joblib.load("../notebooks/test/xgb.pkl")

# @st.cache_resource
# def load_features():
#     return joblib.load("../notebooks/test/preprocessed_columns.pkl")

# # 모델 및 feature 목록 로딩
# model = load_model()
# feature_columns = load_features()

# def categorize(prob):
#     if prob >= 0.7:
#         return "High"
#     elif prob >= 0.3:
#         return "Medium"
#     else:
#         return "Low"

# batch_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

# if batch_file is not None:
#     df = pd.read_csv(batch_file)
#     st.subheader("📋 입력 데이터 미리보기")
#     st.dataframe(df.head())

#     # 전처리: 누락된 feature 채우고 정렬
#     for col in feature_columns:
#         if col not in df.columns:
#             df[col] = 0
#     X = df[feature_columns]

#     # 예측
#     pred_proba = model.predict_proba(X)[:, 1]
#     pred = (pred_proba >= 0.5).astype(int)

#     # 결과 병합
#     df["Prob_Yes"] = np.round(pred_proba, 4)
#     df["Pred"] = np.where(pred == 1, "이탈", "잔류")
#     df["Grade"] = [categorize(p) for p in pred_proba]

#     # 결과 출력
#     st.subheader("✅ 예측 결과 (상위 5개)")
#     st.dataframe(df[["Prob_Yes", "Pred", "Grade"]].head())

#     # 다운로드
#     csv = df.to_csv(index=False).encode("utf-8-sig")
#     st.download_button("📥 결과 다운로드", data=csv, file_name="prediction_result.csv", mime="text/csv")


# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import os

# st.title("📦 대량 이탈 예측 (전처리 완료된 CSV 사용)")

# @st.cache_resource
# def load_model():
#     return joblib.load("../notebooks/test/xgb.pkl")

# @st.cache_resource
# def load_feature_list():
#     return joblib.load("../notebooks/test/preprocessed_columns.pkl")

# model = load_model()
# feature_columns = load_feature_list()

# # 전처리 완료된 CSV 파일 경로
# csv_path = "../data/processed_datasets.csv"

# if not os.path.exists(csv_path):
#     st.error(f"❌ 파일이 존재하지 않습니다: {csv_path}")
# else:
#     df = pd.read_csv(csv_path)
#     st.write("✅ 입력 데이터 (전처리 완료)", df.head())

#     try:
#         # 누락 컬럼 채우기
#         for col in feature_columns:
#             if col not in df.columns:
#                 df[col] = 0
#         X = df[feature_columns]

#         # 예측
#         prob = model.predict_proba(X)[:, 1]
#         pred = (prob >= 0.5).astype(int)

#         def categorize(p):
#             if p >= 0.7: return "High"
#             elif p >= 0.3: return "Medium"
#             return "Low"

#         df["Prob_Yes"] = np.round(prob, 4)
#         df["Pred"] = np.where(pred == 1, "이탈", "잔류")
#         df["Grade"] = [categorize(p) for p in prob]


#         # 5. 이탈 확률 높은 순으로 정렬
#         df_sorted = df.sort_values(by="Prob_Yes", ascending=False)

#         # 결과 표시
#         st.subheader("🔍 예측 결과 (이탈 확률 높은 순 상위 20개)")
#         st.dataframe(df_sorted.head(1000)[feature_columns + ["Prob_Yes", "Pred", "Grade"]])
        

#         # 다운로드
#         csv = df.to_csv(index=False).encode("utf-8-sig")
#         st.download_button("📥 결과 다운로드", data=csv, file_name="predicted_attrition.csv", mime="text/csv")

#     except Exception as e:
#         st.error(f"❌ 예측 중 오류 발생: {e}")


import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.title("📦 대량 이탈 예측 (전처리 완료된 CSV 사용)")

# 1. 모델 및 feature 목록 불러오기
@st.cache_resource
def load_model():
    return joblib.load("../notebooks/test/xgb.pkl")

@st.cache_resource
def load_feature_list():
    return joblib.load("../notebooks/test/preprocessed_columns.pkl")

model = load_model()
feature_columns = load_feature_list()

# 2. CSV 파일 경로
csv_path = "../data/processed_datasets.csv"

if not os.path.exists(csv_path):
    st.error(f"❌ 파일이 존재하지 않습니다: {csv_path}")
else:
    # 전처리 전 원본 데이터 로드
    df_raw = pd.read_csv("../data/datasets.csv")
    st.write("✅ 입력 데이터 (원본)", df_raw.head())

    try:
        # 전처리 (예측용 feature 데이터 생성)
        df = df_raw.copy()
        for col in feature_columns:
            if col not in df.columns:
                df[col] = 0
        X = df[feature_columns]

        # 예측
        prob = model.predict_proba(X)[:, 1]
        pred = (prob >= 0.5).astype(int)

        def categorize(p):
            if p >= 0.7: return "High"
            elif p >= 0.3: return "Medium"
            return "Low"

        # 원본 데이터에 결과 추가
        df_raw["Prob_Yes"] = np.round(prob, 4)
        df_raw["Pred"] = np.where(pred == 1, "이탈", "잔류")
        df_raw["Grade"] = [categorize(p) for p in prob]

        # 확률 높은 순으로 정렬
        df_sorted = df_raw.sort_values(by="Prob_Yes", ascending=False)

        # 상위 20개 출력
        st.subheader("🔍 예측 결과 (이탈 확률 높은 순 Top 20)")
        st.dataframe(df_sorted.head(20))
        st.dataframe(df_sorted.head(1000)[feature_columns + ["Prob_Yes", "Pred", "Grade"]])  # Dropped Columns 있음

        # 전체 결과 다운로드
        csv = df_raw.to_csv(index=False).encode("utf-8-sig")
        st.download_button("📥 결과 다운로드", data=csv, file_name="predicted_attrition.csv", mime="text/csv")

    except Exception as e:
        st.error(f"❌ 예측 중 오류 발생: {e}")
