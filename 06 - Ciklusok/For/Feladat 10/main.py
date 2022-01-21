sum: int = 0
szorzat: int = 1

print("honnan")
kezdoErtek: int = int(input())

print("hová")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    sum += i
    szorzat *= i
    print(f"osszeg={sum}")
    print(f"szorzat={szorzat}")