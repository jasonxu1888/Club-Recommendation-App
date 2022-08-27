DROP TRIGGER IF EXISTS delete_club_members;
delimiter //
CREATE TRIGGER delete_club_members BEFORE DELETE on Club
FOR EACH ROW
BEGIN
DELETE FROM ClubMembership WHERE ClubMembership.ClubId = old.ClubId;
DELETE FROM Sponsorship WHERE Sponsorship.ClubId = old.ClubId;
DELETE FROM MeetingCalendar WHERE MeetingCalendar.ClubId = old.ClubId;
DELETE FROM ActivityParticipation WHERE ActivityParticipation.ClubId = old.ClubId;
INSERT INTO ArchivedClubs (ClubId, ClubName, ClubDesc, ClubAgeYears) VALUES (old.ClubId, old.ClubName, old.ClubDesc, old.ClubAgeYears);
END//
delimiter ; 
