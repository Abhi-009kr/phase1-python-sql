CREATE DATABASE IF NOT EXISTS School;
Use School;

CREATE TABLE IF NOT EXISTS Students
(
    id int Primary key,
    Namex varchar(50),
    course varchar(50),
    marks int
);

INSERT INTO Students (id, Namex, course, marks)
VALUES
(1, 'Abhishek', 'BCA', 80),
(2, 'Aakarsh', 'MCA', 90),
(3, 'Gagan', 'BCAMCA', 88);

SELECT namex, marks
from students
ORDER BY marks desc;

select course, avg(marks)
from students
group by course;
