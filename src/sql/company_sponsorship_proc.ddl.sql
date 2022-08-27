USE `clubrecommendation`;
DROP procedure IF EXISTS `company_sponsorship`;

USE `clubrecommendation`;
DROP procedure IF EXISTS `clubrecommendation`.`company_sponsorship`;
;

DELIMITER $$
USE `clubrecommendation`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `company_sponsorship`(company_id INT, club_id INT, start_date date, end_date date, out total_offers INT)
BEGIN

/*
  Companies offer free program to Studends from specific club. 
  The offer type can be orientation or leadership. 
  The criteria for offer is that the Student has to be active and have experience of more than an year.
  If the Students role in the club is Leader leadership program is offered. If not orientation program is offered.
  Student should not have any role earlier in the company.
  The User interface will pass the companyId, clubId, startDate, endDate.
  company_sponsorship stored procedure will accept these arguments and will return the # of students given offer. It will also insert the information in the career table.
*/
    declare done INT DEFAULT 0;
	declare v_student_id INT;
    declare v_role VARCHAR(20);
    declare v_start_date DATE;
    declare v_status TINYINT;
    declare v_not_eligibile INT default 1;
    declare v_club_experience INT default 0;
	declare studentsFromClub CURSOR FOR SELECT StudentId, Role, StartDate, Status from clubmembership where ClubId = club_id;
   -- declare existingCareers CURSOR FOR SELECT 1 from Career where CompanyId = company_id and StudentId = 1;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
SET @total_offers = 0;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;

OPEN studentsFromClub;
START TRANSACTION;
REPEAT
	FETCH studentsFromClub INTO v_student_id, v_role, v_start_date, v_status;
		SELECT DATEDIFF(CURRENT_TIMESTAMP , v_start_date) into v_club_experience;
        -- Student should be in active standing in the club and have more than 1 year experience.
        -- SELECT concat('experience is is ', v_club_experience);
        IF v_club_experience >= 365 AND v_status = 1 THEN
			SET v_not_eligibile = 1; -- not eligible is 1 so he is not eligible.
			-- Student should not have had any past experience in the company. If he doesnt have exp, not eligbile is 0 so consider.
			SELECT count(1) into v_not_eligibile from Career where CompanyId = company_id and StudentId = v_student_id;
			-- SELECT concat('experience is is ', v_club_experience, 'v_not_eligibile', v_not_eligibile);
			IF v_not_eligibile = 0 THEN
				IF v_role = 'Leader' THEN
					insert into Career (StudentId, CompanyId, CareerId, Title, StartDate, EndDate) values (v_student_id, company_id, 1, 'Leadership', start_date, end_date);
					SET @total_offers = @total_offers + 1;
				ELSE 
					insert into Career (StudentId, CompanyId, CareerId, Title, StartDate, EndDate) values (v_student_id, company_id, 1, 'Orientation', start_date, end_date);
					SET @total_offers = @total_offers + 1;
				END IF;
			END IF;
        END IF;

        -- set to default
UNTIL done
END REPEAT;
COMMIT;

END$$

DELIMITER ;
;

