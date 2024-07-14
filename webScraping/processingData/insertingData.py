import mysql.connector

def main():
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
    
    
    #Run this line ONCE!
    # insertDepartments(departments, my_cursor, radPlannerDB)



#Insert departments into database
def insertDepartments(departmentList, cursor, db):
    sql = get_dept_insert("PLACEHOLDER_DEPT")
    cursor.execute(sql)
    for department in departmentList:
        sql = get_dept_insert(department)
        cursor.execute(sql)
    
    db.commit()


def interpret_prereq_string(data: str) -> list:
    pass


def parse_course_code(data:str) -> list:
    pass

# setup
# - dept
#     - insert placeholder dept 
#     - insert all depts #1

COURSE_CODE_INDEX = 0
COURSE_TITLE_INDEX = 1
COURSE_CREDITS_INDEX = 2
COURSE_DEPT_INDEX = 3
COURSE_URL_INDEX = 4
COURSE_DESCRIPTION_INDEX = 5
COURSE_PREREQ_STRING_INDEX = 6


def insertCourse(data: list, cursor, db) -> None:

    # for each course
        #for course in 
    # - insert subject code #2
    # - query course table #3 & save id if retrieved
    #     - if got id (not null):
    #         - Path A: Update query #4
    #     - else (null)
    #         - Path B: insert #5
    # - insert prereq object #6
    # - map prereq object to proper courses
    #     - to parent:
    #         - simple insert actually #7
    #     - to child
    #         - select course id & save to var #8
    #             - if got id (not null):
    #                 - insert mapping row with retrieved id #9
    #             - else:
    #                 - insert temp row for course #10
    #                 - insert mapping row w/ temp row id #11
    
    pass

#1
def get_dept_insert(dept: str) -> str:
    return f'INSERT IGNORE INTO department (department_name) VALUES (\'{dept}\')'

#2
def get_subject_code_insert(code: str) -> str:
    return f'INSERT IGNORE INTO subject_code (subject_code_string) VALUES ( \'{code}\')'

#3
def get_course_select(full_course_code: str) -> str:
    """ accepts full course code e.g. CSE100 """
    return f'SELECT course_id
                FROM course c
                JOIN subject_code sc
                    ON c.subject_code_id = sc.subject_code_id
                WHERE CONCAT(c.subject_code_string, c.course_code) = \'{full_course_code}\' 
                ;'

#4
def get_course_update(title: str, credits: str, can_audit: str, dept_name: str, fetched_course_id: str) -> str:
    """ credits as int, can_audit as 0 (false) or 1 (true) , fetched_course_id (int.tostring) should come from get_course_select(). Dept name needed to link tables."""
    return f'UPDATE course
                SET course_title = \'{title}\', 
                    course_credit_hrs =  {credits}, 
                    course_can_audit = {can_audit}, 
                    department_id = (SELECT department_id
                                        FROM department
                                        WHERE department_name = \'{dept_name}\' 
                                        LIMIT 1 ;)
                WHERE course_id = {fetched_course_id} 
                ;'


#5
def get_course_insert(subject_code: str, course_code: str, title: str, credits: str, can_audit: str, dept_name: str) -> str:
    return f'INSERT INTO course
                (course_code, course_title, course_credit_hrs, course_can_audit, department_id, subject_code_id)
                VALUES 
                ( \'{course_code}\'),
                ( \'{title}\'),
                ( {credits}),
                ( {can_audit}),
                ( 	(SELECT department_id
                    FROM department
                    WHERE department_name = \'{dept_name}\' 
                    LIMIT 1 ;) ),
                ( 	(SELECT subject_code_id
                    FROM subject_code
                    WHERE subject_code_string = \'{subject_code}\' 
                    LIMIT 1 ;)
                );'


#6 





if __name__ == "main":
    main()
