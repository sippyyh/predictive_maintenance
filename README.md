# 📊 Predictive Maintenance & Machine Risk Intelligence Dashboard

## 🚀 Overview
This project presents an end-to-end **Predictive Maintenance Analytics Solution** designed to identify high-risk machines, reduce unexpected failures, and improve operational efficiency.

It simulates a real-world manufacturing use case by integrating **SQL, Python, and Power BI** for data processing, analysis, and visualization.

---

## 🎯 Business Problem
Frequent machine failures led to:
- Production delays  
- Increased maintenance costs (high MTTR)  
- Lack of visibility into failure patterns  

---

## 🧠 Solution
Developed a data-driven system to:
- Analyze historical machine failure data  
- Compute machine-level KPIs  
- Classify machines based on failure risk  
- Build an interactive dashboard for monitoring and decision-making  

---

## 🛠️ Tech Stack
- **SQL** → Data extraction, cleaning, aggregation  
- **Python (Pandas, NumPy)** → Feature engineering & transformation  
- **Power BI** → Dashboard development & visualization  
- **CSV/Excel** → Data source  

---

## 📂 Project Workflow

### 1️⃣ Data Cleaning & Aggregation (SQL)
- Removed null values and inconsistencies  
- Aggregated failure data at machine level  

```sql
SELECT 
    machine_id,
    COUNT(*) AS total_failures,
    AVG(failure_severity) AS avg_severity
FROM machine_data
GROUP BY machine_id;
