-- lab 2 task 1 
--9.	������� ����� ������� ��� ����������� �������� (��������� � ��� ��������);
/*
SELECT dbo.average (SUM(Payments.summ),COUNT(Payments.summ)) 

CREATE FUNCTION dbo.average (@Summ int, @Count int)
RETURNS INT
BEGIN
RETURN @Summ / @Count
END

*/

DECLARE @surname nchar(10) = '������', @first_name nchar(10) = '����', @middle_name nchar(10) = '����������'

SELECT dbo.average (SUM(Payments.summ),COUNT(Payments.summ)) AS '������� ����� ��������'
FROM Students, Payments
WHERE Students.surname = @surname AND Students.first_name = @first_name AND Students.middle_name = @middle_name AND Students.id_student = Payments.id_student;
