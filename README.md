# NFL QB Analyzer

## How to run

> Requires Python 3.x

```bash
# 1) Get the code
git clone https://github.com/mattwhittemore/nfl-qb-performance-analyzer.git && cd nfl-qb-performance-analyzer

# 2) Create & activate a virtual environment
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1

# 3) Install & run
pip install -r requirements.txt
streamlit run app.py
