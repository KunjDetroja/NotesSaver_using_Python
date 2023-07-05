from datetime import date
class notes:
    perdata={'abc':{'password':'12qw'},'def':{'password':'34er'}}
    pernote={'ac-2023-02-26': ['sdvsfqwfw','sggdgsgg','sdgsgsgsg'],'ac-2023-02-22': ['sdvsfqwfw'],'ac-2022-02-26': ['sdvsfqwfw'],'abc-2022-02-26': ['sfqwfw'],'bac-2022-02-25': ['sdvsfqwfw']}
    tempacc={'ac': {'password': '1w', 'date': '2023-01-26'}}
    
    
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    
    def signup(self):
        f=0
        if '-' in self.username:
            return 3
        for i in notes.perdata:
            if i==self.username:
                f=1
                break
        if f==1:
            return 2
        else:
            notes.perdata.update({self.username:{'password':self.password}})
            return 1
        
        
    def unlist(self):
        f=0
        for i in notes.perdata:
            if i==self.username:
                if notes.perdata[i]['password']==self.password:
                    f=1
        if f==1:
            today=date.today()
            ds=today.strftime('%d')
            month=today.strftime('%m')
            year=today.strftime('%Y')
            dates=str(year)+'-'+str(month)+'-'+str(ds)
            notes.tempacc.update({self.username:{'password':self.password,'date':dates}})
            notes.perdata.pop(self.username)
            print("\nYour account get unlist in 1 month\nIf you signup before 1 month then you get your account back")
        else:
            print("\nAccount doesn't exist")
            
    
    def login(self):
        f=0
        tempdata=[]
        flag=0
        temp=''
        today=date.today()
        ds=int(today.strftime('%d'))
        month=int(today.strftime('%m'))-1
        if month<10:
            month='0'+str(month)
        if ds<10:
            ds='0'+str(ds)
        year=today.strftime('%Y')
        dates=str(year)+'-'+str(month)
        for i in notes.tempacc:
            if dates in notes.tempacc[i]['date'] and int(ds)>=int(notes.tempacc[i]['date'][-2:]):
                temp=i
                flag=1
        if flag==1:
            notes.tempacc.pop(temp)
            for i in notes.pernote:
                x=i.split('-')
                if temp == x[0]:
                    tempdata.append(i)
            for i in tempdata:
                notes.pernote.pop(i)
        for i in notes.perdata:
            if i==self.username:
                if notes.perdata[i]['password']==self.password:
                    f=1
                    break
        for i in notes.tempacc:
            if i==self.username:
                if notes.tempacc[i]['password']==self.password:
                    return 2
        if f==1:
            return 1
        else:
            return 3
        
    
    def note(self):
        today=date.today()
        dates=today.strftime('%d')
        month=today.strftime('%m')
        year=today.strftime('%Y')
        name=self.username+'-'+str(year)+'-'+str(month)+'-'+str(dates)
        yournote=input("enter your note:-")
        f=0
        for i in notes.pernote:
            if i==name:
                notes.pernote[name].append(yournote)
                f=1
        if f==0:
            notes.pernote.update({name:[yournote]})
        print("\nyour note is added")
    
    
    def deletenote(self):
        name=''
        y=int(input("Enter the year"))
        m=int(input("Enter the month"))
        d=int(input("Enter the date"))
        if m<10:
            m='0'+str(m)
        if d<10:
            d='0'+str(d)
        name=self.username+'-'+str(y)+'-'+str(m)+'-'+str(d)
        loop=1
        choice=1
        while(loop==1):
            if choice==1:
                f=0
                for i in notes.pernote:
                    if name in i:
                        for j in range(len(notes.pernote[i])):
                            print(notes.pernote[i][j],' - ',j+1)
                            f=1
                if f==1:
                    index=int(input('enter the index number you want to delete'))
                    notes.pernote[name].pop(int(index-1))
                    if len(notes.pernote[name])==0:
                        notes.pernote.pop(name)
                if f==0:
                    print("\nnote is not entered on this date")
                    loop=0
                exits=int(input('Enter 1 for exit'))
                if exits==1:
                    for j in range(len(notes.pernote[i])):
                        print(notes.pernote[i][j])
                    loop=0
            if choice==2:
                loop=0
            
        
        
    def displaynote(self):
        loop=1
        while(loop==1):
            f=0
            c=int(input('Note Display by:-\n1. By Year\n2. By Month\n3. By Date\n4. Exit\nEnter your choice:- '))
            if c==1:
                name=''
                y=int(input("Enter the year"))
                name=self.username+'-'+str(y)
                for i in notes.pernote:
                    if name in i:
                        print(notes.pernote[i])
                        f=1
                if f==0:
                    print("\nnote is not entered on this year")
            elif c==2:
                name=''
                y=int(input("Enter the year"))
                m=int(input("Enter the month"))
                if m<10:
                    m='0'+str(m)
                name=self.username+'-'+str(y)+'-'+str(m)
                for i in notes.pernote:
                    if name in i:
                        print(notes.pernote[i])
                        f=1 
                if f==0:
                    print("\nnote is not entered on this month")
            elif c==3:
                name=''
                y=int(input("Enter the year"))
                m=int(input("Enter the month"))
                d=int(input("Enter the date"))
                if m<10:
                    m='0'+str(m)
                if d<10:
                    d='0'+str(d)
                name=self.username+'-'+str(y)+'-'+str(m)+'-'+str(d)
                for i in notes.pernote:
                    if name in i:
                        print(notes.pernote[i])
                        f=1
                if f==0:
                    print("\nnote is not entered on this date")
            elif c==4:
                loop=0
            else:
                print('\nInvalid choice')

loop=1
while(loop==1):
    n=int(input("1. For login\n2. for signup\n3. For Unlist\n4. Exit\nEnter your choice:- "))
    if n==1:
        name=input('enter your username:- ')
        pw=input('enter your password:- ')
        p=notes(name,pw)
        if p.login()==1  or p.login()==2:
            if p.login()==1:
                print('\nsuccessfully login')
            if p.login()==2:
                notes.tempacc.pop(name)
                notes.perdata.update({name:{'password':pw}})
                print("\nYou get your account back")
            lup=1
            while(lup==1):
                num=int(input("1. For Add Note\n2. For Display Notes\n3. For Deletenote\n4. Logout\nEnter your choice:-"))
                if num==1:
                    p.note()
                elif num==2:
                    print(p.displaynote())
                elif num==3:
                    p.deletenote()
                elif num==4:
                    lup=0
                else:
                    print("\nInvalid choice")
        else:
            print('\nInvalid username and password')
    elif n==2:
        name=input('Enter your username:- ')
        pw=input('Enter your password:- ')
        p=notes(name,pw)
        if p.signup()==1:
            print('successfully Signup')
        elif p.signup()==2:
            print('Username already taken')
        elif p.signup()==3:
            print("'-' is not allow for username")
            
    elif n==3:
        name=input('enter your username:- ')
        pw=input('enter your password:- ')
        p=notes(name,pw)
        p.unlist()
    elif n==4:
        print('\nThank you for visiting')
        loop=0
    else:
        print('\nInvalid choice')