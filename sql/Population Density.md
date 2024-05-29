You are working on a data analysis project at Deloitte where you need to analyze a dataset containing information
about various cities. Your task is to calculate the population density of these cities, rounded to the nearest integer, and identify the cities with the minimum and maximum densities.

The population density should be calculated as (Population / Area).


The output should contain 'city', 'country', 'density'.

cities_population

city:
varchar

country:
varchar

population:
int

area:
float



```sql

WITH density AS (
    SELECT 
        city, 
        country, 
        ROUND(population / NULLIF(area, 0)) AS density
    FROM 
        cities_population
    WHERE 
        area > 0
),

max_density AS (
    SELECT 
        city, 
        country, 
        density
    FROM 
        density
    WHERE 
        density = (SELECT MAX(density) FROM density)
),

min_density AS (
    SELECT 
        city, 
        country, 
        density
    FROM 
        density
    WHERE 
        density = (SELECT MIN(density) FROM density)
),

combined_density AS (
    SELECT * FROM max_density
    UNION ALL
    SELECT * FROM min_density
)

SELECT 
    city, 
    country, 
    density
FROM 
    combined_density
ORDER BY 
    density ASC;
    
```