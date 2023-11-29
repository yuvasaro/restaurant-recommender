"""Constants used in loading the data and in the recommender system."""

USER_FEATURES = [
    "userID", 
    # "latitude", 
    # "longitude", 
    "smoker", 
    "drink_level", 
    "dress_preference", 
    "ambience", 
    "transport", 
    "marital_status", 
    "hijos", 
    # "birth_year", 
    "interest", 
    "personality", 
    # "religion", 
    "activity", 
    # "weight", 
    "budget", 
    # "height"
]

RESTAURANT_FEATURES = [
    "placeID", 
    # "latitude", 
    # "longitude", 
    "alcohol", 
    "smoking_area", 
    "dress_code", 
    "accessibility", 
    "price", 
    "Rambience", 
    # "franchise", 
    "area", 
    "other_services"
]

USER_FEATURE_OPTIONS = {
    "smoker": ["?", "false", "true"],
    "drink_level": ["?", "abstemious", "social drinker", "casual drinker"],
    "dress_preference": ["?", "informal", "formal", "no preference", "elegant"],
    "ambience": ["?", "family", "friends", "solitary"],
    "transport": ["?", "on foot", "public", "car owner"],
    "marital_status": ["?", "single", "married", "widow"],
    "hijos": ["?", "independent", "kids", "dependent"],
    "interest": ["?", "variety", "technology", "none", "retro", "eco-friendly"],
    "personality": ["?", "thrifty-protector", "hunter-ostentatious", "hard-worker", "conformist"],
    "religion": ["?", "none", "Catholic", "Christian", "Mormon", "Jewish"],
    "activity": ["?", "student", "professional", "unemployed", "working-class"],
    "budget": ["?", "medium", "low", "high"]
}

USER_CUISINES = [
    'Afghan', 'African', 'American', 'Armenian', 'Asian', 'Australian', 'Austrian', 'Bagels', 'Bakery', 'Bar', 'Bar_Pub_Brewery', 
    'Barbecue', 'Basque', 'Brazilian', 'Breakfast-Brunch', 'British', 'Burgers', 'Burmese', 'Cafe-Coffee_Shop', 'Cafeteria', 
    'Cajun-Creole', 'California', 'Cambodian', 'Canadian', 'Caribbean', 'Chilean', 'Chinese', 'Contemporary', 'Continental-European', 
    'Cuban', 'Deli-Sandwiches', 'Dessert-Ice_Cream', 'Dim_Sum', 'Diner', 'Doughnuts', 'Dutch-Belgian', 'Eastern_European', 'Eclectic', 
    'Ethiopian', 'Family', 'Fast_Food', 'Filipino', 'Fine_Dining', 'French', 'Fusion', 'Game', 'German', 'Greek', 'Hawaiian', 
    'Hot_Dogs', 'Hungarian', 'Indian-Pakistani', 'Indigenous', 'Indonesian', 'International', 'Irish', 'Israeli', 'Italian', 'Jamaican', 
    'Japanese', 'Juice', 'Korean', 'Kosher', 'Latin_American', 'Lebanese', 'Malaysian', 'Mediterranean', 'Mexican', 'Middle_Eastern', 
    'Mongolian', 'Moroccan', 'North_African', 'Organic-Healthy', 'Pacific_Northwest', 'Pacific_Rim', 'Persian', 'Peruvian', 'Pizzeria', 
    'Polish', 'Polynesian', 'Portuguese', 'Regional', 'Romanian', 'Russian-Ukrainian', 'Scandinavian', 'Seafood', 'Soup', 'Southeast_Asian', 
    'Southern', 'Southwestern', 'Spanish', 'Steaks', 'Sushi', 'Swiss', 'Tapas', 'Tea_House', 'Tex-Mex', 'Thai', 'Tibetan', 'Tunisian', 
    'Turkish', 'Vegetarian', 'Vietnamese'
]

RESTAURANT_FEATURE_OPTIONS = {
    "alcohol": ["?", "No_Alcohol_Served", "Wine-Beer", "Full_Bar"],
    "smoking_area": ["?", "none", "only at bar", "permitted", "section", "not permitted"],
    "dress_code": ["?", "informal", "casual", "formal"],
    "accessibility": ["?", "no_accessibility", "completely", "partially"],
    "price": ["?", "medium", "low", "high"],
    "Rambience": ["?", "familiar", "quiet"],
    "franchise": ["?", "t", "f"],
    "area": ["?", "open", "closed"],
    "other_services": ["?", "none", "Internet", "variety"]
}

RESTAURANT_CUISINES = [
    'Afghan', 'African', 'American', 'Armenian', 'Asian', 'Bagels', 'Bakery', 'Bar', 'Bar_Pub_Brewery', 'Barbecue', 'Brazilian', 
    'Breakfast-Brunch', 'Burgers', 'Cafe-Coffee_Shop', 'Cafeteria', 'California', 'Caribbean', 'Chinese', 'Contemporary', 
    'Continental-European', 'Deli-Sandwiches', 'Dessert-Ice_Cream', 'Diner', 'Dutch-Belgian', 'Eastern_European', 'Ethiopian', 
    'Family', 'Fast_Food', 'Fine_Dining', 'French', 'Game', 'German', 'Greek', 'Hot_Dogs', 'International', 'Italian', 'Japanese', 
    'Juice', 'Korean', 'Latin_American', 'Mediterranean', 'Mexican', 'Mongolian', 'Organic-Healthy', 'Persian', 'Pizzeria', 'Polish', 
    'Regional', 'Seafood', 'Soup', 'Southern', 'Southwestern', 'Spanish', 'Steaks', 'Sushi', 'Thai', 'Turkish', 'Vegetarian', 'Vietnamese'
]
