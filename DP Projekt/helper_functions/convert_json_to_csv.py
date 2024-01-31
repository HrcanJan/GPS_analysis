import json
import csv
from datetime import datetime

def load_json(file_path):
	with open(file_path, 'r') as json_file:
		data = json.load(json_file)
	return data

def extract_unique_pairs(data, include_time, time_threshold):
	unique_pairs = set()
	for entry in data:
		taxi1 = entry.get('Person ID 1')
		taxi2 = entry.get('Person ID 2')

		timestamps = entry.get('Timestamps')
		timestamp1 = datetime.strptime(timestamps.get(str(taxi1)), "%Y-%m-%d %H:%M:%S")
		timestamp2 = datetime.strptime(timestamps.get(str(taxi2)), "%Y-%m-%d %H:%M:%S")

		if taxi1 is not None and taxi2 is not None:
			if include_time == True:
				if abs((timestamp1 - timestamp2).total_seconds()) <= time_threshold:
					pair = tuple(sorted([taxi1, taxi2]))
					unique_pairs.add(pair)
			else:
				pair = tuple(sorted([taxi1, taxi2]))
				unique_pairs.add(pair)

	return list(unique_pairs)

def save_to_csv(unique_pairs, csv_file, person):
	with open(csv_file, 'w', newline='') as csvfile:
		csv_writer = csv.writer(csvfile)
		if(person == True):
			csv_writer.writerow(['Person1', 'Person2'])
		else:
			csv_writer.writerow(['Taxi1', 'Taxi2'])

		for pair in unique_pairs:
			csv_writer.writerow(pair)

def process_json(json_file_path, csv_file_path, person):
	data = load_json(json_file_path)

	unique_pairs = extract_unique_pairs(data, False, 60)
	save_to_csv(unique_pairs, csv_file_path + '.csv', person)
	print(f"Unique pairs saved to {csv_file_path + '.csv'}")

	unique_pairs = extract_unique_pairs(data, True, 60)
	save_to_csv(unique_pairs, csv_file_path + '_time_1min.csv', person)
	print(f"Unique pairs saved to {csv_file_path + '_time_1min.csv'}")

	unique_pairs = extract_unique_pairs(data, True, 60 * 30)
	save_to_csv(unique_pairs, csv_file_path + '_time_30min.csv', person)
	print(f"Unique pairs saved to {csv_file_path + '_time_30min.csv'}")

	unique_pairs = extract_unique_pairs(data, True, 60 * 60 * 24)
	save_to_csv(unique_pairs, csv_file_path + '_time_1day.csv', person)
	print(f"Unique pairs saved to {csv_file_path + '_time_1day.csv'}")

if __name__ == "__main__":
	process_json('./files/edges/new_geolife.json', './files/edges/geolife', True)
	process_json('./files/edges/new_tdrive.json', './files/edges/tdrive', False)
