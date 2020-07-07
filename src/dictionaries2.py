persons = {"Allison": 18, "Paul": 28, "Erik": 20, "Grace": 25}

print(persons)

persons["Stuart"] = 98

print(persons)

# key must be initialized = "

if "Benson" not in persons:
    persons["Benson"] = 48

print(persons)

# when we add entries in dictionary, order is not maintained

# order is random

# why is dict so important data structure

# dictionary lookup is very fast

if "Paul2" in persons.keys():  # Membership
    print("Paul's age=", persons["Paul"])

