--�������� ���� ������ ������� ���������
create database lab5

use lab5
go 


--������� history
create table history(
id_firm int not null,
workName varchar(5),
paid int,
debt int,
dateOperation date,
)
go


--������� Firm 
create table firm(
id_firm int primary key,
name_firm varchar(10),
adress varchar (10),
phone varchar(10),
isProvider bit DEFAULT(0) NOT NULL,
is�ontractor bit DEFAULT(0) NOT NULL
)
go
