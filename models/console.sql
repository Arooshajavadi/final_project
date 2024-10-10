create database teacher;
create table teacher.profile(
    id int auto_increment primary key,
    name varchar(30),
    family varchar(30),
    username varchar(30),
    password varchar(18),
    phone int,
    skill varchar(30)
);

create database student;
create table student.profile(
    id int auto_increment primary key,
    name varchar(30),
    family varchar(30),
    username varchar(30),
    password varchar(18),
    phone int,
    grade int
);

create database course;
create table course.Choose(
    id int auto_increment primary key,
    username varchar(30),
    password varchar(18),
    title varchar(20),
    teacher varchar(20),
    code int
);