--9.	������� DDL �������, ����������� �������� �� � ������� ���������������� ���������.
CREATE TRIGGER trgTablechanges
ON DATABASE 
FOR ALTER_TABLE
AS 
BEGIN
print 'You cant update'
END;
ROLLBACK


UPDATE Students
Set first_name = '����'
Where Students.id_student = 1;













DROP TRIGGER cantChanges;




/*
CREATE TRIGGER cantChanges
ON Students
INSTEAD OF UPDATE 
AS 
BEGIN
print 'You cant update'
END
*/