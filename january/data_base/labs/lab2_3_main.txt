--select * FROM dbo.debtCheck()
--Create table dbo.tmp_tbl(idDebtStudents varchar(40));
--select * from dbo.tmp_tbl;

DELETE 
FROM dbo.tmp_tbl;
INSERT into dbo.tmp_tbl SELECT * FROM dbo.debtCheck();

/*
UPDATE Payments
SET id_student = NULL
WHERE EXISTS(SELECT * FROM dbo.tmp_tbl WHERE idDebtStudents = Payments.id_student)

DELETE 
FROM Payments, Students
WHERE EXISTS(SELECT * FROM dbo.tmp_tbl WHERE idDebtStudents = Students.id_student)
*/



--SELECT * FROM Students;

/*
delete from Residence
where (ResidenceEndDate < '2017-01-07') AND
(ResidenceID != ALL(
    SELECT PreviousResidenceRef FROM Residence
    WHERE PreviousResidenceRef IS NOT NULL));
*/