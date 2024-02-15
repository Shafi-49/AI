import pyodbc as db 

connect = db.connect('DRIVER={SQL Server};SERVER=DESKTOP-0KSO0CA\MSSQLSERVER01;DATABASE=EmployeeDB')
cursor = connect.cursor()

class Employee:
    def getEmployeeDetails():
        query = 'SELECT * FROM employee_details'
        cursor.execute(query)
        to_list = []
        for i in cursor.fetchall():
            dict = {
                'empID' : i.empID,
                'empName' : i.empName,
                'empAge' : i.empAge,
                'empDesg' : i.empDesg,
                'empSalary' : i.empSalary
            }
            to_list.append(dict)
        print(to_list)
    def Employee_insertion(empID, empName, empAge, empDesg, empSalary):
        insertion = f'''
                        insert into employee_details (empID, empName, empAge, empDesg, empSalary) 
                        values ('{empID}', '{empName}', '{empAge}', '{empDesg}', '{empSalary}')
                    '''
        cursor.execute(insertion)
        connect.commit()
        cursor.close()
        print('Insert command completed successfully!!')
        

choice = 1
while choice in [1, 2]:
    print('1. Get the employees list\n2. Insert a new employee')
    userChoice = int(input('Enter your option: '))
    if userChoice == 1:
        Employee.getEmployeeDetails()
    elif userChoice == 2:
        empID = input('Enter employee id: ') 
        empName = input('Enter employee name: ') 
        empAge = input('Enter employee Age: ') 
        empDesg = input('Enter employee Designation: ') 
        empSalary = input('Enter employee salary: ')
        Employee.Employee_insertion(empID, empName, empAge, empDesg, empSalary)
    else:
        print('Process was interrupted by user!!')
        break;
