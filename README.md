# SKN13-2nd-6Team

repo 구상
```
churn-predictor/
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
