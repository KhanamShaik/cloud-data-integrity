import matplotlib.pyplot as plt
import numpy as np

# Create the heart shape using parametric equations
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plot the heart
plt.figure(figsize=(6, 6))
plt.plot(x, y, color="red")
plt.fill(x, y, color="pink", alpha=0.6)

# Add the "SORRY" text to the heart
plt.text(0, -3, "SORRY SIR JI", fontsize=24, color="black", fontweight="bold", ha="center")

# Adjust plot settings
plt.axis("off")
plt.title("A Heartfelt Sorry", fontsize=16, color="black")
plt.show()
