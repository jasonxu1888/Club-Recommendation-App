update clubmembership set status = 1 where StudentId in 
( select StudentId from Student where GraduatedYear > 2019);

update clubmembership set status = 0 where StudentId in 
( select StudentId from Student where GraduatedYear <= 2019);

update clubmembership set StartDate = '2021-01-01' where status = 1;

update clubmembership set StartDate = '2019-01-01' where status = 0;

select cm.ClubId, c.ClubName, count(1) from clubmembership cm, club c where cm.status = 1 and c.ClubId = cm.ClubId group by cm.ClubId order by Count(1) desc;

-- 470	Lucha Robotics	2 --> gets the deal.

-- select * from clubmembership where ClubId = 470;

-- select * from Student where GraduatedYear > '2020';

delete from clubmembership where ClubId = 470;

insert into clubmembership(StudentId, ClubId, Role, StartDate, Status) values (1, 470, 'Leader', '2021-03-01', 1);
insert into clubmembership(StudentId, ClubId, Role, StartDate, Status) values (177, 470, 'Member', '2021-03-01', 1);
insert into clubmembership(StudentId, ClubId, Role, StartDate, Status) values (333, 470, 'Member', '2021-03-01', 1);
insert into clubmembership(StudentId, ClubId, Role, StartDate, Status) values (510, 470, 'Member', '2021-03-01', 0);
insert into clubmembership(StudentId, ClubId, Role, StartDate, Status) values (21, 470, 'Member', '2021-04-01', 1);
insert into clubmembership(StudentId, ClubId, Role, StartDate, Status) values (30, 470, 'Member', '2021-05-01', 1);
insert into clubmembership(StudentId, ClubId, Role, StartDate, Status) values (37, 470, 'Leader', '2021-03-01', 1);
insert into clubmembership(StudentId, ClubId, Role, StartDate, Status) values (61, 470, 'Member', '2021-03-01', 1);


-- Delete before testing the UI.
-- Use below select for eligbility.

select * from clubmembership c where c.ClubId = 470 and c.Status = 1;

delete from Career where CompanyId = 1 and CareerId = 1; -- filter these rows for greater than 1 year membership...