import json
class Account:
    def createAccount(self):
        self.accNo=int(input("Enter Your No : "))
        self.name=input("Enter your name : ")
        self.type=input("Enter your Account type you want: ")
        self.deposit=int(input("Enter amount you want to deposit : "))

        data=json.load(open('data.json','r'))
        if type(data) is dict:
            data=[data]

        data.append({
            "accNo":self.accNo,
            "name":self.name,
            "type":self.type,
            "deposit":self.deposit,
        })
        with open('data.json','w') as file:
            json.dump(data,file)



        print("Account has been created Successfully!")
    
    def displayAccount(self):
        bank1=Bank()
        ac=int(input("Enter Your Account Number : "))
        bank1.displaySingleAccount(ac)
    
    def depositAmmout(self, num):
        jsonFile = open("data.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        if type(data) is dict:
            data=[data]
        for i in data:
            if i['accNo']==num:
                amm=int(input("Enter Amount you want to deposit : "))
                i['deposit']+=amm
                print(f"you have deposited {amm}")
                print(f"you're updated account balance is : {i['deposit']}")  
            
                ## Save our changes to JSON file
                jsonFile = open("data.json", "w+")
                jsonFile.write(json.dumps(data))
                jsonFile.close()


    def withdrawAmmout(self, num):
        jsonFile = open("data.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        if type(data) is dict:
            data=[data]
        for i in data:
            if i['accNo']==num:
                amm=int(input("Enter Amount you want to deposit : "))
                i['deposit']-=amm
                print(f"you have deposited {amm}")
                print(f"you're updated account balance is : {i['deposit']}")  
            
                ## Save our changes to JSON file
                jsonFile = open("data.json", "w+")
                jsonFile.write(json.dumps(data))
                jsonFile.close()   



class Bank:
    def __init__(self) -> None:
        print("Welcome to Flicken Bank system")
    
    def  CreateNewAccount(self):
        account=Account()
        account.createAccount()
    def displayAllAccount(self):
        jsonFile = open("data.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        if type(data) is dict:
            data=[data]
        for i in data:
            print(i)
    def displaySingleAccount(self,ac):

        jsonFile = open("data.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        if type(data) is dict:
            data=[data]
        for i in data:
            if i['accNo'] == ac:
                print(i['Name'])
                print(i['type'])
                print(i['deposit'])

    def makeTransaction(self,num, num2, amm):
        jsonFile = open("data.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file
        if type(data) is dict:
            data=[data]
        for i in data:
            if i['accNo']==num:
                for j in data:
                    if j['accNo']==num2:
                        i['deposit']-=amm
                        j['deposit']+=amm
                        print(f"The balance for sender is : {i['deposit']}")
                        print(f"The balance for reciver is : {j['deposit']}")
                        ## Save our changes to JSON file
                        jsonFile = open("data.json", "w+")
                        jsonFile.write(json.dumps(data))
                        jsonFile.close() 

                        #####mentain transaction history
                        dat=json.load(open('trans.json','r'))
                        dat.append({
                            "Sender":num,
                            "Reciver":num2,
                            "Amount":amm
                        })
                        with open('trans.json','w') as f:
                            json.dump(dat,f) 




def intro():
    print("FLICKEN")
    print("Hi there! welcome to banking system")
      
       
ch=''
num=0
intro()





while ch != 8:
    #system("cls");
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. Deposit Ammount")
    print("\t3. Withdraw Ammount ")
    print("\t4. Transfer Ammount ")
    print("\t5. Display All Accounts ")
    print("\t6. Display your Account ")

    
   
    ch = input()

    if ch == '1':
        bank1=Bank()
        bank1.CreateNewAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        accd=Account()
        accd.depositAmmout(num)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        accw=Account()
        accw.withdrawAmmout(num)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        num2= int(input("Enter Reciver Account no : "))
        ammount=int(input("Enter amount you want to send : " ))

        banktran=Bank()
        banktran.makeTransaction(num, num2, ammount)
    elif ch == '5':
        bank=Bank()
        bank.displayAllAccount()
    elif ch == '6':
        Acc1=Account()
        Acc1.displayAccount()
        
    
        
   
    
    ch = input("Enter your choice : ")