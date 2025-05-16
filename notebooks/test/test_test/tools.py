def drop_unnecessary_col(data):
    unnecessary_features = [
        'Over18',
        'EmployeeNumber',
        'EmployeeCount',
        'StandardHours',
        'MonthlyIncome',
        'YearsInCurrentRole',
        'YearsAtCompany',
        'YearsWithCurrManager',
        "TotalWorkingYears",
        "TrainingTimesLastYear",
        "DistanceFromHome",
        "EducationField",
        "MonthlyRate",
        "HourlyRate",
        "YearsSinceLastPromotion",
        "PerformanceRating",
        "PercentSalaryHike",
        "DailyRate",
        "Gender"
    ]
    data = data.drop(columns=unnecessary_features,axis=1)
    return data

def mapping_for_page_1(input_df):
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
    return input_df

def mapping(data):
    data['OverTime'] = data['OverTime'].map({'Yes':1,'No':0})

    data['BusinessTravel'] = data['BusinessTravel'].map({
        'Travel_Rarely':2,
        'Travel_Frequently':3,
        'Non-Travel':4
    })

    data['MaritalStatus'] = data['MaritalStatus'].map({
        'Single':2,
        'Married':3,
        'Divorced':4
    })

    data['Department'] = data['Department'].map({
        'Sales':2,
        'Human Resources':3,
        'Research & Development':4
    })

    data['JobRole'] = data['JobRole'].map({
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

    return data