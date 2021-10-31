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
import DISClib.DataStructures.rbt as rbt
import DISClib.Algorithms.Trees.traversal as trv
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import datetime
assert cf
import DISClib.DataStructures.heap as hp

###############################################################################################################
# Construccion de modelos
###############################################################################################################

def initialization():
    catalog = { 'events_list': None,
                'date_posted_RBT': None,
                'cities_list': None,
                'cities_map': None}

    catalog['events_list'] = lt.newList('ARRAY_LIST')
    catalog['date_posted_RBT'] = om.newMap(omaptype='RBT', comparefunction=cmpKeysTree)
    catalog['cities_map'] = mp.newMap(1400, maptype='PROBING', loadfactor=0.5)
    catalog['cities_list'] = lt.newList('ARRAY_LIST')
    catalog['durations_map'] = mp.newMap(123, maptype='PROBING', loadfactor=0.5)
    catalog['durations_list'] = lt.newList('ARRAY_LIST')
    return catalog

###############################################################################################################
# Funciones para agregar informacion al catalogo
###############################################################################################################

def addEventList(catalog, event):
    lt.addLast(catalog['events_list'], event)

###############################################################################################################

def addDatePostedRBT(catalog, event):
    RBT_tree = catalog['date_posted_RBT']
    post_date_event = date_to_seconds(event['date posted'])
    post_date_entry = rbt.get(RBT_tree, post_date_event)

    if post_date_entry is None:
        post_date_list = newEntry(event)
    else:
        post_date_list = me.getValue(post_date_entry)
        lt.addLast(post_date_list, event)

    new_RBT_tree = rbt.put(RBT_tree, post_date_event, post_date_list)
    catalog['date_posted_RBT'] = new_RBT_tree

###############################################################################################################

def addCity(catalog, event):
    city = event['city']
    cities_map = catalog['cities_map']
    cities_list = catalog['cities_list']
    event_date = datetime.strptime(event['datetime'], "%Y-%m-%d %H:%M:%S")

    if mp.contains(cities_map, city):
        city_events_RBT = me.getValue(mp.get(cities_map, city))
        om.put(city_events_RBT, event_date, event)

    else:
        city_events_RBT = om.newMap(omaptype='RBT', comparefunction=cmpKeysTree)
        om.put(city_events_RBT, event_date, event)
        mp.put(cities_map, city, city_events_RBT)
        lt.addLast(cities_list, city)

###############################################################################################################

def addDuration(catalog, event):
    duration = int(event['duration (seconds)'])
    durations_map = catalog['durations_map']
    durations_list = catalog['durations_list']

    if mp.contains(durations_map, duration):
        duration_events_RBT = me.getValue(mp.get(durations_map, duration))
        rbt.put(duration_events_RBT, duration, event)
    else:
        duration_events_RBT = rbt.newMap(om.newMap(cmpKeysTree))
        rbt.put(duration_events_RBT, duration, event)
        mp.put(durations_map, duration, duration_events_RBT)
        lt.addLast(durations_list, duration)

###############################################################################################################
# Funciones para creacion de datos
###############################################################################################################

def newEntry(event):
    time_list = lt.newList('ARRAY_LIST')
    lt.addLast(time_list, event)
    return time_list

###############################################################################################################

def updateEntryList(entry_list, event):
    lt.addLast(entry_list, event)
    return entry_list

###############################################################################################################
# Funciones utilizadas para comparar elementos dentro de una lista
###############################################################################################################

def cmpKeysTree(key_Date_element_1, key_Date_element_2):

    return key_Date_element_1 > key_Date_element_2

###############################################################################################################

def cmpKeysHeap(event_1, event_2):
    event_date_1 = date_to_seconds(event_1['datetime'])
    event_date_2 = date_to_seconds(event_2['datetime'])

    return event_date_1 > event_date_2


###############################################################################################################
# Funciones de ordenamiento
###############################################################################################################

def date_to_seconds(date):
    date_information = date.split('-')
    date_information.append(date_information[2][2:].split(':'))
    date_information[2] = date_information[2][:2]

    sec = int(date_information[3][2])
    minutes_in_sec = int(date_information[3][1])*60
    hours_in_sec = int(date_information[3][0])*60*60
    days_in_sec = int(date_information[2])*60*60*24
    months_in_sec = int(date_information[1])*60*60*24*30
    years_in_sec = int(date_information[0])*60*60*24*30*12

    date_in_seconds = sec + minutes_in_sec + hours_in_sec + days_in_sec + months_in_sec + years_in_sec

    return date_in_seconds

###############################################################################################################

def catalog_information(catalog):
    tree_length = om.size(catalog['date_posted_RBT'])
    num_events = lt.size(catalog['events_list'])

    return tree_length, num_events

###############################################################################################################
# Funciones de consulta
###############################################################################################################

def Requirement1(catalog, city):
    cities_map = catalog['cities_map']
    cities_list = catalog['cities_list']
    
    first_events_list = lt.iterator(lt.newList())
    last_events_list = lt.iterator(lt.newList())
    num_cities = 0
    most_events_city = 'None'
    num_events_city = 0

    if mp.contains(cities_map, city):
        city_RBT = me.getValue(mp.get(cities_map, city))
        city_events_list = trv.inorder(city_RBT)
        num_events_city = lt.size(city_events_list)

        if num_events_city >= 3:
            first_events_list = lt.iterator(lt.subList(city_events_list, 0, 3))
            last_events_list = lt.iterator(lt.subList(city_events_list, num_events_city - 2, 3))
        else:
            first_events_list = lt.iterator(city_events_list)
            last_events_list = first_events_list

        num_cities = lt.size(cities_list)
        major_city_num = 0
        
        for particular_city in lt.iterator(cities_list):
            num_events_particular_city = rbt.size(me.getValue(mp.get(cities_map, particular_city)))
            if num_events_particular_city > major_city_num:
                major_city_num = num_events_particular_city
                most_events_city = particular_city
    
    return first_events_list,  last_events_list, num_cities, most_events_city, num_events_city

###############################################################################################################

def Requirement2(catalog, initial_duration, end_duration):
    durations_map = catalog['durations_map']
    durations_list = catalog['durations_list']
    num_durations = lt.size(durations_list)

    first_events_list = lt.iterator(lt.newList())
    last_events_list = lt.iterator(lt.newList())
    most_duration = 0
    num_events_most_duration = 0
    num_events_duration_interval = 0

    index = 1
    last_duration = 0
    duration_events_list = lt.newList('ARRAY_LIST')
    while index <= num_durations and last_duration != end_duration:
        duration = lt.getElement(durations_list, index)
        duration_events_RBT = me.getValue(mp.get(durations_map, duration))
        num_events_individual_duration_interval = rbt.size(duration_events_RBT)

        if initial_duration <= duration and duration <= end_duration:
            individual_duration_events_list = trv.inorder(duration_events_RBT)
            num_events_duration_interval += num_events_individual_duration_interval

            for event in lt.iterator(individual_duration_events_list):
                lt.addLast(duration_events_list, event)

        if num_events_individual_duration_interval > num_events_most_duration:
            num_events_most_duration = num_events_individual_duration_interval
            most_duration = duration          

        index += 1
        last_duration == duration
            
    if num_events_duration_interval >= 3:
            first_events_list = lt.iterator(lt.subList(duration_events_list, 0, 3))
            last_events_list = lt.iterator(lt.subList(duration_events_list, num_events_duration_interval - 2, 3))
    else:
        first_events_list = lt.iterator(duration_events_list)
        last_events_list = first_events_list

    return  first_events_list, last_events_list, num_durations, most_duration, num_events_most_duration, num_events_duration_interval