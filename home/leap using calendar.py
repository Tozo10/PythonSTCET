import calendar

# Function to check if a year is a leap year
def is_leap_year(year):
    return calendar.isleap(year)

# Define a range of years
start_year = 2000
end_year = 2023  # Replace with your desired end year

# Count the number of leap years within the range
leap_years = [year for year in range(start_year, end_year + 1) if is_leap_year(year)]

# Print the list of leap years and their count
print(f"Leap years between {start_year} and {end_year}:")
print(leap_years)
print(f"Total leap years: {len(leap_years)}")
