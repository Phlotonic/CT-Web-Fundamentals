# Task 2: Fetching Data from the Pokémon API

# Import the requests library to make HTTP requests
import requests

# Define the URL for the Pokémon API
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the name and abilities of the Pokémon
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    
    # Print the name and abilities
    print(f"Name: {name}")
    print("Abilities:", abilities)
else:
    print("Failed to retrieve data")

# Task 3: Analyzing and Displaying Data

# Function to fetch Pokémon data
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}")
        return None

# Function to calculate the average weight of a list of Pokémon
def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

# List of Pokémon names to fetch data for
pokemon_names = ["pikachu", "bulbasaur", "charmander"]

# Fetch data for each Pokémon and store it in a list
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

# Filter out any None values in case of failed requests
pokemon_data = [pokemon for pokemon in pokemon_data if pokemon is not None]

# Calculate the average weight of the Pokémon
average_weight = calculate_average_weight(pokemon_data)

# Print the names, abilities, and average weight of the Pokémon
for pokemon in pokemon_data:
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Name: {name}")
    print("Abilities:", abilities)
print(f"Average Weight: {average_weight}")
