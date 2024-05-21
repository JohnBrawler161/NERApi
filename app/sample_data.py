one_shot = "I want to buy a 2 story house for 700k that is cool with large dogs. I also want a garage, pool and central AC. I want around 1400 sq ft of floor space, that is on the water, with a mountain view, built in 2010 or newer."
second_shot = "I'm in search of a charming single-story, waterfront home nestled in the city of Melborne Beach, FL. My budget range is $350k to $450k. I'm looking for between 1000 and 1200 sq ft of floor space, with at least 3 bedrooms and 2 bathrooms. A central heating system is a must, with a garage and parking for two cars. A small garden in the yard, with solar panels installed on the roof would be ideal. I'm not a smoker, so a non-smoking environment is preferred. Ideally, the lot size would be under 0.25 acres, with a view of the city. I'm looking for a home built after 2000, and HOA fees under $150."

prompts = [
    [one_shot, [
        {'E': 'INTENT', 'W': 'buy'}, {'E': 'TWO STORY', 'W': 'true'}, {'E': 'BUDGET', 'W': '$700,000'},
        {'E': 'PETS', 'W': 'large dog'}, {'E': 'GARAGE', 'W': 'true'}, {'E': 'POOL', 'W': 'true'},
        {'E': 'AC', 'W': 'true'}, {'E': 'FLOOR SPACE', 'W': '1400'}, {'E': 'WATERFRONT', 'W': 'true'},
        {'E': 'VIEW', 'W': 'mountains'}, {'E': 'YEAR BUILT', 'W': '2010'}
    ]],
    [second_shot, [
        {"E": "State", "T": "Enum", "W": "US States"},
        {"E": "City", "T": "Enum", "W": "US Cities"},
        {"E": "Home Type", "T": "Enum", "W": "House, Condo, Multi-family, Apartment, Land"},
        {"E": "Budget Min", "T": "Integer", "W": "Any # ≥ 50,000"},
        {"E": "Budget Max", "T": "Integer", "W": "Any # ≥ 50,000"},
        {"E": "Floor Space", "T": "Min", "W": "Integer	Any # ≥ 500"},
        {"E": "Floor Space", "T": "Max", "W": "Integer	Any # > 1000"},
        {"E": "Bed Min", "T": "Enum", "W": "1-4"},
        {"E": "Bed Max", "T": "Enum", "W": "1-10"},
        {"E": "Bath", "T": "Integer", "W": "Any # > 0"},
        {"E": "AC", "T": "Boolean", "W": "T / F"},
        {"E": "Garage", "T": "Boolean", "W": "T / F"},
        {"E": "Pool	Boolean", "T": "T", "W": "T / F"},
        {"E": "Parking Min", "T": "Enum", "W": "1-4"},
        {"E": "Parking Max", "T": "Enum", "W": "1-6"},
        {"E": "Pets", "T": "Enum", "W": "Cat, Large Dog, Small Dog"},
        {"E": "Smoker", "T": "Boolean", "W": "T / F"},
        {"E": "Lot Size", "T": "Integer", "W": "1000-4356000 sq ft"},
        {"E": "View", "T": "Enum", "W": "Mountain, Water, City, Park"},
        {"E": "Year built", "T": "Integer", "W": "1920-2024"},
        {"E": "Two story", "T": "Boolean", "W": "T / F"},
        {"E": "HOA Min", "T": "Enum", "W": "500-1000"},
        {"E": "HOA Max", "T": "Integer", "W": "Any # > 50"},
        {"E": "Waterfront", "T": "Boolean", "W": "T / F"},
        {"E": "Foreclosure", "T": "Boolean", "W": "T / F"},
        {"E": "Other Requests", "T": "String",
         "W": "Any words related to extra real estate (housing/commercial) requests"},
    ]]
]
