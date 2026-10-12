# Assuming balance 
bal = 10000

#MainMenu
def menu():
    print("---------------------------------------------")
    print("1. To Check your Bank Balance ")
    print("2. To Withdraw Amount from Your Bank Account ") 
    print("3. To Deposit  Amount from Your Bank Account ")
    print("4. To Exit ") 
    choice = input("Select from the following Numbers to Proceed (1-4) :")
    return choice
#withdraw
def withdraw():
    global bal
    amount =int(input("How Much Amount You Want to withdraw : "))
    if amount>bal:
        print("Insufficent Amount !!!") 
    else:
     bal -= amount
     print(f"After Withdrawing ${amount} Your Bank Balance is ${bal:,}:")
    return 0

#deposit
def deposit():
    global bal
    amount= int(input("How Much Amount You Want to deposit : "))  
    bal += amount
    print(f"Your Bank Balance after depositing ${amount} will be ${bal:,}") 

#Main application
while True:
 print(" | WELCOME TO ATM APPLICATION | ")
 print("------------------------------------")
 u = input("| Enter Your UserName :")
 p = input("| Enter Your PassWord :")    
    
 if u == "rafay" and p == "1234":   
      Choice = menu()
      if Choice == '1':
        print(f"Your Current bank Balance is ${bal:,}")
        withdraw() 
      elif Choice == '3':
        deposit()
      elif Choice == '4':
        break
      else :
         print(f"Please Select A Number From (1-4) To Proceed | You have entered : ({Choice}) |")  
  
 else :
        print("Please Enter A valid UserName and Password ")                       
 
 a = input("Do You want Continue Press any Key  OR To Exit Press 'X' : ")
 if a == "X" or a == "x":
     break

#Greeting
print("| Thanks For Coming |")