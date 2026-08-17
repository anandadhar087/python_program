n = int(input("Enter 3-digit number: "))
total = sum(int(d)**3 for d in str(n))
print("Armstrong" if total == n else "Not Armstrong")
