import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
# def create_graph_from_shapefile(shapefile_path):
# # Load the shapefile
#     streets_gdf = gpd.read_file(shapefile_path)

#     # convert the shapefile to single linestring geometry
#     exploded_streets_gdf = streets_gdf.explode(index_parts=True)

#     # ---------
#     # extract the nodes and edges from the shp
#     # ---------

#     nodes = set()
#     edges = []

#     for index, row in exploded_streets_gdf.iterrows():
#         # Extract nodes from the start and end points of each street segment
#         start_node = (row['geometry'].coords[0][0], row['geometry'].coords[0][1])
#         end_node = (row['geometry'].coords[-1][0], row['geometry'].coords[-1][1])

#         # Convert coordinates to strings
#         start_node_str = str(start_node)
#         end_node_str = str(end_node)

#         G.add_edge(start_node_str, end_node_str)

#     # ---------
#     # create the graph as a dictionary where the nodes are the keys and the assosciated values are neighboruing nodes.
#     # ---------
        
#     street_graph = {}

#     for edge in edges:
#         start_node, end_node = edge

#         if start_node not in street_graph:
#             street_graph[start_node] = []
#         street_graph[start_node].append(end_node)

#         if end_node not in street_graph:
#             street_graph[end_node] = []
#         street_graph[end_node].append(start_node)

#     # ---------
#     # create the graph
#     # ---------
#     import networkx as nx
#     import matplotlib.pyplot as plt

#     # Create a graph from the dictionary representation
#     G = nx.from_dict_of_lists(street_graph)
#     print('LOG: Graph created. First line below:')
#     print(G)

    
#     # ---------
#     # check it has converted properly by visualising as a graph
#     # ---------

#         # # Visualize the graph (optional)
#         # nx.draw(G, with_labels=False, font_weight='bold')
#         # plt.show()
    
#     return G

def create_graph_from_shapefile(shapefile_path):
    streets_gdf = gpd.read_file(shapefile_path)
    exploded = streets_gdf.explode()

    G = nx.Graph()

    for index, row in exploded.iterrows():
        start_node = (row['geometry'].coords[0][0], row['geometry'].coords[0][1])
        end_node = (row['geometry'].coords[-1][0], row['geometry'].coords[-1][1])

        # Convert coordinates to strings
        start_node_str = str(start_node)
        end_node_str = str(end_node)

        G.add_edge(start_node_str, end_node_str)

    return G
