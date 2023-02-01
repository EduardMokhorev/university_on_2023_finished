
-- Запрос 1 9)	фамилия, имя, отчество, факультет, дата и сумма оплаты;
Select Students.surname, Students.middle_name, Students.first_name, Faculty.name, Payments.date_pay, Payments.summ
FROM Students,Faculty,Payments
WHERE Students.id_student = Payments.id_student AND Students.name_f = Faculty.name_f;



-- Запрос 2 9)	количество платежей в каждой группе студентов;   
SELECT tr_group, COUNT(Payments.date_pay) AS count_payments
From Students, Payments
GROUP BY tr_group;




-- Запрос3  9)	разность между фактической и запланированной суммами оплаты студентов заданного факультета (параметр);
Select Students.name_f, SUM(Payments.summ) AS 'Фактическая сумма', SUM(Payments.summ) - 504502 AS "Фактическая сумма - Ожидаемая"
FROM Students,Payments
WHERE Students.name_f = 'МиТП' -- тут надо сделать запрос по факулттету
GROUP BY name_f;




--- Запрос 4 9)	создание на основе таблицы «Студенты» новой таблицы, содержащей полные сведения о студентах некоторого города (параметр);
Select id_student, surname,first_name,middle_name,house,flat,phone,birthday,rec_date,tr_group,note,city
From Students, City
Where City.id_city = Students.id_street and City.city = 'Минск'; --Вместо минск нужен запрос
---Улицу забыл
