📊 Predictive Maintenance & Failure Analytics Dashboard
🚀 Project Overview
Built an end-to-end predictive maintenance and failure analytics solution to identify high-risk machines, reduce downtime, and improve operational efficiency.
The project combines SQL + Python + Power BI to simulate real-world manufacturing analytics workflows.

🎯 Business Problem
Frequent machine failures were causing:


Production delays


Increased maintenance costs (high MTTR)


Poor visibility into failure patterns



🧠 Solution Approach


Analyzed historical machine-level failure data


Built risk classification logic to identify high-risk machines


Designed an interactive dashboard for monitoring failures and trends



🛠️ Tech Stack


SQL → Data extraction, aggregation, cleaning


Python (Pandas, NumPy) → Data preprocessing & feature engineering


Power BI → Dashboard & visualization


Excel/CSV → Data source



📂 Project Workflow
1. Data Cleaning (SQL)


Removed null values


Standardized failure severity levels


Aggregated failures at machine level


SELECT     machine_id,    COUNT(*) AS total_failures,    AVG(failure_severity) AS avg_severityFROM machine_dataGROUP BY machine_id;

2. Feature Engineering (Python)


Created failure rate metric


Derived machine-level KPIs


df['failure_rate'] = df['total_failures'] / df['operating_hours']

3. Risk Categorization (Power BI - DAX)
Risk Category = SWITCH(    TRUE(),    machine_summary[failure_rate] > 25, "High Risk",    machine_summary[failure_rate] > 15, "Medium Risk",    "Low Risk")

📊 Dashboard Features


KPI Cards:


Total Machines


Total Failures


Failure Rate




Visuals:


Failures vs Machine ID (bar chart)


Risk Distribution (donut chart)


Machine filter (interactive slicer)





📈 Key Insights


~63% machines fall under High Risk category


Failure distribution is uneven across machines


Identified machines requiring proactive maintenance



💡 Business Impact


Enables proactive maintenance planning


Reduces unexpected downtime


Improves resource allocation for maintenance teams



📸 Dashboard Preview
(Add your screenshot here)

🔗 Future Improvements


Add ML model (Random Forest / XGBoost) for failure prediction


Real-time data pipeline integration


Alert system for high-risk machines



👤 Author
Sipra Sahoo
NIT Rourkela | Data Analyst | Supply Chain Analytics
