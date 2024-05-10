# Create a new dictionary with no None values.
# This code has O(n) because we iterate through the dictionary only once.

user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    if user_pref == None:
        return None
    updated_user_pref = {}
    for key, value in user_pref.items():
        if user_pref[key] != None:
            updated_user_pref[key] = value
    return updated_user_pref

print(update_preferences(user_preferences))
