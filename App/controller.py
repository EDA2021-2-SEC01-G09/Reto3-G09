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
 """

import config as cf
import model
import time
import csv


###############################################################################################################
# Inicialización del Catálogo de Avistamiento
###############################################################################################################

def initialization():
    return model.initialization()

###############################################################################################################
# Funciones para la carga de datos
###############################################################################################################

def loadData(catalog):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    sightings_data = cf.data_dir + 'UFOS/UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(sightings_data, encoding="utf-8"), delimiter=",")

    for event in input_file:
        model.addEventList(catalog, event)
        model.addDatePostedRBT(catalog, event)
        model.addCity(catalog, event)
    return catalog

###############################################################################################################
# Funciones de consulta sobre el catálogo
###############################################################################################################

def catalog_information(catalog):
    return model.catalog_information(catalog)

###############################################################################################################
# Funciones de ordenamiento
###############################################################################################################

def Requirement1(catalog, city):
    start_time = time.process_time()

    information = model.Requirement1(catalog, city)

    first_events_list = information[0]
    last_events_list = information[1]
    num_cities = information[2]
    most_events_city = information[3]
    num_events_city = information[4]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 

    return elapsed_time, first_events_list, last_events_list, num_cities, most_events_city, num_events_city

###############################################################################################################

def Requirement2(catalog, initial_duration, end_duration):
    start_time = time.process_time()

    information = model.Requirement2(catalog, initial_duration, end_duration)

    first_events_list = information[0]
    last_events_list = information[1]
    num_durations = information[2]
    most_duration = information[3]
    num_events_most_duration = information[4]
    num_events_duration_interval = information[5]

    stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000 

    return elapsed_time, first_events_list, last_events_list, num_durations, most_duration, num_events_most_duration, num_events_duration_interval