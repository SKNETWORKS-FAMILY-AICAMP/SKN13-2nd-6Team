# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_echarts import st_echarts
import pickle
import sklearn
from sklearn import preprocessing
import shap
import pandas as pd


# 2. 저장된 모델을 불러오기
with open('xgb.pkl','rb') as f:
    model = pickle.load(f)


# 페이지 1: 이탈 예측 조회

st.title("🔍 이탈 예측 조회")

with st.form("predict_form"):
    st.subheader("직원의 정보를 입력하세요")

        # 예시 컬럼: 범위 슬라이더 및 체크박스
        # feature importance 상위 15개
    left, middle, right, right2 = st.columns(4)
    with left:
        age = st.number_input("나이", value=30)

        Education =st.selectbox("최종학력", ("고등학교 졸업", "전문대 졸업", "학사", "석사", "박사"), index=2)

        EnvironmentSatisfaction = st.selectbox("업무 환경 만족도", ("나쁨", "보통", "좋음", "매우 좋음"), index=1)

    with middle:
        JobInvolvement = st.selectbox("업무 몰입도", ("나쁨", "보통", "좋음", "매우 좋음"), index=1)

        
        JobLevel = st.selectbox("직급", ("고위 임원", "임원", "중간 관리자", "자문위원", "사원"), index=4)
        
        JobSatisfaction = st.selectbox("업무 만족도", ("나쁨", "보통", "좋음", "매우 좋음"), index=1)

    with right:
        MaritalStatus = st.selectbox("결혼 상태", ("미혼", "기혼", "이혼"), index=0)

        NumCompaniesWorked = st.number_input("근무 회사 수", value=0)

        
        RelationshipSatisfaction = st.selectbox("동료 관계 만족도", ("나쁨", "보통", "좋음", "매우 좋음"), index=1)

    with right2:
        StockOptionLevel = st.selectbox("StockOptionLevel", ("0", "1", "2", "3"), index=0)

        WorkLifeBalance = st.selectbox("워라밸", ("나쁨", "보통", "좋음", "매우 좋음"), index=1)

        
    left, middle, right = st.columns(3)
    with left:
        BusinessTravel = st.radio( "출장 빈도수",["거의 안 함", "자주 함", "가본 적 없음"],index=None)

    with middle:
        Department = st.radio("부서", ['Sales','Human Resources','Research & Development'],index=None)
        
    with right : 
            OverTime = st.checkbox("초과근무")

    options = ['Sales Executive','Manufacturing Director','Healthcare Representative','Manager', 
                   'Research Director', 'Laboratory Technician','Sales Representative','Research Scientist', 'Human Resources']
        
        # options = ['영업 임원','생산 이사','의료 담당자','매니저','연구 이사','실험실 기술자','영업 담당자','연구 과학자','인사']
    JobRole = st.segmented_control("업무", options, selection_mode="single")
        

    submit = st.form_submit_button("조회하기")

    if submit:
        #  예측 수행
        input_df = pd.DataFrame({
            "Age":                      [age],
            "BusinessTravel":           [BusinessTravel],
            "Department":               [Department],
            "Education":                [Education],
            "EnvironmentSatisfaction":  [EnvironmentSatisfaction],
            "JobInvolvement":           [JobInvolvement],
            "JobLevel":                 [JobLevel],
            "JobRole":                  [JobRole],
            "JobSatisfaction":          [JobSatisfaction],
            "MaritalStatus":            [MaritalStatus],
            "NumCompaniesWorked":       [NumCompaniesWorked],
            "OverTime":                 [int(OverTime)],
            "RelationshipSatisfaction": [RelationshipSatisfaction],
            "StockOptionLevel":         [StockOptionLevel],
            "WorkLifeBalance":          [WorkLifeBalance]
        })


        # =======================================================================
        # 한글 입력값을 숫자로 매핑
        input_df['Education'] = input_df['Education'].map({
            '고등학교 졸업': 1,
            '전문대 졸업': 2,
            '학사': 3,
            '석사': 4,
            '박사': 5
        })

        input_df['EnvironmentSatisfaction'] = input_df['EnvironmentSatisfaction'].map({
            '나쁨': 1,
            '보통': 2,
            '좋음': 3,
            '매우 좋음': 4
        })

        input_df['JobInvolvement'] = input_df['JobInvolvement'].map({
            '나쁨': 1,
            '보통': 2,
            '좋음': 3,
            '매우 좋음': 4
        })

        input_df['JobLevel'] = input_df['JobLevel'].map({
            '고위 임원': 5,
            '임원': 4,
            '중간 관리자': 3,
            '자문위원': 2,
            '사원': 1
        })

        input_df['JobSatisfaction'] = input_df['JobSatisfaction'].map({
            '나쁨': 1,
            '보통': 2,
            '좋음': 3,
            '매우 좋음': 4
        })

        input_df['MaritalStatus'] = input_df['MaritalStatus'].map({
            '미혼': 2,
            '기혼': 3,
            '이혼': 4
        })

        input_df['RelationshipSatisfaction'] = input_df['RelationshipSatisfaction'].map({
            '나쁨': 1,
            '보통': 2,
            '좋음': 3,
            '매우 좋음': 4
        })

        input_df['StockOptionLevel'] = input_df['StockOptionLevel'].astype(int)

        input_df['WorkLifeBalance'] = input_df['WorkLifeBalance'].map({
            '나쁨': 1,
            '보통': 2,
            '좋음': 3,
            '매우 좋음': 4
        })

        input_df['BusinessTravel'] = input_df['BusinessTravel'].map({
            '거의 안 함': 2,
            '자주 함': 3,
            '가본 적 없음': 4
        })

        input_df['Department'] = input_df['Department'].map({
            'Sales':2,
            'Human Resources':3,
            'Research & Development':4
        })

        # input_df['OverTime'] = input_df['OverTime'].astype(int)

        input_df['JobRole'] = input_df['JobRole'].map({
            'Sales Executive':2,
            'Manufacturing Director':3,
            'Healthcare Representative':4,
            'Manager':2,
            'Research Director':3,
            'Laboratory Technician':4,
            'Sales Representative':2,
            'Research Scientist':3,
            'Human Resources':4
        })
        # =====================================================================

        
        ###
        ## 여기에 scaler
        with open('scaler.pkl','rb') as f:
            scaler = pickle.load(f)

        norm = scaler.transform(input_df)
        norm_df = pd.DataFrame(norm, columns=input_df.columns)
        proba =  float(model.predict_proba(norm_df)[:,1])
        

        # 3. 모델에 돌려서 1일 확률인 proba 구하기
        

        # 결과 등급화
        if proba > 0.7:
            level = "❗ 위험"
            pct = round(proba * 100, 2)
            st.metric("이탈 가능성", f"{pct}%")
            # st.markdown(
            #     "<div style='background-color: #ffa4a4; padding: 10px; border-radius: 5px;'>❗ 매우 높은 이탈 위험</div>",unsafe_allow_html=True)
            st.error(f"{level} 단계입니다.")

        elif proba > 0.4:
            level = "⚠️ 주의"
            pct = round(proba * 100, 2)
            st.metric("이탈 가능성", f"{pct}%")
            # st.markdown(
            #     "<div style='background-color: #FAED7D; padding: 10px; border-radius: 5px;'>⚠️ 주의 필요</div>",unsafe_allow_html=True)
            st.warning(f"{level} 단계입니다.")

        else:
            level = "✅ 안정"
            pct = round(proba * 100, 2)
            st.metric("이탈 가능성", f"{pct}%")
            # st.markdown(
                # "<div style='background-color: #B7F0B1; padding: 10px; border-radius: 5px;'>✅ 안정적</div>",unsafe_allow_html=True)
            st.success(f"{level} 단계입니다.")

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
                "formatter": "{value}%"
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
        # st_echarts(gauge_option_fraction(proba))
        st_echarts(gauge_option_fraction(proba))

    # def column_name(column_name):
    #     for i in range(len(df[0])):
    #         if 
        translation_dict = {
    "JobLevel":               "👔 직급 수준",
    "StockOptionLevel":       "📈 스톡옵션 수준",
    "OverTime":               "⏰ 잔업 여부",
    "MaritalStatus":          "💍 결혼 상태",
    "Department":             "🏢 부서",
    "JobInvolvement":         "💼 업무 몰입도",
    "EnvironmentSatisfaction":"🌟 환경 만족도",
    "JobRole":                "📝 직무 역할",
    "JobSatisfaction":        "😊 업무 만족도",
    "BusinessTravel":         "✈️ 출장 빈도",
    "NumCompaniesWorked":     "🏢 근무 회사 수",
    "Age":                    "🎂 나이",
    "WorkLifeBalance":        "⚖️ 워크–라이프 밸런스",
    "RelationshipSatisfaction":"🤝 동료 관계 만족도",
    "Education":              "🎓 학력 수준",
    "TotalWorkingYears":      "⏳ 총 근무 연수",
    "TrainingTimesLastYear":  "📚 지난해 교육 횟수",
    "DistanceFromHome":       "🏠 집과 거리",
    "EducationField":         "🏫 전공 분야",
    "MonthlyRate":            "💰 월급여",
    "HourlyRate":             "💵 시급",
    "YearsSinceLastPromotion":"📅 마지막 승진 후 경과 연수",
    "PerformanceRating":      "⭐ 성과 평가 등급",
    "PercentSalaryHike":      "📈 급여 인상률",
    "DailyRate":              "📆 DailyRate",
    "Gender":                 "🚻 성별"
}




        # 상위 중요 변수 출력
        st.markdown(
     """
    <h3 style="
        margin: 0; 
        padding: 0;             
        margin-top: -80px; 
    ">
      💡 퇴사 이유 주요 요인
    </h3>
    """,
    unsafe_allow_html=True)            

        def predict_with_explanation(input_df, model, feature_columns):


    # 예측 결과
            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1]  # 퇴사 확률 (Yes 클래스)

    # SHAP 계산기 생성 (Tree 기반 모델용)
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(input_df)

    # SHAP 값 → pandas Series (기여도)
            shap_df = pd.Series(shap_values[0], index=feature_columns).sort_values(key=abs, ascending=False)

    # 상위 5개 피처 + 기여도 값 포함
            top5 = shap_df.head(5).to_dict()

            return {
        'prediction': int(prediction),
        'probability': float(probability),
        'top5_features': top5
    }

        feature_columns = norm_df.columns
        result = predict_with_explanation(norm_df, model, feature_columns)

        features = result['top5_features']


        for idx, feat in enumerate(features, start=1):
            kor = translation_dict.get(feat, "번역 없음")
            if idx == 1:
                st.markdown(
        f'<p style="margin: -20px 0 10px 0px; padding: 0;">{kor}</p>',
        unsafe_allow_html=True)
            else:
                st.markdown(
        f'<p style="margin: 0px 0 10px 0px; padding: 0;">{kor}</p>',
        unsafe_allow_html=True)