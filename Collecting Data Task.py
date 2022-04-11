''' Week 9 Collecting Data Task '''

from tkinter import *

class Person:
    def __init__(self, first_name, last_name, age, has_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.has_phone = has_phone

class Main:
    def __init__(self, root, PEOPLE_DATA = []):
        self.people_data = PEOPLE_DATA
        self.root = root
        self.main_frame = Frame(root)
        self.meme_frame = Frame(root)
        self.main_frame.grid()

        self.show_btn = Button(self.main_frame, text = "Show All", command = self.show_all)
        self.show_btn.grid(row = 0, column = 3)

        name_label = Label(self.main_frame, text = "First Name:")
        lastname_label = Label(self.main_frame, text = "Last Name")
        age_label = Label(self.main_frame, text = "Age")
        name_label.grid(row = 0, column = 1)
        lastname_label.grid(row = 1, column = 1)
        age_label.grid(row = 2, column = 1)

        self.e1 = Entry(self.main_frame)
        self.e2 = Entry(self.main_frame)
        self.e3 = Entry(self.main_frame)
        self.e1.grid(row = 0, column = 2)
        self.e2.grid(row = 1, column = 2)
        self.e3.grid(row = 2, column = 2)

        mobile_label = Label(self.main_frame, text = "Does the User have a Mobile Phone?")
        mobile_label.grid(row = 3, column = 2)

        self.rd = StringVar()
        self.rd.set("?")
        self.rd1 = Radiobutton(self.main_frame, text = "Yes", value = "Yes", variable = self.rd)
        self.rd2 = Radiobutton(self.main_frame, text = "No", value = "No", variable = self.rd)
        self.rd1.grid(row = 3, column = 3)
        self.rd2.grid(row = 4, column = 3)

        self.enter_btn = Button(self.main_frame, text = "Enter Data", command = self.enter_data)
        self.enter_btn.grid(row = 5, column = 2)
    
    def enter_data(self):
        file = open("data.txt", "a")
        file.write("-" * 50)
        file.write(f"\nFirst Name: {self.e1.get()} \nLast Name: {self.e2.get()} \nAge: {self.e3.get()} \nHas Phone: {self.rd.get()}\n")

        self.people_data.append(Person(self.e1.get(), self.e2.get(), self.e3.get(), self.rd.get()))
        self.main_frame.destroy()
        ShowData(root, self.people_data)

    def show_all(self):
        self.main_frame.destroy()
        self.meme_frame.grid()

        label = Label(self.meme_frame, text = "Check The data.txt file :))", font = 15)
        label.grid()

        back = Button(self.meme_frame, text = "Back", command = self.back)
        back.grid(row = 0, column = 3)

    def back(self):
        self.meme_frame.destroy()
        Main(root)

class ShowData:
    def __init__(self, root, PEOPLE_DATA):
        self.people_data = PEOPLE_DATA
        self.root = root
        self.win2_frame = Frame(root)
        self.win2_frame.grid()

        for person in PEOPLE_DATA:
            self.root_frame = Frame(self.win2_frame)
            self.root_frame.grid(column = 0)
            
            first_name = Label(self.root_frame, text = "First Name:")
            last_name = Label(self.root_frame, text = "Last Name:")
            age = Label(self.root_frame, text = "Age:")
            phone = Label(self.root_frame, text = "Has A Phone:")
            
            display_first = Label(self.root_frame, text = person.first_name)
            display_second = Label(self.root_frame, text = person.last_name)
            display_third = Label(self.root_frame, text = person.age)
            display_fourth = Label(self.root_frame, text = f"{person.has_phone}")
            filler_label = Label()

            first_name.grid(row = 0, column = 1)
            last_name.grid(row = 1, column = 1)
            age.grid(row = 2, column = 1)
            phone.grid(row = 3, column = 1)

            display_first.grid(row = 0, column = 2)
            display_second.grid(row = 1, column = 2)
            display_third.grid(row = 2, column = 2)
            display_fourth.grid(row = 3, column = 2)
            filler_label.grid(row = 4, column = 2)

        self.add = Button(self.win2_frame, text = "Add Person", command = self.add_person)
        self.add.grid(row = 0, column = 3)

    def add_person(self):
        self.win2_frame.destroy()
        self.root_frame.destroy()
        Main(root)

if __name__ == "__main__":
    root = Tk()
    root.title("Collecting Data")
    Main(root)
    root.mainloop()