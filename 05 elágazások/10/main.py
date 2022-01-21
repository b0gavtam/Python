print("kérek egy számot")
x:int=int(input())

if(x%2==0 and x%3==0):
    print("ZIZI")
elif(x%2==0):
    print("BIZ")
elif(x%3==0):
    print("BAZ")
else:
    print(f"{x} nem osztható 2vel se és 3al se")