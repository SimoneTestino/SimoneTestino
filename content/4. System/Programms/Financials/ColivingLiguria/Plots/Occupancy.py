import pandas as pd
import plotly.express as px
from datetime import date, timedelta

# 1. Create a sample dataset of events (bookings)
# The data is a list of dictionaries, which can easily be converted to a pandas DataFrame
tasks_data = [
    dict(Task="Room A", Start=date(2025, 9, 1), End=date(2025, 10, 31), Person="Alice"),
    dict(Task="Room A", Start=date(2025, 11, 15), End=date(2025, 12, 15), Person="Bob"),
    dict(Task="Room B", Start=date(2025, 9, 10), End=date(2025, 11, 10), Person="Charlie"),
    dict(Task="Room B", Start=date(2025, 11, 15), End=date(2026, 1, 15), Person="Alice")
]

# 2. Convert the data to a DataFrame
df = pd.DataFrame(tasks_data)

# 3. Create the timeline plot
fig = px.timeline(df, x_start="Start", x_end="End", y="Task", color="Person",
                   title="Simple Booking Schedule")

# 4. Display the plot in a web browser
fig.show()

# You can also save it as a static image or an HTML file
# fig.write_html("simple_timeline.html")
# fig.write_image("simple_timeline.png")pip