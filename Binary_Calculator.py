# PROBLEM 2 " A Binary calculator "
# Mary Magdy Kamal Iskander                 ID:20230302
# Shrouq Osama Fathy abdelhady              ID: 20230188
# Somaya Tamer Magdy Shoaib                 ID: 20231225


# Function to check if the given string is a binary number 
def Binary_number_or_not(numb):
  Binary= {'0','1'}
  for x in numb :
    if x in Binary :
      return True

# Function to compute the one's complement of a binary number    
def Compute_one_complement (var1):
 # Convert the binary number to a list of characters
 make_list=list(var1)
 for i in range(len(make_list)):
    if make_list[i] == '1':  
     make_list[i] = '0'
    elif make_list[i] == '0':
     make_list[i] = '1'
 result = ''.join(make_list)    
 return result

# Function to compute the two's complement of a binary number
def Compute_two_complement (var1):
 # If the binary number is all zeros then the two's complement is equal to '0'
 if all(char == '0' for char in var1):
  return'0'
 reversed_var1=list(var1)
 for i in range(len(reversed_var1)):
    if reversed_var1[i] == '1':  
     reversed_var1[i] = '0'
    elif reversed_var1[i] == '0':
     reversed_var1[i] = '1'  
 var2 =1
 length_of_var1= len (reversed_var1)
 var2= str(var2).zfill(length_of_var1)
 reversed_var1 = ''.join(reversed_var1).zfill(length_of_var1)
 make_list=['0'] * (length_of_var1 + 1) # Initializing a list (make_list) to store the result of addition
 i = length_of_var1-1
 carry_on=0
 # Perform binary addition
 while i >= 0:
    sum= int(reversed_var1[i]) + int(var2[i]) + carry_on
    make_list[i+1]= str(sum %2)
    carry_on= sum//2
    i-=1 
 # Set the first element of the result list to the final carry value   
 make_list[0]= str(carry_on)    
 result = ''.join(make_list) 
 return result   

# Function to perform binary addition
def Binary_Addition (var1,var2):
 length_ofvar2= len (var2)
 length_ofvar1= len (var1)
 maximum_length=max (length_ofvar1,length_ofvar2 )
 var2= str(var2).zfill(maximum_length)
 var1= str(var1).zfill(maximum_length)
 make_list=['0'] * (maximum_length + 1) 
 i = maximum_length-1 # to be able to iterate through the binary numbers from right to left
 carry_on=0
 while i >= 0:
    sum= int(var1[i]) + int(var2[i]) + carry_on
    make_list[i+1]= str(sum %2)
    carry_on= sum//2
    i-=1 # to be able to move to the next position towards the left
 make_list[0]= str(carry_on) 
 # Remove leading zero if it is present in the result   
 if make_list[0] == '0':
  make_list.pop(0)
  result = ''.join(make_list)
 else:
   result = ''.join(make_list) 
 return result

# Function to perform binary subtraction
def Binary_Subtraction (var1,var2):
 length_ofvar2= len (var2)
 length_ofvar1= len (var1)
 maximum_length=max (length_ofvar1,length_ofvar2 )
 var2= str(var2).zfill(maximum_length)
 var1= str(var1).zfill(maximum_length)
 make_list=['0'] * (maximum_length + 1)
 i = maximum_length-1
 carry_on=0
 while i >= 0:
    diff= int(var1[i]) - int(var2[i]) - carry_on
    make_list[i+1]= str(diff %2)
    if diff < 0: # If negative then add 2 to the result and set carry_on to 1
     diff += 2 
     carry_on = 1
    else:
     carry_on = 0  # If non-negative then set carry_on to 0  
    i-=1  
 make_list[0]= str(carry_on)    
 result = ''.join(make_list) 
 result= result.lstrip('0') or '0' # To remove leading zeros from the result
 return result

# The menues and main program
while True:
  print("** Binary Calculator **")
  print("A) Insert new numbers")
  print("B) Exit")
  option = input("Please Enter your choice (A/B) :")
  if option == 'A' or option=='a':
    var1= str (input("Enter a binary number:"))
    if not Binary_number_or_not(var1):
      print ("** Please insert a valid binary number **")
      continue
    while True:
     print("** Please Select the operation **")
     print("A) Compute one's complement")
     print("B) Compute two's complement")
     print("C) Addition")
     print("D) Subtraction")
     other_option = input(" Please Enter your choice (A/B/C/D) :")
     if other_option == 'A' or other_option=='a':
        result=Compute_one_complement(var1)
        print( f"Result: {result}"  )
        break  
     elif other_option == 'B' or other_option=='b':
        result=Compute_two_complement(var1)
        print ( f"Result: {result}" )
        break 
     elif other_option == 'C' or other_option== 'c':
        var2 = str(input(" Please insert a second binary number:"))
        if not Binary_number_or_not(var2):
          print (" ** Please insert a valid binary number** ")
        else :
           result =Binary_Addition(var1 , var2)
           print (f"Result: {result}" )
           break
        
     elif other_option == 'D' or other_option=='d':
        var2 = str (input("Please insert a second binary number:"))
        if not Binary_number_or_not(var2):
           print ("** Please insert a valid binary number **")
           continue 
        else :
           result =Binary_Subtraction(var1 , var2)
           print (f"Result: {result}" ) 
           break 
     else:
        print("Invalid, Please enter A or B or C or D : ")

  elif option == 'B' or option=='b':
    print("Program Exited")
    break 
  else:
    print("Invalid, Please enter A or B")

