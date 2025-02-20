import numpy as np
import matplotlib.pyplot as plt

# Define a function to plot a plane
def plot_plane(a, b, c, d, ax, color='blue', alpha=0.5):
    """
    Plots a plane given the equation ax + by + cz = d.
    """
    x = np.linspace(-10, 10, 20)  # Define range for x
    y = np.linspace(-10, 10, 20)  # Define range for y
    X, Y = np.meshgrid(x, y)
    Z = (d - a * X - b * Y) / c  # Solve for Z

    # Plot the plane
    ax.plot_surface(X, Y, Z, color=color, alpha=alpha, edgecolor='k')


def main():
    # Create a figure
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Define the equations of three planes
    planes = [
        (1, 2, -3, 10, 'cyan'),  # Plane 1: x + 2y - 3z = 10
        (2, -1, 1, 5, 'magenta'),  # Plane 2: 2x - y + z = 5
        (-1, 3, 2, -7, 'yellow')   # Plane 3: -x + 3y + 2z = -7
    ]

    # Plot each plane
    for a, b, c, d, color in planes:
        plot_plane(a, b, c, d, ax, color=color, alpha=0.5)

    # Labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Visualization of Multiple Planes')

    # Show plot
    plt.show()


if __name__ == '__main__':
    main()
