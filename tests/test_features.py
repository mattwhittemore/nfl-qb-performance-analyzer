import pandas as pd
from src.app_utils import engineer_features

def test_engineer_features():
    df = pd.DataFrame({'Attempts':[10,0],'Completions':[6,0],'Yards':[80,0],'TD':[1,0],'INT':[0,0],'Sacks':[1,0],'Player':['A','B'],'Team':['X','Y'],'Year':[2024,2024],'QBRating':[95.0,0.0]})
    out = engineer_features(df)
    assert 'efficiency_score' in out.columns
    assert out['yards_per_att'].iloc[1] == 0
