ALTER TABLE clubmembership RENAME COLUMN RoleId TO Role;
ALTER TABLE clubmembership MODIFY COLUMN Role TO VARCHAR(20);
 
