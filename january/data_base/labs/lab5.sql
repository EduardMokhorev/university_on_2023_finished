--1.������� �������� � ������������ �� ���������� ������
select SUM(paid)/SUM(debt)*100 AS [������� �� ������ ������]
from history inner join firm
on history.id_firm = firm.id_firm
where isProvider = 1 


--2.�������� �������� � �������� ����������*
DELETE
FROM history
where id_firm = 5


--3.���������� �������� � �������� ���������� (����� �������, ���� �����)
update firm
set adress = 'sovetc', phone = '+256222', name_firm = 'Name'
where id_firm  = 2

--4.����� �������� � �������, �� ������� ���� ����� ����������� � �����������. 
select firm.name_firm, workName,paid AS ���������, debt AS ���������������,dateOperation
from history inner join firm
on history.id_firm = firm.id_firm
where paid - debt < 0