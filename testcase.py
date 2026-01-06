employees = [
    {
        "emp_id": 101,
        "emp_name": "Tanmoy Das",
        "company": "CAF softsol",
        "email": "tanmoy@gmail.com"
    },
    {
        "emp_id": 102,
        "emp_name": "Koustav Mondal",
        "company": None,
        "email": "kous@gmail.com"
    },
    {
        "emp_id": 103,
        "emp_name": "",
        "company": "CAF solution",
        "email": None
    },
    {
        "emp_id": 104,
        "emp_name": "Shuvam Singh",
        "company": "",
        "email": ""
    }
]

for emp in employees:

    for key, value in emp.items():

        if key == "emp_name":
            if value is None or value.strip() == "":
                emp[key] = "Unknown Employee"
            else:
                emp[key] = value

        elif key == "email":
            if value is None or value.strip() == "":
                emp[key] = "Not Available"
            else:
                emp[key] = value

        else:
            if value is None or (isinstance(value, str) and value.strip() == ""):
                emp[key] = "N/A"
            else:
                emp[key] = value

    print(emp)
