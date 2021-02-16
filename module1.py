# pop_calculate.py
# CS 1181
# D. Ivan Ochoa
# 16 February, 2021
# Jon Holmes
# Description: script of functions required for population_sim to run.


def as_rate(rate_percentage: str) -> float:
    """accepts desired rate string and returns it as a float"""
    amount_in_percent = float(rate_percentage)/100
    return amount_in_percent


def years_increase(current_pop: float, growth_rate: float) -> float:
    """calculates increase in population for current year
    and returns value as float"""
    pop_increase = current_pop * growth_rate
    return float(pop_increase)


def expected_population(starting_pop: int, pop_growth_time: int, growth_rate: float) -> int:
    """calculates the expected size of the population
    at the end of the time and returns that value as an integer."""
    pop_at_end = starting_pop * (1 + growth_rate) ** pop_growth_time
    return round(pop_at_end)


def ending_population(starting_pop: float, growth_rate: float) -> float:
    """calculates the population at the end of the year and returns
    float"""
    pop_at_end = starting_pop + (years_increase(starting_pop, growth_rate))
    return pop_at_end

