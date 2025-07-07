def max_population_count(logs):
    events = {}
    for birth, death in logs:
        events[birth] = events.get(birth, 0) + 1
        events[death] = events.get(death, 0) - 1

    years = sorted(events.keys())

    max_population = 0
    current_population = 0
    earliest_year = float('inf')

    for year in years:
        current_population += events[year]
        if current_population > max_population:
            max_population = current_population
            earliest_year = year
        elif current_population == max_population:
            earliest_year = min(earliest_year, year)

    return earliest_year


print(max_population_count([[1993, 1999], [2000, 2010]]))
print(max_population_count([[1950, 1961], [1960, 1971], [1970, 1981]]))
print(max_population_count([[1982, 1998], [2013, 2042], [2010, 2035], [2022, 2050], [2047, 2048]]))
