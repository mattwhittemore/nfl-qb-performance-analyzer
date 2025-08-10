import pandas as pd
import streamlit as st
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from src.app_utils import engineer_features

st.set_page_config(page_title="NFL QB Analyzer")

df = pd.read_csv("data/qb_sample.csv")
df = engineer_features(df)
features = [
    "Attempts",
    "Completions",
    "Yards",
    "TD",
    "INT",
    "Sacks",
    "yards_per_att",
    "td_rate",
    "int_rate",
]
X, y = df[features].fillna(0), df["QBRating"].fillna(0)
if len(df) > 10:
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)
    model = RidgeCV(alphas=[0.1, 1.0, 10.0]).fit(Xtr, ytr)
    r2 = r2_score(yte, model.predict(Xte))
    st.write(f"Model R²: **{r2:.3f}**")
else:
    model = RidgeCV(alphas=[1.0]).fit(X, y)

ranked = df.copy()
ranked["ModelScore"] = model.predict(X)
st.title("NFL QB Performance Analyzer")
st.dataframe(ranked[["Player", "Team", "Year", "efficiency_score", "ModelScore", "QBRating"]])
