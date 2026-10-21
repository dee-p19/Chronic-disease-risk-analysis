from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio
from pathlib import Path

app = Flask(__name__)
DATA = Path(__file__).with_name("patient_health_synthetic.csv")

def load_data():
    df = pd.read_csv(DATA)
    # Derived fields for dashboard analysis
    df["Age_Group"] = pd.cut(df["Age"], bins=[17,29,39,49,59,69,120],
        labels=["18–29","30–39","40–49","50–59","60–69","70+"])
    df["BMI_Category"] = pd.cut(df["BMI"], bins=[0,18.5,25,30,100],
        labels=["Underweight","Normal","Overweight","Obese"], right=False)
    return df

@app.route("/")
def index():
    df = load_data()
    age_group = request.args.get("age_group", "All")
    if age_group != "All":
        df = df[df["Age_Group"].astype(str) == age_group]
    n = len(df)
    heart = round(df["Heart_Disease"].mean()*100, 1) if n else 0
    diabetes = round(df["Diabetes"].mean()*100, 1) if n else 0
    stroke = round(df["Stroke"].mean()*100, 1) if n else 0

    disease_df = df[["Heart_Disease","Diabetes","Stroke"]].mean().mul(100).rename_axis("Disease").reset_index(name="Prevalence")
    disease_df["Disease"] = disease_df["Disease"].map({"Heart_Disease":"Heart disease","Diabetes":"Diabetes","Stroke":"Stroke"})
    fig1 = px.bar(disease_df, x="Disease", y="Prevalence", title="Disease prevalence (%)", text_auto=".1f")
    fig1.update_layout(yaxis_title="Patients (%)", xaxis_title="")
    age_df = df.groupby("Age_Group", observed=False)[["Heart_Disease","Diabetes","Stroke"]].mean().mul(100).reset_index().melt(id_vars="Age_Group", var_name="Disease", value_name="Prevalence")
    age_df["Disease"] = age_df["Disease"].replace({"Heart_Disease":"Heart disease"})
    fig2 = px.line(age_df, x="Age_Group", y="Prevalence", color="Disease", markers=True, title="Disease prevalence by age group")
    bmi_df = df.groupby("BMI_Category", observed=False)[["Heart_Disease","Diabetes","Stroke"]].mean().mul(100).reset_index().melt(id_vars="BMI_Category", var_name="Disease", value_name="Prevalence")
    bmi_df["Disease"] = bmi_df["Disease"].replace({"Heart_Disease":"Heart disease"})
    fig3 = px.bar(bmi_df, x="BMI_Category", y="Prevalence", color="Disease", barmode="group", title="Disease prevalence by BMI category")
    lifestyle = df.groupby("Exercise_Level")[["Heart_Disease","Diabetes","Stroke"]].mean().mul(100).reset_index().melt(id_vars="Exercise_Level", var_name="Disease", value_name="Prevalence")
    lifestyle["Disease"] = lifestyle["Disease"].replace({"Heart_Disease":"Heart disease"})
    fig4 = px.bar(lifestyle, x="Exercise_Level", y="Prevalence", color="Disease", barmode="group", title="Disease prevalence by exercise level")
    charts = [pio.to_html(fig, full_html=False, include_plotlyjs="cdn") for fig in [fig1,fig2,fig3,fig4]]
    return render_template("index.html", charts=charts, n=n, heart=heart, diabetes=diabetes,
        stroke=stroke, age_groups=["All","18–29","30–39","40–49","50–59","60–69","70+"], selected=age_group)

if __name__ == "__main__":
    app.run(debug=True)
