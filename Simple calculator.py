def myadd(a,b):   
   return (a+b)
def mysub(a,b):
	  return(a-b)
def mymult(a,b):
 	 return(a*b)
def mydivide(a,b):
 	 return(a/b)
print("1.Addition")
 
print("2.Subtraction")
 
print("3.Multiplication")
 
print("4.Division")
 
choice=input("Enter your choice:")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if choice == "1":
 		     print(a,"+",b,"=",myadd(a,b))
elif choice== "2":
 		     print(a,"+",b,"=",mysub(a,b))
elif choice=="3":
 		     print(a,"*",b,"=",mymult(a,b))
elif choice=="4":
 		     print(a,"/",b,"=",mydivide(a,b))
else:
 		     print("Only numbers can be accepted as an input")
 		     
 		     