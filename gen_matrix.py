import numpy as np
import pandas as pd
import networkx as nx

# Read all the player names and store it as a list
with open('Player_List.csv') as file:
    names = file.readlines()
    players = [x[:-1] for x in names]

# Read the units.csv file using pandas
df = pd.read_csv('units_2.csv')

# Create a matrix with units as rows and players as columns
matrix = np.zeros((df.V2.count(), len(players)))


for i, row in df.iterrows():
    count = -1
    for name in players:
        count = count + 1
        if name in row.V2:
            matrix[i, count] = float(row.V7)

# Convert the bimodal network into unimodal network
new_matrix = np.dot(matrix.T, matrix)

#np.savetxt("matrix.csv", new_matrix, delimiter=",")

# Create a graph with the adjacency matrix
G = nx.Graph(new_matrix)

# Calculate the edge centrality of the graph
centrality = nx.edge_betweenness_centrality(G)

print(['%s %0.4f'%(node,centrality[node]) for node in centrality])
