
update ClubMembership c set StartDate = (select STR_TO_DATE(concat('01,01,', GraduatedYear), '%d,%m,%Y') from Student s where s.StudentId = c.StudentId);

update ClubMembership c set StartDate = '2022-04-01' where StartDate > '2022-06-01';

update ClubMembership c set Status = 1 where StartDate > '2018-01-01';

update ClubMembership c set Status = 0 where StartDate <= '2018-01-01';

insert into Activity values(1, 'Meeting');
insert into Activity values(2, 'Conference');
insert into Activity values(3, 'Hackathon');
insert into Activity values(4, 'Social Events');
insert into Activity values(5, 'Philanthrophy');
insert into Activity values(6, 'Games');
insert into Activity values(7, 'Field Trips');
insert into Activity values(8, 'Outdoor');
insert into Activity values(9, 'Tourism');
insert into Activity values(10, 'Company Visits');
insert into Activity values(11, 'College Visits');
insert into Activity values(12, 'Charity');

/* Hackathon activities */
insert into ActivityParticipation (
select ClubId, 3 from Club where ClubName like '%Computer%' or ClubName like '%Tech%' or ClubName like '%Prog%' or ClubName like '%Engineering%'
							or ClubDesc like '%Computer%' or ClubDesc like '%Tech%' or ClubDesc like '%Prog%' or ClubDesc like '%Engineering%');

/* Meeting */
insert into ActivityParticipation (
select ClubId, 1 from Club);


commit;
