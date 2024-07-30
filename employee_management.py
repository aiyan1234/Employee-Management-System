import time
import random
import sys
sin_det={}
all_det={}
sp={}
ap={}

q = ["MTech", "MSC", 'MBA', "BTech", "BCS", "Diploma"]
sk = ["C", "C++", "Java", "Python", "Sql", "Web development", "Oracle", "Javascript", "C#", "Cloud Computing", "R", "No"]
desg1 = ["Manager", "Software Developer", "Web developer", "Data Analyst", "AI Engineer", "Game Developer", "Cloud Engineer", "Intern"]
sal = {"Manager": 100000, "Software Developer": 70000, "Web developer": 50000, "Data Analyst": 60000, "Cloud Engineer": 80000, "Game Developer": 75000,"AI Engineer":90000, "Intern": 20000}
def applicant():
    global name, age, em_id, cont_num, qual, skill, exp,expy
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    em_id = input("Enter your e-mail id: ")
    cont_num = int(input("Enter your contact number: "))
    qual = input("enter Qualification: ")
    skill = input("enter skills if not enter No: ")
    while True:
        exp = input("Do you have any Work Experience then enter Yes/No: ")
        if exp.lower() == "yes":
            expy = int(input("how many years of experience do you have??: "))
            print("thank you your information is recorded will be responded soon........")
            time.sleep(5)
            selection()
            break
        elif exp.lower() == "no":
            expy=int(input("enter zero if no expirence: "))
            print("thank you your information is recorded will be responded soon...........")
            time.sleep(5)
            selection()
            break
        else:
            print("reenter the as Yes/No")
def selection():
    global flag,desg,sal
    if qual.lower() in [q_item.lower() or q_item.upper() for q_item in q]:
        if skill.lower() or skill.upper() in [sk_item.lower() or sk_item.upper() for sk_item in sk]:
            if expy >= 10:
                flag=True
                desg="Manager"
                sal=100000
                print("You have been appointed as Manager role")
               
            elif 3 < expy <= 9:
                flag=True
                desg="Software Developer"
                sal=70000
                print("You have been appointed as Software Developer")
               
            elif 0<expy<=3 and   skill.lower() == "web development" :
                flag=True
                desg="Web Developer"
                sal=50000
                print("You have been appointed as Web Developer")
            elif 0<expy<=3 and skill.lower() in ["java", "python", "r"]:
                flag=True
                desg="AI Engineer"
                sal=90000
                print("You have been appointed as AI Engineer")
            elif 0<expy<=3 and skill.lower() == "web developer":
                flag=True
                desg="Web Developer"
                sal= 50000
                print("You have been appointed as Web Developer")
            elif 0<expy<=3 and skill.lower() in ["c", "c#", "javascript", "c++"]:
                flag=True
                desg="Game Developer"
                sal=75000
                print("You have been appointed as Game Developer")
            elif 0<expy<=3 and skill.lower() in ["sql", "oracle"]:
                flag=True
                desg="Data Analyst"
                sal= 60000
                print("You have been appointed as Data Analyst")
            elif 0<expy<=3 and skill.lower() == "cloud computing":
                flag=True
                desg="Cloud Engineer"
                sal=80000
                print("You have been appointed as Cloud Engineer")
            elif exp.lower() == "no" and (skill.lower() == "no" or [i for i in sk]) and expy==0 :
                flag=True
                desg=" Intern"
                sal=20000
                print("You have been appointed as Intern")
            employee_details()
    else: 
        flag=False
        print("Sorry!, Better luck next time.....")
def employee_details():
    global sin_det
    if flag==True:
        empl_id = random.randint(10000, 99999)

        sin_det = {
            "Name": name,
            "Age": age,
            "Email": em_id,
            "Contact number": cont_num,
            "Qualification": qual,
            "Skills": skill,
            "Employee id": empl_id,
            "Designation": desg,
            "Salary": sal
        }
        all_det[empl_id]=sin_det
def all_details():
     print(all_det)
def sing_emp_det(employee_id):
        print(all_det[employee_id])    
def salary(employee_id):
    global all_det
    no_days = int(input(f"Enter the total number of working days for employee {employee_id}: "))
    no_pres = int(input(f"Enter the total number of days present for employee out of {no_days} days {employee_id}: "))
    no_abs = no_days - no_pres
    basic_salary = all_det[employee_id].get("Salary", 0)
    emp_salary = round((no_pres / no_days) * basic_salary, 2)
    print(f"Total number of days absent is {no_abs}")
    print(f"The calculated salary for employee {employee_id} is: {emp_salary}")
    print(all_det)
def performance(employee_id):
    no_proj=int(input("enter the num of projects completed in a year: "))
    prof=int(input("enter the num project with high efficiency in a year:  "))
    cus=int(input("enter the num project with high customer satisfaction in a year:  "))
    if no_proj>=4 and  prof>=3 and cus>=3:
        x="Very Good"
        key = "Performance Rating"
        all_det[employee_id][key] = x
    elif no_proj>=3 and  prof>=2 and cus>=2:
        x="Good"
        key = "Performance Rating"
        all_det[employee_id][key] = x
    elif no_proj>=1  and  prof>=1 and cus>=1:
        x="Average"
        key = "Performance Rating"
        all_det[employee_id][key] = x
    elif no_proj==0  and  prof==0 and cus==0:
        x="Poor"
        key = "Performance Rating"
        all_det[employee_id][key] = x

def delete_employee(employee_id):
    global all_det
    if employee_id in all_det:
        del all_det[employee_id]
        print(f"Employee with ID {employee_id} deleted successfully.")
    else:
        print(f"No employee found with ID {employee_id}.")

while True:
    print("\n1.Selection_Process  2.ALL_Employee_Details 3.Single_emp_details 4.Salary  5.Perforamance  6.Update   7.Delete  8.Exit")
    ch=int(input("enter your choose: "))
    match ch:
        case 1:
            applicant()
        case 2:
            all_details()
        case 3:
            if len(all_det)==0:
                print("no data has been saved")
            else:
                employee_id_to_check = int(input("Enter the Employee ID to check single details: "))
                if  employee_id_to_check in all_det:

                    sing_emp_det(employee_id_to_check) 
                else:
                    print(f"Employee with ID {employee_id_to_check} not found.")
        case 4:
            if len(all_det)==0:
                print("no data has been saved")
            else:
                employee_id_to_check = int(input("Enter the Employee ID to generate salary : "))
                salary(employee_id_to_check) 
        case 5:
            if len(all_det)==0:
                print("no data has been saved")
            else:
                employee_id_to_check = int(input("Enter the Employee ID to generate performance : "))
                performance(employee_id_to_check) 
        case 6:
            if len(all_det)==0:
                print("no data has been saved")
            else:
                employee_id_to_check = int(input("Enter the Employee ID for update: "))
                if employee_id_to_check in all_det:
                    for key, value in all_det.items():
                        if key == employee_id_to_check:
                            field = input("Enter the field to update: ")
                            value = input("Enter the value to update: ")
                            field_x=field.capitalize()

                            if value.isnumeric():
                                all_det[key][field_x] = int(value)
                                print(f"{field} updated for employee {key}")
                            else:
                                all_det[key][field_x] = value
                                print(f"{field_x} updated for employee {key}")
                else:
                    print(f"Employee with ID {employee_id_to_check} not found.")

        case 7:
            if len(all_det)==0:
                print("no data has been saved")
            else:
                employee_id_to_check = int(input("Enter the Employee ID for delete: "))
                delete_employee(employee_id_to_check)
        case 8:
            sys.exit()
        





                    
                        

                        




            
               
           

