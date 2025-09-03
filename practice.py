# class book:
#     def book_details(self):
#         self.title = input("Enter book title: ")
#         self.author = input("Enter book author: ")
#         self.availability = input("Is the book available? (yes/no): ")
#     def display_details(self):
# #         print(f"Title: {self.title}, Author: {self.author}, Availability: {self.availability}")
# # ob=book()
# # ob.book_details()
# # ob.display_details()

class student:
    def student_details(self):
        self.name = input("Enter student name: ")
        self.age = int(input("Enter student age: "))
        self.grade = input("Enter student grade: ")
        self.marks=[]
        for i in range(3):
            mark = int(input(f"Enter mark {i+1}: "))
            self.marks.append(mark)
    def average(self):
        self.average_marks= sum(self.marks) / len(self.marks)    

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Average Marks: {self.average_marks:.2f}")
ob = student()
ob.student_details()
ob.average()
ob.display_details()
