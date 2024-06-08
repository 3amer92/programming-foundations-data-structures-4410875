user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    user_pref_2 = {}
    for key, value in user_pref.items():
        if user_pref[key] != None:
            user_pref_2[key] = value
    return user_pref_2


print(update_preferences(user_preferences))
