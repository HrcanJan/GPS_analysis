import pandas as pd

def saveUniqueNodes(input, output):
	df = pd.read_csv(input)
	unique_nodes = set(df['Taxi1'].tolist() + df['Taxi2'].tolist())
	unique_nodes_df = pd.DataFrame({"Node": list(unique_nodes)})
	unique_nodes_df.to_csv(output, index=False)


saveUniqueNodes('./files/geolife.csv', './files/nodes_geolife.csv')
saveUniqueNodes('./files/geolife_time_1min.csv', './files/nodes_geolife_time_1min.csv')
saveUniqueNodes('./files/geolife_time_30min.csv', './files/nodes_geolife_time_30min.csv')
saveUniqueNodes('./files/geolife_time_1day.csv', './files/nodes_geolife_time_1day.csv')

saveUniqueNodes('./files/tdrive.csv', './files/nodes_tdrive.csv')
saveUniqueNodes('./files/tdrive_time_1min.csv', './files/nodes_tdrive_time_1min.csv')
saveUniqueNodes('./files/tdrive_time_30min.csv', './files/nodes_tdrive_time_30min.csv')
saveUniqueNodes('./files/tdrive_time_1day.csv', './files/nodes_tdrive_time_1day.csv')