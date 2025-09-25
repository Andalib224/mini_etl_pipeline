# Mini ELT Pipeline in Python

This project is a mini Extract–Load–Transform (ELT) pipeline built using pure Python.
It simulates how raw employee data from a CSV file is ingested, validated, logged, and cleaned before being ready for downstream use.

## 📌 Project Overview

Extract: Read raw employee data from a CSV file (employees.csv).

Load: Store the data in memory as Python dictionaries.

Transform:

Validate fields (id, name, department, salary).

Remove records with missing or invalid values.

Enforce data quality rules (e.g., no numeric-only names, non-empty department).

Logging: Every step of the pipeline is logged into data.log for monitoring and troubleshooting.

## 🛠 Features
```
✅ Handles missing values in employee data.
✅ Validates names (rejects numeric-only names like "12345").
✅ Logs pipeline execution status (start, success, failure, warnings).
✅ Gracefully handles file-not-found errors.
✅ Produces a cleaned dataset as Python objects for further processing.


mini-elt-pipeline/
│
├── employees.csv      # Raw dataset (contains both valid/invalid records)
├── pipeline.py        # Main Python script
├── data.log           # Log file with pipeline execution history
└── README.md          # Project documentation
```

## 📑 Sample Input (employees.csv)
```
emp_id,name,department,salary
101,Alice,IT,60000
102,Bob,Finance,55000
103,Charlie,HR,0
104,,IT,50000
105,12345,Finance,65000
106,Eva,,48000
107,Frank,IT,abc
108,Alice,IT,60000
109,Grace,Marketing,72000
110,Henry,Finance,
111,Isabel,Finance,58000
112,John,123,45000
113,Kate,IT,-3000
114,Liam,Finance,62000
114,Liam,Finance,62000
114,Liam,Finance,62000
```
## 🎯 Expected Output
```aiignore
[
    {
        "emp_id": "101",
        "name": "Alice",
        "department": "IT",
        "salary": "60000"
    },
    {
        "emp_id": "102",
        "name": "Bob",
        "department": "FINANCE",
        "salary": "55000"
    },
    {
        "emp_id": "108",
        "name": "Alice",
        "department": "IT",
        "salary": "60000"
    },
    {
        "emp_id": "109",
        "name": "Grace",
        "department": "MARKETING",
        "salary": "72000"
    },
    {
        "emp_id": "111",
        "name": "Isabel",
        "department": "FINANCE",
        "salary": "58000"
    },
    {
        "emp_id": "114",
        "name": "Liam",
        "department": "FINANCE",
        "salary": "62000"
    }
]


```
⚠️ Invalid records are filtered out:

- Record 2: Missing name.
- Record 3: Name is numeric only.
- Record 5: Missing department.

## 📝 Logging Examples
employee.log
```aiignore
2025-09-25 11:00:20,013 - INFO - Pipeline has started.
2025-09-25 11:00:20,013 - INFO - Processing file: employees.csv
2025-09-25 11:00:20,014 - INFO - Duplicate record skipped.
2025-09-25 11:00:20,014 - INFO - Duplicate record skipped.
2025-09-25 11:00:20,014 - WARNING - Skipped record: Invalid salary : 0, Record {'emp_id': '103', 'name': 'Charlie', 'department': 'HR', 'salary': '0'}
2025-09-25 11:00:20,014 - WARNING - Skipped record: Missing employee name, Record: {'emp_id': '104', 'name': '', 'department': 'IT', 'salary': '50000'}
2025-09-25 11:00:20,014 - ERROR - Skipped record: Invalid name : 12345, Record: {'emp_id': '105', 'name': '12345', 'department': 'Finance', 'salary': '65000'}
2025-09-25 11:00:20,014 - WARNING - Skipped record: Missing employee department, Record: {'emp_id': '106', 'name': 'Eva', 'department': '', 'salary': '48000'}
2025-09-25 11:00:20,014 - ERROR - Skipped record: Invalid Salary: abc, Record: {'emp_id': '107', 'name': 'Frank', 'department': 'IT', 'salary': 'abc'}
2025-09-25 11:00:20,014 - INFO - Duplicate record skipped.
2025-09-25 11:00:20,014 - INFO - Duplicate record skipped.
2025-09-25 11:00:20,014 - WARNING - Skipped record: Missing employee salary, Record: {'emp_id': '110', 'name': 'Henry', 'department': 'Finance', 'salary': ''}
2025-09-25 11:00:20,014 - INFO - Duplicate record skipped.
2025-09-25 11:00:20,014 - ERROR - Skipped record: Invalid Department: 123, Record: {'emp_id': '112', 'name': 'John', 'department': '123', 'salary': '45000'}
2025-09-25 11:00:20,014 - ERROR - Skipped record: Invalid Salary: -3000, Record: {'emp_id': '113', 'name': 'Kate', 'department': 'IT', 'salary': '-3000'}
2025-09-25 11:00:20,014 - INFO - Duplicate record skipped.
2025-09-25 11:00:20,014 - INFO - Extracted and clean data are saving to json file.
2025-09-25 11:00:20,020 - INFO - Pipeline completed. File saved to json document.
```

## 🚀 How to Run
```
# Clone repository
git clone https://github.com/Andalib224/mini_etl_pipeline.git
cd mini-elt-pipeline

# Run the pipeline
python3 etl.py
```

## 📖 Concepts Covered

- File handling in Python (with open() as file)
- Data cleaning and validation
- Logging with the logging module
- Basic ELT pipeline design
