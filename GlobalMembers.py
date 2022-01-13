import colorama,sys,os,json

def main():
    global data
    while True:
        menu()
        x=input('order :')
        if x=='1':
            insert()
        if x=='2':
            delete()
        if x=='3':
            update()
        if x=='4':
            serch()
        if x=='5':
            try :
                display()
            except :
                print("Null")
        if x=='0':            
            flush()
            sys.exit(0)
def flush():
    global data
    with open("file.json", "w") as file:
        json.dump(data, file, indent=4)
def menu():
    global data
    os.system('cls')
    print(colorama.Fore.CYAN,'menu',colorama.Fore.WHITE)
    print('1)-insert')
    print('2)-delete')
    print('3)-update')
    print('4)-serch')
    print('5)-display')
    print('0)-exit')

def insert():
    global data
    print(colorama.Fore.CYAN,'insert',colorama.Fore.WHITE)
    global data
    frstname=input("Enter frstName :")
    lastname=input("Enter lastName :")
    phonenumber=input("Enter phoneNumber (for multi number use \",\" ) :").split(",")
    tel=input("Enter telPhone (for multi number use \",\" ) :").split(",")
    Email=input("Enter E-mail (for multi E-mail use \",\" ):").split(",")
    website=input("Enter webSite (for multi webSite use \",\" ) :").split(",")
    birthday=input("Enter birthDay :")

    k =[i for i in data.keys() if type(i) is int]
    if len(k)<1:
        k=0
    else:
        k=max(k)
        k+=1
    data[k]={"frstname":frstname,
             "lastname":lastname,
             "phoneNumber":phonenumber,
             "telphone":tel,
             "Email":Email,
             "website":website,
             "birthDay":birthday}
    flush()
def delete():
    global data
    print(colorama.Fore.CYAN,'delete',colorama.Fore.WHITE)
    name=input("Enter name :")
    for i in data.keys():
        if data[i]["frstname"]==name:
            print(f"{i} ",end=" informaion : ")
            print(data[i])
            k=input("do you wanna to delete this contacte [y/n]")
            if k.lower() == "y":
                del data[i]
                k=input("contacte deleted. do you wanna continue ? [y/n]")
                if k.lower() == "n":
                    break
            else:
                print(f"contacte {i} not deleted.")
    flush()
    input('prosses finshed enter any key to continue...!')
def update():
    global data
    print(colorama.Fore.CYAN,'update',colorama.Fore.WHITE)
    name=input("Enter name :")
    q=True
    for i in data.keys():
        if data[i]["frstname"]==name:
            q=False
            print(f"{i} -",end=" informaion : ")
            print(data[i])
            k=input("do you wanna to update this contacte [y/n]")
            if k.lower() == "y":
                x=input(f"old frstName : [{data[i]['frstname']}] Entre new one or pass")
                if not x=="pass":
                    data[i]["frstname"]=x
                x=input(f"old lastName : [{data[i]['lastname']}] Entre new one or pass")
                if not x=="pass":
                    data[i]["lastname"]=x
                x=input(f"old phoneNumber : {data[i]['phoneNumber']} Entre new one or pass")
                if not x=="pass":
                    data[i]["phoneNumber"]=x
                x=input(f"old telphone : {data[i]['telphone']} Entre new one or pass")
                if not x=="pass":
                    data[i]["telphone"]=x
                x=input(f"old Email : {data[i]['Email']} Entre new one or pass")
                if not x=="pass":
                    data[i]["Email"]=x
                x=input(f"old website : {data[i]['website']} Entre new one or pass")
                if not x=="pass":
                    data[i]["website"]=x
                x=input(f"old birthDay : [{data[i]['birthDay']}] Entre new one or pass")
                if not x=="pass":
                    data[i]["birthDay"]=x
    flush()
    if q:
        input('contacte updated. enter any key to continue...!')
    else:
        input('contacte not found. enter any key to continue...!')
def serch():
    global data
    print(colorama.Fore.CYAN,'serch',colorama.Fore.WHITE)
    ke=input("Enter key for search : ")
    if not ke in ["frstname","lastname","phoneNumber","telphone","Email","website","birthDay"]:
        input('key dosnt exiset ..!')
        return
    name=input(f"Enter {ke} : ")
    for i in data.keys():
        if data[i][ke]==name:
            print(f"pk-{i}-",end=" informaion : ")
            print(data[i])
    input('contacte updated. enter any key to continue...!')
def display ():
    global data
    print(colorama.Fore.CYAN,'display',colorama.Fore.WHITE)
    for i in data.keys():
        print(f"{i} ",end=" informaion : ")
        print(data[i])
    input('press any key to continue...')
if __name__ == '__main__':
    if os.path.exists("./file.json") :
        with open("file.json", "r") as file:
            try:
                data = json.load(file)
            except Exception as e:
                with open("file.json", "w") as file:
                    data = {}
    else:
        with open("file.json", "w") as file:
            pass
    main()