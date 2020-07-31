def greet(first_name, last_name):
    print(f"hi {first_name}{last_name}")
    print("welcome aboard")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
file = open("contect.txt", "w")
file.write(message)


