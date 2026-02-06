# 🎓 Student Performance Analysis & Dashboard

## 📌 Project Overview
This project focuses on analyzing student performance data to understand
how various factors such as study hours, attendance, parental support, and
extracurricular activities influence academic outcomes.

In addition to data analysis using Python, an **interactive Streamlit dashboard**
is built to visualize insights and allow users to input student details and
predict performance levels.

---

## 🎯 Objectives
- Analyze student performance using academic and behavioral factors
- Identify patterns affecting final grades
- Visualize insights through an interactive dashboard
- Allow user input to predict student performance levels
- Demonstrate end-to-end data analytics and dashboard development skills

---

## 🛠 Tools & Technologies Used
- **Python**
- **Pandas** – data cleaning and analysis
- **Matplotlib** – data visualization
- **Jupyter Notebook** – exploratory data analysis
- **Streamlit** – interactive dashboard
- **Git & GitHub** – version control

---

## 📂 Dataset Description
The dataset contains student-level academic and behavioral information, including:

- `studentid` – Unique student identifier  
- `name` – Student name  
- `gender` – Gender of the student  
- `studyhoursperweek` – Weekly study hours  
- `attendancerate / attendance_percent` – Attendance percentage  
- `previousgrade` – Previous academic performance  
- `finalgrade` – Final academic score (target variable)  
- `parentalsupport` – Level of parental support  
- `extracurricularactivities` – Participation in activities  
- `online_classes_taken` – Online learning exposure  

The **final grade** is used as the primary indicator of student performance.

---

## 📊 Analysis Workflow

### 🔹 Day 1: Data Understanding & Preparation
-  Loaded and explored the dataset
- Cleaned and standardized column names
- Handled missing values
- Prepared data for analysis
###  Performance Distribution Analysis
- Analyzed final grade distribution
- Examined impact of study hours and attendance
- Identified trends in academic outcomes

###  Factor-wise Performance Analysis
- Gender-wise performance comparison
- Impact of parental support
- Role of extracurricular activities
- Relationship between effort and outcomes

###  Insights & Recommendations
- Categorized students into performance levels
- Summarized key insights
- Provided actionable recommendations

---

## 📈 Streamlit Dashboard Features
- Interactive filters and inputs
- Key performance metrics (KPIs)
- Grade distribution visualization
- Performance comparison by factors
- **Input-based performance prediction**
  - User enters student details
  - Dashboard predicts performance level and estimated grade
  - Output is shown only after clicking the submit button

---

## 🔍 Key Insights
- Higher study hours and attendance correlate with better performance
- Parental support positively impacts final grades
- Extracurricular activities contribute to balanced performance
- Academic outcomes vary across different student groups
- Early identification of low performers can improve intervention strategies

---

## 💡 Business / Academic Recommendations
- Encourage consistent study routines
- Monitor and improve student attendance
- Provide additional support to low-performing students
- Promote parental involvement
- Balance academics with extracurricular activities

---

## 📁 Project Structure

student-performance-analysis/
│
├── app.py # Streamlit dashboard
├── student_analysis.ipynb # Data analysis notebook
├── student_data.csv # Dataset
├── README.md # Project documentation





Open and run:

student_analysis.ipynb




Run the Streamlit Dashboard
streamlit run app.py




🎓 Skills Demonstrated

Data Cleaning & Preparation

Exploratory Data Analysis (EDA)

Analytical & Logical Thinking

Dashboard Development

User Input Handling

Data Visualization

Version Control with GitHub

📌 Conclusion

This project demonstrates how student performance data can be transformed
into meaningful insights using Python and visualized through an interactive
dashboard. It showcases practical data analytics skills applicable to
internships, academic projects, and entry-level data roles.
