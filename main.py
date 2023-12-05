#ARYA MANE -1841
#Assignment - 2

#To input marks of all subjects

a=int(input("Enter your Maths marks: "))
b=int(input("Enter your Pps marks : "))

c=int(input("Enter your Sme marks : ")) 
d=int(input("Enter your Bee marks : "))

e=int(input("Enter your Chemistry marks: ")) 
#To find out percentage by dividing total by 5

sum=(a+b+c+d+e)/5 
#if user has less than 40 then he is marked as

if a<=40 or b<=40 or c<=40 or d<=40 or e<=40: print("You are fail")

elif sum>75:

  print("Distinction")

elif sum<75 and sum>=60:

   print("First class")

elif sum<60 and sum>=50:

   print("Second class")

elif sum<50 and sum>=40: print("Third division")

else:

   print("Invalid number")
   
   
   
   
   
   
   
   
   
   
   
   
   