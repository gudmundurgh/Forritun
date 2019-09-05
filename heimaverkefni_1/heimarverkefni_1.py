population_now = 307357870
seconds_per_year = 60 * 60 * 24 * 365
births_per_year = seconds_per_year / 7
deaths_per_year = seconds_per_year / 13
immigrants_per_year = seconds_per_year / 35
year = int(input("Years: "))

population_future_float = population_now + (year * births_per_year) - (year * deaths_per_year) + (year * immigrants_per_year)
population_future_int = int(population_future_float)
if year < 0:
    print("Invalid input!")
else:
    print("New population after", year, "years is", population_future_int)