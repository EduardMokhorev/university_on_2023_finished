--9.�������� ������� ��������� ��� ������� ��������� ������������ �������� ���������� � ������� ����������;
/*
CREATE TRIGGER cantUpdate
ON Students
INSTEAD OF UPDATE
AS 
BEGIN
PRINT 'You CANT update!' 
END
*/

UPDATE Students
SET first_name = 'lol'
Where id_student = 1

Select *
From Students
where id_student = 1