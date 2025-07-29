import matplotlib.pyplot as plt

languages = ['java', 'python', 'php', 'javascript', 'c#', 'c++']
popularity = [22.2, 17.6, 8.8, 8.0,7.7, 6.7,]  # ✅ Now 6 items

plt.bar(languages, popularity, color='skyblue')
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("pro161.png")
