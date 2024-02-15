from fastapi import FastAPI, HTTPException
import pyodbc as db

app = FastAPI()


@app.get('/getEmployeesData', response_model=list)
def getEmployeeDetailsAPI():
    try:
        connect = db.connect('DRIVER={SQL Server};SERVER=DESKTOP-0KSO0CA\MSSQLSERVER01;DATABASE=EmployeeDB')
        cursor = connect.cursor()
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
        return to_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error connecting to SQL Server: {str(e)}")

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host='127.0.0.1', port=8000)