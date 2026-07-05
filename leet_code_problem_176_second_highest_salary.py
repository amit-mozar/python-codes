import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    second_rank = employee['salary'].sort_values(ascending = False).unique()
    df = pd.DataFrame()
    print(len(second_rank))
    if len(second_rank) > 1:
        df['SecondHighestSalary'] = [second_rank[1]]
    else:
        df['SecondHighestSalary'] = [np.NaN]
    print(employee['salary'].nlargest(2).iloc[-1])
    return df[['SecondHighestSalary']]