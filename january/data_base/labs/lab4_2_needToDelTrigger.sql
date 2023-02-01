--9.	��� ���������� ������ � ������� ��������, ������� �������� � ���������� ��������� �� ������� ������.
-- ����������� ����� �.�. � ������� �������� ���� ����
CREATE TRIGGER whenInsertShowCount
ON Students
AFTER INSERT
AS 
BEGIN

Select Street.street ,COUNT(Students.id_street) AS CountPeoples
From Students
INNER JOIN Street
ON Students.id_street = Street.id_street
Group by Students.id_street,Street.street;

END


INSERT INTO Students (name_f, surname, middle_name) VALUES ('London', 'Hoffman', 's');



/* test
Select Street.street ,COUNT(Students.id_street) AS CountPeoples
From Students
INNER JOIN Street
ON Students.id_street = Street.id_street
Group by Students.id_street,Street.street;
*/