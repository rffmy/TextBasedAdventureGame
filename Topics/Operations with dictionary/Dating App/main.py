def select_dates(potential_dates):
    selected = []
    cutoff_age = 30
    for person in potential_dates:
        if person["age"] > cutoff_age and person["city"] == "Berlin" and "art" in person["hobbies"]:
            selected.append(person["name"])

    return ", ".join(selected)

