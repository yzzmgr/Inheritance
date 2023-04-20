import sys
from student import *
from teacher import *

students = []
teachers = []


def addStudents():

    while True:

        print()
        print('T = Add Teacher')
        print('S = Add Student')
        print()

        add = input('What do you want to add? ')
        add = add.upper()

        print()

        if add == 'S':

            id = input('Enter id: ')
            lastName = input('Enter last name: ')
            firstName = input('Enter first name: ')
            middleName = input('Enter middle name: ')
            type = input('Enter type: ')
            course = input('Enter Course: ')
            year = input('Enter year: ')
            section = input('Enter section: ')
            print('----------------------------')
            filipino = int(input('Grade filipino: '))
            math = int(input('Grade math: '))
            science = int(input('Grade science: '))
            english = int(input('Grade english: '))

            stud = Grade(filipino, math, science, english)
            stud.id = id
            stud.lastName = lastName
            stud.firstName = firstName
            stud.middleName = middleName
            stud.type = type
            stud.course = course
            stud.year = year
            stud.section = section

            students.append(stud)


        elif add == 'T':

            id = input('Enter id: ')
            lastName = input('Enter last name: ')
            firstName = input('Enter first name: ')
            middleName = input('Enter middle name: ')
            type = input('Enter type: ')
            print('----------------------------')
            department = input('Enter Department: ')
            position = input('Enter Position: ')
            subject = input('Enter Subject: ')

            tch = Load(subject)
            tch.department = department
            tch.position = position
            tch.id = id
            tch.lastName = lastName
            tch.firstName = firstName
            tch.middleName = middleName
            tch.type = type

            teachers.append(tch)


        else:
            menu()

        print()
        ans = input('Enter another? [y/n]: ')
        ans = ans.lower()

        if (ans != 'y'):
            break


        menu()

def deleteRecord():

    print()
    print('T = Delete from Teacher')
    print('S - Delete from Student')
    print('DT - Delete Teachers')
    print('DS - Delete Students')
    print('CLR - Delete All')
    print()

    delete = input('What do you want to delete? ')
    delete = delete.upper()

    if delete == 'S':
        i = int(input('Enter index: '))
        students.pop(i)

    elif delete == 'T':
        i = int(input('Enter index: '))
        teachers.pop(i)

    elif delete == 'DT':
        teachers.clear()

    elif delete == 'DS':
        students.clear()

    elif delete == 'CLR':
        students.clear()
        teachers.clear()

    else:
        deleteRecord()


    menu()



def searchRecord():

    print()
    print('T - Search Teacher')
    print('S - Search Student')
    print()

    search = input('Type do you want to search? ')
    search = search.upper()

    if search == 'S':


        i = int(input('Enter index: '))

        print(f'{i} \t | {students[i].getType()} \t | {students[i].getName()} \t | {students[i].getID()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')

    elif search == 'T':
        i = int(input('Enter index: '))
        print(f'{i} \t | {teachers[i].getType()} \t | {teachers[i].getName()} \t | {teachers[i].getID()} \t | {teachers[i].getDepPos()} \t | {teachers[i].getSub()}')

    else:
        searchRecord()

    menu()




def displayRecords():

    print()
    print('T - Display Teacher')
    print('S - Display Student')
    print('A - Display All')
    print()

    display = input('What do you want to display?: ')
    display = display.upper()

    if display == 'S':
        print()
        print('----------------------------------------------------------------------------------')
        i = 0
        for s in students:
            print(f'{i} \t | {s.getType()} \t | {s.getName()} \t | {s.getID()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
            i += 1
        print('----------------------------------------------------------------------------------')

    elif display == 'T':
        print()
        print('----------------------------------------------------------------------------------')
        i = 0
        for t in teachers:
            print(f'{i} \t | {t.getType()} \t | {t.getName()} \t | {t.getID()} \t | {t.getDepPos()} \t | {t.getSub()}')
            i += 1
        print('----------------------------------------------------------------------------------')

    elif display == 'A':
        print()
        print('----------------------------------------------------------------------------------')

        i = 0
        for s in students:
            print(f'{i} \t | {s.getType()} \t | {s.getName()} \t | {s.getID()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
            i += 1

       
        i = 0
        for t in teachers:
            print(f'{i} \t | {t.getType()} \t | {t.getName()} \t | {t.getID()} \t | {t.getDepPos()} \t | {t.getSub()}')
            i += 1
        print('----------------------------------------------------------------------------------')


    else:
        displayRecords()

    menu()




def menu():

    print()
    print()
    print('::Menu::')
    print('D - delete record        S - search record')
    print('A - add record           M - display all')
    print()

    choice = input('Enter a function: ')
    choice = choice.upper()

    if (choice == 'D'):
        deleteRecord()
    elif (choice == 'A'):
        addStudents()
    elif(choice == 'S'):
        searchRecord()
    elif (choice == 'M'):
        displayRecords()
    else:
        menu()


    print()

menu()