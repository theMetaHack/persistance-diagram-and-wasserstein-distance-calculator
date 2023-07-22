import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from ripser import Rips

# Load the image
img_file_path = "insert your file path"
image = plt.imread(img_file_path)

# Convert the image to grayscale
image = np.mean(image, axis=2)

# Compute the persistence diagram
rips = Rips()
diagrams = rips.fit_transform(image)

# Plot the persistence diagram
rips.plot(diagrams)

# Save the persistence diagram as a JPEG
# fig.savefig("persistence_diagram.jpg", format="jpg", dpi=300)
