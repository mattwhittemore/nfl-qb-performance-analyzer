import numpy as np
import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    attempts = out["Attempts"].replace(0, np.nan)
    out["yards_per_att"] = (out["Yards"] / attempts).fillna(0)
    out["td_rate"] = (out["TD"] / attempts).fillna(0)
    out["int_rate"] = (out["INT"] / attempts).fillna(0)
    out["efficiency_score"] = (
        0.35 * out["yards_per_att"] + 0.55 * out["td_rate"] - 0.25 * out["int_rate"]
    )
    return out
