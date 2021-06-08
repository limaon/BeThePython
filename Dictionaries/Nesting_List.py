#Nesting
capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
}


# Nesting a List in a Dictionary

travel_log = {
    "Frace": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburgo", "Stuttgart"], "total_visits": 5} ,
}

# Nesting Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    }, 
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburgo", "Stuttgart"],
        "total_visits": 5
    }
]
