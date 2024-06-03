def take_info():
    name = input("What is your name : ")
    age = int(input("What is your age : "))
    languages = input(
        "Which programming languages do you know write comma separated : "
    ).split(",")

    return {"name": name, "age": age, "languages": languages}


for key, item in take_info().items():
    print(f"{key} : {item}")
