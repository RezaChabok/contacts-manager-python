from typing import Any
import colorama,sys,os
from sqlalchemy import create_engine, Column, String, Integer, CHAR, DATE, update, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Contact(Base):
    __tablename__ = "Contacts"


    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    phonenumber = Column("phonenumber", String, primary_key= True)
    tel = Column("tel", String)
    Email = Column("mail", String)
    website = Column("website", String)
    birthday = Column("birthday", String)

    def __init__(self, firstname, lastname, phonenumber, tel, Email, website, birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.tel = tel
        self.Email = Email
        self.website = website
        self.birthday = birthday

    def __repr__(self):
        return f"test"


engine = create_engine("sqlite:///./mydb.db", echo = False)
Base.metadata.create_all(bind = engine)
Session = sessionmaker(bind = engine)
session = Session()
results = session.query(Contact).all()

def main():
    global data
    while True:
        menu()
        x = input('order :')
        if x == '1':
            insert()
        if x == '2':
            delete()
        if x == '3':
            update()
        if x == '4':
            serch()
        if x == '5':
            try :
                display()
            except :
                print("Null")
        if x == '0':    
            sys.exit(0)

def menu():
    os.system('cls')

    print(colorama.Fore.CYAN,'menu',colorama.Fore.WHITE)

    print('1)-insert')

    print('2)-delete')

    print('3)-update')

    print('4)-serch')

    print('5)-display')

    print('0)-exit')


def insert():

    print(colorama.Fore.CYAN,'insert',colorama.Fore.WHITE)

    firstname = input("Enter firstName :")
    while len(firstname) <= 3 :
        print("firstname must Greater than 4 Character")
        firstname = input("Enter firstName :")
        
    lastname = input("Enter lastName :")
    while len(lastname) <= 3 :
        print("lastname must Greater than 4 Character")
        lastname = input("Enter lastName :")

        
    phonenumber = input("Enter phoneNumber :")
    while len(phonenumber) <= 3 :
        print("phonenumber must Greater than 4 Character")
        phonenumber = input("Enter phoneNumber :").split(",")    


    tel = input("Enter telPhone :")
    while len(tel) <= 3 :
        print("telphone must Greater than 4 Character")
        tel = input("Enter telPhone :")


    Email = input("Enter E-mail :")
    while len(Email) <= 3 or '@' not in Email :
        print("please enter correct mail")
        Email = input("Enter E-mail :")
        
        
    website = input("Enter webSite :")
    while len(website) <= 3 or '.' not in Email :
        print("please enter correct website")
        website = input("Enter webSite :")



    birthday = input("Enter birthDay :")
    while '/' not in birthday and '-' not in birthday :
        print("please enter correct birthday")
        birthday = input("Enter birthDay :")


    session.add(Contact(firstname,
              lastname,
              phonenumber,
              tel,
              Email,
              website,
              birthday))
    session.commit()

    input('prosses finshed enter any key to continue...!')
 
def delete():
    print(colorama.Fore.CYAN,'serch',colorama.Fore.WHITE)
    ke = input("Enter key for search ( firstname, lastname, phoneNumber, telphone, Email, website, birthDay): ")
    if not ke in ["firstname","lastname","phoneNumber","telphone","Email","website","birthDay"]:
        input('key dosnt exiset ..!')
        return    
    name = input(f"Enter {ke} : ")

    
    if ke == "firstname" : q = session.query(Contact).filter(Contact.firstname == name).first()
    elif ke == "lastname" : q = session.query(Contact).filter(Contact.lastname == name).first()
    elif ke == "phoneNumber" : q = session.query(Contact).filter(Contact.phonenumber == name).first()
    elif ke == "telphone" : q = session.query(Contact).filter(Contact.tel == name).first()
    elif ke == "Email" : q = session.query(Contact).filter(Contact.Email == name).first()
    elif ke == "website" : q = session.query(Contact).filter(Contact.website == name).first()
    elif ke == "birthDay" : q = session.query(Contact).filter(Contact.birthday == name).first()
    if q is not None:
        print(f"{q.firstname , q.lastname} ",end=" informaion : ")
        print(f"""phonenumber : {q.phonenumber}
                tel : {q.tel}
                Email : {q.Email}
                website : {q.website}
                birthday : {q.birthday}
                """)
        k = input("do you wanna to delete this contacte [y/n]")

        if k.lower() == "y":
            session.delete(q)
            session.commit()

    input('prosses finshed enter any key to continue...!')


def update():
    print(colorama.Fore.CYAN,'serch',colorama.Fore.WHITE)

    ke = input("Enter key for search ( firstname, lastname, phoneNumber, telphone, Email, website, birthDay): ")

    if not ke in ["firstname","lastname","phoneNumber","telphone","Email","website","birthDay"]:

        input('key dosnt exiset ..!')

        return
    
    name = input(f"Enter {ke} : ")
    
    if ke == "firstname" : q = session.query(Contact).filter(Contact.firstname == name).first()
    elif ke == "lastname" : q = session.query(Contact).filter(Contact.lastname == name).first()
    elif ke == "phoneNumber" : q = session.query(Contact).filter(Contact.phonenumber == name).first()
    elif ke == "telphone" : q = session.query(Contact).filter(Contact.tel == name).first()
    elif ke == "Email" : q = session.query(Contact).filter(Contact.Email == name).first()
    elif ke == "website" : q = session.query(Contact).filter(Contact.website == name).first()
    elif ke == "birthDay" : q = session.query(Contact).filter(Contact.birthday == name).first()
    if q is not None:
        print(f"{q.firstname , q.lastname} ",end=" informaion : ")
        print(f"""phonenumber : {q.phonenumber}
                tel : {q.tel}
                Email : {q.Email}
                website : {q.website}
                birthday : {q.birthday}
                """)
        k = input("do you wanna to update this contacte [y/n]:")

        if k.lower() == "y":

            x = input(f"old firstName : [{q.firstname}] Entre new one or pass:")

            if not x == "pass":
                q.firstname = x

            x = input(f"old lastName : [{q.lastname}] Entre new one or pass:")

            if not x == "pass":
                q.lastname = x

            x = input(f"old phoneNumber : {q.phonenumber} Entre new one or pass:")

            if not x == "pass":
                q.phonenumber = x

            x = input(f"old telphone : {q.tel} Entre new one or pass:")

            if not x == "pass":
                q.tel = x

            x = input(f"old Email : {q.Email} Entre new one or pass:")

            if not x == "pass":
                q.Email = x

            x = input(f"old website : {q.website} Entre new one or pass:")

            if not x == "pass":
                q.website = x

            x = input(f"old birthDay : [{q.birthday}] Entre new one or pass:")

            if not x == "pass":
                q.birthday = x

            session.commit()
            input('contact updated. enter any key to continue...!')
        else:
            input('enter any key to continue...!')
    else:
        input('contact not found. enter any key to continue...!')

        
def serch():
    print(colorama.Fore.CYAN,'serch',colorama.Fore.WHITE)

    ke = input("Enter key for search ( firstname, lastname, phoneNumber, telphone, Email, website, birthDay): ")

    if not ke in ["firstname","lastname","phoneNumber","telphone","Email","website","birthDay"]:

        input('key dosnt exiset ..!')

        return
    name = input(f"Enter {ke} : ")
    
    if ke == "firstname" : q = session.query(Contact).filter(Contact.firstname == name).first()
    elif ke == "lastname" : q = session.query(Contact).filter(Contact.lastname == name).first()
    elif ke == "phoneNumber" : q = session.query(Contact).filter(Contact.phonenumber == name).first()
    elif ke == "telphone" : q = session.query(Contact).filter(Contact.tel == name).first()
    elif ke == "Email" : q = session.query(Contact).filter(Contact.Email == name).first()
    elif ke == "website" : q = session.query(Contact).filter(Contact.website == name).first()
    elif ke == "birthDay" : q = session.query(Contact).filter(Contact.birthday == name).first()
    
    print(f"{q.firstname , q.lastname} ",end=" informaion : ")
    print(f"""phonenumber : {q.phonenumber}
            tel : {q.tel}
            Email : {q.Email}
            website : {q.website}
            birthday : {q.birthday}
            """)

    input('enter any key to continue...!')

    
def display ():
    print(colorama.Fore.CYAN,'display',colorama.Fore.WHITE)
    results = session.query(Contact).all()

    
    for i in results:
        print(f"{i.firstname , i.lastname} ",end=" informaion : ")
        print(f"""phonenumber : {i.phonenumber}
              tel : {i.tel}
              Email : {i.Email}
              website : {i.website}
              birthday : {i.birthday}
              """)

    input('press any key to continue...')


if __name__ == '__main__':
    main()

