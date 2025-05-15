# 페이지 1: 이탈 예측 조회
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_echarts import st_echarts
import pickle
import sklearn    

st.title("🔍 이탈 예측 조회")

with st.form("predict_form"):
    st.subheader("직원의 예상 정보를 입력하세요.")

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
        "Age":                     [age],
        "Education":               [Education],
        "EnvironmentSatisfaction": [EnvironmentSatisfaction],
        "JobInvolvement":          [JobInvolvement],
        "JobLevel":                [JobLevel],
        "JobSatisfaction":         [JobSatisfaction],
        "MaritalStatus":           [MaritalStatus],
        "NumCompaniesWorked":      [NumCompaniesWorked],
        "RelationshipSatisfaction":[RelationshipSatisfaction],
        "StockOptionLevel":        [StockOptionLevel],
        "WorkLifeBalance":         [WorkLifeBalance],
        "BusinessTravel":          [BusinessTravel],
        "Department":              [Department],
        "OverTime":                [int(OverTime)],  # bool → 0/1
        "JobRole":                 [JobRole]
    })
    
        

        # 2. 저장된 모델을 불러오기
        with open('rfc.pkl','rb') as f:
            model = pickle.load(f)

        # proba = model.predict_proba(input_df)[:,1]

        # 3. 모델에 돌려서 1일 확률인 proba 구하기
        # proba = model.predict(input_df)[~~]
        proba = np.random.rand()  # 예시용


        # 결과 등급화
        if proba > 0.7:
            level = "❗ 위험"
            st.metric("이탈 가능성", f"{proba:.2%}")
            # st.markdown(
            #     "<div style='background-color: #ffa4a4; padding: 10px; border-radius: 5px;'>❗ 매우 높은 이탈 위험</div>",unsafe_allow_html=True)
            st.error(f"{level} 단계입니다.")

        elif proba > 0.4:
            level = "⚠️ 주의"
            st.metric("이탈 가능성", f"{proba:.2%}")
            # st.markdown(
            #     "<div style='background-color: #FAED7D; padding: 10px; border-radius: 5px;'>⚠️ 주의 필요</div>",unsafe_allow_html=True)
            st.warning(f"{level} 단계입니다.")

        else:
            level = "✅ 안정"
            st.metric("이탈 가능성", f"{proba:.2%}")
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
                "formatter": "{value} %"
            },
            "title": {
                "show": True,
                "offsetCenter": [0, "-20%"],
                "fontSize": 16,
                # "formatter" : "{b}"
            
            },
            "data": [{"value": pct, "name": "이탈 가능성"}]
        }]
    }
        
        # 옵션 생성 & 렌더링
        st_echarts(gauge_option_fraction(proba))

    # def column_name(column_name):
    #     for i in range(len(df[0])):
    #         if 
        translation_dict = {
    "JobLevel":               "직급 수준을",
    "StockOptionLevel":       "스톡옵션 수준을",
    "OverTime":               "잔업 여부를",
    "MaritalStatus":          "결혼 상태를",
    "Department":             "부서를",
    "JobInvolvement":         "업무 몰입도를",
    "EnvironmentSatisfaction":"환경 만족도를",
    "JobRole":                "직무 역할을",
    "JobSatisfaction":        "업무 만족도를",
    "BusinessTravel":         "출장 빈도를",
    "NumCompaniesWorked":     "근무 회사 수를",
    "Age":                    "나이를",
    "WorkLifeBalance":        "워크–라이프 밸런스를",
    "RelationshipSatisfaction":"동료 관계 만족도를",
    "Education":              "학력 수준을",
    "TotalWorkingYears":      "총 근무 연수를",
    "TrainingTimesLastYear":  "지난해 교육 횟수를",
    "DistanceFromHome":       "집과 거리를",
    "EducationField":         "전공 분야를",
    "MonthlyRate":            "월급여를",
    "HourlyRate":             "시급을",
    "YearsSinceLastPromotion":"마지막 승진 후 경과 연수를",
    "PerformanceRating":      "성과 평가 등급을",
    "PercentSalaryHike":      "급여 인상률을",
    "DailyRate":              "일일 요율을",
    "Gender":                 "성별을"
}
        # imp_df : 
        def summarize_features(feat_list: list[str]):
            """
            feat_list: 피처명(영어)만 들어있는 리스트
            반환: feature | korean_name | mean 컬럼을 가진 DataFrame
            """
            records = []
            for feat in feat_list:
                # 1) 번역
                kor = translation_dict.get(feat, "번역 없음")
        
                 # 2) 평균 계산
                 # df는 feature의 평균을 구할 수 있는 dataframe (혹시 이게 있을까,,?ㅎㅎ)
                if feat in df.columns:
                    mean_val = df[feat].mean()
                else:
                    mean_val = None  # 혹은 np.nan
        
                records.append({"feature":feat, "korean_name":kor, "mean": mean_val})
            return pd.DataFrame(records)


        # 상위 중요 변수 출력
    #     st.markdown(
    # "<h3 style='margin-top:-100px;'>퇴사 이유 주요 요인</h3>",
    # unsafe_allow_html=True)
        # summarize_df = summarize_features(feat_list) # feat_list : feature, feature_dictionary, mean가 있는 dataframe 
        
        if level == "✅ 안정":
            st.markdown(
    "<h3 style='margin-top:-100px;'>✅ 조정할 수 있다면 조정해주세요</h3>",
    unsafe_allow_html=True)
            st.markdown(
    "<h6 style='margin-top:-50px;'>퇴사 이유 주요 요인</h6>",
    unsafe_allow_html=True)
            # st.write(f"{feature}이/가 {mean}만큼 부족합니다. {컬럼명:dictonary.key}")
            

        elif level == "⚠️ 주의":
            st.markdown(
    "<h3 style='margin-top:-100px;'>⚠️ 지금은 아니지만 조정이 필요합니다</h3>",
    unsafe_allow_html=True)
            st.markdown(
    "<h6 style='margin-top:-50px;'>퇴사 이유 주요 요인</h6>",
    unsafe_allow_html=True)
            

        elif level == "❗ 위험":
            st.markdown(
    "<h3 style='margin-top:-100px;'>❗ 빠른 시일 내로 조정해주세요</h3>",
    unsafe_allow_html=True)
            st.markdown(
    "<h6 style='margin-top:-50px;'>퇴사 이유 주요 요인</h6>",
    unsafe_allow_html=True)
    
        features = [
    'BusinessTravel', 'Department', 'Education',
    'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel', 'JobRole',
    'JobSatisfaction', 'MaritalStatus', 'NumCompaniesWorked', 'OverTime',
    'RelationshipSatisfaction', 'StockOptionLevel', 'WorkLifeBalance','Age'
]
        means = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for feat, mean_val in zip(features[:5], means[:5]):
            kor = translation_dict.get(feat, "번역 없음")

            st.write(f"{kor} 확인해주세요")
