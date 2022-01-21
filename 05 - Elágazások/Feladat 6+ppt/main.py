print("x =")
x:int = int(input())

print("y =")
y:int = int(input())

print("z =")
z:int = int(input())

print("a =")
a:int = int(input())

if(x > y > z > a):
    print(f"{a}, {z}, {y} {x}") 
elif(x < y < z < a):
    print(f"{x}, {y}, {z}, {a}")
elif(x == y == a < z):
    print(f"{x}, {y}, {a}, {z}")
elif(x == a == z < y):
    print(f"{x}, {a}, {z}, {y}")
elif(x == a == z > y):
    print(f"{y}, {z}, {a}, {x}")
elif(y == a == z > x):
    print(f"{x}, {z}, {a}, {y}")
elif(y == a == z < x):
    print(f"{y}, {a}, {z}, {x}")
elif(x == y == a > z):
    print(f"{z}, {a}, {y}, {x}")
elif(x == y == z < a):
    print(f" {x}, {y}, {z}, {a}")
elif(x == y == z > a):
    print(f"{a}, {z}, {y}, {x} ")
elif(x == y > z > a):
    print(f"{a}, {z}, {y}, {x}")
elif(x == y < z < a):
    print(f"{x}, {y}, {z}, {a}")
elif(x == y > z > a):
    print(f"{a}, {z}, {y}, {x}")
elif(x == y > a > z):
    print(f"{z}, {a}, {y}, {x}")
elif(x == y < a < z):
    print(f"{x}, {y}, {a}, {z}")
elif(x == z > y > a):
    print(f"{a}, {y}, {z}, {x}")
elif(x == z < y < a):
    print(f"{x}, {z}, {y}, {a}")
elif(x == z > a > y):
    print(f"{y}, {a}, {z}, {x}")
elif(x == z < a < y):
    print(f"{x}, {z}, {a}, {y}")
elif(y == z < a < x):
    print(f"{y}, {z}, {a}, {x}")
elif(y == z > a > x):
    print(f"{x}, {a}, {z}, {y}")
elif(z == a < y < x):
    print(f"{z}, {a}, {y}, {x}")
elif(z == a > y > x):
    print(f"{x}, {y}, {a}, {z}")
elif(z == a < x < y):
    print(f"{z}, {a}, {x}, {y}")
elif(z == a > x > y):
    print(f"{y}, {x}, {a}, {z}")
elif(x == a < z < y):
    print(f"{x}, {a}, {z}, {y}")
elif(x == a > z > y):
    print(f"{y}, {z}, {a}, {x}")
elif(x == a < y < z):
    print(f"{x}, {a}, {y}, {z}")
elif(x == a > y > z):
    print(f"{z}, {y}, {a}, {x}")     
else:
    print("mind egyenlő")