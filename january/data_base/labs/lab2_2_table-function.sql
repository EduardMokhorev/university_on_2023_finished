-- 2.2   9.	количество студентов заданного факультета, проживающих в заданном городе (для списка городов);

CREATE FUNCTION Count_in_siti_and_fak (@City char(5), @Name_f char(5))
RETURNS TABLE
AS RETURN        (
         SELECT COUNT(Students.id_student) AS 'Количество студентов заданного факультета и заданного города'
         FROM Students
		 INNER JOIN City  
		 ON Students.id_street = City.id_city
		 WHERE City.city = @City AND Students.name_f = @name_f
);