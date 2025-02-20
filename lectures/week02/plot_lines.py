import numpy as np
import matplotlib.pyplot as plt


def main():
    # Define equations of lines: ax + by = c
    lines = [
        (2, -1, 4),   # 2x - y = 4  -> y = 2x - 4
        (-1, 2, 2),   # -x + 2y = 2 -> y = 0.5x + 1
        (1, 1, 6)     # x + y = 6   -> y = 6 - x
    ]

    # Define the range for x-values
    x = np.linspace(-5, 10, 100)

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot each line
    for a, b, c in lines:
        y = (c - a * x) / b  # Solve for y
        ax.plot(x, y, label=f"{a}x + {b}y = {c}")

    # Solve system of equations to find intersection points
    A = np.array([[2, -1], [-1, 2], [1, 1]])  # Coefficients
    C = np.array([4, 2, 6])  # Constants

    # Find all pairwise intersections
    solutions = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            try:
                intersection = np.linalg.solve(A[[i, j]], C[[i, j]])
                solutions.append(intersection)
            except np.linalg.LinAlgError:
                pass  # Skip if lines are parallel

    # Plot intersection points
    for sol in solutions:
        ax.scatter(sol[0], sol[1], color='red', s=100, zorder=3, label="Solution" if sol is solutions[0] else "")

    # Customize plot
    ax.axhline(0, color='black', linewidth=1)  # x-axis
    ax.axvline(0, color='black', linewidth=1)  # y-axis
    ax.set_xlim(-5, 10)
    ax.set_ylim(-5, 10)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Graphical Representation of Linear Equations")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)

    # Show plot
    plt.show()


if __name__ == '__main__':
    main()
