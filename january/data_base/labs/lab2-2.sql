/*
-- 2.2   9.	���������� ��������� ��������� ����������, ����������� � �������� ������ (��� ������ �������);

CREATE FUNCTION Count_in_siti_and_fak (@City char(5), @Name_f char(5))
RETURNS TABLE
AS RETURN        (
         SELECT COUNT(Students.id_student) AS '���������� ��������� ��������� ���������� � ��������� ������'
         FROM Students
		 INNER JOIN City  
		 ON Students.id_street = City.id_city
		 WHERE City.city = @City AND Students.name_f = @name_f
);
*/

SELECT *
FROM Count_in_siti_and_fak ('Минск', 'МиТП');
