class Person:
    # Protected members
    _mobile: str = ""

    __email: str = ""

    no_of_person: int = 0

    name: str = ""

    occupation: str = ""

    @classmethod
    def get_no_of_person(cls):
        print(f"There are {cls.no_of_person} person created.")

    def __init__(self, name, occupation, mobile, email) -> None:
        self.name = name
        self.occupation = occupation
        self._mobile = mobile
        self.__email = email
        Person.no_of_person += 1

    def _protected_method(self):
        print("Accessing Protected Member : ", self._mobile)

    def __private_email_method(self):
        print("Accessing Private Member : ", self.__email)

    def access_private_method(self):
        self.__private_email_method()

    def work(self):
        print(f"{self.name} is Working")

    @property
    def email(self):
        return self.__email

    def introduce(self):
        print(
            f"Name : {self.name}\nOccupation : {self.occupation}\nMobile : {self._mobile}\nEmail : {self.__email}"
        )

    @staticmethod
    def isPersonAdult(age):
        return age >= 18


p1 = Person("aakash", "developer", "9898989898", "aakash@mail.com")


class Student(Person):

    __student_id: str = ""

    _div: int = 0

    def __init__(self, name, occupation, mobile, email, student_id="", div=0) -> None:
        super().__init__(name, occupation, mobile, email)
        self.__student_id = student_id
        self._div = div

    @property
    def student_id(self):
        return self.__student_id

    def introduce(self):
        print(
            f"Name : {self.name}\nOccupation : {self.occupation}\nMobile : {self._mobile}\nEmail : {self.email}\nStudent_Id : {self.__student_id}\nDiv : {self._div}"
        )


class Human:
    def breathing(self):
        print("Breathing")

    def eating(self):
        print("eating")

    def walking(self):
        print("walking")


class Developer(Student, Human):
    __dev_experience: int = 0

    def __init__(
        self,
        name: str,
        occupation: str,
        mobile: str,
        email: str,
        experience: int,
        technology: str,
    ) -> None:
        super().__init__(name, occupation, mobile, email)
        self.__dev_experience = experience
        self.technology = technology

    def introduce(self):
        print(
            f"Hello I am {self.occupation}\nMy Name is {self.name}\nMobile : {self._mobile}\nEmail : {self.email}\nMy Favourite Technology is {self.technology}\nI have {self.__dev_experience} yrs of experience"
        )

    def develope_app(self, app_name):
        print(f"Hey I am developing an {app_name}")


# calling protected method
p1._protected_method()

p1.introduce()

print("-----------------------------------")

s1 = Student(
    "Pratham", "Junior Assistant", "8855746541", "pratham@gmail.com", "pra114", 12
)

s1.introduce()

print("-----------------------------------")

d1 = Developer("bharat", "coder", "7547454568", "bharat@gmail.com", 2, ".Net")

d1.introduce()

d1.develope_app("Food Ordering Website ...")

print("----------------------------------")

Person.get_no_of_person()
