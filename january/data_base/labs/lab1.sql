
-- ������ 1 9)	�������, ���, ��������, ���������, ���� � ����� ������;
Select Students.surname, Students.middle_name, Students.first_name, Faculty.name, Payments.date_pay, Payments.summ
FROM Students,Faculty,Payments
WHERE Students.id_student = Payments.id_student AND Students.name_f = Faculty.name_f;



-- ������ 2 9)	���������� �������� � ������ ������ ���������;   
SELECT tr_group, COUNT(Payments.date_pay) AS count_payments
From Students, Payments
GROUP BY tr_group;




-- ������3  9)	�������� ����� ����������� � ��������������� ������� ������ ��������� ��������� ���������� (��������);
Select Students.name_f, SUM(Payments.summ) AS '����������� �����', SUM(Payments.summ) - 504502 AS "����������� ����� - ���������"
FROM Students,Payments
WHERE Students.name_f = '����' -- ��� ���� ������� ������ �� ����������
GROUP BY name_f;




--- ������ 4 9)	�������� �� ������ ������� ���������� ����� �������, ���������� ������ �������� � ��������� ���������� ������ (��������);
Select id_student, surname,first_name,middle_name,house,flat,phone,birthday,rec_date,tr_group,note,city
From Students, City
Where City.id_city = Students.id_street and City.city = '�����'; --������ ����� ����� ������
---����� �����
