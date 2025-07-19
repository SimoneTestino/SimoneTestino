---
draft: 
date: 2025-05-22
---
```Python
  from datetime import date, timedelta

from typing import List, Tuple, Optional

import calendar

  

# Define allowed string options for type hinting and validation

PROPERTY_TYPES = ["room shared facilities", "room with private facilities", "flat", "house", "villa"]

AIRBNB_RANKINGS = ["super host", "guest's favourite", "other"]

PREDEFINED_LOCATIONS = ["Ronco", "Busalla", "Crocefieschi", "Isola del Cantone", "Minceto", "Parco dell'Antola", "Borgo Fornari", "San Bartolomeo"]

  

class BnB:

DEFAULT_REMOTENESS_SCORES = {

"Busalla": 2,

"Ronco": 3,

"Isola del Cantone": 3,

"Crocefieschi": 4,

"Minceto": 5,

"Parco dell'Antola": 5,

"Borgo Fornari": 3,

"San Bartolomeo": 3

}

  

def __init__(

self,

raw_price_config: List[Optional[int]],

max_total_guests: int,

open_date_span: Tuple[date, date],

unavailable_periods: List[Tuple[date, date]],

rented_dates: List[Tuple[date, date, int]],

stars: float,

num_reviews: int,

property_type: str,

kitchen_available: bool,

pets_allowed: bool = True,

hosting_years: int = 0,

airbnb_ranking: str = "other",

bed_distribution: str = "",

breakfast_offered: bool = False,

breakfast_quality: Optional[int] = None,

location_name: str = "Unknown",

remoteness_score_input: Optional[int] = None,

link = None

):

# Validations for max guests

if not (0 <= max_total_guests):

raise ValueError("Maximum total guests cannot be negative.")

self.max_total_guests = max_total_guests

  

# Price List Validation

if max_total_guests > 0 and (not raw_price_config or raw_price_config[0] is None):

raise ValueError("Price for at least one person must be provided in raw_price_config if max_total_guests > 0.")

  

# Process pricing logic

prices_for_1_to_8_people = []

current_price_tier = raw_price_config[0] if raw_price_config and raw_price_config[0] is not None else 0

for i in range(8):

if i < len(raw_price_config) and raw_price_config[i] is not None:

current_price_tier = raw_price_config[i]

prices_for_1_to_8_people.append(current_price_tier)

  

self.effective_nightly_prices: List[int] = []

if self.max_total_guests > 0:

for i in range(self.max_total_guests):

if i < 8:

self.effective_nightly_prices.append(prices_for_1_to_8_people[i])

else:

self.effective_nightly_prices.append(prices_for_1_to_8_people[7])

  

# Calendar Details

if not (isinstance(open_date_span, tuple) and len(open_date_span) == 2 and

isinstance(open_date_span[0], date) and isinstance(open_date_span[1], date) and

open_date_span[0] <= open_date_span[1]):

raise ValueError("open_date_span must be a tuple of two valid dates (start, end) with start <= end.")

self.open_date_span: Tuple[date, date] = open_date_span

  

# Unavailable Periods

self.unavailable_periods: List[Tuple[date, date]] = [

period for period in unavailable_periods if period[0] <= period[1]

]

  

# Rented Dates

self.rented_dates: List[Tuple[date, date, int]] = [

booking for booking in rented_dates if booking[0] <= booking[1] and booking[2] > 0

]

  

# Validate stars

if not (0.0 <= stars <= 5.0):

raise ValueError("Stars must be a float between 0.0 and 5.0.")

self.stars: float = stars

  

# Validate number of reviews

if not isinstance(num_reviews, int) or num_reviews < 0:

raise ValueError("Number of reviews must be a non-negative integer.")

self.num_reviews: int = num_reviews

  

# Validate property type

if property_type not in PROPERTY_TYPES:

raise ValueError(f"Invalid property_type: '{property_type}'. Must be one of {PROPERTY_TYPES}")

self.property_type: str = property_type

  

self.kitchen_available: bool = kitchen_available

self.pets_allowed: bool = pets_allowed

self.hosting_years: int = max(hosting_years, 0)

self.airbnb_ranking: str = airbnb_ranking if airbnb_ranking in AIRBNB_RANKINGS else "other"

self.bed_distribution: str = bed_distribution

self.breakfast_offered: bool = breakfast_offered

  

if self.breakfast_offered:

if breakfast_quality is None or not (0 <= breakfast_quality <= 5):

raise ValueError("Breakfast quality must be between 0 and 5 if breakfast is offered.")

self.breakfast_quality: Optional[int] = breakfast_quality

else:

self.breakfast_quality: Optional[int] = None

  

self.location_name: str = location_name

  

if remoteness_score_input is not None:

if not (0 <= remoteness_score_input <= 5):

raise ValueError("Remoteness score must be between 0 and 5.")

self.remoteness_score: int = remoteness_score_input

elif location_name in self.DEFAULT_REMOTENESS_SCORES:

self.remoteness_score: int = self.DEFAULT_REMOTENESS_SCORES[location_name]

else:

raise ValueError(f"Remoteness score must be provided for unrecognized location: '{location_name}'.")

  

def get_price_for_guests(self, num_guests: int) -> Optional[int]:

if not (1 <= num_guests <= self.max_total_guests):

return None

return self.effective_nightly_prices[num_guests - 1]

  

def calculate_revenue(self) -> float:

"""Calculate total revenue based on rented dates and nightly price."""

revenue = 0

for start_date, end_date, guests in self.rented_dates:

nights = (end_date - start_date).days # Calculate number of nights

price_per_night = self.get_price_for_guests(guests)

if price_per_night:

revenue += nights * price_per_night

return revenue

  

def __repr__(self):

return (f"BnB(location='{self.location_name}', max_guests={self.max_total_guests}, "

f"stars={self.stars}, type='{self.property_type}', reviews={self.num_reviews})")

  

# --- Airbnb Instances ---

bnb_list: List[BnB] = [

BnB(raw_price_config=[82], max_total_guests=4, open_date_span=(date(2025, 5, 25), date(2025, 7, 23)), unavailable_periods=[], rented_dates=[

(date(2025, 5, 27), date(2025, 6, 1), 2),

(date(2025, 6, 6), date(2025, 6, 10), 2),

(date(2025, 6, 14), date(2025, 6, 15), 2),

(date(2025, 6, 19), date(2025, 6, 22), 2),

(date(2025, 7, 8), date(2025, 7, 15), 2)

], stars=4.96, num_reviews=49, property_type="flat", kitchen_available=True, pets_allowed=True, hosting_years=2, airbnb_ranking="super host", bed_distribution="2 bedrooms, 3 beds, 1 bathroom", breakfast_offered=False, location_name="Crocefieschi"),

BnB(raw_price_config=[69], max_total_guests=3, open_date_span=(date(2025, 5, 25), date(2025, 10, 30)), unavailable_periods=[], rented_dates=[

(date(2025, 5, 27), date(2025, 6, 7), 2),

(date(2025, 6, 16), date(2025, 6, 22), 2),

(date(2025, 6, 28), date(2025, 7, 8), 2),

(date(2025, 8, 2), date(2025, 8, 15), 2),

(date(2025, 8, 30), date(2025, 9, 10), 2)

], stars=5.0, num_reviews=52, property_type="flat", kitchen_available=True, pets_allowed=True, hosting_years=2, airbnb_ranking="super host", bed_distribution="1 bedrooms, 2 beds, 1 bathroom", breakfast_offered=False, location_name="Borgo Fornari"),

BnB(raw_price_config=[64], max_total_guests=5, open_date_span=(date(2025, 6, 1), date(2025, 9, 30)), unavailable_periods=[], rented_dates=[

(date(2025, 6, 6), date(2025, 6, 7), 2),

(date(2025, 6, 10), date(2025, 6, 15), 2),

(date(2025, 6, 21), date(2025, 7, 22), 2),

(date(2025, 7, 2), date(2025, 7, 2), 2),

(date(2025, 8, 8), date(2025, 8, 10), 2),

(date(2025, 8, 17), date(2025, 8, 18), 2),

(date(2025, 9, 3), date(2025, 9, 11), 2),

(date(2025, 9, 27), date(2025, 9, 30), 2)

], stars=5.0, num_reviews=52, property_type="room with private facilities", kitchen_available=True, pets_allowed=True, hosting_years=2, airbnb_ranking="super host", bed_distribution="B&B", breakfast_offered=True, breakfast_quality=3, location_name="Busalla"),

BnB(raw_price_config=[60], max_total_guests=4, open_date_span=(date(2025, 5, 25), date(2025, 10, 1)), unavailable_periods=[], rented_dates=[

(date(2025, 5, 30), date(2025, 7, 2), 2),

(date(2025, 6, 7), date(2025, 6, 9), 2),

(date(2025, 6, 20), date(2025, 7, 22), 2),

(date(2025, 8, 3), date(2025, 8, 5), 2),

(date(2025, 8, 8), date(2025, 8, 10), 2),

(date(2025, 8, 16), date(2025, 8, 23), 2),

(date(2025, 8, 29), date(2025, 9, 12), 2)

], stars=4.87, num_reviews=117, property_type="flat", kitchen_available=True, pets_allowed=True, hosting_years=7, airbnb_ranking="none", bed_distribution="1 bedrooms, 2 beds, 1 bathroom", breakfast_offered=False, location_name="San Bartolomeo")

]

# --- Exclude BnBs based on User Choice ---

excluded_indices = {} # Example: Exclude the 3rd Airbnb in the list

bnb_list_filtered = [bnb for idx, bnb in enumerate(bnb_list) if (idx + 1) not in excluded_indices]

  

print("List of Considered BnBs:")

for idx, bnb in enumerate(bnb_list_filtered):

print(f" {idx + 1}: {bnb.location_name} ({bnb.property_type}) - Stars: {bnb.stars}, Reviews: {bnb.num_reviews}")

  

# --- Run Calculations ---

  

# --- Configuration Parameters ---

income_percentage_out = 0.05 # 15% tax

fixed_cost_per_booking = 0 # Fixed costs per booking (set to 0 for now)

house_value_eur = 18000.00 # Value of the house

  

# --- Initialize Data Structures ---

average_gross_monthly_profit = {}

average_net_monthly_profit = {}

bnb_active_days_per_month = {}

net_monthly_average_per_day = {}

percentage_open_airbnb = {}

  

# --- Calculate Overall Date Range for All BnBs ---

start_dates = [bnb.open_date_span[0] for bnb in bnb_list_filtered]

end_dates = [bnb.open_date_span[1] for bnb in bnb_list_filtered]

overall_start_date = min(start_dates)

overall_end_date = max(end_dates)

  

# Initialize data structures for each month in the range

current_date_iterator = overall_start_date

while current_date_iterator <= overall_end_date:

year_month = (current_date_iterator.year, current_date_iterator.month)

average_gross_monthly_profit[year_month] = 0

average_net_monthly_profit[year_month] = 0

bnb_active_days_per_month[year_month] = {}

net_monthly_average_per_day[year_month] = 0

percentage_open_airbnb[year_month] = 0

current_date_iterator = (current_date_iterator.replace(day=28) + timedelta(days=4)).replace(day=1)

  

total_bnb_count = len(bnb_list_filtered)

  

# --- Compute Monthly Profits and Stats ---

for bnb in bnb_list:

for booking_start_date, booking_end_date, guests in bnb.rented_dates:

current_night = booking_start_date

while current_night < booking_end_date:

year_month = (current_night.year, current_night.month)

  

# Gross and net profit computations

price_per_night = bnb.get_price_for_guests(guests) or 0

average_gross_monthly_profit[year_month] += price_per_night / total_bnb_count

average_net_monthly_profit[year_month] += (price_per_night * (1 - income_percentage_out)) / total_bnb_count

  

# Track days of activity for each BnB in this month

if bnb not in bnb_active_days_per_month[year_month]:

bnb_active_days_per_month[year_month][bnb] = set()

bnb_active_days_per_month[year_month][bnb].add(current_night)

  

current_night += timedelta(days=1)

  

# --- Finalize Calculations for Averages and Open Percentages ---

for year_month in average_gross_monthly_profit.keys():

# Total days in the month

days_in_month = calendar.monthrange(year_month[0], year_month[1])[1]

  

# Calculate the daily average net profit (net profit / total days in the month)

net_monthly_average_per_day[year_month] = average_net_monthly_profit[year_month] / days_in_month

  

# Determine the percentage of Airbnbs open in this month

bnbs_open_in_month = sum(

1 for bnb in bnb_list_filtered

if bnb.open_date_span[0] <= date(year_month[0], year_month[1], days_in_month) and

bnb.open_date_span[1] >= date(year_month[0], year_month[1], 1)

)

percentage_open_airbnb[year_month] = (bnbs_open_in_month / total_bnb_count) * 100

  

# --- Output Results ---

print("Enhanced Market Analysis:")

print(f" Overall Airbnb Open Dates: {overall_start_date} to {overall_end_date}\n")

  

print(" Monthly Profit Analysis (Averages Across All BnBs):")

seasonal_gross_revenue = {"Spring": 0, "Summer": 0, "Autumn": 0, "Winter": 0}

seasonal_net_revenue = {"Spring": 0, "Summer": 0, "Autumn": 0, "Winter": 0}

  

seasons_map = {

3: "Spring", 4: "Spring", 5: "Spring",

6: "Summer", 7: "Summer", 8: "Summer",

9: "Autumn", 10: "Autumn", 11: "Autumn",

12: "Winter", 1: "Winter", 2: "Winter",

}

  

total_months_reported = 0

total_avg_gross_revenue = 0

total_avg_net_revenue = 0

  

for (year, month), gross in sorted(average_gross_monthly_profit.items()):

if gross > 0:

net = average_net_monthly_profit[(year, month)]

net_avg_per_day = net_monthly_average_per_day[(year, month)]

airbnb_open_percentage = percentage_open_airbnb[(year, month)]

month_name = calendar.month_name[month]

  

print(f"{month_name} {year}")

print(f" Average Gross Profit Per BnB: €{gross:.2f}")

print(f" Average Net Profit Per BnB: €{net:.2f}")

print(f" Average Net Profit Per Day: €{net_avg_per_day:.2f}")

print(f" Percentage of Airbnbs Open: {airbnb_open_percentage:.2f}%\n")

  

# Update seasonal revenues (normalized for average per Airbnb)

seasonal_gross_revenue[seasons_map[month]] += gross

seasonal_net_revenue[seasons_map[month]] += net

  

total_months_reported += 1

total_avg_gross_revenue += gross

total_avg_net_revenue += net

  

# --- Display Seasonal and Overall Totals ---

print("\nSeasonal Net Revenue (Per Average Airbnb):")

for season, revenue in seasonal_net_revenue.items():

print(f" {season}: €{revenue:.2f}")

  

if total_months_reported > 0:

print(f"\nAverage Yearly Gross Revenue (Per Airbnb): €{total_avg_gross_revenue:.2f}")

print(f"Average Yearlt Net Revenue (Per Airbnb): €{total_avg_net_revenue:.2f}")

  

if house_value_eur > 0:

net_revenue_ratio = (total_avg_net_revenue / house_value_eur) * 100

print(f"\nNet Revenue as % of House Value: {net_revenue_ratio:.2f}%")

else:

print("\nHouse value not set or zero, cannot calculate net revenue as percentage of house value.")
```