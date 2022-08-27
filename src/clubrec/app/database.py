import random
from app import db
def query():
    return random.choice(["Batman","Superman","Spider-Man"])

def getStudent() -> dict:
    conn = db.connect()
    results = conn.execute("SELECT * FROM Student").fetchall()
    conn.close()
    student_list = []
    for result in results:
        item = {
            "student_id":result[0],
            "student_first_name":result[1],
            "student_last_name":result[2]
        }
        student_list.append(item)
    return student_list

def getActivitiesForDept(deptLike) -> dict:
    conn = db.connect()
    query_string = """SELECT dDetail.DeptName, aDetail.ActivityCategory, sCount from 
    (SELECT d.DeptId dId, ActivityId aId, count(1) sCount FROM Department d JOIN Student s ON (s.DeptId = d.DeptId) JOIN ClubMembership c ON (s.StudentId = c.StudentId) JOIN ActivityParticipation p ON (c.ClubId = p.ClubId) 
    GROUP BY d.DeptId, ActivityId) sub 
    JOIN Department dDetail ON (dDetail.DeptId = sub.dId) JOIN Activity aDetail ON (aDetail.ActivityId = sub.aId) 
    WHERE dDetail.DeptName LIKE '%%"""+deptLike+"""%%'
    AND sCount >= ALL (SELECT count(1) FROM Department d1 JOIN Student s1 ON (s1.DeptId = d1.DeptId) JOIN ClubMembership c1 ON (s1.StudentId = c1.StudentId) JOIN ActivityParticipation p1 ON (c1.ClubId = p1.ClubId) WHERE d1.DeptId = sub.dId GROUP BY d1.DeptId, p1.ActivityId)"""
    results = conn.execute(query_string).fetchall()
    conn.close()
    dept_act_list = []
    for result in results:
        item = {
            "dept_name":result[0],
            "activity_category":result[1],
            "student_count":result[2]
        }
        dept_act_list.append(item)
    print(dept_act_list)
    return dept_act_list

def getBachelorStudentsForDept() -> dict:
    conn = db.connect()
    results = conn.execute("SELECT DeptName, COUNT(*) AS NumOfStudents FROM Student NATURAL JOIN Department WHERE Degree = 'Bachelors' GROUP BY DeptName ORDER BY DeptName").fetchall()
    conn.close()
    student_list = []
    for result in results:
        item = {
            "dept_name":result[0],
            "count":result[1]
        }
        student_list.append(item)
    print(student_list)
    return student_list
    #  Sample from TA  #

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from tasks;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        id = result[0]
        task = result[1]
        status = result[2]
        print(id)
        print(task + "|" + status)
        item = {
            "id": id,
            "task": task,
            "status": status
        }
        todo_list.append(item)

    return todo_list

def fetch_students() -> dict:
    """Reads all students. may need to limit the student rows or may need pagination.

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Student;").fetchall()
    conn.close()
    student_list = []
    for result in query_results:
        id = result[0]
        fname = result[1]
        lname = result[2]
        curyear = result[3]
        degree = result[4]
        gradyear = result[5]
        deptid = result[6] 
        student = {
            "id": id,
            "fname": fname,
            "lname": lname,
            "curyear": curyear,
            "degree": degree,
            "gradyear": gradyear,
            "deptid": deptid
        }
        student_list.append(student)

    return student_list


def update_student_fname(student_id: int, fname: str) -> None:
    """Updates student's firstname based on given `student_id'"""

    conn = db.connect()
    query = 'update Student set FirstName = "{}" where StudentId = {};'.format(fname, student_id)
    conn.execute(query)
    conn.close()


def update_student_lname(student_id: int, lname: str) -> None:
    """Updates student's lastname based on given `student_id`"""

    conn = db.connect()
    query = 'update Student set LastName = "{}" where StudentId = {};'.format(lname, student_id)
    conn.execute(query)
    conn.close()

def update_student_curyear(student_id: int, curyear: str) -> None:
    """Updates student's currentyear based on given `student_id`"""

    conn = db.connect()
    query = 'update Student set CurrentYear = "{}" where StudentId = {};'.format(curyear, student_id)
    conn.execute(query)
    conn.close()

def update_student_degree(student_id: int, degree: str) -> None:
    """Updates student's degree based on given `student_id`"""

    conn = db.connect()
    query = 'update Student set Degree = "{}" where StudentId = {};'.format(degree, student_id)
    conn.execute(query)
    conn.close()

def update_student_gradyear(student_id: int, gradyear: str) -> None:
    """Updates student's graduatedyear based on given `student_id`"""

    conn = db.connect()
    query = 'update Student set GraduatedYear = "{}" where StudentId = {};'.format(gradyear, student_id)
    conn.execute(query)
    conn.close()

def update_student_dept(student_id: int, dept: int) -> None:
    """Updates student's deptid based on given `student_id`"""

    conn = db.connect()
    query = 'update Student set DeptId = "{}" where StudentId = {};'.format(dept, student_id)
    conn.execute(query)
    conn.close()

def insert_new_student(fname: str, lname: str, curyear: str, degree: str, gradyear: str, deptid: int) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """
    query = "select max(StudentId) + 1 from Student"
    conn = db.connect()
    query_results = conn.execute(query)
    for result in query_results:
        id = result[0]
    query = 'insert into Student (StudentId, FirstName, LastName, CurrentYear, Degree, GraduatedYear, DeptId) values ("{}", "{}", "{}", "{}","{}", "{}","{}");'.format(id, fname, lname, curyear, degree, gradyear, deptid)
    print(query)
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_student_by_id(net_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'delete from Student where StudentId = {};'.format(net_id)
    conn.execute(query)
    conn.close()

def fetch_clubs():
    conn = db.connect()
    results = conn.execute("SELECT * FROM Club").fetchall()
    conn.close()
    club_list = []
    for result in results:
        item = {
            "club_id":result[0],
            "club_name":result[1],
            "club_desc":result[2],
            "club_age":result[3]
        }
        club_list.append(item)
    return club_list

def getClubsLikeDesc(desc):
    conn = db.connect()
    results = conn.execute("""SELECT * FROM Club WHERE ClubDesc LIKE '%%"""+desc+"""%%'""").fetchall()
    conn.close()
    club_list = []
    for result in results:
        item = {
            "club_id":result[0],
            "club_name":result[1],
            "club_desc":result[2],
            "club_age":result[3]
        }
        club_list.append(item)
    print(club_list)
    return club_list

def update_club_name(club_id: int, clubname: str) -> None:

    conn = db.connect()
    query = 'update Club set ClubName = "{}" where ClubId = {};'.format(clubname, club_id)
    conn.execute(query)
    conn.close()


def update_club_desc(club_id: int, clubdesc: str) -> None:

    conn = db.connect()
    query = 'update Club set ClubDesc = "{}" where ClubId = {};'.format(clubdesc, club_id)
    conn.execute(query)
    conn.close()

def update_club_age(club_id: int, clubage: str) -> None:

    conn = db.connect()
    query = 'update Club set ClubAgeYears = "{}" where ClubId = {};'.format(clubage, club_id)
    conn.execute(query)
    conn.close()

def insert_new_club(cname: str, cdesc: str, cage: int):

    query = "select max(ClubId) + 1 from Club"
    conn = db.connect()
    query_results = conn.execute(query)
    for result in query_results:
        id = result[0]
    query = 'insert into Club (ClubId, ClubName, ClubDesc, ClubAgeYears) values ("{}", "{}", "{}", "{}");'.format(id, cname, cdesc, cage)
    conn.execute(query)
    conn.close()

def delete_club(club_id: int):
    conn = db.connect()
    query = 'delete from Club where ClubId = {};'.format(club_id)
    conn.execute(query)
    conn.close()    

################################################Club Membership functions here##########################################
def fetch_clubmembership():
    conn = db.connect()
    results = conn.execute("SELECT * FROM ClubMembership").fetchall()
    conn.close()
    clubmembership_list = []
    for result in results:
        item = {
            "cm_studentid":result[0],
            "cm_clubid":result[1],
            "cm_role":result[2],
            "cm_startdate":result[3],
            "cm_status": result[4]
        }
        clubmembership_list.append(item)
    return clubmembership_list

def insert_entry_clubmembership(student_id:int, club_id: int, role: str, start_date: str, status: str):
    conn = db.connect()
    query = 'insert into ClubMembership (StudentId, ClubId, Role, StartDate, Status) values ("{}", "{}", "{}", "{}", {}");'.format(student_id, club_id, role, start_date, status)
    conn.execute(query)
    conn.close()

def delete_entry_clubmembership(student_id:int, club_id:int):
    conn = db.connect()
    query = 'delete from ClubMembership where StudentId = {} and ClubId = {};'.format(student_id, club_id)
    conn.execute(query)
    conn.close()

