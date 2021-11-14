#if user wants to convert decimal to binary this program will run.
def DTB(n):
   if n == 0 or n == 1:
       print(n, end=" ")
       return
   DTB(int(n/2))   
   DTB(n%2)

#if user wants to convert decimal to octal this program will run.
def DTO():
    pass

#if user wants to convert decimal to hexadecimal this program will run.
def DTH():
    pass

#Getting the input from user for which type of conversion he/she wants to do.
num = int(input("Enter the your decimal number here - "))
typeinp = input("In which format you want to convert this number [1]Binary, [2]Octal, [3]Hexadecimal: ")

#verifing and calling a particular function
if typeinp == "1" :
    print("The Binary number for your number is -> ", end=" ")
    DTB(num)
elif typeinp == "2" :
    DTO()
    pass
elif typeinp == "3" :
    DTH()
    pass
else:
    print("Something went wrong")

