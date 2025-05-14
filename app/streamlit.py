# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_echarts import st_echarts


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
        if proba > 0.7:
            level = "❗ 매우 높은 이탈 위험"
            st.metric("이탈 가능성", f"{proba:.2%}") 
            st.error(level)

        elif proba > 0.4:
            level = "⚠️ 주의 필요"
            st.metric("이탈 가능성", f"{proba:.2%}")
            st.warning(level)

        else:
            level = "✅ 안정적"
            st.metric("이탈 가능성", f"{proba:.2%}")
            st.success(level)

        # 반원형 게이지 차트
        def gauge_option_fraction(val):
            
            pct = round(val * 100, 2)
            # 영역 비율 (0~1)
            r1 = 40 / 100
            r2 = 70 / 100
            rp = pct / 100

            # 동적 색상 구간 만들기
            segments = []
            if rp <= r1: # 35% 미만일 경우
                segments = [
            [rp, "#B7F0B1"],   # 0~pct: 초록
            [1.0, "#ffffff"]   # 나머지: 흰색
        ]
            elif rp <= r2: # 35% ~70%일 경우
                segments = [
            [r1, "#B7F0B1"],   # 0~35%: 초록
            [rp, "#FAED7D"],   # 35%~pct: 노랑
            [1.0, "#ffffff"]   # 나머지: 흰색
        ]
            else: # 70% 이상일 경우
                segments = [
            [r1, "#B7F0B1"],   # 0~35%: 초록
            [r2, "#FAED7D"],   # 35~70%: 노랑
            [rp, "#FFA7A7"],   # 70%~pct: 빨강
            [1.0, "#ffffff"]   # 나머지: 흰색
        ]

            return {
        "tooltip": {"show": False},
        "series": [{
            "type": "gauge",
            "startAngle": 180,
            "endAngle": 0,
            "min": 0,
            "max": 100,
            "progress": {"show": False},
            "axisLine": {
                "lineStyle": {
                    "width": 60,
                    "color": segments
                }
            },
            "pointer": {"show": False},
            "axisTick":   {"show": False},
            "splitLine":  {"show": False},
            "axisLabel":  {"show": False},
            "detail": {
                "valueAnimation": True,
                "fontSize": 24,
                "offsetCenter": [0, "0%"],
                "formatter": "{value} %"
            },
            "title": {
                "show": True,
                "offsetCenter": [0, "-20%"],
                "fontSize": 16,
                "formatter" : "{b}"
            
            },
            "data": [{"value": pct, "name": "이탈 가능성"}]
        }]
    }
        
        # 옵션 생성 & 렌더링
        st_echarts(gauge_option_fraction(proba))

        # 상위 중요 변수 출력
        st.markdown(
    "<h3 style='margin-top:-100px;'>상위 주요 요인</h3>",
    unsafe_allow_html=True)
        st.write("~~")


# 페이지 2: 컬럼별 상관관계 분석
elif menu == "상관관계 분석":
    st.title("컬럼별 상관관계 분석")




# 페이지 3: 대량 조회
elif menu == "대량 조회":
    st.title("대량 이탈 예측")

    batch_file = st.file_uploader("대량 데이터 파일 업로드", type=["csv"])
    if batch_file is not None:
        # 1. csv 읽기
        df = pd.read_csv(batch_file)
        st.write("입력 데이터", df.head())

        # 2. 전처리
        # feature = df['전처리 필요한 피처명']
        # X_Scaled = sclaer.transform(feature)

        # 3. 예측
        # pred_proba(확률)
        # pred(이탈 여부)

        # 4. 결과 병합
        # df["Prob_Yes"] = pred_proba
        # df["Pred"] = pred

        # 결과 등급 결정 함수 
        # def categorize(prob):
        #     if prob >= 0.7: return "High"
        #     if prob >= 0.3:  return "Medium"
        #     return "Low"
        # df['Grade'] = [categorize(p) for p in pred_proba]

        # 5. 화면에 일부 출력
        # st.subheader("예측 결과 (상위 5개)")
        # st.dataframe(df["Prob_Yes"].head(5))
        # st.dataframe(df["Pred"].head(5))

        # 6. 다운로드 링크
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("결과 다운로드", data=csv, file_name="prediction_result.csv", mime="text/csv")


