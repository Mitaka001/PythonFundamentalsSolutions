company_info = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break

    company_name, employees_id = command[0], command[1]

    if company_name not in company_info.keys():
        company_info[company_name] = []
    if employees_id not in company_info[company_name]:
        company_info[company_name].append(employees_id)

for company_name, employees_id in company_info.items():
    print(f"{company_name}")
    for employee in employees_id:
        print(f"-- {employee}")
