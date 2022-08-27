/*CREATE SCHEMA clubrecommendation;*/
USE clubrecommendation;
CREATE TABLE if not exists clubrecommendation.Department(
    DeptId INT NOT NULL,
    DeptName VARCHAR(25),
    DeptCollege VARCHAR(25),
    DeptCampus VARCHAR(25),
    PRIMARY KEY(DeptId)
);

CREATE TABLE if not exists clubrecommendation.Student(
    StudentId INT NOT NULL,
    FirstName VARCHAR(25),
    LastName VARCHAR(25),
    CurrentYear VARCHAR(25),
    Degree VARCHAR(25),
    GraduatedYear VARCHAR(4),
    DeptId INT NOT NULL,
    PRIMARY KEY(StudentId),
    FOREIGN KEY(DeptId)
        REFERENCES Department(DeptId)
);

CREATE TABLE if not exists clubrecommendation.Club(
    ClubId INT NOT NULL,
    ClubName VARCHAR(45),
    ClubDesc VARCHAR(2000),
    ClubAgeYears INT,
    PRIMARY KEY(ClubId)
);

CREATE TABLE if not exists clubrecommendation.Company(
    CompanyId INT NOT NULL,
    CompanyName VARCHAR(45),
    CompanyDesc VARCHAR(2000),
    CompanyCategory VARCHAR(45),
    MarketCapMillions BIGINT,
    CompanyEmployeeCount INT,
    PRIMARY KEY(CompanyId)
);

CREATE TABLE if not exists clubrecommendation.Activity(
    ActivityId INT NOT NULL,
    ActivityCategory VARCHAR(45),
    PRIMARY KEY(ActivityId)
);

CREATE TABLE if not exists clubrecommendation.Sponsorship(
    ClubId INT NOT NULL,
    CompanyId INT NOT NULL,
    FOREIGN KEY(ClubId)
        REFERENCES Club(ClubId),
    FOREIGN KEY(CompanyId)
        REFERENCES Company(CompanyId)
);

CREATE TABLE if not exists clubrecommendation.ClubMembership(
    StudentId INT NOT NULL,
    ClubId INT NOT NULL,
    RoleId INT,
    StartDate DATE,
    Status TinyInt,
    PRIMARY KEY(StudentId, ClubId), 
    FOREIGN KEY(ClubId)
        REFERENCES Club(ClubId),
    FOREIGN KEY(StudentId)
        REFERENCES Student(StudentId)
);

CREATE TABLE if not exists clubrecommendation.MeetingCalendar(
    MeetingId INT NOT NULL,
    ClubId INT NOT NULL,
    MeetingDesc VARCHAR(2000),
    MeetingDay VARCHAR(45),
    MeetingStartTime TIME,
    MeetingEndTime TIME,
    MeetingLocation VARCHAR(2000),
    PRIMARY KEY(MeetingId, ClubId),
    FOREIGN KEY(ClubId)
        REFERENCES Club(ClubId)
);

CREATE TABLE if not exists clubrecommendation.ActivityParticipation(
    ClubId INT NOT NULL,
    ActivityId INT NOT NULL,
    PRIMARY KEY(ActivityId, ClubId),
    FOREIGN KEY(ActivityId)
        REFERENCES Activity(ActivityId),
    FOREIGN KEY(ClubId)
        REFERENCES Club(ClubId)
);

CREATE TABLE if not exists clubrecommendation.Career(
    StudentId INT NOT NULL,
    CompanyId INT NOT NULL,
    CareerId INT NOT NULL,
    Title VARCHAR(200),
    StartDate DATE,
    EndDate DATE,
    PRIMARY KEY(StudentId, CompanyId, CareerId),
    FOREIGN KEY(StudentId)
        REFERENCES Student(StudentId),
    FOREIGN KEY(CompanyId)
        REFERENCES Company(CompanyId)
);

CREATE TABLE if not exists clubrecommendation.ArchivedClubs(
    ClubId INT NOT NULL,
    ClubName VARCHAR(45),
    ClubDesc VARCHAR(2000),
    ClubAgeYears INT,
    PRIMARY KEY(ClubId)
);

/* Alter commands after first iteration */
alter table Club modify ClubName varchar(255);
