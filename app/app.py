# import streamlit as st
# from streamlit_extras.switch_page_button import switch_page

# st.set_page_config(page_title="이탈 예측 시스템", layout="wide")

# st.title("🧠 이탈 예측 시스템 대시보드")

# st.markdown("""
# ### 👋 환영합니다!
# 사이드바 또는 아래 기능 카드에서 원하는 분석 기능을 선택하세요.
# """)

# # 컬럼 3개로 배치
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("### 🏠 이탈 예측")
#     st.markdown("직원 개별 정보를 입력하면 이탈 위험을 예측합니다.")
#     if st.button("➡️ 이동", key="predict"):
#         switch_page("1_이탈_예측")

# with col2:
#     st.markdown("### 📈 상관관계 분석")
#     st.markdown("여러 변수 간의 관계를 시각적으로 분석합니다.")
#     if st.button("➡️ 이동", key="correlation"):
#         switch_page("2_상관관계_분석")

# with col3:
#     st.markdown("### 📦 대량 이탈 예측")
#     st.mark다운("CSV 파일을 업로드하면 이탈 확률을 일괄 예측합니다.")
#     if st.button("➡️ 이동", key="bulk"):
#         switch_page("3_대량조회")

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="이탈 예측 시스템", layout="wide")

# 헤더
st.title("👩‍💼 직원 이탈 예측 시스템")
st.markdown("이직 가능성을 예측하고, 상관관계 및 집단 분석을 제공합니다.")

# 데이터 로드
df = pd.read_csv("../data/datasets.csv")  # 경로 확인 필요

# ✅ 이직률 계산을 위한 전처리 (추가)
if df["Attrition"].dtype == object:
    df["Attrition"] = df["Attrition"].replace({"Yes": 1, "No": 0})
df["Attrition"] = df["Attrition"].astype(int)

# 기본 통계
total_employees = len(df)
attrition_rate = df["Attrition"].mean()  # ✅ 수정됨
avg_age = df["Age"].mean()

# 지표 카드
col1, col2, col3 = st.columns(3)
col1.metric("총 인원 수", f"{total_employees:,}명")
col2.metric("이직률", f"{attrition_rate:.2%}")
col3.metric("평균 나이", f"{avg_age:.1f}세")

# 전체 이직 vs 잔류 Pie chart
attrition_count = df["Attrition"].value_counts().rename({0: "잔류", 1: "이직"})
fig = px.pie(
    names=attrition_count.index,
    values=attrition_count.values,
    title="이직/잔류 비율",
    color_discrete_sequence=["lightgreen", "salmon"]
)
st.plotly_chart(fig, use_container_width=True)

# 페이지 이동 안내
st.markdown("👉 **좌측 메뉴에서 이탈 예측 조회 / 상관관계 분석 / 대량 예측 페이지로 이동하세요.**")