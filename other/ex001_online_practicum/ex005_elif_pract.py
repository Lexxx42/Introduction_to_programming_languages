holiday = False
temperature = -916
age = 3
temperature_to_stay_at_home = -27
age_limit_for_elementary_school = 12

if holiday == True:
    print("Today is a holyday!")
elif temperature < temperature_to_stay_at_home:
    if age < age_limit_for_elementary_school:
        print("Stay at home :)")
    else:
        print("Slowly go to school :(")
else:
    print("Go to school :(")
