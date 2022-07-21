dict_student_detail = dict()
temp = 1
dict1 = dict()
# name, no,marks (5)
status = True
while status:
    menu = input('''
    Menu:
    1)  Add Student
    2)  Update Student Details
    3)  Remove Student
    4)  Search Student
    5)  Dispaly All Student
    6)  Dispaly Highest Percentage Wise Student List
    7)  Display Lowest Percentafe Wise Student List
    8)  Display Highest Student Name
    9)  Display Lowest Student Name
    10) Add Fees

    ''')
    # name, no,marks (5)
    while True:
        if menu.isdigit():
            menu = int(menu)
            break
        else:
            menu = input('''
                Menu:
                1)  Add Student
                2)  Update Student Details
                3)  Remove Student
                4)  Search Student
                5)  Dispaly All Student
                6)  Dispaly Highest Percentage Wise Student List
                7)  Display Lowest Percentafe Wise Student List
                8)  Display Highest Student Name
                9)  Display Lowest Student Name
                10) Add Fees
                Enter in number format only: 
                ''')
        print(menu)
        # while True:
        #     if menu == 1:
        #         name = input("Enter Student Name: ")
        #         while True:
        #             if name.isalpha():
        #                 break
        #             else:
        #                 name = input("Enter Student Name in valid format: ")
        #         dict_student_detail['Name'] = name
        #         no = input("Enter Students Number: ")
        #         while True:
        #             if no.isdigit() and len(no) == 10:
        #                 break
        #             else:
        #                 no = input("Enter Students Number: ")
        #         dict_student_detail['Number'] = no
        #         for i in range(1,5):
        #             a = int(input(f"Enter marks {i}: "))
        #             dict_student_detail[f'Marks-{i}'] = a
        #         dict1[temp] = dict_student_detail
        #         temp += 1
        #         choice = input("Do you want to add more students \'y\' for Yes and \'n\' for no: ").lower()
        #         if choice == 'y':
        #             continue
        #         else:
        #             break
        #     elif menu == 2:
        #         get_value = input("Enter Student Name: ")
        #         for i in dict1.values():
        #             if i.values() == get_value:
        #                 print(i)
        #             else:
        #                 print("Invalid Name: ")
                

