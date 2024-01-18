import pandas as pd

points_list = [0] * 4

def result_deco(func):
    def wrapper(*args, **kwargs):
        global points_list
        question_no, points, result = func(*args, **kwargs)
        if result:
            points_list[question_no] = points
            print(f'정답입니다! {points}점 누적 되었습니다!')
        else:
            points_list[question_no] = 0
            print('오답입니다. 다시 한번 확인해주세요.')        

        print('현재 누적 점수:', sum(points_list), '/ 100')
        
    return wrapper

# 문제 1
@result_deco
def check_01(df: pd.core.frame.DataFrame):
    question_no, points = 0, 30

    condition_dict = {
        'condition01': len(df) == 10,
        'condition02': df.개봉일.is_monotonic_increasing,
        'condition03': df.iloc[-2:].순위.is_monotonic_decreasing,
        'condition04': df.순위증감.apply(lambda x: bool('(' in x)).sum() == 0,
        'condition05': (df.순위증감 == 'new').sum() == 2,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 문제 2
@result_deco
def check_02(df: pd.core.frame.DataFrame):
    question_no, points = 1, 30

    condition_dict = {
        'condition01': len(df) == 500,
        'condition02': df.주.is_monotonic_increasing,
        'condition03': df.순위.iloc[:10].apply(lambda x: int(x[:-1])).is_monotonic_increasing,
        'condition04': df.index.is_monotonic_increasing,
        'condition05': (df.순위증감 == 'new').sum() == 194,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 문제 3-1
@result_deco
def check_03_01(df: pd.core.frame.DataFrame):
    question_no, points = 2, 20

    condition_dict = {
        'condition01': df.duplicated(keep=False).sum() == 15,
        'condition02': df[df.빈도 == 6].빈도.is_monotonic_increasing,
        'condition03': df.빈도.to_list()[:3] == [12, 11, 8],
        'condition04': sum([bool('(디지털)' not in idx) for idx in df.index]) == 2,
        'condition05': df.index[3] == '싱크홀(2021)',
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 문제 3-2
@result_deco
def check_03_02(df: pd.core.frame.DataFrame):
    question_no, points = 3, 20

    condition_dict = {
        'condition01': df.예매점유율.duplicated(keep=False).sum() == 88,
        'condition02': df[df.예매점유율 == '0.70%'].index.is_monotonic_increasing,
        'condition03': df.iloc[25, 0] == '14.00%',
        'condition04': df.예매점유율.apply(lambda x: float(x.replace('%', ''))).is_monotonic_decreasing,
        'condition05': df.예매점유율.apply(lambda x: len(x[x.find('.')+1:-1]) != 2).sum() == 0,
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result