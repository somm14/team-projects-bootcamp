
# Query para ver el informe del crimen
query1 = '''
SELECT *
FROM crime_scene_report
WHERE ("date" LIKE 20180115) AND (type = "murder") AND (city LIKE "SQL City");
'''

# Query para saber quién es la testigo_1
query2 = '''
SELECT a.name, a.address_street_name, a.address_number, b.transcript
FROM person AS a
LEFT JOIN interview AS b
ON a.id = b.person_id
WHERE (address_street_name LIKE "%Northwestern Dr%")
'''

# Query del testigo_2

query3 = '''
SELECT a.name, a.address_street_name, a.address_number, b.transcript
FROM person AS a
LEFT JOIN interview AS b
ON a.id = b.person_id
WHERE (address_street_name LIKE "%Franklin Ave%") AND (a.name LIKE "%Annabel%")
'''

# Query filtrando por las pistas_3

query4 = '''
SELECT * 
FROM "get_fit_now_member"
WHERE (membership_status = "gold") AND (id LIKE "%48%")
'''

# Query para saber quien tiene la matricula
query5 = '''
SELECT a.name, b.plate_number
FROM person AS a
LEFT JOIN drivers_license AS b
ON a.license_id = b.id
WHERE (a.id = 28819) OR (a.id = 67318)
AND b.plate_number LIKE "%H42W%"
'''

# Query para ver el testimonio del asesino
query6 = '''
SELECT a.name, b.transcript
FROM person AS a
LEFT JOIN interview AS b
ON a.id = b.person_id
WHERE a.id = 67318
'''

# Query para buscar a la mujer que contrató al asesino
# Buscamos por sus características.
query7 = ''' 
SELECT *
FROM drivers_license
WHERE hair_color = "red"
AND gender = "female"
AND (height > 65 AND height < 67)
AND hair_color = "red"
AND car_model LIKE "%Model%"
'''
# Filtramos por ID para buscar su nombre
query8 = '''
SELECT a.id, a.name
FROM person AS a
LEFT JOIN drivers_license AS b
ON a.license_id = b.id
WHERE license_id = 202298 OR license_id = 291182
'''
#Filtramos por nombre en los eventos de facebook
query9 = '''
SELECT a.*, b.name
FROM facebook_event_checkin AS a
LEFT JOIN person AS b
ON a.person_id = b.id
WHERE a.person_id = 90700 OR a.person_id = 99716
'''