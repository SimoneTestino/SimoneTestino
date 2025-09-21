#!/usr/bin/env python3
"""
OccupancyGanttChart.py

Generates a detailed, bed-by-bed occupancy Gantt chart for all bookings.
This advanced chart provides a high-precision timeline, differentiating booking
types with a custom green color palette and representing each available bed
as a distinct row.
"""

import sys
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date, timedelta

# --- ROBUST PATH SETUP ---
current_dir = os.path.dirname(os.path.abspath(__file__))
coliving_dir = os.path.dirname(current_dir)
if coliving_dir not in sys.path:
    sys.path.insert(0, coliving_dir)

# --- Project Imports ---
from Constants.ActualData import cascina_brignone_register
from RegisterClasses.Booking import Booking
# --- FIX: Import the centralized color palette instead of defining colors locally ---
from Plots.Palette import PALETTE

# ==============================================================================
# PLOTTING FUNCTION
# ==============================================================================

def plot_occupancy_gantt(register):
    """
    Generates and displays a detailed, bed-by-bed Gantt chart of bookings.
    """
    if not register.bookings:
        print("No bookings found in the register to plot.")
        return

    # 1. DATA PREPARATION: CREATE INDIVIDUAL BED SLOTS
    y_labels = []
    bookable_rooms = sorted(
        list(set(b.room for b in register.bookings if b.room.actual_capacity > 0)),
        key=lambda r: r.name
    )
    for room in bookable_rooms:
        for i in range(1, room.actual_capacity + 1):
            y_labels.append(f"{room.name} [{i}]")

    if not y_labels:
        print("No bookable rooms with capacity found.")
        return
        
    fig, ax = plt.subplots(figsize=(22, 14))
    # --- FIX: Use colors from the imported PALETTE ---
    fig.patch.set_facecolor(PALETTE['background'])
    ax.set_facecolor(PALETTE['background'])

    # 2. PLOTTING LOGIC: PLACE BOOKINGS AND CUSTOM GRIDLINES
    bed_occupancy = {label: [] for label in y_labels}
    sorted_bookings = sorted(register.bookings, key=lambda b: b.check_in_date)
    
    ax.set_ylim(len(y_labels) - 0.5, -0.5)

    for booking in sorted_bookings:
        placed = False
        possible_labels = [label for label in y_labels if booking.room.name in label]
        
        for label in possible_labels:
            is_occupied = False
            for start, end in bed_occupancy[label]:
                if max(start, booking.check_in_date) < min(end, booking.check_out_date):
                    is_occupied = True
                    break
            
            if not is_occupied:
                y_pos = y_labels.index(label)
                bed_occupancy[label].append((booking.check_in_date, booking.check_out_date))
                # --- FIX: Use colors from the imported PALETTE ---
                color = PALETTE['private_booking'] if booking.room_type == 'private' else PALETTE['shared_booking']
                duration = (booking.check_out_date - booking.check_in_date).days
                start_date_num = mdates.date2num(booking.check_in_date)

                ax.barh(y_pos, duration, left=start_date_num, height=0.6, 
                        color=color, edgecolor=PALETTE['border'], alpha=0.9, linewidth=0.7, zorder=2)
                
                line_y_start = y_pos + 0.3
                line_y_end = ax.get_ylim()[0]
                
                # --- FIX: Use colors from the imported PALETTE ---
                ax.plot([booking.check_in_date, booking.check_in_date], [line_y_start, line_y_end],
                        color=PALETTE['grid_major'], linestyle='--', linewidth=1.0, zorder=1)
                ax.plot([booking.check_out_date, booking.check_out_date], [line_y_start, line_y_end],
                        color=PALETTE['grid_major'], linestyle='--', linewidth=1.0, zorder=1)

                ax.text(start_date_num + duration / 2, y_pos, f" {booking.guest.name}",
                        ha='center', va='center', color=PALETTE['text_primary'], 
                        fontweight='bold', fontsize=9, clip_on=True, zorder=3)
                
                placed = True
                break
        
        if not placed:
            print(f"Warning: Could not place booking for {booking.guest.name} in {booking.room.name}. Room may be overbooked.")

    # 3. FORMATTING THE PLOT
    # --- FIX: Use colors from the imported PALETTE ---
    ax.set_yticks(range(len(y_labels)))
    ax.set_yticklabels(y_labels, fontsize=10, color=PALETTE['text_primary'])

    min_date = min(b.check_in_date for b in register.bookings) - timedelta(days=5)
    max_date = max(b.check_out_date for b in register.bookings) + timedelta(days=5)

    important_dates = set()
    for b in register.bookings:
        important_dates.add(b.check_in_date)
        important_dates.add(b.check_out_date)

    sorted_dates = sorted(list(important_dates))

    ax.set_xticks(sorted_dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    ax.xaxis_date()
    
    # --- FIX: Use colors from the imported PALETTE ---
    ax.grid(axis='x', linestyle=':', color=PALETTE['grid_minor'], which='minor')

    ax.set_xlim(min_date, max_date)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", color=PALETTE['text_primary'])
    
    # --- FIX: Use colors from the imported PALETTE ---
    ax.set_title(f"Occupancy Chart for {register.name}", fontsize=18, fontweight='bold', color=PALETTE['text_primary'], pad=20)
    ax.set_xlabel("Date", fontsize=12, color=PALETTE['text_primary'])
    ax.set_ylabel("Bed Slot", fontsize=12, color=PALETTE['text_primary'])
    
    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis='both', which='both', length=0)

    # --- FIX: Use colors from the imported PALETTE ---
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, color=PALETTE['private_booking'], label='Private Booking'),
        plt.Rectangle((0, 0), 1, 1, color=PALETTE['shared_booking'], label='Shared Booking')
    ]
    ax.legend(handles=legend_elements, loc='upper right', frameon=False,
              labelcolor=PALETTE['text_primary'], bbox_to_anchor=(0.99, 0.99))

    plt.tight_layout()
    plt.show()

# --- SCRIPT EXECUTION ---
if __name__ == "__main__":
    print("Generating High-Precision Occupancy Gantt Chart...")
    plot_occupancy_gantt(cascina_brignone_register)
    print("Plot display complete.")

