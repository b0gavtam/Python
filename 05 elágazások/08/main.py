print("kérek egy számot")
x:int=int(input())

if (x % 4 == 0 and x % 6 == 0):
    print(f"{x} osztható 4el is és 6al is")
else:
    print(f"{x} nem osztható 4el is és 6al is")