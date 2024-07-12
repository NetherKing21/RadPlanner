import mysql.connector

#Change this latter for the actual database
radPlannerDB = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="rad_planner"
)

my_cursor = radPlannerDB.cursor()

#Get departments
departments = ['PLACEHOLDER Department']

with open('CoursesWithPrerequisites copy.csv', 'r') as file:
    for line in file:
        parts = line.strip().split(',')
        department = parts[3].strip()

        if department not in departments:
            departments.append(department)

print(departments)

#Insert departments into database
def insertDepartments(departmentList, cursor, db):
    for department in departmentList:
        sql = f'INSERT IGNORE INTO department (department_name) VALUES ("{department}")'
        cursor.execute(sql)
    
    db.commit()

#Run this line ONCE!
# insertDepartments(departments, my_cursor, radPlannerDB)
