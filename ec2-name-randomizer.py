import random
import string

def ec2_name_generator():
    counter = 1
    allowed_departments = ('marketing','accounting','finops')
    department_name = input("What is your department? ")

    if department_name not in allowed_departments:
        while counter < 2:
            print()
            print("You've entered an invalid name.")
            print("Please check your spelling and use lowercase letters." )
            counter += 1
            print()
            print("---2 attempts remaing---")
            print()
            input("What is your department? ")
        while counter == 2 and department_name not in allowed_departments:
            print()
            print("You've entered an invalid name, again.")
            print("Please check your spelling and use lowercase letters." )
            counter += 1
            print()
            print("---1 attempt remaining---")
            print()
            input("What is your department? ")
        while counter >= 3 and department_name not in allowed_departments:
            print()
            print("This name is invalid, or this department is not allowed.")
            print()
            print("---------------------------------------------------------")
            print("-------Please contact I.T. for further information-------")
            print("---------------------------------------------------------")
            print()
            break
    
    if department_name in allowed_departments:
        name_quantity = int(input('How many EC2 instances would you like unique names for? '))

    for _ in range (name_quantity):
        random_numbers = random.randint(100000,900000)
        instance_name = f'{department_name}-{random_numbers}'
        instance_id_names = instance_name
        print(instance_id_names)
print('''
····················································
:  ______ _____ ___    _   _                       :
: |  ____/ ____|__ \  | \ | |                      :
: | |__ | |       ) | |  \| | __ _ _ __ ___   ___  :
: |  __|| |      / /  | . ` |/ _` | '_ ` _ \ / _ \ :
: | |___| |____ / /_  | |\  | (_| | | | | | |  __/ :
: |______\_____|____| |_| \_|\__,_|_| |_| |_|\___| :
:   _____                           _              :
:  / ____|                         | |             :
: | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __  :
: | | |_ |/ _ | '_ \ / _ | '__/ _` | __/ _ \| '__| :
: | |__| |  __| | | |  __| | | (_| | || (_) | |    :
:  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|    :
····················································

Welcome to the generator!
''')

ec2_name_generator()