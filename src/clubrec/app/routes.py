from email.errors import StartBoundaryNotFoundDefect
from flask import render_template, request, jsonify
from app import context
from app import database as db_helper
from app import add_database as db_helper1
import datetime as date


@context.route("/clubs/<string:club_desc>", methods=['GET'])
def getClubsWithDesc(club_desc):
    print('User is searching for clubs matching the description...')
    return render_template("club.html", club_list = db_helper.getClubsLikeDesc(club_desc))

@context.route("/clubs/", methods = ['GET'])
def ClubHomepage():
    print('Getting all clubs...')
    return render_template("club.html", club_list = db_helper.fetch_clubs())

@context.route("/create-club", methods=['POST'])
def createClub():
    """ recieves post requests to create new club """
    data = request.get_json()

    cname = data['club_name']
    cdesc = data['club_desc']
    cage = data['club_age']

    db_helper.insert_new_club(cname, cdesc, cage)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@context.route("/edit-club/<int:club_id>", methods=['POST'])
def updateClub(club_id):
    """ recieved post requests for editing club """

    data = request.get_json()

    try:
        db_helper.update_club_name(club_id, data['club_name'])
        db_helper.update_club_desc(club_id, data['club_desc'])
        db_helper.update_club_age(club_id, data['club_age'])
        result = {'success': True, 'response': 'All fields updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

#Delete club, should automatically execute trigger that deletes members associated with that club in the Club Membership table
@context.route("/delete-club/<int:club_id>", methods=['POST'])
def deleteClub(club_id):
    try:
        db_helper.delete_club(club_id)
        result = {'success': True, 'response': 'Removed Club'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@context.route("/dept-activity/", methods=['GET'])
def getDeptActivityAll():
    print('User is searching for activities for all departments')
    return render_template("search.html", dept_act_list=db_helper.getActivitiesForDept(''))


@context.route("/dept-activity/<string:dept_like>", methods=['GET'])
def getDeptActivity(dept_like):
    print('User is searching for activities matching dept:' + dept_like)
    return render_template("search.html", dept_act_list=db_helper.getActivitiesForDept(dept_like))

@context.route("/dept-bachelor/", methods=['GET'])
def getDeptBachelor():
    print('User is searching for bachelor student count for all departments')
    return render_template("bachelor.html", student_list=db_helper.getBachelorStudentsForDept())

@context.route("/delete-student/<int:student_id>", methods=['POST'])
def deleteStudent(student_id):
    """ recieved post requests for student entry delete """

    try:
        db_helper.remove_student_by_id(student_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@context.route("/edit-student/<int:student_id>", methods=['POST'])
def updateStudent(student_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        db_helper.update_student_fname(student_id, data['fname'])
        db_helper.update_student_lname(student_id, data['lname'])
        db_helper.update_student_curyear(student_id, data['curyear'])
        db_helper.update_student_degree(student_id, data['degree'])
        db_helper.update_student_gradyear(student_id, data['gradyear'])
        db_helper.update_student_dept(student_id, data['deptid'])
        result = {'success': True, 'response': 'All fields updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@context.route("/create-student", methods=['POST'])
def createStudent():
    """ recieves post requests to add new task """
    data = request.get_json()
    print("This is the create input from UI:")
    print(data)
    fname = data['fname']
    lname = data['lname']
    curyear = data['curyear']
    degree = data['degree']
    gradyear = data['gradyear']
    deptid = data['deptid']
    db_helper.insert_new_student(fname, lname, curyear, degree, gradyear, deptid)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@context.route("/")
def homepage():
    """ returns rendered homepage """
    students = db_helper.fetch_students()
    return render_template("index.html", students=students)

#For homepage - needs work TODO
@context.route("/top-clubs/<string:dept_like>", methods=['GET'])
def getTopClubs(dept_like):
    print('User is searching for top clubs matching dept:' + dept_like)
    clubList = []
    club = {'club_id':1,'club_name':'Coding Club','total_enrollment': 30}
    clubList.append(club)
    club = {'club_id':2,'club_name':'Debate Club','total_enrollment': 40}
    clubList.append(club)
    print(clubList)
    return render_template("index.html", clubList=clubList)


@context.route("/company-offers/test/", methods=['GET'])
def companyIntershipOffersTest():
    company_id = 1
    club_id = 470
    start_date = date.datetime(2023, 1, 2)
    end_date = date.datetime(2023, 1, 18)
    totalOffers = db_helper1.companySponsorship(company_id, club_id, start_date, end_date)
    return render_template("test.html", totalOffers=totalOffers)

#For integration with UI
@context.route("/company-offers/", methods=['POST'])
def companyIntershipOffers():
    print('inside company -offers')
    data = request.get_json()
    print(data)
    company_id = data['companyId']
    club_id = data['clubId']
    start_date = data['startDate']
    end_date = data['endDate']
    totalOffers = db_helper1.companySponsorship(company_id, club_id, start_date, end_date)

############################################################### Clubmembership routes here #############################################
@context.route("/club-membership/", methods = ['GET'])
def ClubMembershipHomepage():
    print('Getting all members in clubs...')
    return render_template("clubmembership.html", club_list = db_helper.fetch_clubmembership())

@context.route("/delete-clubmembership/", methods=['POST'])
def deleteClubMembership():
    data = request.get_json()
    studentid = data['StudentId']
    clubid = data['ClubId']
    try:
        db_helper.delete_entry_clubmembership(studentid, clubid)
        result = {'success': True, 'response': 'Removed clubmembership'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@context.route("/create-clubmembership/", methods=['POST'])
def createClubMembership():
    """ recieves post requests to create new club """
    data = request.get_json()

    studentid = data['StudentId']
    clubid = data['ClubId']
    role = data['Role']
    startdate = data['StartDate']
    status = data['Status']

    db_helper.insert_entry_clubmembership(studentid, clubid, role, startdate, status)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)