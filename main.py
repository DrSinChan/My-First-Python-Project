print("Hello World, Python is working.")
while True:
    name= input("Enter your name: ")
    while True:
        try:
            age = int(input("Enter your age (in years): "))
            if age <= 0:
                print("Invalid age entered. Enter valid age in years.")
                continue
            break
        except ValueError:
            print("Invalid age entered. Enter valid age in years.")

    while True:
        gender = input("Enter your gender (m/f/o) : ").strip().lower()
        if gender=="m":
            pronoun="his"
            break
        elif gender=="f":
            pronoun="her"
            break
        elif gender=="o":
            pronoun="his/her"
            break
        else:
            print("Invalid gender entered. Please enter m, f or o.")

    if  age==1:
        stage= "Infant"
    elif 2 <= age <= 3:
        stage = "Toddler"
    elif 4<= age <= 12:
        stage = "Child"
    elif 13<= age <= 19:
        stage= "Teenager"
    elif 20<= age <= 60:
        stage="Adult"
    elif age >= 60:
        stage= "Senior Citizen"
    else:
        print("An error occured. Could be an invalid age.")

    if stage[0].lower() in "aeiou":
        article = "an"
    else:
        article="a"

    print(name, "is", article, stage, "and", pronoun, "age is", age, "years.")

    choice=input("\nDo you want to enter another record (y/n): ").strip().lower()
    if choice !="y":
        break
