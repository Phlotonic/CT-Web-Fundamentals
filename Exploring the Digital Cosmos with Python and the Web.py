# Task 2: Fetch Data from a Space API

import requests

def fetch_planet_data():
    # Define the API endpoint
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    # Make a GET request to the API
    response = requests.get(url)
    
    # Parse the JSON response
    planets = response.json()['bodies']

    # Process each planet's information
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']  # Get planet's English name
            mass = planet['mass']['massValue']  # Get planet's mass
            orbit_period = planet['sideralOrbit']  # Get planet's orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

# Task 3: Data Presentation and Analysis

def fetch_planet_data():
    # Define the API endpoint
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    # Make a GET request to the API
    response = requests.get(url)
    
    # Parse the JSON response
    planets = response.json()['bodies']

    # Extract relevant planet information
    planet_data = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']  # Get planet's English name
            mass = planet['mass']['massValue']  # Get planet's mass
            orbit_period = planet['sideralOrbit']  # Get planet's orbit period
            planet_data.append((name, mass, orbit_period))
    
    return planet_data

def find_heaviest_planet(planets):
    # Find the planet with the maximum mass
    heaviest_planet = max(planets, key=lambda x: x[1])
    return heaviest_planet

# Fetch planet data
planets = fetch_planet_data()

# Find the heaviest planet
name, mass, _ = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")

