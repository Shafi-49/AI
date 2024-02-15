import requests 
import pandas as pd

API_URL = 'http://localhost:8000/getEmployeesData'

response = requests.get(API_URL)

if response.status_code == 200:
    try:
        data = response.json()
        df = pd.DataFrame(data)

        df.to_csv('C:\Task\Employee.csv', index=False)
        print('Data successfully converted to CSV file')
    except Exception as e:
        print('Something went wrong!!!!')
else:
    Error = response.status_code
    print('Error', Error)



