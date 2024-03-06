import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Set a black background
plt.style.use('dark_background')

# Function to generate random data for the plots
def generate_data(offset):
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x + offset)
    y2 = np.cos(x + offset)
    y3 = np.sin(x + offset) + np.cos(x + offset)
    y4 = np.random.rand(100)

    return x, y1, y2, y3, y4

# Function to update the plots in the animation
def update(frame):
    x, y1, y2, y3, y4 = generate_data(frame / 10)

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax1.plot(x, y1, label='Sin(x)', color='red')
    ax2.plot(x, y2, label='Cos(x)', color='cyan')
    ax3.plot(x, y3, label='Sin(x) + Cos(x)', color='green')
    ax4.bar(x, y4, color='purple', alpha=0.7)

    ax1.set_title('Sin(x)')
    ax2.set_title('Cos(x)')
    ax3.set_title('Sin(x) + Cos(x)')
    ax4.set_title('Bar Plot')

    ax1.legend()
    ax2.legend()
    ax3.legend()

# Create subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

# Set animation
ani = FuncAnimation(fig, update, frames=200, interval=200, repeat=True)

# Show the animated plot
plt.tight_layout()
plt.show()
