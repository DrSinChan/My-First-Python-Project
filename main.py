print("Hello World, Python is working.")
while True:
    name= input("Enter name: ").strip().upper()

    while True:        
        age_input = input(f"Enter age of {name} (in whole years): ").strip()
        if "/" in age_input:
            print(f"{age_input} is a fraction. Please enter valid age of {name} only as number in whole years (no fractions).")
            continue
        try:
            age_float=float(age_input)

            if not age_float.is_integer():
                print(f"{age_input} is a decimal number. Please enter valid age of {name} only as number in whole years (no decimals).")
                continue

            else:
                age = int(age_float)
                if age == 0:
                    print(f"Age cannot be {age_input}. Please enter valid age of {name} only as positive number in whole years .")
                    continue
                if age < 0:
                    print(f"{age} is a negative number. Please enter valid age of {name} only as positive number in whole years.")
                    continue                
                else:
                    break
        
        except ValueError:
            print(f"{age_input} is an invalid text. Please enter valid age of {name} only as number in whole years.")
            continue

    gender_map={
        "m":"his",
        "male":"his",
        
        "f": "her",
        "female":"her",

        "o":"his/her",
        "other":"his/her",
        "others":"his/her"
    }

    while True:
        gender = input(f"Enter gender of {name} : ").strip().lower()    
        if gender in gender_map:
            pronoun=gender_map[gender]
            break
        else:
            print("Invalid gender entered. Please enter 'male / female / other' or related shortforms")

    if  age==1:
        stage= "Infant"
    elif age <= 3:
        stage = "Toddler"
    elif age <= 12:
        stage = "Child"
    elif age <= 19:
        stage= "Teenager"
    elif age <= 60:
        stage="Adult"
    elif age >= 60:
        stage= "Senior Citizen"
    else:
        print("An error occured. Could be an invalid age.")
        continue

    if stage[0].lower() in "aeiou":
        article = "an"
    else:
        article="a"

    if age==1:
        year="year."
    else:
        year="years."

    print(f"{name} is {article} {stage} and {pronoun} age is {age} {year}")

    choice=input("\nDo you want to enter another record (y/n): ").strip().lower()
    if choice !="y":
        break
          
input("Press enter to exit...")