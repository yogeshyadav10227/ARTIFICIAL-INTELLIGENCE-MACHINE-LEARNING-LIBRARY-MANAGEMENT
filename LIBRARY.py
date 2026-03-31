import pandas as pd
from collections import Counter

Books={'ID':['Title','Author','Publisher','Edition','Genre','Price','Status']}
Members={'ID':['Name','DOB','Contact','Address','Books issued','DOJ','MED','Status']}
Issued={'ID':['Book ID','Book Name']}

def Add(field):
    no=int(input(f"How many {field} do you want to add"))
    while no>0:
        if field=='books':
            try:
                bid=int(input("Enter book id"))
                if bid not in Books:
                    btitle=input("Enter book name")
                    bauthor=input("Enter author's name")
                    bpubl=input("Enter publisher's name")
                    bedi=int(input("Enter the edition"))
                    bgen=input("Enter the genre")
                    bprice=float(input("Enter price of the book"))
                    bstat=input("Enter the status:-('A'->Available or 'I'->Issued)")
                    details=[btitle,bauthor,bpubl,bedi,bgen,bprice,bstat]
                    Books.setdefault(bid,details)
                    print("Books added sucessfully")
                else:
                    print("Book ID already exist")
            except ValueError:
                print("Invalid input")
        else:
            try:
                mid=int(input("Enter member id"))
                if mid not in Members:
                    mname=input("Enter member name")
                    mdob=input("Enter DOB (dd/mm/yyyy)")
                    mpho=int(input("Enter member's contact"))
                    madd=input("Enter member's address")
                    mbook=int(input("Enter number of book's issued:"))
                    mdoj=input("Enter date of joining (dd/mm/yyyy)")
                    mexpi=input("Enter membership expiry date (dd/mm/yyyy)")
                    mstat=input("Enter the membership status:-('A'->Active or 'E'->Expired)")
                    details=[mname,mdob,mpho,madd,mbook,mdoj,mexpi,mstat]
                    Members.setdefault(mid,details)
                    print("Members added sucessfully")
                else:
                    print("Member ID already exist")
            except ValueError:
                print("Invalid input")
        no-=1

def Displayall(field):
    df_vertical=pd.DataFrame(field)
    df_horizontal=df_vertical.T
    df_horizontal.columns=df_horizontal.iloc[0]
    df_final=df_horizontal[1:]
    print(df_final.to_markdown(tablefmt="grid", stralign="center"))

def Search(tempfield,field,index=None,search=None):
    found=False
    if search==None:
        for i in field:
            if i==index:
                tempfield.setdefault(i,field[i])
                found=True
    else:
        for i in field:
            if str(field[i][index]).lower()==search.lower():
                tempfield.setdefault(i,field[i])
                found=True
    if found:
        Displayall(tempfield)
    else:
        print("No records found")
            
def Select(field):
    while True:
        if field=='books':
            tempfield={'ID':['Title','Author','Publisher','Edition','Genre','Price','Status']}
            try:
                ch0=int(input("What do you want:-\n1)Select books by a category\n2)Select a specific book\n3)Quit"))
                if ch0==1:
                    ch1=int(input("Enter your choice:-\n1)Search by author's name\n2)Search by publisher's name\n3)Search by genre\n4)Search by status"))
                    if ch1==1:
                        auth=input("Enter author's name")
                        Search(tempfield,Books,1,auth)
                    elif ch1==2:
                        publ=input("Enter publisher's name")
                        Search(tempfield,Books,2,publ)
                    elif ch1==3:
                        genr=input("Enter genre")
                        Search(tempfield,Books,4,genr)
                    elif ch1==4:
                        stat=input("Enter status of availability:-\n'A' for available\n'I' for Issued")
                        Search(tempfield,Books,6,stat)
                    else:
                        print("Invalid Choice")
                elif ch0==2:
                    tempid=int(input("Enter book id"))
                    Search(tempfield,Books,tempid)
                elif ch0==3:
                    print("Quitting...")
                    break
                else:
                    print("Invalid Choice\nTry again")
            except ValueError:
                print("Invalid input\nTry Again...")
        else:
            tempfield={'ID':['Name','DOB','Contact','Address','Books issued','DOJ','MED','Status']}
            try:
                ch0=int(input("What do you want:-\n1)Select members by a category\n2)Select a specific member\n3)Quit"))
                if ch0==1:
                    ch1=int(input("Enter your choice:-\n1)Search by member's name\n2)Search by member's address \n3)Search by status"))
                    if ch1==1:
                        mem=input("Enter member's name")
                        Search(tempfield,Members,0,mem)
                    elif ch1==2:
                        add=input("Enter address")
                        Search(tempfield,Members,3,add)
                    elif ch1==3:
                        stat=input("Enter status:-\n'A' for active\n'E' for expired")
                        Search(tempfield,Members,7,stat)
                    else:
                        print("Invalid Choice")
                elif ch0==2:
                    tempid=int(input("Enter member id"))
                    Search(tempfield,Members,tempid)
                elif ch0==3:
                    print("Quitting...")
                    break
                else:
                    print("Invalid Choice\nTry again")
            except ValueError:
                print("Invalid input\nTry Again...")

def check(field,te_id):
    if te_id in field:
        return True
    else:
        print("No records found")
        return False
        
def Update(field,te_id,index,value):
    field[te_id][index]=value
    found=True
    print("Updated successfully")


def Modify(field):
    while True:
        if field=='books':
            try:
                ch2=int(input("What do you want to do\n1)Update title\n2)Update author's name\n3)Update publisher's name\n4)Update edition\n5)Update genre\n6)Update price\n7)Update status\n8)Quit"))
                if ch2==1:
                    tempid=int(input("Enter book id"))
                    if check(Books,tempid):
                        newtitle=input("Enter new title")
                        Update(Books,tempid,0,newtitle)
                elif ch2==2:
                    tempid=int(input("Enter book id"))
                    if check(Books,tempid):
                        newauth=input("Enter new author's name")
                        Update(Books,tempid,1,newauth)
                elif ch2==3:
                    tempid=int(input("Enter book id"))
                    if check(Books,tempid):
                        newpubl=input("Enter new publisher's name")
                        Update(Books,tempid,2,newpubl)
                elif ch2==4:
                    tempid=int(input("Enter book id"))
                    if check(Books,tempid):
                        newedi=int(input("Enter new edition"))
                        Update(Books,tempid,3,newedi)
                elif ch2==5:
                    tempid=int(input("Enter book id"))
                    if check(Books,tempid):
                        newgenr=input("Enter new genre")
                        Update(Books,tempid,4,newgenr)
                elif ch2==6:
                    tempid=int(input("Enter book id"))
                    if check(Books,tempid):
                        newpri=float(input("Enter new price"))
                        Update(Books,tempid,5,newpri)
                elif ch2==7:
                    tempid=int(input("Enter book id"))
                    if check(Books,tempid):
                        newstat=input("Update the status:-\n'A' for Available\n'I' for Issued\n'L' for Lost")
                        Update(Books,tempid,6,newstat.upper())
                elif ch2==8:
                    print("Exiting...")
                    break
                else:
                    print("Invalid Choice\nTry Again...")
            except ValueError:
                print("Invalid Input")
        else:
            try:
                ch2=int(input("What do you want to do\n1)Update name\n2)Update DOB\n3)Update Contact\n4)Update Address\n5)Update Book Issued\n6)Update DOJ\n7)Update MED\n8)Update Status\n9)Quit"))
                if ch2==1:
                    tempid=int(input("Enter member id"))
                    if check(Members,tempid):
                        newname=input("Enter new name")
                        Update(Members,tempid,0,newname)
                elif ch2==2:
                    tempid=int(input("Enter member id"))
                    if check(Members,tempid):
                        newdob=input("Enter new DOB")
                        Update(Members,tempid,1,newdob)
                elif ch2==3:
                    tempid=int(input("Enter member id"))
                    if check(Members,tempid):
                        newcon=int(input("Enter new contact"))
                        Update(Members,tempid,2,newcon)
                elif ch2==4:
                    tempid=int(input("Enter member id"))
                    if check(Members,tempid):
                        newadd=input("Enter new address")
                        Update(Members,tempid,3,newadd)
                elif ch2==5:
                    tempid=int(input("Enter member id"))
                    if check(Members,tempid):
                        newiss=int(input("Enter new number of books issued"))
                        Update(Members,tempid,4,newiss)
                elif ch2==6:
                    tempid=int(input("Enter member id"))
                    if check(Members,tempid):
                        newdoj=input("Enter new DOJ")
                        Update(Members,tempid,5,newdoj)
                elif ch2==7:
                    tempid=int(input("Enter member id"))
                    if check(Members,tempid):
                        newmed=input("Update MED")
                        Update(Members,tempid,6,newmed)
                elif ch2==8:
                    tempid=int(input("Enter member id"))
                    if check(Members,tempid):
                        newstat=input("Update the status:-\n'A' for Active\n'E' for Expired")
                        Update(Members,tempid,7,newstat.upper())
                elif ch2==9:
                    print("Exiting...")
                    break
                else:
                    print("Invalid Choice\nTry Again...")
            except ValueError:
                print("Invalid Input")


def Delete(field):
    if field=='books':
        try:
            tempid=int(input("Enter book id"))
            if tempid in Books:
                remove=Books.pop(tempid)
                print(tempid,':',remove,"has been removed")
            else:
                print("Records doesn't exist")
        except ValueError:
            print("Invalid input")
    else:
        try:
            tempid=int(input("Enter member id"))
            if tempid in Members:
                remove=Members.pop(tempid)
                print(tempid,':',remove,"has been removed")
            else:
                print("Records doesn't exist")
        except ValueError:
            print("Invalid input")

def issue():
    while True:
        mid=int(input("Enter member id"))
        if mid in Members:
            for i in Books:
                print(i,Books[i])
            no=int(input("How many books you want to issue:"))
            while no>0:
                bid=int(input("Enter book id to issue:"))
                if Books[bid][6].upper()=='A':
                    Books[bid][6]='I'
                    Members[mid][4]+=1
                    if mid not in Issued:
                        Issued.setdefault(mid,[bid,Books[bid][0]])
                    else:
                        Issued[mid].extend([bid,Books[bid][0]])
                    print(f"Book ID {bid} has been issued to Member ID {mid}")
                else:
                    print("Book is not available for issue")
                no-=1
            break
        else:
            print("Invalid Member ID or Book ID")
            break
    Recommend(mid)
    
    
def Recommend(mid):
    most=[]
    mostgenre=[]
    if mid not in Members:
        print("Member not found.")
        return

    else:
        for iid in Issued:
            bid=Issued[iid][0]
            most.append(bid)
            for i in most:
                found=i in Books
                if found==True:
                    genre=Books[i][4]
                    mostgenre.append(genre)
    mostgenre=Counter(mostgenre).most_common(1)[0][0]
    print(f"\nAI INSIGHT: I noticed you are highly interested in '{mostgenre}'.")
    print("Here are some more books you might like:\n")
    for i in Books:
        if Books[i][4].lower()==mostgenre.lower():
            print(i,Books[i])

while True:
    try:
        ch=int(input("Which data do you want to access:-\n1)Books\n2)Members\n3)Issue a book\n4)Quit"))
        if ch==1:
            print("Accessing books data...")
            while True:
                try:
                    ch01=int(input("What do you want to do:-\n1)Add books\n2)Display all books\n3)Search books\n4)Modify books\n5)Delete book\n6)Quit"))
                    if ch01==1:
                        Add('books')
                    elif ch01==2:
                        Displayall(Books)
                    elif ch01==3:
                        Select('books')
                    elif ch01==4:
                        Modify('books')
                    elif ch01==5:
                        Delete('books')
                    elif ch01==6:
                        print("Exiting...")
                        break
                    else:
                        print("Invalid Choice")
                except ValueError:
                    print("Invalid Input")
        elif ch==2:
            print("Accessing members data...")
            while True:
                try:
                    ch01=int(input("What do you want to do:-\n1)Add member\n2)Display all member\n3)Search member\n4)Modify member\n5)Delete member\n6)Quit"))
                    if ch01==1:
                        Add('members')
                    elif ch01==2:
                        Displayall(Members)
                    elif ch01==3:
                        Select('members')
                    elif ch01==4:
                        Modify('members')
                    elif ch01==5:
                        Delete('members')
                    elif ch01==6:
                        print("Exiting...")
                        break
                    else:
                        print("Invalid Choice")
                except ValueError:
                    print("Invalid Input")
        elif ch==3:
            issue()
        elif ch==4:
            print("Quitting the program...")
            break
        else:
            print("Invalid Choice\nTry Again")
    except ValueError:
        print("Invalid Input")
