-- 9.	Разработать хранимую процедуру для определения количества полных лет студентов заданной группы; входные параметры: группа, факультет.

     --Создание ХП
USE Payments_of_Students;
GO
CREATE PROCEDURE countAge(@namef CHAR(10), @nameGroup CHAR(10)) AS
     BEGIN
	 Select birthday,(YEAR('10.06.2022')) - YEAR(birthday) AS age  
	 From Students
	 Where Students.name_f = @namef AND Students.tr_group = @nameGroup
     end;

	 --вызов ХП
EXECUTE countAge 'МиТП','ПО-3' 
