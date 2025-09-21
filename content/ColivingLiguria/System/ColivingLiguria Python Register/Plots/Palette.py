#!/usr/bin/env python3
"""
Palette.py

Defines the central color palette and color scales for all plots and
visualizations within the ColivingLiguria project.

This file acts as a single source of truth for the project's visual identity,
ensuring a consistent brand aesthetic across all outputs. To use these colors,
import the `PALETTE` dictionary or the `HEATMAP_GREENS` list from this module.
"""

PALETTE = {
    # --- Primary Tones for Bookings ---
    # Used for core data representation like booking bars. A clear contrast is key.
    'private_booking': '#556B2F',  # DarkOliveGreen: A muted, darker green for primary elements.
    'shared_booking': '#C1E1C1',   # A very light, pastel green for secondary elements.
    'volunteer_booking': '#8FBC8F',# DarkSeaGreen: A mid-tone green for volunteer-specific items.

    # --- Neutral Tones (Backgrounds & Text) ---
    # A scale from light to dark for general chart elements.
    'background': '#F8F8F8',       # Ghost White: A clean, slightly off-white background.
    'text_primary': '#2F4F4F',     # DarkSlateGray: High-contrast dark text for titles/labels.
    'text_secondary': '#696969',   # DimGray: For annotations or less important text.
    'border': '#4F4F4F',           # A dark grey for subtle borders around chart elements.

    # --- Financial Tones ---
    # For use in financial dashboards (e.g., Revenue Waterfall).
    'financial_positive': '#2E8B57', # SeaGreen: For positive income or growth.
    'financial_negative': '#708090', # SlateGray: A neutral color for expenses or negative values.

    # --- Accent & Grid Tones ---
    # Used for guides and lines that should be present but not overpowering.
    'grid_major': '#A9A9A9',       # DarkGray: For important gridlines (e.g., check-in/out dates).
    'grid_minor': '#E0E0E0',       # A very light grey for subtle, daily background gridlines.
}

# --- Heatmap Color Scale ---
# A sequential green color scale designed for the Occupancy Heatmap Calendar.
# It ranges from very light (low occupancy) to very dark (high occupancy).
HEATMAP_GREENS = [
    '#F0FFF0',  # Honeydew (0% Occupancy)
    '#C1E1C1',  # Light Green
    '#8FBC8F',  # DarkSeaGreen
    '#556B2F',  # DarkOliveGreen
    '#2E402E'   # Very Dark Green (100% Occupancy)
]


# --- Visualizer (for direct execution) ---
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import numpy as np

    # --- Create the plot structure ---
    # We use gridspec for a more controlled layout
    fig = plt.figure(figsize=(12, 8))
    fig.patch.set_facecolor(PALETTE['background'])
    gs = fig.add_gridspec(3, 4, height_ratios=[1, 1, 0.5], hspace=0.8, wspace=0.4)

    fig.suptitle("ColivingLiguria Plotting Palette", fontsize=20, fontweight='bold', color=PALETTE['text_primary'])

    # --- Plot Discrete Palette Swatches ---
    palette_items = list(PALETTE.items())
    for i in range(min(len(palette_items), 8)):
        row = i // 4
        col = i % 4
        ax = fig.add_subplot(gs[row, col])
        
        name, color = palette_items[i]
        
        ax.add_patch(plt.Rectangle((0, 0.2), 1, 0.8, color=color))
        ax.text(0.5, 0.05, f"{name}\n({color})", ha='center', va='top', fontsize=10, color=PALETTE['text_secondary'])
        
        # Clean up the axes
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

    # --- Plot the Heatmap Gradient ---
    ax_heatmap = fig.add_subplot(gs[2, :]) # Span the full width of the last row
    
    cmap = mcolors.LinearSegmentedColormap.from_list("heatmap_greens", HEATMAP_GREENS)
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    
    ax_heatmap.imshow(gradient, aspect='auto', cmap=cmap)
    ax_heatmap.text(0.5, 1.2, "Occupancy Heatmap Gradient", transform=ax_heatmap.transAxes,
                    ha='center', va='bottom', fontsize=12, fontweight='bold', color=PALETTE['text_primary'])
    
    # Clean up the heatmap axes
    ax_heatmap.set_yticks([])
    ax_heatmap.set_xticks([0, 255])
    ax_heatmap.set_xticklabels(['0%', '100%'], color=PALETTE['text_secondary'])

    plt.show()

