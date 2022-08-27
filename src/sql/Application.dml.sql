-- For given department, find what activities Students are most interested in.
select studentsCount, activityCategory from (
select count(1) studentsCount, ActivityId from Department d join Student s on (d.DeptId = s.DeptId) join ClubMembership c on (s.StudentId = c.StudentId) join ActivityParticipation p on (c.ClubId = p.ClubId)
 where d.DeptId = 1
 group by p.ActivityId order by count(1)) activitySummary join Activity b on (b.ActivityId = activitySummary.ActivityId)
 order by studentsCount desc;
