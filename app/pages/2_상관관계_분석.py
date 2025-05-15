import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import altair as alt
import plotly.express as px
import io
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.title("📈 컬럼별 상관관계 분석")

# 데이터 업로드 또는 불러오기
# uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
# if uploaded_file:

df = pd.read_csv("../data/processed_datasets.csv")
st.write("데이터 미리보기", df.head())

# 수치형 컬럼만 필터링
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

if len(numeric_cols) < 2:
    st.warning("수치형 컬럼이 2개 이상 필요합니다.")
else:
    # 선택된 변수 기준 상관계수
    target_col = st.selectbox("기준 컬럼 선택", numeric_cols)
    method = st.selectbox("상관계수 방식", ["pearson", "spearman", "kendall"])

    # 상관계수 계산
    corr_matrix = df[numeric_cols].corr(method=method)

    # st.subheader(f"🔗 전체 상관계수 히트맵 ({method})")
    # import plotly.express as px
    # fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
    # st.plotly_chart(fig, use_container_width=True)

    st.subheader(f"🔗 전체 상관계수 히트맵 ({method})")

    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1
    )

    # 축 글자 안 잘리도록 크기 확대 + label 모두 표시
    fig.update_layout(
        height=1000,
        width=1200,
        margin=dict(t=50, b=50),
        xaxis=dict(tickmode='array', tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns.tolist()),
        yaxis=dict(tickmode='array', tickvals=list(range(len(corr_matrix.index))), ticktext=corr_matrix.index.tolist())
    )

    st.plotly_chart(fig, use_container_width=True)

    # st.subheader(f"📊 '{target_col}'와의 상관관계 Top 10")
    # target_corr = corr_matrix[target_col].drop(target_col).sort_values(key=abs, ascending=False).head(10)
    # st.dataframe(target_corr.to_frame(name="상관계수"))

    # 예시: corr_matrix와 target_col이 이미 존재하는 경우
    st.subheader(f"📊 '{target_col}'와의 상관관계 Top 10")

    # 절댓값 기준 top10 추출 후 부호 유지
    target_corr_series = corr_matrix[target_col].drop(target_col)
    top10_indices = target_corr_series.abs().sort_values(ascending=False).head(10).index
    target_corr = target_corr_series.loc[top10_indices]

    # # 상관계수 상위 10개 추출
    # target_corr = corr_matrix[target_col].drop(target_col).sort_values(key=abs, ascending=False).head(10)

    # 데이터프레임으로 변환 (시각화를 위해)
    corr_df = target_corr.reset_index()
    corr_df.columns = ['Feature', 'Correlation']

    # Altair 막대그래프
    bar_chart = alt.Chart(corr_df).mark_bar().encode(
        x=alt.X('Correlation:Q', scale=alt.Scale(domain=[-1, 1])),  # 상관계수 범위 지정
        y=alt.Y('Feature:N', sort='-x'),
        color=alt.condition(
            alt.datum.Correlation > 0,
            alt.value("#4daf4a"),  # 양의 상관: 녹색
            alt.value("#e41a1c")   # 음의 상관: 빨강
        )
    ).properties(
        width=600,
        height=400,
        title=f"'{target_col}'와의 상관관계 (Top 10)"
    )

    st.altair_chart(bar_chart, use_container_width=True)