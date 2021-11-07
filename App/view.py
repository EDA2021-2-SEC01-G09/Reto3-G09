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

def PrintRequirement1(city, first_events_list, last_events_list, 
                                                        num_cities, most_events_city, num_events_city):
    print('=============== Req No. 1 Inputs ===============')
    print('UFO Sightings in the city of:', city)
    print('')
    print('=============== Req No. 1 Answer ===============')
    print('There are', num_cities, 'different cities with UFO sightings...')
    print('The city with most UFO sightings is:', most_events_city)
    print('')
    print('There are', num_events_city, 'sightings at the:', city, 'city.')
    print('The first 3 and last 3 UFO sightings in the city are:')
    print('+' + 22*'-' + '+' + 50*'-' + '+' + 10*'-'+ '+' + 10*'-' + '+' + 11*'-' + '+' + 16*'-' + '+')
    print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format('datetime', 'city', 'state', 'country',
                                                                        'shape', 'duration (seg)'))
    print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in first_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in last_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')

###############################################################################################################

def PrintRequirement2(initial_duration, end_duration, first_events_list, last_events_list, 
                    num_durations, longest_duration, num_events_longest_duration, num_events_duration_interval):
    print('=============== Req No. 2 Inputs ===============')
    print('UFO Sightings between', initial_duration, 'and', end_duration, 'seg')
    print('')
    print('=============== Req No. 2 Answer ===============')
    print('There are', num_durations, 'different durations of UFO sightings...')
    print('The longest UFO sightings are:')
    print('+' + 21*'-' + '+' + 8*'-' + '+')
    print('|{:>20} |{:>7} |'.format('duration (seconds)', 'count'))
    print('+' + 21*'=' + '+' + 8*'=' + '+')
    print('|{:>20} |{:>7} |'.format(int(longest_duration), num_events_longest_duration))
    print('+' + 21*'-' + '+' + 8*'-' + '+')
    print('')
    print('There are', num_events_duration_interval, 'sightings between:', float(initial_duration), 'and', 
                                                                    float(end_duration), 'seg of duration')
    print('The first 3 and last 3 UFO sightings in the duration time are:')
    print('+' + 22*'-' + '+' + 50*'-' + '+' + 10*'-'+ '+' + 10*'-' + '+' + 11*'-' + '+' + 16*'-' + '+')
    print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format('datetime', 'city', 'state', 'country',
                                                                        'shape', 'duration (seg)'))
    print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in first_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in last_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')

###############################################################################################################

def PrintRequirement3(initial_time, end_time, first_events_list, last_events_list, 
                                    num_times, latest_time, num_events_latest_time, num_events_time_interval):
    print('=============== Req No. 3 Inputs ===============')
    print('UFO Sightings between', initial_time, 'and', end_time)
    print('')
    print('=============== Req No. 3 Answer ===============')
    print('There are', num_times, 'UFO sightings with different times [hh:mm:ss]...')
    print('The longest UFO sightings are:')
    print('+' + 10*'-' + '+' + 8*'-' + '+')
    print('|{:^9} |{:>7} |'.format('time', 'count'))
    print('+' + 10*'=' + '+' + 8*'=' + '+')
    print('|{:>9} |{:>7} |'.format(str(latest_time)[11:], num_events_latest_time))
    print('+' + 10*'-' + '+' + 8*'-' + '+')
    print('')
    print('There are', num_events_time_interval, 'sightings between:', initial_time, 'and', end_time)
    print('The first 3 and last 3 UFO sightings in this time are:')
    print('+' + 22*'-' + '+' + 50*'-' + '+' + 10*'-'+ '+' + 10*'-' + '+' + 11*'-' + '+' + 16*'-' + '+')
    print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format('datetime', 'city', 'state', 'country',
                                                                        'shape', 'duration (seg)'))
    print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in first_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')
    for event in last_events_list:
        datetime = event['datetime']
        city = event['city']
        state = event['state']
        country = event['country']
        shape = event['shape']
        duration = int(float(event['duration (seconds)']))
        print('| {:<21}| {:<49}| {:<9}| {:<9}| {:<10}|{:>15} |'.format(datetime, city, state, country,
                                                                                        shape, duration))
        print('+' + 22*'=' + '+' + 50*'=' + '+' + 10*'=' + '+' + 10*'=' + '+' + 11*'=' + '+' + 16*'=' + '+')

###############################################################################################################
# Menu principal
###############################################################################################################

catalog = None

def Menu():
    print('')
    print('Welcome')
    print('0- Load information')
    print('1- Requirement 1')
    print('2- Requirement 2')
    print('3- Requirement 3')
    print('4- Requirement 4')
    print('5- Requirement 5')
    print('6- Requirement 6')
    print('7- Finish program')
    option = int(input('Choose an option: '))
    return option

def UserProgram(test, option, catalog, input_1, input_2, input_3):
    if not test:
        option = Menu()
        while option != 7:
            if option == 0:
                print('Loading Information from UFOS/UFOS-utf8-small.csv ....')
                catalog = controller.initialization()
                controller.loadData(catalog)
                                                            
            elif option == 1:
                city = input('Enter a City: ')
                print('')
                print('Loading...')
                information = controller.Requirement1(catalog, city)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_cities = information[3]
                most_events_city = information[4]
                num_events_city = information[5]
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement1(city, first_events_list, last_events_list, 
                                                        num_cities, most_events_city, num_events_city)

            elif option == 2:
                initial_duration = int(input('Enter the first duration of the interval: '))
                end_duration = int(input('Enter the last duration of the interval: ')) 
                print('')
                print('Loading...')
                information = controller.Requirement2(catalog, initial_duration, end_duration)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_durations = information[3]
                longest_duration = information[4]
                num_events_longest_duration = information[5]
                num_events_duration_interval = information[6]
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement2(initial_duration, end_duration, first_events_list, last_events_list, 
                    num_durations, longest_duration, num_events_longest_duration, num_events_duration_interval)

            elif option == 3:
                initial_time = input('Enter the first time of the interval [hh:mm:ss]: ')
                end_time = input('Enter the last time of the interval [hh:mm:ss]: ')
                print('')
                print('Loading...')
                information = controller.Requirement3(catalog, initial_time, end_time)
                time_elapsed = information[0]
                first_events_list = information[1]
                last_events_list = information[2]
                num_times = information[3]
                latest_time = information[4]
                num_events_latest_time = information[5]
                num_events_time_interval = information[6]
                print('')
                print('The requirement took', time_elapsed, 'mseg to execute')
                print('')
                PrintRequirement3(initial_time, end_time, first_events_list, last_events_list, 
                                        num_times, latest_time, num_events_latest_time, num_events_time_interval)

            else:
                print('Please choose a valid option')
            
            option = Menu()
    
    else:
        if option == 0:
           catalog = controller.initialization()
           controller.loadData(catalog)
           return  catalog
        elif option == 1:
            return controller.Requirement1(catalog, input_1)[0]
        elif option == 2:
            return controller.Requirement2(catalog, input_1, input_2)[0]
        elif option == 3:
            return controller.Requirement3(catalog, input_1, input_2)[0]
           
    
UserProgram(False, 0, catalog, 0, 0, 0)