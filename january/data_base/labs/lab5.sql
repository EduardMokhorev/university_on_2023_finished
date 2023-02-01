--1.Процент расчетов с поставщиками за конкретный период
select SUM(paid)/SUM(debt)*100 AS [Процент от нужной оплаты]
from history inner join firm
on history.id_firm = firm.id_firm
where isProvider = 1 


--2.Удаление сведений о заданном поставщике*
DELETE
FROM history
where id_firm = 5


--3.Обновление сведений о заданном подрядчике (Адрес Телефон, Назв Фирмы)
update firm
set adress = 'sovetc', phone = '+256222', name_firm = 'Name'
where id_firm  = 2

--4.Вывод сведений о заказах, по которым есть долги поставщикам и подрядчикам. 
select firm.name_firm, workName,paid AS Заплатили, debt AS СтоимостьУслуги,dateOperation
from history inner join firm
on history.id_firm = firm.id_firm
where paid - debt < 0