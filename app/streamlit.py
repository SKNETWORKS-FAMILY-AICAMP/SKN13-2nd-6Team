# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


st.set_page_config(page_title="이탈 예측 시스템", layout="wide")

# 사이드바 메뉴
menu = st.sidebar.selectbox(
    "서비스 선택", ["이탈 예측 조회", "상관관계 분석", "대량 조회"]
)


# 페이지 1: 이탈 예측 조회
if menu == "이탈 예측 조회":
    st.title("이탈 예측 조회")

    with st.form("predict_form"):
        st.subheader("정보 입력")

        # 예시 컬럼: 범위 슬라이더 및 체크박스
        age = st.slider("age", 18, 65, 30)
        BusinessTravel = st.checkbox("BusinessTravel 여부")
        DailyRate = st.selectbox("DailyRate", [1, 2, 3, 4, 5])
        Income = st.number_input("Department", 1000, 30000, step=100)
        options = ["Research & Development", "Marketing", "Sales", "Human Resources"]
        selection = st.segmented_control("Department", options, selection_mode="multi")
        Married = st.toggle("Married")
        

        submit = st.form_submit_button("조회하기")

    if submit:
        #  예측 수행
        # 1. dataframe을 만들기
        # input_df = pd.DataFrame({
        #     "Age": [age]
        #     "OverTime": [int(overtime)],
        #     "JobLevel": [job_level],
        #     "Income": [Income]
        # })
        

        # 2. 저장된 모델을 불러오기



        # 3. 모델에 돌려서 1일 확률인 proba 구하기
        # proba = model.predict(input_df)[~~]
        proba = np.random.rand()  # 예시용


        # 결과 등급화
        if proba > 0.8:
            level = "❗ 매우 높은 이탈 위험"
            st.metric("이탈 가능성", f"{proba:.2%}") 
            st.error(level)

        elif proba > 0.5:
            level = "⚠️ 주의 필요"
            st.metric("이탈 가능성", f"{proba:.2%}")
            st.warning(level)

        else:
            level = "✅ 안정적"
            st.metric("이탈 가능성", f"{proba:.2%}")
            st.success(level)

        # 반원형 게이지 차트
        # 배경
        fig1 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=proba * 100,
            number = {'suffix': "%"},
            domain={'x': [0, 1], 'y': [0.5, 1]},
            title={'text': '이탈 확률', 'font': {'size': 24}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "gray"}, 
                'bar' : {'color' : 'rgba(0,0,0,0)'},
                "steps":[{"range": [0, 35], "color": "lightgreen"}, {"range": [36, 70], "color": "yellow"}, {"range": [71, 100], "color": "red"}],
                'bgcolor': 'rgba(0,0,0,0)' # 투명
            }
        ))

        # 막대그래프 흰색
        fig2 = go.Figure(go.Indicator(
             mode="gauge",
             value=proba * 100,
             domain={'x': [0, 1], 'y': [0.5, 1]},
            #  title={'text': '이탈 확률', 'font': {'size': 24}},
             gauge={
                 'axis': {'range': [100, 0], 'visible' : False},
                 'bar' : {'color' : 'white','thickness': 0.99},
                 'bgcolor': 'rgba(0,0,0,0)',
             }
         ))

        
        
        # 1) 새 Figure를 빈 채로 생성
        combined = go.Figure()

        # 2) 배경용 트레이스(fig1.data)부터 먼저 추가
        combined.add_traces(fig1.data)

        # 3) 흰색 바(fig2.data[0])를 그 위에 추가
        combined.add_trace(fig2.data[0])

        # 4) 레이아웃 조정
        combined.update_layout( margin={'t':80,'b':0,'l':0,'r':0}, height=350)

        # 5) 스트림릿에 렌더링
        st.plotly_chart(combined, use_container_width=True)







        #  # 반원형 게이지 차트
        # fig = go.Figure(go.Indicator(
        #     mode="gauge+number",
        #     value=proba * 100,
        #     number = {'suffix': "%"},
        #     domain={'x': [0, 1], 'y': [0.5, 1]},
        #     title={'text': '이탈 확률', 'font': {'size': 24}},
        #     gauge={
        #         'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "gray"},
        #         'bar' : 
        #         # 'bar' : {'color' : 'gray'},
        #         # "steps":[{"range": [0, 35], "color": "lightgreen" }, {"range": [36, 70], "color": "yellow"}, {"range": [71, 100], "color": "red"}],
        #         'bgcolor': "white",
        #         'borderwidth': 1,
        #         'bordercolor': "gray"
        #     }
        # ))
        # fig.update_layout(margin={'t':80, 'b':0, 'l':0, 'r':0}, height=350)
        # st.plotly_chart(fig, use_container_width=True)

        # 상위 중요 변수 출력 예시
        st.subheader("상위 주요 요인")
        st.write("~~")


# 페이지 2: 컬럼별 상관관계 분석
elif menu == "상관관계 분석":
    st.title("컬럼별 상관관계 분석")




# 페이지 3: 대량 조회
elif menu == "대량 조회":
    st.title("대량 이탈 예측")

    batch_file = st.file_uploader("대량 데이터 파일 업로드", type=["csv"])
    if batch_file is not None:
        df = pd.read_csv(batch_file)
        st.write("입력 데이터", df.head())

        df["이탈 확률"] = np.random.rand(len(df))  # 예시

        st.write("예측 결과", df[["이탈 확률"]].head())

        # 다운로드 링크
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("결과 다운로드", data=csv, file_name="prediction_result.csv", mime="text/csv")
