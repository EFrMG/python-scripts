def add_setting(user_settings, new_entry):
    key, value = new_entry

    key = str(key).lower()
    value = str(value).lower()

    if key in user_settings:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )
    else:
        user_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(user_settings, update_entry):
    key, value = update_entry

    key = str(key).lower()
    value = str(value).lower()

    if key in user_settings:
        user_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(user_settings, key_to_delete):
    key_to_delete = str(key_to_delete).lower()

    if key_to_delete in user_settings:
        del user_settings[key_to_delete]
        return f"Setting '{key_to_delete}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(user_settings):
    if not user_settings and isinstance(user_settings, dict):
        return "No settings available."

    total_settings = "Current User Settings:\n"

    for key, value in user_settings.items():
        total_settings += f"{key.capitalize()}: {value}\n"

    return total_settings


test_settings = {
    "Theme": "gray",
    "please": "something else",
    "this": "is just a test",
}

print(view_settings(test_settings))
