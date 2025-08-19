import pandas as pd

# 2D list
data = [
    [1, 'Alice', 85],
    [2, 'Bob', 90],
    [3, 'Charlie', 95]
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['ID', 'Name', 'Score'])

# Display the DataFrame
print("Converted DataFrame:")
print(df)
