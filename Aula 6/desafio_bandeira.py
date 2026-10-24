import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

bandeira = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 2, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 2, 3, 2, 1, 1, 1, 0],
  [0, 0, 1, 1, 1, 2, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

cmap = ListedColormap(["green", "yellow", "blue", "white"])
plt.figure(figsize=(5, 5))
plt.imshow(bandeira, cmap=cmap)
plt.axis('off')
plt.show()