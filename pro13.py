import numpy as np
import matplotlib.pyplot as plt

# Load data from file using numpy
data = np.loadtxt("test.txt")  # Assumes two columns of numbers

# Split into x and y
x = data[:, 0]  # First column
y = data[:, 1]  # Second column

# Plot
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Plot from File")
plt.grid(True)
#plt.show()
plt.savefig("plot.png")
print("Plot saved as plot.png")
