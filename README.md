###### SK네트웍스 Family AI 캠프 13기
# **🚩IBM 직원 이탈 예측**
📅 개발 기간 : 2025.05.15 ~ 2025.05.16


## **📑 목차**
* [프로젝트 개요](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B0%9C%EC%9A%94)
   * [프로젝트 주제](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%A3%BC%EC%A0%9C)
   * [프로젝트 목표](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%AA%A9%ED%91%9C)
   * [데이터셋 소개](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B-%EC%86%8C%EA%B0%9C)
* [팀원 및 담당 업무](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%ED%8C%80%EC%9B%90-%EB%B0%8F-%EB%8B%B4%EB%8B%B9-%EC%97%85%EB%AC%B4)
   * [팀원 소개](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%ED%8C%80%EC%9B%90-%EC%86%8C%EA%B0%9C)
   * [담당 업무](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%EB%8B%B4%EB%8B%B9%EC%97%85%EB%AC%B4)
* [사용기술 스택](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%EA%B8%B0%EC%88%A0%EC%8A%A4%ED%83%9D)
* [프로젝트 디렉토리 구조](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC-%EA%B5%AC%EC%A1%B0)
* [탐색적 데이터 분석(EDA)](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%ED%83%90%EC%83%89%EC%A0%81-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D-eda)
    * [결측치 처리 및 불필요한 컬럼 제거](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#1-%EA%B2%B0%EC%B8%A1%EC%B9%98-%EC%B2%98%EB%A6%AC-%EB%B0%8F-%EB%B6%88%ED%95%84%EC%9A%94%ED%95%9C-%EC%BB%AC%EB%9F%BC-%EC%A0%9C%EA%B1%B0)
    * [주요 변수 선택 및 차원 축소](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#2-%EC%A3%BC%EC%9A%94-%EB%B3%80%EC%88%98-%EC%84%A0%ED%83%9D-%EB%B0%8F-%EC%B0%A8%EC%9B%90-%EC%B6%95%EC%86%8C)
    * [데이터 전처리](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#3-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EC%B2%98%EB%A6%AC)
* [모델링 및 성능 개선](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%EB%AA%A8%EB%8D%B8%EB%A7%81-%EB%B0%8F-%EC%84%B1%EB%8A%A5-%EA%B0%9C%EC%84%A0-%EA%B3%BC%EC%A0%95)
    * [초기 모델 성능 비교](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#%EF%B8%8F-%EC%B4%88%EA%B8%B0-%EB%AA%A8%EB%8D%B8%EB%A7%81---%EB%8B%A8%EC%88%9C-%ED%95%99%EC%8A%B5-smote-%EC%A0%81%EC%9A%A9-%EC%A0%84-column-drop-%EC%A0%84)
    * [SMOTE 적용 및 불균형 해결](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#%EF%B8%8F-%ED%81%B4%EB%9E%98%EC%8A%A4-%EB%B6%88%EA%B7%A0%ED%98%95-%EB%AC%B8%EC%A0%9C-%EC%9D%B8%EC%8B%9D---smote%EC%A0%81%EC%9A%A9-smote-%EC%A0%81%EC%9A%A9-%ED%9B%84-column-drop-%EC%A0%84)
    * [Feature Selection 적용](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#%EF%B8%8F-%EC%97%B0%EC%82%B0-%ED%9A%A8%EC%9C%A8%EC%84%B1%EA%B3%BC-%EA%B3%BC%EC%A0%81%ED%95%A9-%EB%B0%A9%EC%A7%80---columns-drop-%ED%9B%84-%ED%95%99%EC%8A%B5-smote-%EC%A0%81%EC%9A%A9-%ED%9B%84-column-drop-%ED%9B%84)
    * [최종 모델 선택 및 평가 지표](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%EC%B5%9C%EC%A2%85-%EC%84%A0%ED%83%9D-%EB%AA%A8%EB%8D%B8)
* [Streamlit 대시보드 구현](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-streamlit-%EA%B5%AC%ED%98%84)
* [인사이트 및 결론](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN13-2nd-6Team?tab=readme-ov-file#-%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%B0%8F-%EA%B2%B0%EB%A1%A0)


## **💡 프로젝트 개요**
### ✅ 프로젝트 주제
직원 이탈 원인 분석 및 이탈 예측
### ✅ 프로젝트 목표
- 직원 주요 이탈 요인 분석
- 이탈 확률을 통해, 저/중/고 위험도 분류하여 이탈 예측
### ✅ 데이터셋 소개
#### 📂 출처
<https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset>
#### 🧾 설명
이 데이터셋은 IBM의 가상 인사 데이터를 기반으로 구축된 이직(Attrition) 예측 분석용 자료입니다. HR 부서가 직면하는 조직 내 이탈 문제를 해결하기 위해 설계되었으며, 개인 특성, 직무 정보, 근무 환경, 만족도, 성과, 보상 등 다양한 요소가 포함되어 있어 실무에 가까운 분석이 가능합니다.
#### 🎯 Target Variable
  > Attrition (범주형) : 이직 여부 (Yes: 이직, No: 재직)


## **👤 팀원 및 담당 업무**
팀명 : 조이름추천해조
### **🥸 팀원 소개**
| 구자현 | 민경재 | 박현아 | 우지훈 |
|---|---|---|---|
| 🐶 | 🐱 | 🐰 | 🐼 |
|<a href="https://github.com/Koojh99"><img src="https://img.shields.io/badge/GitHub-Koojh99-FF585B?logo=github" alt="구자현 GitHub"/></a>|<a href="https://github.com/rudwo524"><img src="https://img.shields.io/badge/GitHub-rudwo524-FF585B?logo=github" alt="민경재 GitHub"/></a>|<a href="https://github.com/hyun-ah-0"><img src="https://img.shields.io/badge/GitHub-hyun--ah--0-5086C2?logo=github" alt="박현아 GitHub"/></a>|<a href="https://github.com/WooZhoon"><img src="https://img.shields.io/badge/GitHub-WooZhoon-1F1F1F?logo=github" alt="우지훈 GitHub"/></a>|
### **🧑‍💻 담당업무**
| 이름 | 역할 |
|---|---|
| 구자현 |모델 학습, 최종모델 선정, ReadMe작성 |
| 민경재 | 모델 학습 , Streamlit 구현, ReadMe작성 |
| 박현아 | 모델 학습, Streamlit 구현 |
| 우지훈 | 팀장, 데이터 전처리 및 모델 학습, 최종모델 선정 |


## **🔧 기술스택** 
![image](https://github.com/user-attachments/assets/4842b4d2-a7b6-4f79-9465-3b5baa632bb8)
![image](https://github.com/user-attachments/assets/edb303e4-5756-4267-999e-0473c443a5b9)
![image](https://github.com/user-attachments/assets/d34ac1d9-79ee-4db1-a6a1-5f7a155efeb4)
![image](https://github.com/user-attachments/assets/1ce88e67-ba26-4277-b1e6-790f4aa64e4f)

![image](https://github.com/user-attachments/assets/37e004cc-f457-48da-8e70-2c2467debf7a)
![image](https://github.com/user-attachments/assets/632c14c1-25ae-41eb-a83b-cf3750d9dcce)
![image](https://github.com/user-attachments/assets/818414e4-a71e-4189-b1dd-e8d01fac0c74)
![image](https://github.com/user-attachments/assets/85046805-be7a-490f-b5c0-0e9bae7b99e3)


## **📁 프로젝트 디렉토리 구조**
```
  project/
  │
  ├── data/                    # 데이터셋 (크면 .gitignore)
  │   ├── datasets.csv
  │   ├── trainset.csv
  │   └── testset.csv
  │
  ├── models/                  # 학습된 모델 저장소
  │   ├── gb_clf.pkl           
  │   ├── lgbm_clf.pkl
  │   ├── lr_clf.pkl
  │   ├── rf_clf.pkl
  │   └── xgb_clf.pkl
  │
  ├── notebooks/               # 분석, 실험용 노트북
  │   └── done.ipynb
  │
  ├── app/                     # Streamlit 관련 모든 코드
  │   ├── app.py               # Streamlit 진입점 (streamlit run app/main.py)
  │   └── pages/               # 여러 페이지 구성할 경우 사용 (Streamlit 1.10+)
  │       ├── 1_직원_퇴사_예측.py
  │       ├── 2_일괄_예측_조회.py
  │       └── 3_주요_변수간_상관관계.py
  │
  ├── utils/                   # ML/데이터 관련 로직
  │   ├── scaler.pkl           # scaler 파일
  │   └── utils.py             
  │
  ├── README.md                # 프로젝트 설명
  └── .gitignore               # 모델, 캐시, 데이터 제외
```


## **📊 탐색적 데이터 분석 (EDA)**
### 1) 결측치 처리 및 불필요한 컬럼 제거
#### 결측치 처리
> (1) **Attrition** : 예측 대상(Target)으로, 결측치는 분석 불가능 -> 결측행 제거 <br> 
> (2) **TotalWorkingYears / YearsAtCompany** : 0으로 나누기 방지용 NaN 처리

#### 불필요한 컬럼 제거
| 컬럼명           | 설명                                      | 제거 사유 |
|------------------|-------------------------------------------|-----------|
| `EmployeeNumber` | 사번, 각 직원의 고유 식별자                 | 모델이 단순 식별자에 과적합할 수 있어 제거 |
| `EmployeeCount`  | 모든 값이 동일한 상수 (예: 모두 1)          | 정보 제공 없음 (분산 = 0) |
| `Over18`         | 모든 값이 동일 ("Y")                       | 예측에 영향 없음 |
| `StandardHours`  | 모든 값이 동일 (예: 80시간)                | 실제 근무 시간과 무관, 예측 변수로 부적절 |

### 2) 주요 변수 선택 및 차원 축소
> 모델의 성능을 높이기 위해 전체 변수 중 Target(Attrition)과의 중요성 분석을 수행하였습니다.<br>
> 분석 결과, target 값과 유의미한 중요성을 가지는 상위 15개 변수만 선별하였으며, 나머지 변수들은 예측 성능에 기여도가 낮다고 판단되어 제거하였습니다.
#### **📌 Feature Importance 분석 결과**
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

### 3) 데이터 전처리
* 원-핫 인코딩(One-Hot Encoding) : ❌
* 라벨 인코딩(Label Encoding)

| Feature                    | 설명 |매핑방식|
|---------------------------|------------------|-----------------|
| Attrition                  | 퇴사 여부 (Yes->1, No->0)  | 직접처리|
| OverTime          | 초과 근무 여부 (Yes->1, No->0)   | ManualMapper| 
| BusinessTravel                  | 출장 빈도 (Travel_Rarely → 2, Travel_Frequently → 3, Non-Travel → 4)  | ManualMapper|
| MaritalStatus        | 결혼 상태 (	Single → 2, Married → 3, Divorced → 4) | ManualMapper|
| Department             | 부서 (Sales → 2, Human Resources → 3, Research & Development → 4)  | ManualMapper|
| JobRole   | 직무 (다양한 직무를 2~4 사이 값으로 라벨 매핑)   | ManualMapper |


## **🧪 모델링 및 성능 개선 과정**
### **⚙️ 초기 모델링 - 단순 학습 (SMOTE 적용 전, column drop 전)**
처음에 전체 데이터를 그대로 활용하여, 전처리만 수행한 뒤 다양한 분류 모델 학습
#### < 모델 성능 비교 및 분석 > 
| model                    | accuracy |
|---------------------------|------------|
|            Logistic Regression       | 	0.8741   |
| Random Forest         | 0.8605   |
| Gradient Boosting                  | 0.8605   |
| LightGBM        | 0.8469   |
| XGBoost             | 0.8571   |

📈 모델 성능은 전반적으로 나쁘지 않지만, 실제 분류 문제에서 단순 정확도만으로 판단하는 것으로 위험할 수 있다고 판단과 성능 개선을 위해 후속 분석 수행.
#### **🔍  성능 개선**
클래스 비율 확인
```python
# 이직 여부 분포 확인
df['Attrition'].value_counts(normalize=True).plot.pie(autopct='%1.1f%%')
```
![image](https://github.com/user-attachments/assets/07672410-0e02-4007-be4d-3200ea0d485b)

✅ 이직한 사람: 약 16% <br>
✅ 재직 중인 사람: 약 84%
* Target(Attrition)의 분포를 확인해보니 클래스 불균형이 매우 심각함
* 모델이 'No'로만 예측해도 약 84% 정확도를 달성할 수 있었기에, 이는 불균형으로 인한 과대평가된 성능이라 판단

### **⚙️ 클래스 불균형 문제 인식 - SMOTE적용 (SMOTE 적용 후, column drop 전)**
#### 🔧 SMOTE 적용을 통한 데이터 균형 조정
```python
from imblearn.over_sampling import SMOTE

X = pd.DataFrame(norm_df.drop(columns='Attrition'))
Y = pd.DataFrame(norm_df.Attrition).values.reshape(-1, 1)
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)
```
* SMOTE(Synthetic Minority Over-sampling Technique) 기법 도입 
* SMOTE기법을 도입하여 minority 클래스인 'Yes(이직)'에 해당하는 샘플을 오버샘플링 
* SMOTE 적용 후, 이직/재직 클래스 비율 1:1로 조정됨

#### < 모델 성능 비교 및 분석 > 
| model                    | accuracy |
|---------------------------|------------|
|            Logistic Regression       | 	0.8036   |
| Random Forest         | 0.9393   |
| Gradient Boosting                  | 0.9211   |
| LightGBM        | 0.9312   |
| XGBoost             | 0.9332   |

📈 SMOTE적용 이후 전반적으로 모든 모델의 성능이 눈에 띄게 향상되었으며, 특히 **Random Forest 모델**은 약94%의 정확도를 기록하여 가장 우수한 성능을 보임

#### 🔍  성능 개선
* SMOTE 적용만으로도 상당한 성능 향상을 이끌어냈지만, 추가적으로 모델의 연산 효율성과 일반화 성능을 향상시키기 위해 Feature Selection을 진행
* 앞서 수행한 EDA과정에서, 전체 피처들 중에서 Attrition 예측에 유의미한 영향을 주는 상위 15개 변수만 선별하였고, 정보가 거의 없거나 모델에 불필요한 노이즈가 될 수 있는 컬럼 확인.
```python
# 중요도 추출
importances = model.feature_importances_
feature_names = X.columns

# 결과 정리 및 정렬
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

top_features = feature_importance_df.head(15)
```

#### 📌 Feature Importance 분석 결과
![image](https://github.com/user-attachments/assets/b9f0f5ed-4bec-41e8-b9ef-efe5c4f640f0)

### **⚙️ 연산 효율성과 과적합 방지 - columns drop 후 학습 (SMOTE 적용 후, column drop 후)**
#### < 모델 성능 비교 및 분석 > 
| model                    | accuracy |
|---------------------------|------------|
|            Logistic Regression       | 	0.7854  |
| Random Forest         | 0.9473   |
| Gradient Boosting                  | 0.9170   |
| LightGBM        | 0.9109   |
| XGBoost             | 0.9089   |

📈 columns drop 이후에도 Random Forest는 여전히 가장 우수한 성능을 유지했으며, 전체적으로 SMOTE + Feature Selection 조합이 모델 성능과 효율성 모두에 긍정적인 효과를 준 것으로 확인

### **📌 최종 선택 모델**
> RandomForestClassifier
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score

# 모델 학습
rf_clf = RandomForestClassifier(random_state=42)
rf_clf.fit(X_train, y_train)

# 예측
y_pred_rf = rf_clf.predict(X_test)

# 평가 지표 출력
accuracy = accuracy_score(y_test, y_pred_rf)
recall = recall_score(y_test, y_pred_rf)
f1 = f1_score(y_test, y_pred_rf)

print(f"✅ Random Forest 성능 지표")
print(f"Accuracy : {accuracy:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1-score : {f1:.4f}")
```
#### **✅ Random Forest 성능 지표**
|scoring|value|
|---|---|
|Accuracy | 0.9473|
|Recall   | 0.9205|
|F1-score | 0.9419|

```python
cm = confusion_matrix(y_test, y_pred_rf)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No", "Yes"], yticklabels=["No", "Yes"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title(f"Confusion Matrix (rf)")
plt.tight_layout()
plt.savefig('Confusion Matrix (rf).png')
plt.show()
```
![image](https://github.com/user-attachments/assets/5464ebea-b32e-4e88-9229-d4f73c0586c9)

```python
from sklearn.metrics import roc_auc_score

# 양성 클래스(Attrition = 1)에 대한 확률 예측
y_proba = rf_clf.predict_proba(X_test)[:, 1]

# ROC-AUC 점수 계산
roc_auc = roc_auc_score(y_test, y_proba)

print(f"✅ ROC-AUC score: {roc_auc:.4f}")
```
✅ ROC-AUC score: 0.9855


## **🚀 Streamlit 구현**
### run
```bash
streamlit run app.py
```
### main page
앱 실행 시 초기 진입 화면에 표시되는 메인 페이지 구성 요소입니다:
> 1. 페이지 설정: 페이지 제목 : 👩‍💼 직원 이탈 예측 시스템
> 2. 기본 통계 카드 (3컬럼 레이아웃) : 총 인원 수, 이직률, 평균 나이
> 3. 이직/잔류 파이 차트 : 파이차트를 이용해 Attrition 분포 시각화
> 4. 페이지 이동 안내
> 5. 사이드바 메뉴(직원 퇴사 예측/ 상관관계 분석 / 대량 예측) 사용 안내 메시지 출력

![Image](https://github.com/user-attachments/assets/49f19cc0-9ee6-4992-98a9-56694c86d9ea)

### page 1: 직원 퇴사 예측 페이지
사전 학습된 RandomForest 모델과 전처리 파이프라인을 활용하여 직원 정보의 입력값을 받아 이탈 예측을 수행합니다. 특성 중요도 기준으로 상위 15개의 특성을 입력할 수 있습니다. 퇴사 가능성의 시각화된 정보와 만일 퇴사 가능성이 높다면 해당 직원의 퇴사 주요 요인을 제공합니다.
#### **주요 기능**
- 입력값 받기: 특성 중요도 기준 상위 15개 특성에 대한 직원의 정보를 직접 입력
- 데이터 전처리: utils.py의 mapping 함수로 범주형 인코딩 수행
- 정규화: 학습 시 사용된 scaler.pkl 스케일러 적용
- 모델 예측: rf_clf.pkl(RandomForest 분류기)를 로드하여 이탈 가능성인 퇴사 가능성 생성
- 위험 등급: 확률에 따라 안정/주의/위험 등급(Grade) 부여
- 시각화: 퇴사 가능성과 위험 등급을 직관적으로 표시
- 주요 요인 추출: 퇴사 가능성의 등급이 주의 혹은 위험이라면 중요도가 높은 특성 출력
  
![Image](https://github.com/user-attachments/assets/41556142-c754-4b42-a0e3-cbea77d9f583)
![Image](https://github.com/user-attachments/assets/d7e15e52-f5f3-42bd-961e-2359c95e329f)
![Image](https://github.com/user-attachments/assets/7a57e871-510c-4c51-921c-6606be34fc54)
![Image](https://github.com/user-attachments/assets/f3953db2-91f6-4409-ab96-f7c2682d40aa)
![Image](https://github.com/user-attachments/assets/6138c550-a65a-4b54-97e0-15779fbf74be)

### page 2: 일괄 예측 조회 페이지
사전 학습된 RandomForest 모델과 전처리 파이프라인을 활용하여 대규모 직원 이탈 예측을 수행합니다. 사용자는 전처리된 CSV 파일을 업로드하면, 자동으로 불필요 컬럼 제거, 매핑, 정규화를 거쳐 이탈 확률을 계산하고, 상위 20명의 고위험 직원 정보를 제공합니다.
#### **주요 기능**
- 데이터 전처리: utils.py의 drop_unnecessary_col과 mapping 함수로 불필요 컬럼 제거 및 범주형 인코딩 수행
- 정규화: 학습 시 사용된 scaler.pkl 스케일러 적용
- 모델 예측: rf_clf.pkl(RandomForest 분류기)를 로드하여 이탈 확률(Attrition_Prob) 및 예측(Pred) 생성
- 위험 등급: 확률에 따라 High/Medium/Low 등급(Grade) 부여
- Top 20 추출: 이탈 확률 상위 20명 테이블 출력
- 결과 다운로드: 전체 예측 결과를 📥 결과 다운로드 버튼으로 CSV 파일로 저장 가능
  
![Image](https://github.com/user-attachments/assets/ded1c720-2452-448f-afd2-34317f27d434)
![Image](https://github.com/user-attachments/assets/154c6b46-183c-441e-b87d-909b25ff3384)
![Image](https://github.com/user-attachments/assets/395853e7-6078-4499-9359-308433edb18e)

### page 3: 주요 변수간 상관관계 페이지
사전 학습된 RandomForest 모델과 전처리 파이프라인을 바탕으로 주요 변수간의 상관 관계를 시각화하여 제공합니다. 사용자는 선택한 feature의 상관관계가 높은 5개를 막대그래프로 확인할 수 있습니다. 또한, 전체 특성 간의 히트맵을 확인할 수 있습니다. 
#### 주요 기능
- 상관계수 계산: 15개의 주요 피처 간 Pearson 상관계수를 계산
- 시각화: 상관관계 분석 페이지 구현과 사용 방법, 사용자가 선택한 기준 피처와 나머지 14개의 feature 중 Top 5 상관 관계를 막대 그래프로 시각화
- 히트맵: 전체 피처 간 히트맵을 Plotly로 표시

![Image](https://github.com/user-attachments/assets/910f466c-962b-400f-ba9d-e4002b464acf)
![Image](https://github.com/user-attachments/assets/9680e62d-27ce-47e4-8e5d-987da2462049)


## **🔍 인사이트 및 결론**
### 주요 인사이트
**1. 클래스 불균형 문제 해결이 성능 향상에 결정적**

초기에 SMOTE(Synthetic Minority Over-sampling Technique)를 적용하지 않았을 때는 이탈 클래스(Attrition=1)의 수가 적어 모델이 해당 케이스를 거의 학습하지 못했습니다.<br>
<ins>**SMOTE** 적용 이후, **accuracy가 크게 개선**되었으며, 특히 이탈자 탐지 **성능이 향상**되어 업무 적용 가능성이 높아졌습니다.</ins>

**2. 불필요한 변수 제거는 학습 효율 및 해석력 향상에 기여**

Feature Importance 분석을 통해 상위 15개 중요 변수만 선별하여 모델을 재학습한 결과, 약간의 성능 저하(Accuracy 감소)는 있었으나, 모델이 보다 명확한 변수에 집중하게 되어 모델 해석력과 속도가 향상되었습니다.

**3. Random Forest 모델이 높은 성능을 보임**

다양한 모델을 비교한 결과, RandomForestClassifier가 전반적으로 가장 높은 Accuracy, Recall, F1-score, ROC-AUC를 보여 실제 업무에 적용 가능한 수준의 예측력을 갖추었습니다.

### 결론 및 시사점
**SMOTE와 같은 데이터 불균형 처리 기법은 HR 데이터 분석에 필수적인 전처리 요소임을 확인하였습니다.**

분석 결과에 따르면, JobLevel, OverTime, JobInvolvement, Age 등은 이직 가능성과 높은 상관관계를 가지므로, HR 전략 수립에 있어 주요 관리 지표로 고려될 수 있습니다.<br>
최종적으로 개발한 예측 모델 streamlit을 통해 직관적인 시각화 및 사용자 친화적인 예측 도구로 구현되어, 직원마다 이탈율을 예측하여 저/중/고 위험도 분류하여 관리 가능하게 될 수 있습니다.

---
### **📖 회고록**
구자현
> 이번 프로젝트를 통해, 초기 데이터 전처리부터 모델링, 평가 및 시각화까지 전체 흐름을 수행하면서 실제 실무 적용 가능성을 고려한 분석 사고력을 키울 수 있었습니다. 특히, 다양한 모델을 실험하면서 단순히 정확도에만 의존해서는 안된다는 점과 클래스 불균형 문제에 대응하기 위한 SMOTE 등의 기법이 실제 예측 성능에 큰 영향을 미친다는 사실을 배울 수 있는 프로젝트가 된 것 같습니다.

민경재
> 이번 프로젝트를 통해 Attrition데이터를 활용하여 전처리, 모델링, 평가, 시각화 및 화면 구현까지 하는 전체 흐름을 익힐 수 있었습니다. 그리고 SMOTE 기법을 활용하여 보다 더  좋은 예측을 할 수 있었습니다. 불과 2일밖에 안 되는 시간이었지만 좋은 팀원들 덕분에 잘 마무리할 수 있었던 것 같습니다.

박현아
> 모델 학습과 다양한 streamlit 구현을 해볼 수 있는 기회였습니다. 데이터 모델링부터 쉬운 과정 하나 없었지만 팀원들 덕분에 프로젝트를 무사히 잘 마칠 수 있었다고 생각합니다. 생각보다 시간이 촉박했지만, 팀원들 덕에 좋은 결과를 만들 수 있었다고 생각합니다. 다들너무 죄송하고 감사해요 정말...

우지훈
> 데이터의 수가 부족하고 데이터의 분포 자체가 불균형이 심한 데이터 셋의 문제를 해결할 수 있는 방법인 SMOTE라는 기술을 알게 되는 기회였습니다. 머신러닝의 데이터 전처리부터 성능 향상까지 많은 것을 배우게 되었습니다. **우리 팀원들이 최고!** 멋지다 6조~
