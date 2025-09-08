from matplotlib.patches import FancyBboxPatch							
import matplotlib.pyplot as plt		
import pandas as pd					
							
# Create figure and axis							
							
fig, ax1 = plt.subplots(figsize=(10,6))							
# Sample data							
							
products = ["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10"]							
values = [50000,40000,30000,20000,15000,10000,8000,7000,5000,4000]							
							
# Bar plot (individual contributions)							
bars = ax1.bar(products, values, color="skyblue")							
ax1.set_xlabel("Products")							
ax1.set_ylabel("Annual Value (₹)", color="blue")							
ax1.tick_params(axis="y", labelcolor="blue")							
							
# Calculate cumulative percentages							
# Calculate total and percentages							
# Line plot cumulative percentage							
							
total = sum(values)							
percentages = [(v/total)*100 for v in values]							
cumulative = []							
cum_sum = 0							
for p in percentages:							
 cum_sum += p							
 cumulative.append(cum_sum)							
ax2 = ax1.twinx()							
ax2.plot(products, cumulative, color="red", marker="o", linestyle="-")							
ax2.set_ylabel("Cumulative % of Value", color="red")							
ax2.tick_params(axis="y", labelcolor="red")							
ax2.set_ylim(0, 110)							
							
# Highlight A, B, C categories							
# A: P1-P3, B: P4-P6, C: P7-P10							
for i in range(0, 3):							
 bars[i].set_color("green") # A items							
for i in range(3, 6):							
 bars[i].set_color("orange") # B items							
for i in range(6, 10):							
 bars[i].set_color("gray") # C items							
							
# Add grid and title							
plt.title("Pareto Chart with ABC Classification Highlighted")							
plt.grid(axis="y", linestyle="--", alpha=0.6)							
							
# Legend							
from matplotlib.patches import Patch							
legend_elements = [							
Patch(facecolor="green", label="A items (Top 63%)"),							
Patch(facecolor="orange", label="B items (Next ~25%)"),							
Patch(facecolor="gray", label="C items (Remaining ~13%)")							
]							
# Create legend							
leg = ax1.legend(							
handles=legend_elements,							
loc="upper right",							
bbox_to_anchor=(1, 0.72), # position							
framealpha=0.2,  # semi-transparent							
shadow=True, # enable shadow							
fancybox=True  # rounded corners							
)							
							
# Fine-tune the legend box							
frame = leg.get_frame()							
frame.set_boxstyle("round,pad=0.1,rounding_size=1") # control roundness							
frame.set_edgecolor("black") # border color							
frame.set_linewidth(0.8) # border thickness							
							
# Show plot							
plt.show()							
