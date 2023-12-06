import pandas as pd

def saveUniqueNodes(input, output):
	df = pd.read_csv(input)
	unique_nodes = set(df['Taxi1'].tolist() + df['Taxi2'].tolist())
	unique_nodes_df = pd.DataFrame({"Node": list(unique_nodes)})
	unique_nodes_df.to_csv(output, index=False)


saveUniqueNodes('../files/edges/geolife.csv', '../files/nodes/nodes_geolife.csv')
saveUniqueNodes('../files/edges/geolife_time_1min.csv', '../files/nodes/nodes_geolife_time_1min.csv')
saveUniqueNodes('../files/edges/geolife_time_30min.csv', '../files/nodes/nodes_geolife_time_30min.csv')
saveUniqueNodes('../files/edges/geolife_time_1day.csv', '../files/nodes/nodes_geolife_time_1day.csv')

saveUniqueNodes('../files/edges/tdrive.csv', '../files/nodes/nodes_tdrive.csv')
saveUniqueNodes('../files/edges/tdrive_time_1min.csv', '../files/nodes/nodes_tdrive_time_1min.csv')
saveUniqueNodes('../files/edges/tdrive_time_30min.csv', '../files/nodes/nodes_tdrive_time_30min.csv')
saveUniqueNodes('../files/edges/tdrive_time_1day.csv', '../files/nodes/nodes_tdrive_time_1day.csv')