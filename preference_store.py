memory = {}

def save_preferences_for_user(name, preferences):
    memory[name] = preferences

def get_preferences(name):
    return memory.get(name)
