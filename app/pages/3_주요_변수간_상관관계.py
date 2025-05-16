# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import plotly.graph_objects as go
# import altair as alt
# import plotly.express as px
# import io
# from PIL import Image
# from streamlit_extras.switch_page_button import switch_page

# st.title("📈 컬럼별 상관관계 분석")

# # 데이터 업로드 또는 불러오기
# # uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
# # if uploaded_file:

# df = pd.read_csv("../data/processed_datasets.csv")
# st.write("데이터 미리보기", df.head())

# # 수치형 컬럼만 필터링
# numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# if len(numeric_cols) < 2:
#     st.warning("수치형 컬럼이 2개 이상 필요합니다.")
# else:
#     # 선택된 변수 기준 상관계수
#     target_col = st.selectbox("기준 컬럼 선택", numeric_cols)
#     method = st.selectbox("상관계수 방식", ["pearson", "spearman", "kendall"])

#     # 상관계수 계산
#     corr_matrix = df[numeric_cols].corr(method=method)

#     # st.subheader(f"🔗 전체 상관계수 히트맵 ({method})")
#     # import plotly.express as px
#     # fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
#     # st.plotly_chart(fig, use_container_width=True)

#     st.subheader(f"🔗 전체 상관계수 히트맵 ({method})")

#     fig = px.imshow(
#         corr_matrix,
#         text_auto=True,
#         color_continuous_scale="RdBu_r",
#         zmin=-1,
#         zmax=1
#     )

#     # 축 글자 안 잘리도록 크기 확대 + label 모두 표시
#     fig.update_layout(
#         height=1000,
#         width=1200,
#         margin=dict(t=50, b=50),
#         xaxis=dict(tickmode='array', tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns.tolist()),
#         yaxis=dict(tickmode='array', tickvals=list(range(len(corr_matrix.index))), ticktext=corr_matrix.index.tolist())
#     )

#     st.plotly_chart(fig, use_container_width=True)

#     # st.subheader(f"📊 '{target_col}'와의 상관관계 Top 10")
#     # target_corr = corr_matrix[target_col].drop(target_col).sort_values(key=abs, ascending=False).head(10)
#     # st.dataframe(target_corr.to_frame(name="상관계수"))

#     # 예시: corr_matrix와 target_col이 이미 존재하는 경우
#     st.subheader(f"📊 '{target_col}'와의 상관관계 Top 10")

#     # 절댓값 기준 top10 추출 후 부호 유지
#     target_corr_series = corr_matrix[target_col].drop(target_col)
#     top10_indices = target_corr_series.abs().sort_values(ascending=False).head(10).index
#     target_corr = target_corr_series.loc[top10_indices]

#     # # 상관계수 상위 10개 추출
#     # target_corr = corr_matrix[target_col].drop(target_col).sort_values(key=abs, ascending=False).head(10)

#     # 데이터프레임으로 변환 (시각화를 위해)
#     corr_df = target_corr.reset_index()
#     corr_df.columns = ['Feature', 'Correlation']

#     # Altair 막대그래프
#     bar_chart = alt.Chart(corr_df).mark_bar().encode(
#         x=alt.X('Correlation:Q', scale=alt.Scale(domain=[-1, 1])),  # 상관계수 범위 지정
#         y=alt.Y('Feature:N', sort='-x'),
#         color=alt.condition(
#             alt.datum.Correlation > 0,
#             alt.value("#4daf4a"),  # 양의 상관: 녹색
#             alt.value("#e41a1c")   # 음의 상관: 빨강
#         )
#     ).properties(
#         width=600,
#         height=400,
#         title=f"'{target_col}'와의 상관관계 (Top 10)"
#     )

#     st.altair_chart(bar_chart, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import altair as alt

# st.title("📈 선택된 Feature 간 상관관계 분석 (범주형 통합 포함)")

# # 데이터 불러오기
# df = pd.read_csv("../data/datasets.csv")

# # 사용할 feature 원본
# selected_features = [
#     'Age', 'BusinessTravel', 'Department', 'Education',
#     'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel', 'JobRole',
#     'JobSatisfaction', 'MaritalStatus', 'NumCompaniesWorked', 'OverTime',
#     'RelationshipSatisfaction', 'StockOptionLevel', 'WorkLifeBalance'
# ]

# # df에서 선택된 feature만 추출
# df_filtered = df[selected_features].copy()

# # 범주형 인코딩
# df_encoded = pd.get_dummies(df_filtered, drop_first=True)

# # ✅ 범주형 prefix 목록 (묶을 대상)
# group_prefixes = ["BusinessTravel", "Department", "JobRole", "MaritalStatus", "OverTime"]

# # ✅ One-Hot 컬럼 그룹별로 평균값으로 통합
# def collapse_onehot_features(df, prefix_list):
#     result = df.copy()
#     for prefix in prefix_list:
#         cols = [col for col in df.columns if col.startswith(prefix + "_")]
#         if cols:
#             result[prefix + "_combined"] = df[cols].mean(axis=1)
#             result.drop(columns=cols, inplace=True)
#     return result

# df_collapsed = collapse_onehot_features(df_encoded, group_prefixes)

# # 상관계수 방식 선택
# method = st.selectbox("상관계수 계산 방식", ["pearson", "spearman", "kendall"])
# corr_matrix = df_collapsed.corr(method=method)

# # 히트맵
# st.subheader(f"🔗 상관계수 히트맵 (method = {method})")
# fig = px.imshow(
#     corr_matrix,
#     text_auto=True,
#     color_continuous_scale="RdBu_r",
#     zmin=-1, zmax=1
# )
# fig.update_layout(
#     height=900,
#     width=1000,
#     margin=dict(t=50, b=50),
#     xaxis=dict(tickmode='array', tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns.tolist()),
#     yaxis=dict(tickmode='array', tickvals=list(range(len(corr_matrix.index))), ticktext=corr_matrix.index.tolist())
# )
# st.plotly_chart(fig, use_container_width=True)

# # 기준 feature 선택
# target_col = st.selectbox("기준 Feature 선택", [col for col in corr_matrix.columns])

# # Top 8 상관계수 막대 그래프
# st.subheader(f"📊 '{target_col}'과의 상관관계 (Top 5)")
# target_corr_series = corr_matrix[target_col].drop(target_col)
# top8_indices = target_corr_series.abs().sort_values(ascending=False).head(5).index
# target_corr = target_corr_series.loc[top8_indices]

# corr_df = target_corr.reset_index()
# corr_df.columns = ['Feature', 'Correlation']

# bar_chart = alt.Chart(corr_df).mark_bar().encode(
#     x=alt.X('Correlation:Q', scale=alt.Scale(domain=[-1, 1])),
#     y=alt.Y('Feature:N', sort='-x'),
#     color=alt.condition(
#         alt.datum.Correlation > 0,
#         alt.value("#4daf4a"),
#         alt.value("#e41a1c")
#     )
# ).properties(
#     width=600,
#     height=400,
#     title=f"'{target_col}'와의 상관관계 (Top 5)"
# )
# st.altair_chart(bar_chart, use_container_width=True)

# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import altair as alt
# from sklearn.ensemble import RandomForestClassifier

# st.title("📈 컬럼별 상관관계 분석 & 🌲 Random Forest Feature Importance")

# # ——————————————————————————————————————————————————————————
# # 1) 상관관계 분석 (기존 코드)
# # ——————————————————————————————————————————————————————————
# df = pd.read_csv("../data/processed_datasets.csv")
# st.write("데이터 미리보기", df.head())

# numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
# if len(numeric_cols) >= 2:
#     target_col = st.selectbox("기준 컬럼 선택", numeric_cols)
#     method = st.selectbox("상관계수 방식", ["pearson", "spearman", "kendall"])
#     corr_matrix = df[numeric_cols].corr(method=method)

#     st.subheader(f"🔗 전체 상관계수 히트맵 ({method})")
#     fig = px.imshow(
#         corr_matrix, text_auto=True,
#         color_continuous_scale="RdBu_r", zmin=-1, zmax=1
#     )
#     fig.update_layout(
#         height=800, width=1000,
#         margin=dict(t=50,b=50),
#         xaxis=dict(tickmode='array', tickvals=list(range(len(corr_matrix.columns))),
#                    ticktext=corr_matrix.columns),
#         yaxis=dict(tickmode='array', tickvals=list(range(len(corr_matrix.index))),
#                    ticktext=corr_matrix.index)
#     )
#     st.plotly_chart(fig, use_container_width=True)

#     st.subheader(f"📊 '{target_col}'와의 상관관계 Top 10")
#     tc = corr_matrix[target_col].drop(target_col)
#     top10 = tc.abs().sort_values(ascending=False).head(10).index
#     corr_df = tc.loc[top10].reset_index()
#     corr_df.columns = ["Feature","Correlation"]
#     bar = alt.Chart(corr_df).mark_bar().encode(
#         x=alt.X("Correlation:Q", scale=alt.Scale(domain=[-1,1])),
#         y=alt.Y("Feature:N", sort="-x"),
#         color=alt.condition(alt.datum.Correlation>0,
#                              alt.value("#4daf4a"), alt.value("#e41a1c"))
#     ).properties(width=600, height=350)
#     st.altair_chart(bar, use_container_width=True)
# else:
#     st.warning("수치형 컬럼이 2개 이상 필요합니다.")

# # ——————————————————————————————————————————————————————————
# # 2) Random Forest Feature Importance (OneHotEncoder 없이)
# # ——————————————————————————————————————————————————————————
# st.subheader("🌲 Random Forest Feature Importance")

# # 1) X, y 준비
# # 처리된 CSV에는 이미 all numeric(dummy + scaled) 칼럼만 남아 있다고 가정
# # 'Attrition' 칼럼만 예측 대상으로 분리
# X = df.drop(columns=["Attrition"])
# y = df["Attrition"].map({"Yes":1, "No":0})

# # 2) 모델 학습
# rf = RandomForestClassifier(n_estimators=100, random_state=42)
# with st.spinner("Random Forest 학습 중…"):
#     rf.fit(X, y)

# # 3) 중요도 추출 & DataFrame화
# feat_imp = rf.feature_importances_
# fi_df = pd.DataFrame({
#     "Feature": X.columns,
#     "Importance": feat_imp
# }).sort_values("Importance", ascending=False)

# # 4) 상위 N개 표시
# top_n = st.slider("Feature Importance: 상위 N개 보기", 5, min(len(fi_df), 50), 10)
# fi_top = fi_df.head(top_n)

# # 5) Altair 막대그래프로 시각화
# chart = alt.Chart(fi_top).mark_bar().encode(
#     x=alt.X("Importance:Q", title="중요도"),
#     y=alt.Y("Feature:N", sort="-x", title=None),
# ).properties(
#     width=600, height=400,
#     title=f"Random Forest Feature Importance Top {top_n}"
# )
# st.altair_chart(chart, use_container_width=True)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

st.set_page_config(
    layout="wide",       # ← 여기!
    initial_sidebar_state="auto"
)

st.title("📈 선택된 Feature 간 상관관계 분석")

# 데이터 불러오기
df = pd.read_csv("../data/datasets.csv")

# 사용할 feature 원본
selected_features = [
    'Age', 'BusinessTravel', 'Department', 'Education',
    'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel', 'JobRole',
    'JobSatisfaction', 'MaritalStatus', 'NumCompaniesWorked', 'OverTime',
    'RelationshipSatisfaction', 'StockOptionLevel', 'WorkLifeBalance'
]

# df에서 선택된 feature만 추출
df_filtered = df[selected_features].copy()

# 범주형 인코딩
df_encoded = pd.get_dummies(df_filtered, drop_first=True)

# 범주형 그룹별 prefix
group_prefixes = ["BusinessTravel", "Department", "JobRole", "MaritalStatus", "OverTime"]

# One-Hot 컬럼 그룹별로 평균값으로 통합
def collapse_onehot_features(df, prefix_list):
    result = df.copy()
    for prefix in prefix_list:
        cols = [col for col in df.columns if col.startswith(prefix + "_")]
        if cols:
            result[prefix + "_combined"] = df[cols].mean(axis=1)
            result.drop(columns=cols, inplace=True)
    return result

df_collapsed = collapse_onehot_features(df_encoded, group_prefixes)

# Pearson 상관계수로 고정
method = 'pearson'
corr_matrix = df_collapsed.corr(method=method)

# 기준 feature 선택
target_col = st.selectbox("기준 Feature 선택", corr_matrix.columns.tolist())

# 📊 상관계수 막대그래프 (Top 5)
st.subheader(f"📊 '{target_col}'과의 상관관계 (Top 5)")
target_corr_series = corr_matrix[target_col].drop(target_col)
top5_indices = target_corr_series.abs().sort_values(ascending=False).head(5).index
target_corr = target_corr_series.loc[top5_indices]

corr_df = target_corr.reset_index()
corr_df.columns = ['Feature', 'Correlation']

bar_chart = alt.Chart(corr_df).mark_bar().encode(
    x=alt.X('Correlation:Q', scale=alt.Scale(domain=[-1, 1])),
    y=alt.Y('Feature:N', sort='-x'),
    color=alt.condition(
        alt.datum.Correlation > 0,
        alt.value("#4daf4a"),
        alt.value("#e41a1c")
    )
).properties(
    width=600,
    height=400,
    title=f""
)
st.altair_chart(bar_chart, use_container_width=True)

# 🔗 히트맵 (Pearson 고정)
st.subheader(f"🔗 Pearson 상관계수 히트맵")
fig = px.imshow(
    corr_matrix,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    zmin=-1, zmax=1
)
fig.update_layout(
    height=900,
    width=1000,
    margin=dict(t=50, b=50),
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(len(corr_matrix.columns))),
        ticktext=corr_matrix.columns.tolist()
    ),
    yaxis=dict(
        tickmode='array',
        tickvals=list(range(len(corr_matrix.index))),
        ticktext=corr_matrix.index.tolist()
    )
)
st.plotly_chart(fig, use_container_width=True)

