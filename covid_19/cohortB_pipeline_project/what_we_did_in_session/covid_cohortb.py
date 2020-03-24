import pandas as pd
import datetime as dt
import sys


covid_data = pd.read_csv('full_data.csv')


def COVID_TERROR_PANIC_RUN_FIRE_EVERYWHERE(country):
#Corrects the case of the country
country = country.title()

#If the country isn't valid then return False
if country not in covid_data['location'].values:
print('No.')
return False;

#Grabs the rows from the table with the specified country
country_rows = covid_data[covid_data['location'] == country]

#Gets the last date entry of the country
max_date = country_rows.date.max()
#Formats the date into Month Day, Year
formated_date = dt.datetime.strptime(max_date, '%Y-%m-%d')
formated_date = formated_date.strftime('%B %d, %Y')

#Grabs the total cases and total deaths using max
total_case = country_rows.total_cases.max()
total_death = country_rows.total_deaths.max()
#Grabs the new_cases of the most recent date
date_new_case = int(country_rows.new_cases.tail(1))
#Grabs the total nu total_new_case = int(covid_data[covid_data['location'] == 'World'].new_cases.tail(1))

#Calculates the death rate using the total deaths and total cases
death_rate = (total_death / total_case) * 100

#Prints up the information in a fancy way
print('The total number of {} cases as of {}: {}.'.format(country, formated_date, total_case))
print('The total number of {} deaths as of {}: {:.0f}.'.format(country, formated_date, total_death))
print('As of {}, our {} death rate is {:.2f}%.'.format(formated_date, country, death_rate))
print('On {}, there were {:.0f} new cases reported in {}.'.format(max_date, date_new_case, country))
print('On {}, there are {:.0f} new cases reported.'.format(max_date, total_new_case))



if __name__ == '__main__':
print('Program Starting')
for i in sys.argv[1:]:
COVID_TERROR_PANIC_RUN_FIRE_EVERYWHERE(i)
print('\n')
print('Program Ended')

