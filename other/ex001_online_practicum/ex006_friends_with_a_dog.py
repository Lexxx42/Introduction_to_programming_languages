# friends with a dog
distance = 100
first_friend_speed = 1
second_friend_speed = 2
dog_speed = 4
distance_when_frinds_meet = 2
count = 0
friend = 2

while distance > distance_when_frinds_meet:
    if friend == 1:
        time = distance / (first_friend_speed + dog_speed)
        friend = 2
    else:
        time = distance / (second_friend_speed + dog_speed)
        friend = 1
    distance = distance - (first_friend_speed + second_friend_speed)*time
    count = count + 1
print("friends met!","Distance=",distance,"Dog count=",count)
