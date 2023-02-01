CREATE FUNCTION dbo.average (@Summ int, @Count int)
RETURNS INT
BEGIN
RETURN @Summ / @Count
END