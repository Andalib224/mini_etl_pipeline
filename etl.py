import csv
import logging
import json
import re

logging.basicConfig(
    filename="employees.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_id(record, emp_id):
    if emp_id.isdigit() and int(emp_id) > 0:
        return emp_id

    elif emp_id == "":
        logging.warning(f"Skipped record: Missing employee id, Record: {record}")
    else:
        logging.error(f"Skipped record: Invalid id : {emp_id}, Record: {record}")


def validate_name(record, emp_name):
    pattern = re.compile(r"^[A-Za-z’'\- ]+$")

    if pattern.match(emp_name):

        emp_name = emp_name.replace('-',' ').title()
        return emp_name

    elif emp_name == "":
        logging.warning(f"Skipped record: Missing employee name, Record: {record}")

    else:
        logging.error(f"Skipped record: Invalid name : {emp_name}, Record: {record}")


def validate_department(record, emp_dept):

    if emp_dept.isalpha():
        emp_dept = emp_dept.upper()
        return emp_dept

    elif emp_dept == "":
        logging.warning(f"Skipped record: Missing employee department, Record: {record}")
    else:
        logging.error(f"Skipped record: Invalid Department: {emp_dept}, Record: {record}")


def validate_salary(record, emp_salary):
    pattern = re.compile(r"^[0-9.]+")

    if pattern.match(emp_salary):
        if "." in emp_salary:
            if int(float(emp_salary)) > 0:
                return emp_salary
            elif int(float(emp_salary)) <= 0:
                logging.warning(f"Skipped record: Invalid salary : {emp_salary}, Record {record}")
                return None

        elif int(emp_salary) <= 0:
            logging.warning(f"Skipped record: Invalid salary : {emp_salary}, Record {record}")
            return None
        return emp_salary

    elif emp_salary == "":
        logging.warning(f"Skipped record: Missing employee salary, Record: {record}")
    else:
        logging.error(f"Skipped record: Invalid Salary: {emp_salary}, Record: {record}")


def write_json(filename, src_file):
    logging.info("Extracted and clean data are saving to json file.")
    base_filename = filename.split('.')[0]
    with open(f"{base_filename}.json", "w") as fileobj:
        json.dump(src_file, fileobj, indent=4)
    logging.info("Pipeline completed. File saved to json document.")

def read_csv(filename):
    logging.info(f"Processing file: {filename}")
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            seen = set()
            result = []
            for row in reader:
                headers = list(row.keys())

                filtered_id = validate_id(row, row["emp_id"].strip())
                if filtered_id is None:
                    continue

                filtered_name = validate_name(row, row["name"].strip())
                if filtered_name is None:
                    continue

                filtered_department = validate_department(row, row["department"].strip())
                if filtered_department is None:
                    continue

                filtered_salary = validate_salary(row, row["salary"].strip())
                if filtered_salary is None:
                    continue

                key = (filtered_id, filtered_name, filtered_department, filtered_salary)

                if key not in seen:
                    seen.add(key)
                    logging.info("Duplicate record skipped.")
                    clean_record = dict(zip(headers, key))
                    result.append(clean_record)

        print(result, type(result))
        write_json(filename, result)

    except FileNotFoundError:
        print(f"File: {filename} doesn't exist.")
        logging.error("File doesn't exist.")
        return []

    except Exception as e:
        print("Unexpected exception occurred.")
        logging.error(f"Unexpected exception occurred. {e}")
        return []



if __name__ == "__main__":
    logging.info("Pipeline has started.")
    read_csv("employees.csv")





