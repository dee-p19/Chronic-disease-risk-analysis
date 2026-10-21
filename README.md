# Chronic Disease Risk Analysis — Tableau + Flask Starter

## Included
- `patient_health_synthetic.csv`: 500 synthetic patient records for demonstration only.
- `app.py`: Flask dashboard with four interactive Plotly charts and an age-group filter.
- `templates/index.html`: responsive dashboard UI.
- `requirements.txt`: Python dependencies.
- `PROJECT_DOCUMENTATION.md`: build steps, Tableau worksheet/dashboard/story plan, testing checklist and demo script.

## Run the web prototype
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Create a virtual environment (optional but recommended):
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Open the local URL printed in the terminal (usually http://127.0.0.1:5000).

## Tableau in the one-hour version
1. Open Tableau Public/Desktop and connect to `patient_health_synthetic.csv`.
2. Create calculated fields as documented.
3. Build worksheets and a dashboard following the checklist in `PROJECT_DOCUMENTATION.md`.
4. Publish only if appropriate for your data/privacy requirements.
5. If publishing is not feasible in time, demonstrate the Flask prototype and clearly describe Tableau publishing as the remaining integration step.

The Flask charts are Plotly charts; they are not embedded Tableau views. To embed Tableau, publish a workbook and replace the placeholder/integration area with Tableau's official embed code or a trusted Tableau embed URL.

## Tableau Dashboard

**Project:** Chronic Disease Risk Analysis

**Tableau Public Dashboard:**   https://public.tableau.com/authoring/ChronicDiseaseRiskAnalysisDashboard/Dashboard1#1

## Project Demo Video

Demo video: https://drive.google.com/file/d/1gXMSVa4OPMnXJDVYjrGPO06wdqyVOHdW/view?usp=drivesdk

## Technologies Used

- Python
- Flask
- Pandas
- Plotly
- Tableau Public
- HTML and CSS

## Project Overview

This project explores synthetic patient health data to visualize
patterns associated with heart disease, diabetes, and stroke.

The dashboard includes disease analysis and comparisons of patient
health indicators.

**Disclaimer:** The dataset is synthetic and the visualizations
are for educational purposes only.
