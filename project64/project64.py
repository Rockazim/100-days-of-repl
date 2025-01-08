"""Create a generic 'job' class.
The init method will store the details for name, salary and hours worked.
'job' will have another method that prints those details nicely.
Create two sub-classes from job: 'doctor' and 'teacher'
The 'doctor' subclass should also include 'speciality' and 'years of experience'.
The 'teacher' subclass should also include 'subject' and 'position'.
The print functions for each sub-class should print this extra data.
Instantiate a lawyer, a computer science teacher, and a pediatric doctor (this is a doctor for children) with 7 years of experience.
Output the information for each job."""




class job:
    name = None
    salary = None
    hoursWorked = None

    def __init__(self, name, salary, hoursWorked):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked

    def print(self):
        print(f"Job type: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hoursWorked}")


class doctor(job):
    experience = None
    speciality = None
    
    def __init__(self, salary, hoursWorked, speciality, experience):
        self.name = "Doctor"
        self.salary = salary
        self.hoursWorked = hoursWorked
        self.speciality = speciality
        self.experience = experience
    
    def print(self):
        print(f"Job type: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hoursWorked}\nSpeciality: {self.speciality}\nYears of Experience: {self.experience}")

class teacher(job):
    subject = None
    position = None
    
    def __init__(self, salary, hoursWorked, subject, position):
        self.name = "Teacher"
        self.salary = salary
        self.hoursWorked = hoursWorked
        self.subject = subject
        self.position = position
    
    def print(self):
        print(f"Job type: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hoursWorked}\nPosition: {self.position}\nSubject: {self.subject}")

lawyer = job("lawyer", 69400, 10)
lawyer.print()
print()
doctor = doctor(100000,5,"Consultant", "7 months")
doctor.print()
print()
teacher = teacher(5,1000,"Gender Studies", "Principal")
teacher.print()