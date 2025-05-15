📅**개발 기간** : 2025.05.15 ~ 2025.05.16

# 🚩**IBM 직원 이탈 예측**
--------------------------------------------------------------
## 👤 팀원 및 담당 업무
| 이름     | 역할                        |
|----------|-----------------------------|
| 구자현   | ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ |
| 민경재   | ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ        |
| 박현아   | ㅁㅁㅁㅁㅁㅁㅁㅁ        |
| 우지훈   | ㅁㅁㅁㅁㅁㅁㅁㅁ          |
--------------------------------------------------------------
- SK네트웍스 Family AI 캠프 13기
- 팀명 : 6조
## 🔧 기술스택 
![image](https://github.com/user-attachments/assets/4842b4d2-a7b6-4f79-9465-3b5baa632bb8)
![image](https://github.com/user-attachments/assets/edb303e4-5756-4267-999e-0473c443a5b9)
![image](https://github.com/user-attachments/assets/d34ac1d9-79ee-4db1-a6a1-5f7a155efeb4)
![image](https://github.com/user-attachments/assets/1ce88e67-ba26-4277-b1e6-790f4aa64e4f)

![image](https://github.com/user-attachments/assets/37e004cc-f457-48da-8e70-2c2467debf7a)
![image](https://github.com/user-attachments/assets/632c14c1-25ae-41eb-a83b-cf3750d9dcce)
![image](https://github.com/user-attachments/assets/818414e4-a71e-4189-b1dd-e8d01fac0c74)
![image](https://github.com/user-attachments/assets/85046805-be7a-490f-b5c0-0e9bae7b99e3)


--------------------------------------------------------------
# 💡 프로젝트 개요
## ✅ 프로젝트 주제 
### 직원 이탈 원인 분석 및 이탈 예측
## ✅ 프로젝트 목표
### - 직원 주요 이탈 요인 분석
### - 직원 이탈 예측하여, 이탈 저/중/고 위험도 분류하여 직원 유치
## ✅ 데이터셋 
### - 출처 
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
### - 설명 
###### 이 데이터셋은 IBM의 가상 인사 데이터를 기반으로 구축된 이직(Attrition) 예측 분석용 자료입니다. HR 부서가 직면하는 조직 내 이탈 문제를 해결하기 위해 설계되었으며, 개인 특성, 직무 정보, 근무 환경, 만족도, 성과, 보상 등 다양한 요소가 포함되어 있어 실무에 가까운 분석이 가능합니다.
### - 🎯 Target Variable
#### Attrition (범주형) : 이직 여부 (Yes: 이직, No: 재직)
--------------------------------------------------------------
# 📁 프로젝트 디렉토리 구조

```
  project/
  │
  ├── data/                    # 데이터셋 (크면 .gitignore)
  │   └── employees.csv
  │
  ├── models/                  # 학습된 모델 저장소
  │   └── churn_model.pkl
  │
  ├── notebooks/               # 분석, 실험용 노트북
  │   └── 01_EDA.ipynb
  │
  ├── app/                     # Streamlit 관련 모든 코드
  │   ├── __init__.py
  │   ├── main.py              # Streamlit 진입점 (streamlit run app/main.py)
  │   ├── pages/               # 여러 페이지 구성할 경우 사용 (Streamlit 1.10+)
  │   │   └── dashboard.py
  │   └── components/          # 그래프, 위젯 등 서브 컴포넌트
  │       ├── charts.py
  │       └── layout.py
  │
  ├── src/                     # ML/데이터 관련 로직
  │   ├── __init__.py
  │   ├── config.py
  │   ├── data_loader.py       # CSV 불러오기, 전처리
  │   ├── trainer.py           # 모델 학습
  │   ├── predictor.py         # 예측 로직 (model.predict)
  │   └── utils.py
  │
  ├── tests/                   # pytest 기반 테스트 코드
  │   ├── test_data_loader.py
  │   └── test_predictor.py
  │
  ├── requirements.txt         # 패키지 목록
  ├── README.md                # 프로젝트 설명
  ├── .gitignore               # 모델, 캐시, 데이터 제외
  └── run.sh                   # Streamlit 실행용 스크립트 (선택사항)
```
--------------------------------------------------------------
# 📊 탐색적 데이터 분석 (EDA)
## 1) 결측치 처리 및 불필요한 컬럼 제거
### - 결측치 처리
(1) **Attrition** : 예측 대상(Target)으로, 결측치는 분석 불가능 -> 결측행 제거 <br> 
(2) **TotalWorkingYears / YearsAtCompany** : 0으로 나누기 방지용 NaN 처리

### - 불필요한 컬럼 제거
| 컬럼명           | 설명                                      | 제거 사유 |
|------------------|-------------------------------------------|-----------|
| `EmployeeNumber` | 사번, 각 직원의 고유 식별자               | 모델이 단순 식별자에 과적합할 수 있어 제거 |
| `EmployeeCount`  | 모든 값이 동일한 상수 (예: 모두 1)         | 정보 제공 없음 (분산 = 0) |
| `Over18`         | 모든 값이 동일 ("Y")                      | 예측에 영향 없음 |
| `StandardHours`  | 모든 값이 동일 (예: 80시간)                | 실제 근무 시간과 무관, 예측 변수로 부적절 |

## 2) 주요 변수 선택 및 차원 축소
###### 모델의 성능을 높이기 위해 전체 변수 중 Target(Attrition)과의 중요성 분석을 수행하였습니다.<br> 
###### 분석 결과, target 값과 유의미한 중요성을 가지는 상위 15개 변수만 선별하였으며, 나머지 변수들은 예측 성능에 기여도가 낮다고 판단되어 제거하였습니다.
###### 📌 Feature Importance 분석 결과

| Feature                    | Importance |
|---------------------------|------------|
| JobLevel                  | 0.222696   |
| StockOptionLevel          | 0.141220   |
| OverTime                  | 0.078135   |
| YearsInCurrentRole        | 0.041642   |
| MaritalStatus             | 0.040173   |
| EnvironmentSatisfaction   | 0.040092   |
| JobRole                   | 0.036193   |
| Department                | 0.035971   |
| JobInvolvement            | 0.032841   |
| Age                       | 0.027762   |
| BusinessTravel            | 0.027067   |
| JobSatisfaction           | 0.026314   |
| WorkLifeBalance           | 0.024771   |
| YearsWithCurrManager      | 0.022859   |
| NumCompaniesWorked        | 0.019836   |
