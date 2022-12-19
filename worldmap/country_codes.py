from pygal.maps.world import COUNTRIES

additional_name = {
    "Russia": "ru",
    "US": "us",
    "Bolivia": "bo",
    "Brunei": "bn", 
    "Czechia": "cz",
    "Iran": "ir",
    "Korea, South": "kr",
    "Laos": "la",
    "Libya":  "ly",
    "Moldova": "md",
    "North Macedonia": "mk",
    "Qatar": "gq",
    "South Sudan": "sd",
    "Syria": 'sy',
    "Taiwan": "tw",
    "Venezuela": "ve",
    "Vietnam": "vn"
}

def get_country_code(country_name):
    return_code = None
    
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    
    return additional_name[country_name] if country_name in additional_name else None
