"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

###############################################################################################################

def PrintRequirement1(city, first_events_list, last_events_list, num_cities,
                                                               most_events_city, num_events_city):
    print('=============== Req No. 1 Inputs ===============')
    print('UFO Sightings in the city of:', city)
    print('')
    print('=============== Req No. 1 Answer ===============')
    print('There are', num_cities, 'different cities with UFO sightings...')
    print('The city with most UFO sightings is:', most_events_city)
    print('')
    print('There are', num_events_city, 'sightings at the:', city, ' city.')
    print('The first 3 and last 3 UFO sightings in the city are:')
    print('+' + 22*'-' + '+' + 30*'-' + '+' + 10*'-'+ '+' + 10*'-' + '+' + 11*'-' + '+' + 16*'-' + '+')
    print('| {:<21}| {:<29}| {:<9}| {:<9}| {:<10}|{:>15} |'.format('datetime', 'city', 'state', 'country',
                                                                        'shape', 'duration (seg)'))
    print('+' + 22*'=' + '+' + 30*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in first_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<29}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 30*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in last_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<29}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 30*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')

###############################################################################################################

def PrintRequirement2(initial_duration, end_duration, first_events_list, last_events_list, 
                    num_durations, most_duration, num_events_most_duration, num_events_duration_interval):
    print('=============== Req No. 2 Inputs ===============')
    print('UFO Sightings between', initial_duration, 'and', end_duration, 'seg')
    print('')
    print('=============== Req No. 2 Answer ===============')
    print('There are', num_durations, 'different durations of UFO sightings...')
    print('The longest UFO sightings are:')
    print('+' + 21*'-' + '+' + 8*'-' + '+')
    print('|{:>20} |{:>7} |'.format('duration (seconds)', 'count'))
    print('+' + 21*'=' + '+' + 8*'=' + '+')
    print('|{:>20} |{:>7} |'.format(most_duration, num_events_most_duration))
    print('+' + 21*'-' + '+' + 8*'-' + '+')
    print('')
    print('There are', num_events_duration_interval, 'sightings between:', initial_duration, 'and', 
                                                                    end_duration, 'seg of duration')
    print('The first 3 and last 3 UFO sightings in the duration time are:')
    print('+' + 22*'-' + '+' + 30*'-' + '+' + 10*'-'+ '+' + 10*'-' + '+' + 11*'-' + '+' + 16*'-' + '+')
    print('| {:<21}| {:<29}| {:<9}| {:<9}| {:<10}|{:>15} |'.format('datetime', 'city', 'state', 'country',
                                                                        'shape', 'duration (seg)'))
    print('+' + 22*'=' + '+' + 30*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in first_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<29}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 30*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in last_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<29}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 30*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')

###############################################################################################################
# Menu principal
###############################################################################################################

catalog = None

def Menu():
    print('')
    print("Welcome")
    print("1- Initialize catalog")
    print('2- Load information from catalog')
    print('3- Show information from catalog')
    print('4- Requirement 1')
    print('5- Requirement 2')
    print('6- Requirement 3')
    print('7- Requirement 4')
    print('8- Requirement 5')
    print('9- Requirement 6')
    print('0- Finish program')
    option = int(input('Choose an option: '))
    return option

def UserProgram(test, option, catalog, input_1, input_2, input_3):
    if not test:
        option = Menu()
        while option != 0:
            if option == 1:
                print("initializing Information from UFOS-utf8-small.csv ....")
                catalog = controller.initialization()
                print('test')

            elif option == 2:
                print("Loading Information from UFOS-utf8-small.csv ....")
                controller.loadData(catalog)
            
            elif option == 3:
                information = controller.catalog_information(catalog)
                tree_length = information[0]
                num_sighting = information[1]
                print('The length of the RBT tree is', tree_length, 'there are ',
                                                                num_sighting, 'events registred.')
                                                            
            elif option == 4:
                city = input('Enter a City: ')
                print('Loading...')
                information = controller.Requirement1(catalog, city)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_cities = information[3]
                most_events_city = information[4]
                num_events_city = information[5]
                print('The requiremnt took', time_elapsed, 'mseg to execute')
                PrintRequirement1(city, first_events_list, last_events_list, 
                                                        num_cities, most_events_city, num_events_city)

            elif option == 5:
                initial_duration = int(input('Enter the first duration of the interval: '))
                end_duration = int(input('Enter the last duration of the interval: ')) 
                print('Loading...')
                information = controller.Requirement2(catalog, initial_duration, end_duration)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_durations = information[3]
                most_duration = information[4]
                num_events_most_duration = information[5]
                num_events_duration_interval = information[6]
                print('The requiremnt took', time_elapsed, 'mseg to execute')
                PrintRequirement2(initial_duration, end_duration, first_events_list, last_events_list, 
                    num_durations, most_duration, num_events_most_duration, num_events_duration_interval)

            else:
                print('Please choose a valid option')
            
            option = Menu()
    
    else:
        if option == 0:
           catalog = controller.initialization()
           controller.loadData(catalog)
           return  catalog
        elif option == 1:
            city_name = input_1
            information = controller.Requirement1(catalog, city_name)
            time_elapsed = information[0]
            return time_elapsed
    
UserProgram(False, 0, catalog, 0, 0, 0)