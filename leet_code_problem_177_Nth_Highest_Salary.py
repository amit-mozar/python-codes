import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    rank = employee['salary'].sort_values(ascending = False).unique()
    df = pd.DataFrame()
    if N <= len(rank) and N > 0:
        nth_rank = rank[N-1]
        df[f'getNthHighestSalary({N})'] = [nth_rank]
    else:
        df[f'getNthHighestSalary({N})'] = [np.NaN]
    return df