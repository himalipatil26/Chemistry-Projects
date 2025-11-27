"""
pH Indicator Visualizer
-----------------------
A colorful chemistry mini-project to visualize the relationship between pH,
solution color, and hydrogen ion concentration.

Developed for Class 11 Chemistry using Python and Matplotlib.
Author: Himali Patil
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex

# =====================================================
# Utility Functions
# =====================================================

def ph_to_rgb(ph: float):
    """
    Convert pH value (0–14) to RGB color.
    Acidic (0) → Red | Neutral (7) → Green | Basic (14) → Blue
    """
    ph = np.clip(ph, 0, 14)
    if ph <= 7:
        t = ph / 7
        r = 1 - t
        g = t
        b = 0
    else:
        t = (ph - 7) / 7
        r = 0
        g = 1 - t
        b = t
    return (r, g, b)


def classify(ph: float):
    """Return solution type based on pH."""
    if ph < 7:
        return "Acidic"
    elif ph > 7:
        return "Basic"
    return "Neutral"


# =====================================================
# Visualization Function
# =====================================================

def show_visualization(ph: float):
    """
    Display:
    - pH-based color
    - Hydrogen ion concentration graph [H+] vs pH
    """
    ph = np.clip(ph, 0, 14)
    color = ph_to_rgb(ph)
    hex_color = to_hex(color)

    # Create figure
    fig, (ax_color, ax_graph) = plt.subplots(1, 2, figsize=(9, 3.8))
    fig.suptitle("pH Indicator Visualizer", fontsize=15, fontweight="bold")

    # ------------------------------
    # Left: Color block visualization
    # ------------------------------
    ax_color.imshow([[color]])
    ax_color.set_title(f"pH = {ph:.2f}\n({classify(ph)})", fontsize=12, pad=12)
    ax_color.text(0.5, -0.25, f"Color Code: {hex_color}",
                  transform=ax_color.transAxes,
                  ha="center", fontsize=10, color="#333")
    ax_color.axis("off")

    # ------------------------------
    # Right: [H⁺] vs pH graph
    # ------------------------------
    ph_values = np.linspace(0, 14, 300)
    h_conc = 10 ** (-ph_values)

    ax_graph.semilogy(ph_values, h_conc, color='darkgreen', lw=2)
    ax_graph.scatter(ph, 10 ** (-ph), color=color, edgecolor='black', s=80, zorder=5)

    ax_graph.set_xlabel("pH", fontsize=11)
    ax_graph.set_ylabel("[H⁺] (mol/L)", fontsize=11)
    ax_graph.set_xlim(0, 14)
    ax_graph.set_ylim(1e-15, 1)
    ax_graph.grid(True, linestyle="--", alpha=0.6)
    ax_graph.set_title("Hydrogen Ion Concentration vs pH", fontsize=12)

    plt.tight_layout()
    plt.show()


# =====================================================
# Program Entry Point
# =====================================================

if __name__ == "__main__":
    print("🔬 pH Indicator Visualizer — Chemistry Mini Project")
    print("---------------------------------------------------")
    print("This program shows how pH relates to color and [H⁺] concentration.\n")

    try:
        user_ph = float(input("Enter a pH value (0–14): "))
        show_visualization(user_ph)
    except ValueError:
        print("⚠️ Invalid input! Please enter a numeric value between 0 and 14.")
