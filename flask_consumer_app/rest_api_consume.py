
import requests

ADDRESS_BASE_URI = 'http://localhost:8000/api/v1/address/'
STUDENT_BASE_URI = 'http://localhost:8000/api/v1/student/'


class Student:
    def __init__(self,id,nm,ag,em,fs,dt,adr):
        self.id=id
        self.studname=nm
        self.studage=ag
        self.studemail=em
        self.studfees=fs
        self.studdept=dt
        self.studAddress=adr
    def __str__(self):
        return f'''
        StudId : {self.id}
        StudName : {self.studname}
        StudAge : {self.studage}
        StudEmail : {self.studemail}
        StudFees : {self.studfees}
        StudDept : {self.studdept}
        StudAddress : {self.studAddress}
        '''

    def __repr__(self):
        return str(self)


class Address:

    def __init__(self,aid,city,st,pin):
        self.id=aid
        self.city=city
        self.state=st
        self.pincode=pin

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
            AID : {self.id}
            CITY : {self.city}
            STATE : {self.state}
            PINCODE : {self.pincode}
        '''

def get_all_addresses():
    response = requests.get(ADDRESS_BASE_URI)
    print(response.json())
    return response.json()

def get_single_addresses(aid):
    response = requests.get(ADDRESS_BASE_URI+str(aid)+'/')

    if response.status_code==204:
        print('No records found..!')
    else:
        print(response.json())
        return response.json()


def create_address(address):
    addressJson = {
          "city": address.city,
          "pincode": address.pincode,
          "state": address.state
        }
    response = requests.post(ADDRESS_BASE_URI,json=addressJson)
    print(response.status_code)
    print(response.json())
    return response.json()

def update_address(address):
    addressJson = {
          "city": address.city,
          "pincode": address.pincode,
          "state": address.state
        }
    response = requests.put(ADDRESS_BASE_URI+str(address.id)+'/',json=addressJson)
    print(response.status_code)
    print(response.json())
    return response.json()


def delete_address(adrid):
    response = requests.delete(ADDRESS_BASE_URI+str(adrid)+'/')
    print(response.status_code)
    if response.status_code==204:
        print('Record removed Successfully...!')
    else:
        print('Record Not Found..')


    #print(response.json())
    #return response.json()

def create_student(st):
    address =st.studAddress
    addressJson = {
        "id" : address.id,
        "city": address.city,
        "pincode": address.pincode,
        "state": address.state
    }

    studJson = {
          "studname": st.studname,
          "studage": st.studage,
          "studemail": st.studemail,
          "studfees": st.studfees,
          "studdept": st.studdept,
          "studAddress": addressJson["id"]
        }

    print(studJson)
    response = requests.post(STUDENT_BASE_URI,json=studJson)
    print(response.status_code)
    print(response.json())
    return response.json()

if __name__ == '__main__':
    ad1 = Address(aid=3,city='XXXXX',st='MHHH',pin=288282)
    st = Student(id=1111,nm='AAAA',ag=23,em='abc@gmail.commm',fs=9383.34,dt='CSE',adr=ad1)
    create_student(st)
   #update_address(ad)
    #delete_address(1)