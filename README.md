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
#### 직원 이탈 원인 분석 및 이탈 예측
## ✅ 프로젝트 목표
#### - 직원 주요 이탈 요인 분석
#### - 이탈 확률을 통해, 저/중/고 위험도 분류하여 이탈 예측
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

## 3) 데이터 전처리
###### (1) 원-핫 인코딩(One-Hot Encoding) : ❌
###### (2) 라벨 인코딩(Label Encoding)

| Feature                    | 설명 |매핑방식|
|---------------------------|------------------|-----------------|
| Attrition                  | 퇴사 여부 (Yes->1, No->0)  | 직접처리|
| OverTime          | 초과 근무 여부 (Yes->1, No->0)   | ManualMapper| 
| BusinessTravel                  | 출장 빈도 (Travel_Rarely → 2, Travel_Frequently → 3, Non-Travel → 4)  | ManualMapper|
| MaritalStatus        | 결혼 상태 (	Single → 2, Married → 3, Divorced → 4) | ManualMapper|
| Department             | 부서 (Sales → 2, Human Resources → 3, Research & Development → 4)  | ManualMapper|
| JobRole   | 직무 (다양한 직무를 2~4 사이 값으로 라벨 매핑)   | ManualMapper |

--------------------------------------------------------------
# 🧪 모델링 및 성능 개선 과정
## ⚙️ 1. 초기 모델링 - 단순 학습 (SMOTE 적용 전, column drop 전)
##### 처음에 전체 데이터를 그대로 활용하여, 전처리만 수행한 뒤 다양한 분류 모델 학습
##### < 모델 성능 비교 및 분석 > 
| model                    | accuracy |
|---------------------------|------------|
|            Logistic Regression       | 	0.8741   |
| Random Forest         | 0.8605   |
| Gradient Boosting                  | 0.8605   |
| LightGBM        | 0.8469   |
| XGBoost             | 0.8571   |

##### 📈 모델 성능은 전반적으로 나쁘지 않지만, 실제 분류 문제에서 단순 정확도만으로 판단하는 것으로 위험할 수 있다고 판단과 성능 개선을 위해 후속 분석 수행.
## 🔍  성능 개선 
#### 클래스 비율 확인
```
# 이직 여부 분포 확인
df['Attrition'].value_counts(normalize=True).plot.pie(autopct='%1.1f%%')
```
![image](https://github.com/user-attachments/assets/07672410-0e02-4007-be4d-3200ea0d485b)
##### ✅ 이직한 사람: 약 16%
##### ✅ 재직 중인 사람: 약 84%
##### ● Target(Attrition)의 분포를 확인해보니 클래스 불균형이 매우 심각함
##### ● 모델이 'No'로만 예측해도 약 84% 정확도를 달성할 수 있었기에, 이는 불균형으로 인한 과대평가된 성능이라 판단 <br>

## ⚙️ 2. 클래스 불균형 문제 인식 - SMOTE적용 (SMOTE 적용 후, column drop 전)
## 🔧 SMOTE 적용을 통한 데이터 균형 조정
```
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)
```
##### ● SMOTE(Synthetic Minority Over-sampling Technique) 기법 도입 
##### ● SMOTE기법을 도입하여 minority 클래스인 'Yes(이직)'에 해당하는 샘플을 오버샘플링 
##### ● SMOTE 적용 후, 이직/재직 클래스 비율 1:1로 조정됨
##### < 모델 성능 비교 및 분석 > 
| model                    | accuracy |
|---------------------------|------------|
|            Logistic Regression       | 	0.8036   |
| Random Forest         | 0.9393   |
| Gradient Boosting                  | 0.9211   |
| LightGBM        | 0.9312   |
| XGBoost             | 0.9332   |

##### 📈SMOTE적용 이후 전반적으로 모든 모델의 성능이 눈에 띄게 향상되었으며, 특히 **Random Forest 모델**은 약94%의 정확도를 기록하여 가장 우수한 성능을 보임
--------------------------------------------------------------


### < 이후 과정 >
### 모델 -> 클래스 불균형때문에 정확도 낮음 (파이 그래프로 클래스 비율 시각화) -> SMOTE 사용이후 모델 -> 모델 중 가장 높은 성능 보이는 것 선정 -> streamlit 구현 화면  -> 인사이트 및 결론 -> + 회고록
