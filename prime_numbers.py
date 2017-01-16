# take input from a user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
prime = []

for num in range(lower, upper + 1):
    # Prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime.append(num)

print(prime)
