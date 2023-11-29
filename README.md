# GPS_analysis of Geolife and Tdrive databases

Geolife and Tdrive are GPS databases, both made based on GPS data collected in Beijing. Geolife database has data recorded by people using various methods of transportation (most commonly, by walking). </br>
Tdrive database is based on data recorded by Taxi drivers.</br>
Both databases have Longitude, Latitude and Timestamp in their columns. </br>
Additionally Tdrive has a Taxi ID column, so we can easily tell one Taxi from another</br>
Geolife, however, has a different .plt file for each person, so parsing the data is a bit more challenging. Geolife dataset also provides altitude data. Additionally, some directories has info about which transportation method was used during data recording.

# Organization notes
Images will be stored inside img folder</br>
Files will be separated inside the files folder. There will be an additional folder for edges, nodes and graphs inside files folder.</br>
Data is store inside data folder.</br>
Models will be stored inside model folder.</br>
Additional folders are explained below.

# Load data
To load data, go to the load_data folder. Run ```load_data.ipynb``` to load geolife dataset and to save it as a model (you can find all models inside the model directory).</br>
Run ```load_data2.ipynb``` to load tdrive dataset and to save it as a model (you can find all models inside the model directory).</br>
Run ```load_labels_data.ipynb`` to load geolife dataset transportation methods and to save it as a model (you can find all models inside the model directory).

# Initial analysis
Go to the analyze_db folder to launch initial analysis based on the first models that we created.</br>
```main.ipynb``` represents geolife data and ```main2.ipynb``` represents tdrive data.

# Find people and taxis that have passed each other
This is the main focus of this analysis. We narrowed the search down to saving all users who were 100m from each other (at any time) to a json file.</br>
Launch ```node_analyze.ipynb``` to create a ```geolife.json``` and launch ```node_analyze_tdrive.ipynb``` to create a ```tdrive.json```</br>
The process may take a while

# Json to CSV
While json files are nice for analysis, we decided to filter some data and save to csv, since it's faster while analysing.</br>
Be sure to run ```convert_data.py``` to create 2 csv files from the inital json file (one for tdrive and one for geolife data). </br>
Additionally, if you want to follow up with the rest of the tutorial, create ```geolife_time_1min.csv```, ```geolife_time_30min.csv``` and ```geolife_time_1day.csv``` by changing variables include_time and time_treshold inside extract_unique_pairs function.
Do the same thing with the tdrive data.</br>
Then run ```extract_nodes.py``` to extract nodes.

# Visualize data
Go to the folder visualize. Run ```visualize.py``` to visualize .json files. You can again adjust include_time, time_threshold and distance_treshold (as long as the value is between 0 - 100).</br>
Run ```visualize2.py``` for visualization of the csv files. Make sure to change the name of the csv file you want to visualize. Use this function for bigger dataset (such as ```geolife.csv```)</br>
Run ```visualize_pyvis.py``` to visualize smaller datasets, as this way you can interact with the data, by dragging the data.

# Analyze data
Now all of the files we've created so far will be loaded into ```analyze.py``` and runned here. As an output you will get these per csv file:</br>
Number of edges</br>
Number of nodes</br>
Number of nodes with edges</br>
Max number of edges from a node</br>
Min number of edges from a node</br>
Average number of edges per node</br>
Average number of edges per active node</br>
Graph Nodes and Their Occurrences</br>
Graph Distribution of Node Occurrences
