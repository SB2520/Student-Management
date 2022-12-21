def enrollment(): #enrollment
 
    while True:
        
        l=[]
        
        k=[]
        
        adm=input("admission no.-")
        
        l.append(adm)
        
        name=input("student name-")
        
        n=name.upper()
        
        l.append(n)
        
        c=input("class-")
        
        l.append(c)
        
        sec=input("section-")
        
        s=sec.upper()
        
        l.append(s)
        
        phone=input("phone number-")
        
        l.append(phone)
        
        attend=input("attendance-")
        
        l.append(attend)
        
        result=input("percentage of the student, in numeric value-")
        
        l.append(result)
        
        k.append(l)
        
        with open("STUDENTS.CSV","a") as s:
            
            sM=csv.writer(s)
            
            for i in k:
                
                sM.writerow(i)
                
                ch=input("want to add more (y/n)-")
                
            if ch=='N' or 'n':
                    
                 break
                    
def edit(): # edit
    
    with open("STUDENTS.CSV","r") as s:
        
        sM=csv.reader(s)
        
        for i in sM:
            
            if i[0]==row:
                
                change=int(input("what would you like to edit admission no.(0),students name(1),class(2),section(3), contact no.(4),attendance(5),result(6)"))
                
                l=[]
                
                with open("STUDENTS.CSV","r") as s :
                    
                    sM=csv.reader(s)
                    
                    for i in sM:
                        
                        if i[0]==row:
                            
                            new=input("new entry")
                            
                            k=i
                            
                            k[change]=new
                            
                            print("new record ",k)
                            
                            l.append(k)
                            
                            break
                            
                        else:
                            l.append(i)
                       
                    with open("STUDENTS.CSV","w") as s:
                        
                        sm=csv.writer(s)
                        
                        for i in l:
                            
                            sm.writerow(i)
                            
                    with open("STUDENTS.CSV","r") as s:
                        
                        sM=csv.reader(s)
                        
                        for i in sM:
                            
                            print(i)
                        break
                                                              
def delete(): #delete
    
    row=input("admission no. of the student whose record you want to delete ")
    
    t=[]
    
    with open("STUDENTS.CSV","r") as s :
        
        sM=csv.reader(s)
        
        for i in sM:
            
            if i[0]!=row:
                
                k=i
                
                t.append(k)
                
                with open("STUDENTS.CSV","w") as s:
                    
                    sm=csv.writer(s)
                    
                    for i in t:
                        
                        sm.writerow(i)
                        
                        with open("STUDENTS.CSV","r") as s:
                            
                            sM=csv.reader(s)
                            
                            for i in sM:
                                
                                print(i)
                                
 
def sort(): #sorting
 
     k=int(input("on what basis would you like to sort the data admn no.(0),name(1),class(2),section(3)"))
     
     l=[]
     
     with open("STUDENTS.CSV","r") as s:
        
        sM=csv.reader(s)
        
        for i in sM:
            
            l.append(i)
            
            n=len(l)
            
        for i in range(0,n-1):
            
                for j in range(0,n-i-1):
                    
                    if l[j][k]>l[j+1][k]:
                        
                        l[j],l[j+1]=l[j+1],l[j]
                        
        for i in range(1,len(l)):
                print(l[i])
                            
def search(): #search
 
    row=input("enter the admission no. of the record you are searching for")
    
    with open("STUDENTS.CSV","r") as s:
        
        sM=csv.reader(s)
        
        l=[]
        
        for i in sM:
            
            l.append(i) 
            
            for i in l:
                
                if i[0]==row:
                    
                    print(i)
                    
def attendance(): #attendance
 
    row=input("enter the admission no. of the record you are searching for")
    
    with open("STUDENTS.CSV","r") as s:
        
        sM=csv.reader(s)
        
        for i in sM:
            
            l=i
            
            if l[0]==row:
                
                print(i[5],"is the attendance of ",i[1],"out of 108 days")
                
                break
        
        else:
        
         print("invalid admission number")
                
def result(): #result
 
    row=input("enter the admission no. of the record you are searching for")
    
    with open("STUDENTS.CSV","r") as s:
        
        sM=csv.reader(s)
        
        for i in sM:
            
            l=i
            
            if l[0]==row:
                
                print(i[6],"% is the result of ",i[1])
                
                break
                
        else :
            
            print("invalid admission number")
                
def report(): #report
 
    x=int(input("which action would you like to perform, students below 80% attendance(1), students who are eligible for scholar badge(2)"))
    
    if x==1:
        
        with open("STUDENTS.CSV","r") as s:
            
            sM=csv.reader(s)
            
            for i in sM:
                
                L=i
                
                if L[0]=='Admission number':
                    
                    f=1
                    
                elif int(L[5])<85:
                    
                    print(L)
    elif x==2:
        
        with open ("STUDENTS.CSV",'r') as s:
            
            sM=csv.reader(s)
            
            for i in sM:
                
                L=i
                
                if L[0]=='Admission number':
                    
                    f=1
                    
                elif int(L[6])>89:
                    
                    print(L)
                    
                else:
                    print("invalid option")
                    
import csv
 
with open("STUDENTS.CSV","a") as s: #by default entries
 
     sM=csv.writer(s)
     
     sM.writerow(["Admission number","Student Name","Class","Section","Contact no.","Attendance out of 108 days","result(%)"])
     
     sM.writerow(["54135","ABC","12","A","875421"," 102 ","90"])
     
     sM.writerow(["52143","BCD","12","B","821345","95 ","83"])
     
     sM.writerow(["54631","CDE","11","D","953214","106 ","92"])
     
     sM.writerow(["52114","DEF","9","C","841727"," 82","75"])
     
user=input("admin or service-") #admin or service portal
 
l=user.lower()
 
while l not in ("admin","service"):
    
    k=input("invalid option re enter - ")
    
    l=k.lower()
    
if l== "admin" :
    
    password=int(input("what is the password-")) #password
    
    while password!=1234:
        
        password=int(input("wrong password, re-enter-"))
        
    else:
        
         while True:
            
            t=input("which task would you like to perform (student enrollment(1),editing(2),deletion(3),quit(4)) enter the no. of the task-")#option selection
            
            while t not in ('1','2','3','4'):
                
                t=input("invalid option re enter")
                
            else:
                
                if t=="1":
                    
                    enrollment()
                    
                elif t=="2":
                    
                    row=input("enter the admission number you want to edit")
                    
                    with open("STUDENTS.CSV",'r') as s:
                        
                        sM=csv.reader(s)
                        
                        for i in sM:
                            
                            if i[0]==row:
                                
                                edit()
                                
                                break
                        else:
                            print("record not found")
                    
                    
                elif t=='3':
                    
                    delete()
                    
                elif t=='4':
                    
                    print("thank you") #quit
                    
                    break
                    
elif l=="service":
    
    while True:
        
            t=input("which task would you like to perform (display(1),sorting(2),searching(3),attendance(4),result(5),report(6),quit(7)) enter the no. of the task") #service portal
            
            while t not in ('1','2','3','4','5','6','7'):
                
                t=input("invalid option re enter")
                
            else:
                
                if t=="1": #display
                
                    with open("STUDENTS.CSV","r") as s:
                        
                        sM=csv.reader(s)
 
                        for i in sM:
                       
                           print(i)
                            
                    print("thank you")
                        
                elif t=="2": #sorting
                
                    sort()
                    
                elif t=="3": #searching
                
                    search()
                    
                elif t=="4": #attendanfe
                
                    attendance()
                    
                elif t=="5": #result
                
                    result()
                    
                elif t=="6": #report
                
                    report()
                    
                elif t=="7": # quit
                
                    print("thank you")
                    
                    break
