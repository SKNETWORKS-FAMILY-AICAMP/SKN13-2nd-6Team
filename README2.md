## Streamlit

### 디렉토리 구조



project/
├─ app.py                 # Streamlit 앱 실행 스크립트
├─ tools.py               # 전처리 유틸리티 함수
├─ notebooks/
│  └─ test/test_test/
│     ├─ xgb_clf.pkl       # 학습된 XGBoost 모델
│     └─ dummy_scaler.pkl  # 학습된 스케일러
├─ data/                  # 사용자 업로드 CSV 저장(없을 시 업로드)
├─ README.md              # 프로젝트 설명 문서
└─ requirements.txt       # 의존성 목록

실행
streamlit run app.py

### main page

### page 1

### page 2

### page 3

이 Streamlit 페이지는 사전 학습된 XGBoost 모델과 전처리 파이프라인을 활용하여 대규모 직원 이탈 예측을 수행합니다. 사용자는 전처리된 CSV 파일을 업로드하면, 자동으로 불필요 컬럼 제거, 매핑, 정규화를 거쳐 이탈 확률을 계산하고, 상위 20명의 고위험 직원 정보를 제공합니다.

#### 주요 기능

- 데이터 전처리: tools.py의 drop_unnecessary_col과 mapping 함수로 불필요 컬럼 제거 및 범주형 인코딩 수행
- 정규화: 학습 시 사용된 dummy_scaler.pkl 스케일러 적용
- 모델 예측: xgb_clf.pkl XGBoost 분류기를 로드하여 이탈 확률(Attrition_Prob) 및 예측(Pred) 생성
- 위험 등급: 확률에 따라 High/Medium/Low 등급(Grade) 부여
- Top 20 추출: 이탈 확률 상위 20명 테이블 출력
- 결과 다운로드: 전체 예측 결과 CSV 파일로 저장 가능

#### user

- 브라우저에서 나타나는 UI에서 대량 데이터 파일 업로드 클릭 -> 전처리된 CSV 파일 선택
- 자동 전처리 → 예측 → Top 20 이탈 확률 높은 대상 테이블 확인
- 📥 결과 다운로드 버튼으로 전체 결과 저장
