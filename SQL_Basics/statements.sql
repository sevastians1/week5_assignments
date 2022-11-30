select * from classes;
select name credits from classes where credits>3;
select * from classes where credits%2=0;
select * from enrollments where grade IS NULL AND student_id='1';
select students.first_name, students.last_name, enrollments.class_id from students inner join  enrollments on students.id=enrollments.student_id where grade IS NULL and first_name='Tianna';
select students.first_name, students.last_name, classes.name  from students  inner join  enrollments on students.id=enrollments.student_id inner join classes on enrollments.class_id=classes.id where grade IS NULL and first_name='Tianna';

