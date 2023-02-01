--Создание базы данных Платежи студентов
create database Payments_of_Students

use Payments_of_Students
go 

--Таблица Факультеты Faculty
create table Faculty (
name_f varchar(10) not null primary key,
name varchar(30) not null)

go
--Таблица Города City
create table City (
id_city int primary key identity(1,1),
city varchar(30) not null)

go
--Таблица Назначение оплат Purpose_pay
create table Purpose_pay (
goal varchar(40) not null primary key)

go
--Таблица Улицы Street
create table Street(
id_street int primary key identity(1,1),
street varchar(40) not null,
id_city int not null constraint to_city references City(id_city))

go
--Таблица Студенты Students 
create table Students(
id_student int primary key identity(1,1),
surname varchar(50) not null,
first_name varchar(50) not null,
middle_name varchar(50) not null,
id_street int not null constraint to_street references Street(id_street),
house varchar(5),
flat varchar(5),
phone varchar(10),
birthday date,
rec_date int,
tr_group varchar(10),
name_f varchar(10) not null constraint to_faculty references Faculty(name_f),
note text)

go
--Таблица Платежи Payments 
create table Payments(
id_student int not null constraint to_student references Students(id_student),
date_pay date not null,
summ float not null,
goal varchar(40) not null constraint to_purpose_pay references Purpose_pay(goal))