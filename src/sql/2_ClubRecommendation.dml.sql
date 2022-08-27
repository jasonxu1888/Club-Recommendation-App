use clubrecommendation;
/*
DELETE FROM Career; 
DELETE FROM ActivityParticipation;
DELETE FROM MeetingCalendar;
DELETE FROM ClubMembership;
DELETE FROM Sponsorship;
DELETE FROM Activity;
DELETE FROM Company;
DELETE FROM Club;
DELETE FROM Student;
*/

/* Department */
INSERT INTO Department (DeptId, DeptName, DeptCollege, DeptCampus) VALUES (1, 'Systems Engineering', 'Grainger', 'UIUC');
/* Student */
INSERT INTO Student (StudentId, FirstName, LastName, CurrentYear, Degree, GraduatedYear, DeptId) VALUES (1,'Raki', 'Jeyaraman', 'Sophomore', 'Bachelors', '2024', 1);
/* Club */
INSERT INTO Club (ClubId, ClubName, ClubDesc, ClubAgeYears) VALUES (1, 'Accounting Club', 'student experience through company presentations, philanthropic opportunities, and social events.  importance of leadership, ethics, communication, professionalism, and networking', 2);
/* Company */
INSERT INTO Company(CompanyId, CompanyName, CompanyDesc, CompanyCategory, MarketCapMillions, CompanyEmployeeCount) VALUES (1, 'Google', 'provides various technology products and platforms throughout the world.', 'Technology', 1577000, 139995);
/* Activity */
INSERT INTO Activity(ActivityId, ActivityCategory) VALUES (1, 'Conference');
/* Sponsorship */
INSERT INTO Sponsorship(ClubId, CompanyId) VALUES (1,1);
/* ClubMembership */
INSERT INTO ClubMembership(StudentId, ClubId, RoleId, StartDate, Status) VALUES (1,1,1,'2021-11-13',1);
/* MeetingCalendar */
INSERT INTO MeetingCalendar(MeetingId, ClubId, MeetingDesc, MeetingDay, MeetingStartTime, MeetingEndTime, MeetingLocation) VALUES (1,1,'General meeting.','Tuesday','14:00:00','16:00:00',"Siebel Center for Computer Science");
/* ActivityParticipation */
INSERT INTO ActivityParticipation(ClubId, ActivityId) VALUES (1,1);
/* Career */
INSERT INTO Career(StudentId, CompanyId, CareerId, Title, StartDate, EndDate) VALUES (1,1,1,'Intern','2021-07-07', '2021-08-28');
commit;
