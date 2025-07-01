class Student:
    def __init__(self, name, rollno, mark):
        self.name = name
        self.rollno = rollno
        self.mark = mark
        
    def display_info(self):  # self is needed here
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.mark)
        
    def is_passed(self):  # self is needed here
        if self.mark >= 50:
            print("Result: Passed")
        else:
            print("Result: Not Passed")
            

s1 = Student("Asha", 101, 73)
s1.display_info()
s1.is_passed()
