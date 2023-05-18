#loops in python
#for loop
for num in range(1,11):
    print(num)
    
#example2 for loop with strings
name="clarence"
for i in name:
    print(i)
    
    
#looping with list
students=['clarence', 'richard','eliz','mary']
ages=[1,2,3,4]   
for i in students:
    print(i)
for i  in ages:
    if i==4:
        print('hey welcome')
    else:
        print('welcome')
        
# for loop
for num1 in range(1,21):
    print(num1)
    
#performing sum of first 10 numbers using for loop(0 to 9)
sum=0
for i in range(1,10):
    sum= sum+1
print ('the sum of the numbers is' ,sum)

#performing sum of the 20 number using for loop (1 to 20)
sum=1
for i in range(1,21):
    sum=sum+1
print ('the sum of the numbers is' ,sum)  

#python program to illustrate while loop
count=0
#while(count<3):
    #count=count+1
    #print('Hey Clarence')
while(count<5): count+=1; print('Hey Clarence welcome')

#while loop
count=10
while count>=1:
   print(count)
count=count-1
   
# print even and odd number between 1 to 10
for i in range (1,10):
    if i % 2==0:
       print('even number :',i)
    else:
       print('odd number',i)
       
# print the sum of the even numbers between 1 to 10
numbers = [1,2,3,4,5,6,7,8,9,10]
even_sum = sum_of_even(number)
print("The sum of all even numbers in the list is:", even_sum)


sum=0 
while True:
    num1 = int(input("Enter a positive number or enter -1 to exit"))
    if num == -1:
        break
    
    if num > 0:
        sum=sum+num
        
    else:
        print("invalid input enter a positive number")
    print("print the sum of the positive number is :", sum)
        
    
