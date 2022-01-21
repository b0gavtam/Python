print("Kérek egy számot")
x:int=int(input())

if((x>=-20 and x<=-10) or(x<=20 and x>=10)):
    print(f"{x} -20 és -10 vagy 10 és 20 közé esik")
else:
     print(f"{x} nem esik -20 és -10 vagy 10 és 20 közé ")