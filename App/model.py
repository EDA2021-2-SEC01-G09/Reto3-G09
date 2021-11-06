"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """
import DISClib.Algorithms.Trees.traversal as trv
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import bst as bst
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import datetime
assert cf
import DISClib.DataStructures.heap as hp

###############################################################################################################
# Construccion de modelos
###############################################################################################################

def initialization():
    catalog = { 'cities_list': None,
                'cities_map': None,
                'durations_map': None,
                'durations_BST': None}

    catalog['cities_map'] = mp.newMap(1400, maptype='PROBING', loadfactor=0.5)
    catalog['cities_list'] = lt.newList('ARRAY_LIST')
    catalog['durations_map'] = mp.newMap(123, maptype='PROBING', loadfactor=0.5)
    catalog['durations_BST'] = bst.newMap(cmpFunction1)
    return catalog

###############################################################################################################
# Funciones para agregar informacion al catalogo
###############################################################################################################

def addCity(catalog, event):
    city = event['city']
    cities_map = catalog['cities_map']
    cities_list = catalog['cities_list']
    event_date = datetime.strptime(event['datetime'], "%Y-%m-%d %H:%M:%S")

    if mp.contains(cities_map, city):
        city_events_BST = me.getValue(mp.get(cities_map, city))
        bst.put(city_events_BST, event_date, event)

    else:
        city_events_BST = bst.newMap(cmpFunction1)
        bst.put(city_events_BST, event_date, event)
        mp.put(cities_map, city, city_events_BST)
        lt.addLast(cities_list, city)

###############################################################################################################

def addDuration(catalog, event):
    city = event['city']
    country = event['country']
    country_city = city + country
    duration = event['duration (seconds)']
    durations_map = catalog['durations_map']
    durations_BST = catalog['durations_BST']

    if mp.contains(durations_map, duration):
        duration_events_BST = me.getValue(mp.get(durations_map, duration))
        bst.put(duration_events_BST, country_city, event)
    else:
        duration_events_BST = bst.newMap(cmpFunction2)
        bst.put(duration_events_BST, country_city, event)
        mp.put(durations_map, duration, duration_events_BST)
        bst.put(durations_BST, float(duration), float(duration))

###############################################################################################################
# Funciones para creacion de datos
###############################################################################################################

def getFirstandLastElements(lst, num_positions, comparition):
    num_elements_list = lt.size(lst)

    if num_elements_list >= num_positions:
        if comparition == '>':
            first_events_list = lt.iterator(lt.subList(lst, 1, num_positions))
            last_events_list = lt.iterator(lt.subList(lst, num_elements_list - (num_positions - 1), num_positions))
        else:
            last_events_list = lt.iterator(lt.subList(lst, 1, num_positions))
            first_events_list = lt.iterator(lt.subList(lst, num_elements_list - (num_positions - 1), num_positions))
    else:
        first_events_list = lt.iterator(lst)
        last_events_list = first_events_list

    return first_events_list, last_events_list, num_elements_list

###############################################################################################################

def getMostElement(lst, map_list, comparition):
    num_elements_list = lt.size(lst)

    if comparition == '>':
        most_element = lt.getElement(lst, num_elements_list)
    else:
        most_element = lt.getElement(lst, 1)

    most_element_value = me.getValue(mp.get(map_list, str(most_element)))

    return most_element, most_element_value, num_elements_list


###############################################################################################################
# Funciones utilizadas para comparar elementos dentro de una lista
###############################################################################################################

def cmpFunction1(key_node_1, key_node_2):
    if key_node_1 > key_node_2:
        return 1
    elif key_node_1 < key_node_2:
        return -1
    else:
        return 0

def cmpFunction2(key_node_1, key_node_2):
    if key_node_1 > key_node_2:
        return 1
    elif key_node_1 < key_node_2:
        return -1
    else:
        return 1

###############################################################################################################
# Funciones de consulta
###############################################################################################################

def Requirement1(catalog, city):
    cities_map = catalog['cities_map']
    cities_list = catalog['cities_list']
    num_cities = lt.size(cities_list)

    if mp.contains(cities_map, city):
        city_events_list = trv.inorder(me.getValue(mp.get(cities_map, city)))
        city_events_info = getFirstandLastElements(city_events_list, 3, '>')
        first_events_list = city_events_info[0]
        last_events_list = city_events_info[1]
        num_events_city = city_events_info[2]

        num_events_most_city = -1
        for city in lt.iterator(cities_list):
            num_events_particular_city = bst.size(me.getValue(mp.get(cities_map, city)))
            if num_events_particular_city > num_events_most_city:
                num_events_most_city = num_events_particular_city
                most_events_city = city
    else:
        first_events_list = lt.iterator(lt.newList())
        last_events_list = first_events_list
        most_events_city = 'None'
        num_events_city = 0

    return first_events_list, last_events_list, num_cities, most_events_city, num_events_city

###############################################################################################################

def Requirement2(catalog, initial_duration, end_duration):
    durations_map = catalog['durations_map']
    durations_BST = catalog['durations_BST']
    durations_list = trv.inorder(durations_BST)

    longest_duration_info = getMostElement(durations_list, durations_map, '>')
    longest_duration = longest_duration_info[0]
    num_events_longest_duration = bst.size(longest_duration_info[1])
    num_durations = longest_duration_info[2]

    index = 1
    previous_duration = -1
    duration_interval_events_list = lt.newList('ARRAY_LIST')
    while index <= num_durations and previous_duration <= end_duration:
        duration = lt.getElement(durations_list, index)

        if initial_duration <= duration and duration <= end_duration:
            duration_events_list = trv.inorder(me.getValue(mp.get(durations_map, str(duration))))
            for event in lt.iterator(duration_events_list):
                lt.addLast(duration_interval_events_list, event)
        index += 1
        previous_duration == duration
            
    duration_interval_events_info = getFirstandLastElements(duration_interval_events_list, 3, '>')
    first_events_list = duration_interval_events_info[0]
    last_events_list = duration_interval_events_info[1]
    num_events_duration_interval = duration_interval_events_info[2]

    return first_events_list, last_events_list, num_durations, longest_duration, num_events_longest_duration, num_events_duration_interval