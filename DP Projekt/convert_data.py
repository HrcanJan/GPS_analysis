import json
import csv

def load_json(file_path):
	with open(file_path, 'r') as json_file:
		data = json.load(json_file)
	return data

def extract_unique_pairs(data):
	unique_pairs = set()
	for entry in data:
		taxi1 = entry.get('Taxi1')
		taxi2 = entry.get('Taxi2')

		if taxi1 is not None and taxi2 is not None:
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
	process_json('./files/tdrive.json', './files/tdrive.csv')
