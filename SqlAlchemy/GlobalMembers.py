from typing import Any
import colorama,sys,os
from sqlalchemy import create_engine, Column, String, Integer, CHAR, DATE, update, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Contact(Base):
    __tablename__ = "Contacts"
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    mobile_num = Column("mobile_num", String, primary_key= True)
    tel = Column("tel", String)
    mail = Column("mail", String)
    site = Column("site", String)
    birthday = Column("birthday", String)

    def __init__(self, first_name, last_name, mobile_num, tel, mail, site, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_num = mobile_num
        self.tel = tel
        self.mail = mail
        self.site = site
        self.birthday = birthday

    def __repr__(self):
        return f"test"
        

engine = create_engine("sqlite:///./mydb.db", echo = False)
Base.metadata.create_all(bind = engine)
Session = sessionmaker(bind = engine)
session = Session()

def fetch():
    key = ''
    while key not in ["first_name","last_name","mobile_num","tel","mail","site","birthday"]:        
        key = input("Enter key for search (first_name, last_name, mobile_num, tel, mail, site, birthday): ")
    if key == "first_name" : q = session.query(Contact).filter(Contact.first_name == value).first()
    elif key == "last_name" : q = session.query(Contact).filter(Contact.last_name == value).first()
    elif key == "mobile_num" : q = session.query(Contact).filter(Contact.mobile_num == value).first()
    elif key == "tel" : q = session.query(Contact).filter(Contact.tel == value).first()
    elif key == "mail" : q = session.query(Contact).filter(Contact.mail == value).first()
    elif key == "site" : q = session.query(Contact).filter(Contact.site == value).first()
    elif key == "birthday" : q = session.query(Contact).filter(Contact.birthday == value).first()
    return q    
    
def main():
    while True:
        menu()
        new_value = input('order :')
        if new_value == '1':
            insert()
        if new_value == '2':
            delete()
        if new_value == '3':
            update()
        if new_value == '4':
            serch()
        if new_value == '5':
            display()
        if new_value == '0':    
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
    first_name = input("Enter first value : ")
    while len(first_name) <= 3 :
        print("first value must Greater than 4 Character")
        first_name = input("Enter first value : ")
    last_name = input("Enter last value: ")
    while len(last_name) <= 3 :
        print("last value must Greater than 4 Character")
        last_name = input("Enter last value : ")
    mobile_num = input("Enter mobile number : ")
    while len(mobile_num) <= 3 :
        print("mobile number must Greater than 4 Character")
        mobile_num = input("Enter mobile number : ").split(",")    
    tel = input("Enter tel number : ")
    while len(tel) <= 3 :
        print("tel must Greater than 4 Character")
        tel = input("Enter tel number : ")
    mail = input("Enter E-mail : ")
    while len(mail) <= 3 or '@' not in mail :
        print("please enter correct E-mail !!!")
        mail = input("Enter E-mail :")                
    site = input("Enter site :")
    while len(site) <= 3 or '.' not in mail :
        print("please enter correct site")
        site = input("Enter site :")
    birthday = input("Enter birthday :")
    while '/' not in birthday and '-' not in birthday :
        print("please enter correct birthday")
        birthday = input("Enter birthday :")
    session.add(Contact(first_name,
              last_name,
              mobile_num,
              tel,
              mail,
              site,
              birthday))
    session.commit()
    input('prosses finshed enter any key to continue...!')
 
def delete():
    print(colorama.Fore.CYAN,'serch',colorama.Fore.WHITE)
    q = fetch()
    if q is None:
        input('prosses finshed enter any key to continue...!')
        return
    print(f"{q.first_name , q.last_name} ",end=" informaion : ")
    print(f"""mobile_num : {q.mobile_num}
                tel : {q.tel}
                mail : {q.mail}
                site : {q.site}
                birthday : {q.birthday}
                """)
    key = input("do you wanna to delete this contacte [y/n]")
    if key.lower() == "y":
        session.delete(q)
        session.commit()
        print("Deleted.")    
        return
    input('prosses finshed enter any key to continue...!')    

def update():
    print(colorama.Fore.CYAN,'serch',colorama.Fore.WHITE)       
    q = fetch()
    if q is None:
        input('contact not found. enter any key to continue...!')    
        return
    print(f"{q.first_name , q.last_name} ",end=" informaion : ")
    print(f"""mobile_num : {q.mobile_num}
                tel : {q.tel}
                mail : {q.mail}
                site : {q.site}
                birthday : {q.birthday}
                """)
    key = input("do you wanna to update this contacte [y/n]:")    
    if key.lower() == "y":
        new_value = input(f"old first_name : [{q.first_name}] Entre new one or pass:")
        if not new_value == "pass":
            q.first_name = new_value
        new_value = input(f"old last_name : [{q.last_name}] Entre new one or pass:")
        if not new_value == "pass":
            q.last_name = new_value
        new_value = input(f"old mobile_num : {q.mobile_num} Entre new one or pass:")
        if not new_value == "pass":
            q.mobile_num = new_value
        new_value = input(f"old tel : {q.tel} Entre new one or pass:")
        if not new_value == "pass":
            q.tel = new_value
        new_value = input(f"old mail : {q.mail} Entre new one or pass:")
        if not new_value == "pass":
            q.mail = new_value
        new_value = input(f"old site : {q.site} Entre new one or pass:")
        if not new_value == "pass":
            q.site = new_value
        new_value = input(f"old birthday : [{q.birthday}] Entre new one or pass:")
        if not new_value == "pass":
            q.birthday = new_value
        session.commit()
        input('contact updated. enter any key to continue...!')
        return
    input('enter any key to continue...!')
    return
        
def search():
    print(colorama.Fore.CYAN,'serch',colorama.Fore.WHITE)
    q = fetch()
    print(f"{q.first_name , q.last_name} ",end=" informaion : ")
    print(f"""mobile_num : {q.mobile_num}
            tel : {q.tel}
            mail : {q.mail}
            site : {q.site}
            birthday : {q.birthday}
            """)
    input('enter any key to continue...!')
    return
    
def display ():
    print(colorama.Fore.CYAN,'display',colorama.Fore.WHITE)
    contacts = session.query(Contact).all()    
    for i in contacts:
        print(f"{i.first_name , i.last_name} ",end=" informaion : ")
        print(f"""mobile_num : {i.mobile_num}
              tel : {i.tel}
              mail : {i.mail}
              site : {i.site}
              birthday : {i.birthday}
              """)
    input('press any key to continue...')

if __name__ == '__main__':
    main()
