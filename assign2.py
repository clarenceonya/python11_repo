sum=0 
while True:
    num = int(input("Enter a positive number or enter -1 to exit : "))
    if num == -1:
        break
    
    if num > 0:
        sum=sum+num
        
    else:
        print("invalid input enter a positive number")
    print("print the sum of the positive number is :", sum)
        