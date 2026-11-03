#this helps to register patient
def register_patient(name,age):
    if age <= 0: #this validates patient age 
        raise ValueError("Age must be positive")
    return {
        "name": name,
        "age": age
    }
