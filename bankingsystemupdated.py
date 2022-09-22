import json
class Account:
    def createAccount(self):
        self.accNo=int(input("Enter Your No : "))
        self.name=input("Enter your name : ")
        self.deposit=int(input("Enter amount you want to deposit : "))

        print("Account has been created Successfully!")


def intro():
    print("FLICKEN")
    print("Hi there! welcome to banking system")


def writeAccount():
    account=Account()
    account.createAccount()
    writeAccountFile(account)

def writeAccountFile(account):
    data=json.load(open('data.json','r'))
    if type(data) is dict:
        data=[data]

    data.append({
        "accNo":account.accNo,
        "name":account.name,
        "deposit":account.deposit,
    })
    with open('data.json','w') as file:
        json.dump(data,file) 

def depositAmount(num):
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
        
def withdrawAmount(num):
    jsonFile = open("data.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    if type(data) is dict:
        data=[data]
    for i in data:
        if i['accNo']==num:
            amm=int(input("Enter Amount you want to withdraw : "))
            i['deposit']-=amm
            print(f"you have withdrawn {amm}")
            print(f"you're updated account balance is : {i['deposit']}")  
            
            ## Save our changes to JSON file
            jsonFile = open("data.json", "w+")
            jsonFile.write(json.dumps(data))
            jsonFile.close()      
       

def maketrans(num,num2,amm):
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
   
    ch = input()

    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAmount(num)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        withdrawAmount(num)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        num2= int(input("Enter Reciver Account no : "))
        ammount=int(input("Enter amount you want to send : " ))

        maketrans(num,num2,ammount)
   
    
    ch = input("Enter your choice : ")