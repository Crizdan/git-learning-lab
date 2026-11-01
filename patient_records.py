def register_patient(name,age):
    if age <= 0:
        raise ValueError("Age must be positive")
    return {
        "name": name,
        "age": age
    }
