
import torch
import torchvision
import torchvision.transforms as transforms
from torchvision import models
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
import networkx as nx
import matplotlib.pyplot as plt

transformation = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

full_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transformation)

# Select a subset
random_indices = np.random.choice(len(full_dataset), 500, replace=False)
subset_data = torch.utils.data.Subset(full_dataset, random_indices)
data_loader = torch.utils.data.DataLoader(subset_data, batch_size=32, shuffle=False)

# Feature Extraction
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
resnet_model = models.resnet18(pretrained=True)
resnet_model.fc = torch.nn.Identity() # Remove the last classification layer
resnet_model.to(device)
resnet_model.eval()

feature_vectors = []
with torch.no_grad():
    for images, _ in data_loader:
        outputs = resnet_model(images.to(device))
        feature_vectors.append(outputs.cpu().numpy())

feature_vectors = np.vstack(feature_vectors)
print(f"Feature vectors shape: {feature_vectors.shape}")

# K-NN Graph Construction
k_neighbors = 3
distance_matrix = euclidean_distances(feature_vectors)

similarity_graph = nx.Graph()

# For each image, find its K nearest neighbors
for i in range(len(distance_matrix)):
    # Get indices of the nearest neighbors
    nearest_neighbors = np.argsort(distance_matrix[i])[1:k_neighbors+1]
    for neighbor in nearest_neighbors:
        similarity_graph.add_edge(i, neighbor, weight=distance_matrix[i][neighbor])

print(f"Graph created with {similarity_graph.number_of_nodes()} nodes and {similarity_graph.number_of_edges()} edges.")

# Similarity Graph Visualization
plt.figure(figsize=(15, 10))
node_layout = nx.spring_layout(similarity_graph, k=0.15, seed=42)
nx.draw(similarity_graph, node_layout, node_size=20, node_color='teal', edge_color='gray', alpha=0.6, with_labels=False)
plt.title("K-NN Graph: Visual Similarity Connections")
plt.show()

import numpy as np

# 1. Define a threshold
# We will use the average of the existing edge weights
weights = [d['weight'] for u, v, d in similarity_graph.edges(data=True)]
pruning_threshold = np.mean(weights)

# 2. Create a copy of the graph to keep the original intact
pruned_graph = similarity_graph.copy()

# 3. Identify and remove edges that exceed the threshold
edges_to_remove = [(u, v) for u, v, d in pruned_graph.edges(data=True) if d['weight'] > pruning_threshold]
pruned_graph.remove_edges_from(edges_to_remove)

print(f"Distance threshold applied: {pruning_threshold:.4f}")
print(f"Edges removed: {len(edges_to_remove)}")
print(f"Edges remaining: {pruned_graph.number_of_edges()}")

plt.figure(figsize=(15, 10))

pruned_layout = nx.spring_layout(pruned_graph, k=0.15, seed=42)

nx.draw(pruned_graph, pruned_layout,
        node_size=30,
        node_color='salmon',
        edge_color='black',
        alpha=0.4,
        with_labels=False)

plt.title("K-NN Graph with Edge Pruning (Strong connections only)")
plt.show()
