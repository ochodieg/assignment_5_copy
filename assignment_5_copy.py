# population_sim.py
# CS 1181
# D. Ivan Ochoa
# 16 February, 2021
# Jon Holmes
# Description: Imports a script I made that is required to run.
# Then prompts user Variables required to run a population
# growth simulation during an asked amount of time.
import module1

# first two function simply request for string imput and
# return the input as ints


def get_population() -> int :
    """Prompts user for starting population"""
    starting_pop = input("What will be the starting population? ")
    return int(starting_pop)


def get_years_to_run() -> int:
    """prompts user for simulation length"""
    simulation_length = input("How many years should the simulations run? ")
    return int(simulation_length)


def get_growth_rate() -> float:     # this finction returns user input as float
    """prompts user for growth rate"""  # the user input is a string
    requested_rate = input("What will be the predicted population growth rate percentage? ")
    rate_in_float = module1.as_rate(requested_rate)   # the string is then converted...
    return rate_in_float        # ...to and returned as float by using imported function


def get_table_row(year: int, starting_pop: float, rate_in_float: float) -> str:
    """Gives: year, starting population, increase, and ending population
     formatted in columns"""
    # function prints out rows of predicted populations increase. Amount of rows
    # depends on user input

    line = ""
    num = 1
    starting_population = starting_pop
    

    for one in range(year): # for loop iterates by value passed down from function parameters

        increase = module1.years_increase(starting_population, rate_in_float)
        ending_pop = module1.ending_population(starting_population, rate_in_float)
      
        line = line + format(str(num), "<5") + \
            format(str(round(starting_population)), "^32") + \
            format(str(round(increase)), "^10") + \
            format(str(round(ending_pop)), "^30") + "\n"

        num = num + 1
        starting_population = starting_population + increase        

    return line


population = get_population()
population_string = str(population)
growth_rate = get_growth_rate()
growth_rate_string = str(growth_rate * 100)
years = get_years_to_run()
years_string = str(years)


print("\nGiven a starting population of "\
      + population_string + ", "\
      + years_string + " years of time,"\
      + "\nand a growth rate of "\
      + growth_rate_string + "%, "\
      "the ending population \nshould be approximately: "\
      + '{:,.0f}'.format(module1.expected_population(population, years, growth_rate))\
      # line above formats value to have commas.
      + " residents."\
      "\n\nHere are the results:")


table_rows = get_table_row(years, population, growth_rate)

print("\nyears" + format("starting", "^33") + format("increase", "^3") + format("ending", "^30") + "\n"\
      + "---------------------------------------------------------------------\n" + table_rows)


