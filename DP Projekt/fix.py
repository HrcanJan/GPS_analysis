import json

# Read the original file
with open('./files/meeting_data_geolife2.json', 'r') as file:
    data = file.readlines()

# Create a list to store valid JSON strings
valid_json_list = []

# Iterate through the lines, load each line as JSON, and add to the list
for line in data:
    try:
        json_obj = json.loads(line)
        valid_json_list.append(json_obj)
    except json.JSONDecodeError:
        print(f"Skipping invalid JSON: {line}")

# Write the list of valid JSON objects back to a new file
with open('./files/geolife.json', 'w') as file:
    json.dump(valid_json_list, file, indent=2)
