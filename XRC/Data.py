import json


def read_value_from_json(filepath, keys):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

    if not keys or keys[0] != 'myrobot':
        print("Error: keys must start with 'myrobot'")
        return None

    myrobot_list = data.get('myrobot')
    if not isinstance(myrobot_list, list):
        print("Error: 'myrobot' is not a list.")
        return None

    if len(keys) < 2:
        print("Error: Need at least a second key to specify the 'name'.")
        return None

    target_name = keys[1]
    target_entry = None
    for entry in myrobot_list:
        if isinstance(entry, dict) and entry.get('name') == target_name:
            target_entry = entry
            break

    if target_entry is None:
        print(f"Error: No entry with name '{target_name}' found.")
        return None

    current = target_entry
    for key in keys[2:]:
        if key in current:
            current = current[key]
        else:
            print(f"Error: Key '{key}' not found inside entry '{target_name}'.")
            return None

    return current


# Usage example
a = r"C:\tmp\xRCsim\myRobot.txt"
b = ['myrobot', 'Body', 'global rot']

value = read_value_from_json(a, b)
print("Value:", value)
