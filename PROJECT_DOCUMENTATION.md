# Project Documentation
## Title
Chronic Disease Risk Analysis and Visualization Using Tableau and Flask

## 1. Problem statement
Chronic diseases such as heart disease, diabetes, and stroke are influenced by multiple demographic, clinical, and lifestyle factors. Manually reviewing patient-level data makes it difficult to compare groups and communicate trends. This project prepares a dataset and presents disease prevalence, age-group comparisons, BMI comparisons, and exercise-level comparisons through visual dashboards.

## 2. Objectives
- Prepare a structured patient health dataset for visualization.
- Compare the prevalence of three disease outcomes.
- Explore patterns by age group, BMI category, and exercise level.
- Provide interactive filtering and KPI summaries.
- Demonstrate a responsive web dashboard and document the Tableau workflow.

## 3. Technical architecture
Synthetic CSV → Pandas data preparation / Tableau data connection → Tableau worksheets → Tableau dashboard → Tableau story → publishing → optional Tableau embed in Flask.
A Flask prototype is included to provide a working web demonstration. Its Plotly charts are a separate implementation and do not constitute an embedded Tableau workbook.

## 4. Dataset and preparation
File: `patient_health_synthetic.csv` (500 rows).
Fields: Patient_ID, Age, Sex, BMI, Systolic_BP, Cholesterol, Glucose, Smoking, Alcohol_Use, Exercise_Level, Fatigue, Chest_Pain, Dizziness, Heart_Disease, Diabetes, Stroke.
The dataset is synthetic and algorithmically generated for demonstration. It is not collected from real patients and should not be used to draw medical conclusions.
Preparation tasks: check field types, inspect missing values, remove duplicates if present, confirm binary outcomes are 0/1, create age bands and BMI categories, and verify that measures aggregate correctly.

## 5. Tableau calculated fields
**Age Group**
```
IF [Age] < 30 THEN "18–29"
ELSEIF [Age] < 40 THEN "30–39"
ELSEIF [Age] < 50 THEN "40–49"
ELSEIF [Age] < 60 THEN "50–59"
ELSEIF [Age] < 70 THEN "60–69"
ELSE "70+"
END
```
**BMI Category**
```
IF [BMI] < 18.5 THEN "Underweight"
ELSEIF [BMI] < 25 THEN "Normal"
ELSEIF [BMI] < 30 THEN "Overweight"
ELSE "Obese"
END
```
**Heart Disease Prevalence**
```
AVG(INT([Heart_Disease])) * 100
```
Similarly use `AVG(INT([Diabetes])) * 100` and `AVG(INT([Stroke])) * 100`. If the source fields are already numeric, use `AVG([Heart_Disease]) * 100` etc.

## 6. Recommended Tableau worksheets (at least 5)
1. KPI — patient count: `COUNTD([Patient_ID])`.
2. Disease prevalence — bar chart using average of each binary outcome.
3. Disease prevalence by Age Group — age group on Columns, prevalence on Rows, disease as color.
4. Disease prevalence by BMI Category — BMI category on Columns, prevalence on Rows, disease as color.
5. Exercise Level vs Disease — exercise level on Columns and prevalence on Rows.
6. Risk-factor heatmap — Smoking or Exercise Level vs Age Group; color by disease prevalence.
7. Clinical indicators — scatter plot of BMI vs Glucose, color by Diabetes (exploratory only).

## 7. Dashboard design
- Title: Chronic Disease Risk Analysis.
- Top row: total patients, heart disease %, diabetes %, stroke %.
- Middle row: disease prevalence and age-group trend.
- Bottom row: BMI category and exercise-level comparisons.
- Filters: Age Group, Sex, Smoking, Exercise Level.
- Keep consistent fonts, concise titles, readable labels, and tooltips. Use tiled layout and test at laptop screen size.

## 8. Tableau story (3 scenes)
1. **Population overview:** patient count and overall prevalence by disease.
2. **Who may be more vulnerable?** compare age groups and BMI categories.
3. **Lifestyle and clinical indicators:** compare exercise level, smoking, blood pressure, cholesterol and glucose; state that observed associations do not prove causation.

## 9. Flask prototype
Install dependencies with `pip install -r requirements.txt`; run `python app.py`; open `http://127.0.0.1:5000`. The web page provides KPI cards, four charts and an age-group filter. It is a local prototype and does not automatically publish or embed a Tableau workbook. For actual Tableau embedding, publish the workbook and use the official Tableau embed code/URL, following access and privacy requirements.

## 10. Performance testing checklist
- Record row count and number of columns loaded.
- Check for missing values and duplicate Patient_ID values.
- Test every filter and reset option.
- Confirm all chart titles, axes, labels, and tooltips.
- Record number of calculated fields, worksheets, and dashboard objects.
- Check load time and usability on a normal laptop browser.
- Test the Flask route with all age groups and the All option.
- Never publish real identifiable health data to a public workbook.

## 11. Expected outcomes
The project provides an interactive way to compare disease prevalence across demographic and lifestyle groups. The output can help users formulate questions for further analysis; it does not establish medical causation or diagnose individuals.

## 12. Conclusion
A prepared dataset and interactive visualization workflow can make patterns easier to explore and communicate. Tableau supports worksheet, dashboard and story creation, while Flask can provide a web interface. The current package includes a runnable Flask prototype and instructions for building the Tableau deliverables. Tableau publication and real Tableau embedding must be completed separately in Tableau.

## 13. Short demonstration script
“Hello, my project is Chronic Disease Risk Analysis using Tableau and Flask. The goal is to explore how disease prevalence varies across age, BMI and lifestyle groups. I first connect the CSV dataset and prepare the fields, then create KPI and comparison worksheets, combine them in a dashboard, and organize the findings into a three-scene story. The included Flask prototype demonstrates responsive KPI cards, charts and age filtering. The data are synthetic and intended only for software demonstration, not clinical decisions.”
