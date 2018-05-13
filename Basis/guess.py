# Author:Colin

age_of_Colin = 23

count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_Colin:
        print('bingo')
        break
    elif guess_age > age_of_Colin:
        print("think smaller...")
    else:
        print("think bigge...")
    count += 1
else:
    print("you have tried too many times...fuck off")

for i in range(0,10,2):
    print("loop",i)

