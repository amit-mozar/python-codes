import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by = 'score', ascending = False)
    rank_map = {score:i+1 for i, score in enumerate(scores['score'].unique())}
    scores['rank'] = scores['score'].map(rank_map)
    print(scores)
    return scores[['score', 'rank']]