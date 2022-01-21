print("x =")
x:int = int (input())

print("y =")
y:int = int (input())

print("z =")
z:int = int (input())

if(x % y == 0 and x % z ==0):
    print("x osztható mindkét számmal")
elif(x % y == 0):
    print("x osztható y-al")
elif(x % z == 0):
    print("x osztható z-vel")
else:
    print("x nem osztható egyik számmal sem")
