number = input("Enter the number you want to know whether it is prime number or not :")
for i in range(2, int(number)):
    if int(number) % i == 0:
        print(f"{number} is not a prime number")
        break
    elif i == int(number)-1:
        print(f"{number} is a prime number")
