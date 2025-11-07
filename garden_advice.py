# Dedicated data structures for advice (From Issue #1, now inside the function context for modularity)
SEASONAL_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

def get_gardening_advice(season: str, plant_type: str) -> str:
    """
    Generates tailored gardening advice based on the current season and plant type.

    This function looks up predefined advice from dictionaries for two categories 
    and returns a combined message.

    Args:
        season: The current time of year (e.g., "summer", "winter").
        plant_type: The type of plant the user has (e.g., "flower", "vegetable").

    Returns:
        A string containing a two-part gardening advice message.
    """
    
    advice = ""
    
    # Determine advice based on the season
    # .get() provides a default message if the key (season) is not found
    advice += SEASONAL_ADVICE.get(season.lower(), "No advice for this season.") + "\n"

    # Determine advice based on the plant type
    advice += PLANT_ADVICE.get(plant_type.lower(), "No advice for this type of plant.")
    
    return advice

# --- Main Program Execution ---

# Input values (still hardcoded, as per the original TODO)
current_season = "summer"  
current_plant_type = "flower"  

# Generate and print the advice using the new function
final_advice = get_gardening_advice(current_season, current_plant_type)
print(final_advice)

# TODO: The remaining original TODOs can be addressed in future issues:
# - Add detailed comments explaining each block of code.
# - Store advice in a dictionary for multiple plants and seasons. (Largely done in Issue #1)
# - Recommend plants based on the entered season.