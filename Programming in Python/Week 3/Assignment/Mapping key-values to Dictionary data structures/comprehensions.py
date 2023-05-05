# Input data: List of dictionaries
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]


# Function to be passed to the map() function. Do not change this.
def mod(employee_lists):
    temp = employee_lists['name'] + "_" + employee_lists["department"]
    return temp


def to_mod_list(employee_lists):
    mod_list = list(map(mod, employee_list))
    return mod_list


# list from username
def generate_usernames(mod_list):
    username_list = [item.replace(" ", "_") for item in mod_list]
    return username_list


# dict from initial as key and id as value
def map_id_to_initial(employee_lists):
    initial_dict = {employee["name"][0]: employee["id"] for employee in employee_list}
    return initial_dict


def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")


if __name__ == "__main__":
    main()
