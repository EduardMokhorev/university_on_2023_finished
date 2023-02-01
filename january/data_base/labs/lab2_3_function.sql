
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE FUNCTION debtCheck()
RETURNS @whoHaveDebtId TABLE  
(
	idDebtStudents varchar(40)
)
AS
BEGIN
	INSERT INTO @whoHaveDebtId
	SELECT
		Students.id_student
	FROM Students INNER JOIN Payments
	ON Students.id_student = Payments.id_student
	GROUP BY Students.id_student HAVING (MAX(Payments.date_pay) < '01.06.2023')
	RETURN 
END
GO