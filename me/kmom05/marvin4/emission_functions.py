#!/usr/bin/env python3
""" Functions to calculate emissions for different contries """

from operator import itemgetter
import emission_data
#import emission_data_small

file_to_read = emission_data

def get_emission_year(year):
    """ Get emission data for a specified year """

    if year == 1990:
        emission = file_to_read.emission_1990
    elif year == 2005:
        emission = file_to_read.emission_2005
    elif year == 2017:
        emission = file_to_read.emission_2017
    else:
        raise ValueError
    
    return emission

def search_country(search_word, get_all_data = False):
    """ Get all the countries from a search word """

    countries = []
    country_data = []
    for key, value in file_to_read.country_data.items():
        if search_word.upper() in key.upper():
            countries.append(key)
            country_data.append(value)

    if not countries:
        raise ValueError

    if get_all_data:
        return (countries[0], country_data)

    return countries

def get_country_year_data_megaton(country, year):
    """ Get emission for a year from a defined country """

    country_id = file_to_read.country_data[country]["id"]
    try:
        emission_all = get_emission_year(year)
        emission = emission_all[country_id]
    except ValueError as exc:
        raise ValueError from exc
    
    return emission * 1000000

def get_country_change_for_years(country, year1, year2):
    """ Calculate the chaneg in emission for a country between two specified years """

    try:
        year1_emission = get_country_year_data_megaton(country, int(year1))
        year2_emission = get_country_year_data_megaton(country, int(year2))
        diff = year2_emission - year1_emission
        emission_change = diff / year1_emission * 100
    except ValueError as exc:
        raise ValueError from exc
 
    return round(emission_change, 2)

def get_country_data(country_name):
    """ Collect att data for a specific country """

    data = {}
    tup = search_country(country_name, True)
    country = tup[0]
    population = tup[1][0]['population']
    if len(population) == 0:
        population = [None, None, None]  

    emission_list = []
    years = [1990, 2005, 2017]
    for year in years:
        emission_list.append(get_country_year_data_megaton(country, year))
    
    data["name"] = country
    for index, year in enumerate(years):
        data[year] = {"emission": emission_list[index], "population": population[index]}

    emission_change1 = get_country_change_for_years(country, years[0], years[1])
    emission_change2 = get_country_change_for_years(country, years[1], years[2])
    data["emission_change"] = (emission_change1, emission_change2)

    return data

def print_country_data(data):
    """ Print the data from function 'get_country_data' """

    result = data["name"] + "\n"
    for key, value in data.items():
        if key == "emission_change":
            result += "Emission change - 1990-2005: " + str(value[0]) + "% - 2005-2017: " + str(value[1]) + "%\n"
        elif not key == "name":
            result += "Emission - " + str(key) + ": " + str(value["emission"]) +"\n"
            if not value["population"]:
                result += "Missing population data!\n" 
            else:
                result += "Population - " + str(key) + ": " + str(value["population"]) +"\n"
    print(result)

def get_nr_of_countries_emissions_for_a_year(year, nr_of_countries):
    """ Get a nr of sorted contries-emission for a specified year """

    data = ""
    emissions = get_emission_year(int(year))        
    countries = file_to_read.country_data
    emissions_as_list = emissions.items()
    sorted_emissions = sorted(emissions_as_list, key=itemgetter(1), reverse=True)
    count = 0

    for key, value in sorted_emissions:
        for key2 in countries:
            if countries.get(key2, {}).get("id") == key:
                data += key2 + ": " + str(value * 1000000) + "\n"
                count += 1
                break
        if count == int(nr_of_countries):
            break

    print(data)

def emissions_per_capita(year, nr_of_countries=-1):
    """ Get emission per capita for all or a specified nr of countries for a specific year """

    data = {}
    emissions = get_emission_year(int(year))
    countries_data = file_to_read.country_data

    index_pop = -1
    if year == "1990":
        index_pop = 0
    elif year == "2005":
        index_pop = 1
    elif year == "2017":
        index_pop = 2
    else:
        raise ValueError

    for key, value in emissions.items():
        for k in countries_data:
            if countries_data.get(k, {}).get("id") == key:
                try:
                    emission_per_capita = (round(value * 1000000 / 
                        countries_data.get(k, {}).get("population")[index_pop], 2))
                    data[k] = emission_per_capita
                except IndexError:
                    data[k] = -1

    sorted_res = sorted(data.items(), key=itemgetter(1), reverse=True)
    
    if int(nr_of_countries):
        temp = sorted_res[0:int(nr_of_countries)]
    
    result = ""
    for key, value in temp:
        result += key + ": " + str(value) + "\n"
    
    print(result)

def emissions_per_area(year, nr_of_countries=-1):
    """ Get emission per area for all or a specified nr of countries for a specific year """

    data = {}
    emissions = get_emission_year(int(year))
    countries_data = file_to_read.country_data

    for key, value in emissions.items():
        for k in countries_data:
            if countries_data.get(k, {}).get("id") == key:
                try:
                    emission_per_area = round(value * 1000000 / countries_data.get(k, {}).get("area"), 2) 
                    data[k] = emission_per_area
                except (IndexError, ZeroDivisionError):
                    data[k] = -1

    sorted_res = sorted(data.items(), key=itemgetter(1), reverse=True)
    
    if int(nr_of_countries):
        temp = sorted_res[0:int(nr_of_countries)]

    result = ""
    for key, value in temp:
        result += key + ": " + str(value) + "\n"
    
    print(result)
