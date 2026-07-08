# Riliv Study Case 2 - Data Cleaning & Dashboard

## 📌 Project Overview
This project was completed as part of the **Riliv Data Analyst Internship Study Case**.

The objective is to clean and transform raw registration data containing dynamic question-response pairs into a structured dataset suitable for analysis and dashboard visualization.

---

## 📂 Dataset
The dataset consists of:

- 7,270 records
- 24 columns
- Dynamic questionnaire format:
  - Question 1 – Response 1
  - Question 2 – Response 2
  - ...
  - Question 10 – Response 10

Because each registration form contains different question labels, data transformation is required before analysis.

---

## 🎯 Objectives

- Explore all unique question labels.
- Standardize different labels into consistent columns.
- Transform Question-Response pairs into a structured table.
- Export cleaned data into Excel.
- Prepare the dataset for dashboard visualization.

---

## 🛠️ Tools

- Python
- Pandas
- OpenPyXL
- Microsoft Excel
- Google Sheets
- Looker Studio

---

## ⚙️ Data Processing

The Python script performs:

- Read raw Excel dataset
- Detect Question & Response columns
- Extract unique question labels
- Standardize question names using mapping
- Convert Question-Response pairs into structured columns
- Preserve registration metadata
- Export cleaned dataset to Excel

---

## 📁 Project Structure

```
Riliv-StudyCase/
│
├── Raw Data.xlsx
├── Riliv_Data_Cleaning_Final.py
├── StudyCase_Hasil_Clean.xlsx
├── README.md
└── Dashboard/
```

---

## 📊 Dashboard

The cleaned dataset is used to create an interactive dashboard containing:

- Total Registrations
- Gender Distribution
- Age Distribution
- Counseling Service Distribution
- Counseling Topics
- Company Distribution
- Registration Trends

---

## 🚀 How to Run

Clone the repository.

```bash
git clone https://github.com/yourusername/Riliv-StudyCase.git
```

Install dependencies.

```bash
pip install pandas openpyxl
```

Run the script.

```bash
python Riliv_Data_Cleaning_Final.py
```

The cleaned dataset will be generated as:

```
StudyCase_Hasil_Clean.xlsx
```

---

## 📈 Output

- Cleaned Excel Dataset
- Structured Data Table
- Dashboard Visualization

---


- LinkedIn: https://www.linkedin.com/in/disya-nurul-ariza24
- GitHub: https://github.com/DisyaAriza
