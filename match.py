a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))

match a>b:
    case 1:
        max=a
    case 0:
        max=b

print("Maximum value is=",max)

match a<b:
    case 1:
        min=a
    case 0:
        min=b

print("Minimum value is=",min)        
