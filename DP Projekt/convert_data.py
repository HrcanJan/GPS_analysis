import json
import csv
from datetime import datetime

def load_json(file_path):
	with open(file_path, 'r') as json_file:
		data = json.load(json_file)
	return data

def extract_unique_pairs(data):
	include_time = False
	time_threshold = 60 # seconds

	unique_pairs = set()
	for entry in data:
		taxi1 = entry.get('Taxi1')
		taxi2 = entry.get('Taxi2')

		timestamp1 = datetime.strptime(entry.get('Timestamp1'), "%Y-%m-%d %H:%M:%S")
		timestamp2 = datetime.strptime(entry.get('Timestamp2'), "%Y-%m-%d %H:%M:%S")

		if taxi1 is not None and taxi2 is not None:
			if include_time == True:
				if abs((timestamp1 - timestamp2).total_seconds()) <= time_threshold:
					pair = tuple(sorted([taxi1, taxi2]))
					unique_pairs.add(pair)
			else:
				pair = tuple(sorted([taxi1, taxi2]))
				unique_pairs.add(pair)

	return list(unique_pairs)

def save_to_csv(unique_pairs, csv_file):
	with open(csv_file, 'w', newline='') as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(['Taxi1', 'Taxi2'])  # Header

		for pair in unique_pairs:
			csv_writer.writerow(pair)

def process_json(json_file_path, csv_file_path):
	data = load_json(json_file_path)
	unique_pairs = extract_unique_pairs(data)
	save_to_csv(unique_pairs, csv_file_path)
	print(f"Unique pairs saved to {csv_file_path}")

if __name__ == "__main__":
	process_json('./files/geolife.json', './files/geolife.csv')
	process_json('./files/tdrive2.json', './files/tdrive.csv')
