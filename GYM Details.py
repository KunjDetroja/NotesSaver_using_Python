class bank:
    bank_acc={'12334':{'name':'qaws','balance':50230},'1111':{'name':'admin','balance':150540}}
    
    def __init__(self,acc_num,name,fee):
        self.acc_num=acc_num
        self.name=name
        self.fee=fee
        
    def payment(self):
        for i in bank.bank_acc:
            if self.acc_num==i:
                if self.fee<=bank.bank_acc[i]['balance']:
                    bank.bank_acc[i]['balance']-=self.fee
                    bank.bank_acc['1111']['balance']+=self.fee
                    return True


class gym:
    member_acc={'qwe':{'password':'1q2w'},'rty':{'password':'4r5t'}}
    admin_acc={'az':{'password':'12'}}
    member_detail={'qwe':{'meal':'Meal 1:- Protein shake with milk + 2 parathas or rice\n Meal 2:- 4 rotis  + veg.(subji) + 1 bowl curd\n Meal 3:- rice + daal + veg. + 3 eggs','type':'Weight gain'}}
    
    
    def __init__(self,username,password):
        self.username=username
        self.password=password
    
    
    
    def login(self):
        
        for i in gym.member_acc:
            if i==self.username:
                if gym.member_acc[i]['password']==self.password:
                    return 1
                else:
                    return 2
        else:
            return 3
    
    
    def adminlogin(self):
        for i in gym.admin_acc:
            if i==self.username:
                if gym.admin_acc[i]['password']==self.password:
                    return 1
        else:
            return 2
    def add_details(self):
        name=input("\nEnter the username of person of which you want to add details:- ")
        for i in gym.member_acc:
            if name == i:
                types=input("Enter the type of person:- ")
                meals=input("Enter the meal of person:- ")
                gym.member_detail.update({name:{'meal':meals,'type':types}})
                break
        else:
            print("\nThere is noone of this username")
            
            
    def search_details(self):
        name=input("\nEnter the username of person of which you want to search details:- ")
        for i in gym.member_detail:
            if name == i:
                print('\nType:- ',gym.member_detail[i]['type'],'\nMeal:-\n',gym.member_detail[i]['meal'])
                break
        else:
            print("\nThere is no details of this username")
            
    
    def money(m):
        acc_num=input("\nEenter the account number:- ")
        name=input("Enter the name")
        pay=bank(acc_num,name,m)
        if pay.payment():
            print("\nPayment done")
            loop=1
            while(loop==1):
                flag=1
                username=input("\nEnter your username:-")
                for i in gym.member_acc:
                    if username==i:
                        flag=0
                if flag==1:
                    loop=0
                else:
                    print("\nThis name is already taken")
            password=input("enter your password")
            gym.member_acc.update({username:{'password':password}})
            print("\nYour are member of our gym")
    def displaydetails(self):
        flag=0
        for i in gym.member_detail:
            if self.username==i:
                print('\nType:- ',gym.member_detail[i]['type'],'\nMeal:-\n',gym.member_detail[i]['meal'])
                flag=1
        if flag==0:
            print("\nno detail found")
            

loop=1
while(loop==1):
    choice=int(input("\n1. For login\n2. for signup\n3. Admin login\n4. Exit\nEnter your choice:- "))
    if choice==1:
        user=input('\nenter your username:- ')
        pw=input('enter your password:- ')
        m=gym(user,pw)
        if m.login()==3:
            print("\nAccount doesn't exist")
        elif m.login()==2:
            print("\nIncorrect username and password")
        elif m.login()==1:
            print("\nsuccessfully login")
            lup=1
            while(lup==1):
                x=int(input('\n1. display details\n2. Exit\nEnter your choice:-'))
                if x==1:
                    m.displaydetails()
                elif x==2:
                    lup=0
    if choice==2:
        option=int(input("\n1. 3000rs for 3 months\n2. 8000rs for 6 months\n3. 12000rs for 1 year\nEnter your choice:- "))
        if option == 1:
            gym.money(3000)
        elif option == 2:
            gym.money(8000)
        elif option == 3:
            gym.money(12000)
        else:
            print("\nInvalid choice")
    if choice==3:
        user=input('\nEnter your username:- ')
        pw=input('Enter your password:- ')
        m=gym(user,pw)
        if m.adminlogin()==2:
            print("\nIncorrect username and password")
        elif m.adminlogin()==1:
            print("\nSuccessfully login")
            lup=1
            while(lup==1):
                x=int(input('\n1. add details\n2. search details\n3. For Account balance\n4. Exit\nEnter your choice:-'))
                if x==1:
                    m.add_details()
                elif x==2:
                    m.search_details()
                elif x==3:
                    print('\nTotal balance is ',bank.bank_acc['1111']['balance'])
                elif x==4:
                    lup=0
    if choice==4:
        print('\nThank you for visiting')
        loop=0