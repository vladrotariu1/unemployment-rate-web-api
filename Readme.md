# Unemployment rate in Romania API

This API provides different statistics related to the unemployment rate in Romaina

## Endpoints
- /history/
- /history/age/
- /history/sex/



## History endpoint

It is used to get the number of unemployed people in a time interval

### URL query parameters

- county-id (from 1 to 42)
- from-month (from 1 to 12)
- from-year
- to-month (from 1 to 12)
- to-year

### URL example:

http://localhost:8000/history/?county-id=42&from-month=5&from-year=2020&to-month=8&to-year=2020


## History by age endpoint

It is used to get the number of unemployed people from a chosen month  by age

### URL query parameters

- county-id (from 1 to 42)
- month (from 1 to 12)
- year

### URL example:

http://localhost:8000/history/age/?county-id=42&month=5&year=2020


## History by sex endpoint

It is used to get the number of unemployed people from a chosen month by sex

### URL query parameters

- county-id (from 1 to 42)
- month (from 1 to 12)
- year

### URL example:

http://localhost:8000/history/sex/?county-id=42&month=5&year=2020