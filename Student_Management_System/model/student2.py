class student2:
    def __init__(self, roll,name,gender,dob,stu_class,email,contact,country,city,address):
        self.__roll=roll
        self.__name=name
        self.__gender=gender
        self.__dob=dob
        self.__stu_class=stu_class
        self.__email = email
        self.__contact=contact
        self.__country=country
        self.__city=city
        self.__address=address

    def set_roll(self, roll):
        self.__roll = roll
    def get_roll(self):
        return self.__roll

    def set_name(self, name):
        self.__name =name
    def get_name(self):
        return self.__name

    def set_gender(self, gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender

    def set_dob(self, dob):
        self.__dob =dob
    def get_dob(self):
        return self.__dob

    def set_stu_class(self, stu_class):
        self.__stu_class =stu_class
    def get_stu_class(self):
        return self.__stu_class

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_contact(self, contact):
        self.__contact = contact
    def get_contact(self):
        return self.__contact

    def set_country(self, country):
        self.__country = country
    def get_country(self):
        return self.__country

    def set_city(self, city):
        self.__city = city
    def get_city(self):
        return self.__city

    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.__address

