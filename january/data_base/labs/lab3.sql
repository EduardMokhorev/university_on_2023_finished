-- 9.	����������� �������� ��������� ��� ����������� ���������� ������ ��� ��������� �������� ������; ������� ���������: ������, ���������.

     --�������� ��
USE Payments_of_Students;
GO
CREATE PROCEDURE countAge(@namef CHAR(10), @nameGroup CHAR(10)) AS
     BEGIN
	 Select birthday,(YEAR('10.06.2022')) - YEAR(birthday) AS age  
	 From Students
	 Where Students.name_f = @namef AND Students.tr_group = @nameGroup
     end;

	 --����� ��
EXECUTE countAge '����','��-3' 
