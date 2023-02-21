a = 10
b = 4
c = 8 
z = a + b
def switch(x):
    match x:
        case 2:
            return 1
        case 4:
            return 2
        case _:
            return 0  
y = switch(b)
print(y)        
    