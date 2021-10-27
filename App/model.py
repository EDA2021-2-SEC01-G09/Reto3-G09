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
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initialization():
    catalog = {'events': None,
                'dateIndex': None
                }

    catalog['events'] = lt.newList('SINGLE_LINKED')
    catalog['dateIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDatesTree)
    return catalog

# Funciones para agregar informacion al catalogo

def addEvent(catalog, event):
    lt.addLast(catalog['events'], event)
    catalog['dateIndex'] = updateDateIndex(catalog['dateIndex'], event)
    return catalog

def updateDateIndex(rbt_tree, event):
    event_date = date_to_days(event['date posted'])
    entry = rbt.get(rbt_tree, event_date)
    if entry is None:
        date_entry = newDataEntry(event)
    else:
        date_entry = updateDataEntry(me.getValue(entry), event)
    tree = rbt.put(rbt_tree, event_date, date_entry)
    return tree

def newDataEntry(event):
    entry = lt.newList('SINGLE_LINKED', compareDatesList)
    lt.addLast(entry, event)
    return entry

def updateDataEntry(date_entry, event):
    lt.addLast(date_entry, event)
    return date_entry

# Funciones para creacion de datos

# Funciones de consulta

def date_to_days(date):
    date_information = date.split('-')
    date_information[2] = date_information[2][:2]
    if len(date_information) != 1:
        date_in_days = int(date_information[0])*365 + int(date_information[1])*30 + int(date_information[2])
    else:
        date_in_days = 0
    return date_in_days

def catalog_information(catalog):
    tree_length = om.size(catalog['dateIndex'])
    num_events = lt.size(catalog['events'])

    return tree_length, num_events

# Funciones utilizadas para comparar elementos dentro de una lista

def compareDatesList(element_1, element_2):
    date_element_1 = date_to_days(element_1['date posted'])
    date_element_2 = date_to_days(element_2['date posted'])
    return date_element_1 > date_element_2

def compareDatesTree(key_element_1, key_element_2):
    return key_element_1 > key_element_2

# Funciones de ordenamiento