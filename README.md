# HealthMate (Flask Web App)

A simple, privacy-friendly health web app with calculators for BMI, WHR, BMR, Stroke Risk (simplified), and Arthritis screening. Results are stored in a local SQLite database.

## Features
- BMI with WHO categories
- WHR (gender-specific thresholds)
- BMR (Mifflin–St Jeor)
- Stroke risk awareness score (simplified)
- Arthritis screening score
- History page (saved to SQLite)

## Quickstart

```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the app
python app.py

# 4) Open in your browser
http://127.0.0.1:5000
```

> Default DB file: `healthmate.db` (auto-created).  
> Change the Flask `SECRET_KEY` in `app.py` before deploying publicly.

## Notes
- These tools are **educational/awareness** aids, not medical diagnoses.
- You can extend with authentication, charts, or APIs later.