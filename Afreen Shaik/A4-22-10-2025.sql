CREATE table Trainer_Info(
Trainer_Id varchar(20) primary key,
Salutation varchar(7),
Trainer_Name varchar(30),
Trainer_Location varchar(30),
Trainer_Track varchar(15),
Trainer_Qualification varchar(100),
Trainer_Experiance varchar(11),
Trainer_Email varchar(100),
Trainer_Password varchar(20) );

CREATE table Batch_Info(
Batch_Id varchar(20) primary key,
Batch_Owner varchar(30),
Batch_BU_Name varchar(30)
);

CREATE table Module_Info(
Module_Id varchar(20) primary key,
Module_Name varchar(40),
Module_Duration varchar(11)
);

CREATE table Associate_Info(
Associate_Id varchar(20) primary key,
Salutation varchar(7),
Associate_Name varchar(30),
Associate_Location varchar(30),
Associate_Track varchar(15),
Associate_Qualification varchar(200),
Associate_Email varchar(100),
Associate_Password varchar(20) 
);

CREATE table Questions(
Question_Id varchar(20) primary key,
Module_Id varchar(20),
Question_Textvar varchar(900),
foreign key (Module_Id) REFERENCES Module_Info(Module_Id)
);

CREATE TABLE Associate_Status (
Associate_Id varchar(20),
Module_Id varchar(20),
Batch_Id varchar(20),
Trainer_Id varchar(20),
Start_Date date,
End_Date date,
AFeedbackGiven varchar(20),
TFeedbackGiven varchar(20),
foreign key (Associate_Id) references Associate_Info(Associate_Id),
foreign key (Module_Id) references Module_Info(Module_Id),
foreign key (Batch_Id) references Batch_Info(Batch_Id),
foreign key (Trainer_Id) references Trainer_Info(Trainer_Id)
);

CREATE TABLE Trainer_Feedback (
Trainer_Id varchar(20),
Question_Id varchar(20),
Batch_Id varchar(20),
Module_Id varchar(20),
Trainer_Rating INT,
foreign key (Trainer_Id) references Trainer_Info(Trainer_Id),
foreign key (Question_Id) references Questions(Question_Id),
foreign key (Batch_Id) references Batch_Info(Batch_Id),
foreign key (Module_Id) references Module_Info(Module_Id)
);

CREATE TABLE Associate_Feedback (
Associate_Id VARCHAR(20),
Question_Id VARCHAR(20),
Module_Id VARCHAR(20),
Associate_Rating INT,
foreign key (Associate_Id) references Associate_Info(Associate_Id),
foreign key (Question_Id) references Questions(Question_Id),
foreign key (Module_Id) references Module_Info(Module_Id)
);

CREATE TABLE Login_Details (
User_Id VARCHAR(20) PRIMARY KEY,
User_Password VARCHAR(20)
);

INSERT INTO Trainer_Info VALUES
('F001','Mr.','PANKAJ GHOSH','Pune','Java','Bachelor of Technology',12,'Pankaj.Ghosh@alliance.com','fac1@123'),
('F002','Mr.','SANJAY RADHAKRISHNAN','Bangalore','DotNet','Bachelor of Technology',12,'Sanjay.Radhakrishnan@alliance.com','fac2@123'),
('F003','Mr.','VIJAY MATHUR','Chennai','Mainframe','Bachelor of Technology',10,'Vijay.Mathur@alliance.com','fac3@123'),
('F004','Mrs.','NANDINI NAIR','Kolkata','Java','Master of Computer Applications',9,'Nandini.Nair@alliance.com','fac4@123'),
('F005','Miss.','ANITHA PAREKH','Hyderabad','Testing','Master of Computer Applications',6,'Anitha.Parekh@alliance.com','fac5@123'),
('F006','Mr.','MANOJ AGRAWAL','Mumbai','Mainframe','Bachelor of Technology',9,'Manoj.Agrawal@alliance.com','fac6@123'),
('F007','Ms.','MEENA KULKARNI','Coimbatore','Testing','Bachelor of Technology',5,'Meena.Kulkarni@alliance.com','fac7@123'),
('F009','Mr.','SAGAR MENON','Mumbai','Java','Master of Science In Information Technology',12,'Sagar.Menon@alliance.com','fac8@123');

INSERT INTO Batch_Info VALUES
('B001','MRS.SWATI ROY','MSP'),
('B002','MRS.ARURNA K','HEALTHCARE'),
('B003','MR.RAJESH KRISHNAN','LIFE SCIENCES'),
('B004','MR.SACHIN SHETTY','BFS'),
('B005','MR.RAMESH PATEL','COMMUNICATIONS'),
('B006','MRS.SUSAN CHERIAN','RETAIL & HOSPITALITY'),
('B007','MRS.SAMPADA JAIN','MSP'),
('B008','MRS.KAVITA REGE','BPO'),
('B009','MR.RAVI SEJPAL','MSP');

INSERT INTO Module_Info VALUES
('O10SQL','Oracle 10g SQL',16),
('O10PLSQL','Oracle 10g PL/ SQL',16),
('J2SE','Core Java SE 1.6',288),
('J2EE','Advanced Java EE 1.6',80),
('JAVAFX','JavaFX 2.1',80),
('DOTNT4','.Net Framework 4.0',50),
('SQL2008','MS SQl Server 2008',120),
('MSBI08','MS BI Studio 2008',158),
('SHRPNT','MS Share Point',80),
('ANDRD4','Android 4.0',200),
('EM001','Instructor',0),
('EM002','Course Material',0),
('EM003','Learning Effectiveness',0),
('EM004','Environment',0),
('EM005','Job Impact',0),
('TM001','Attendees',0),
('TM002','Course Material',0),
('TM003','Environment',0);

INSERT INTO Associate_Info VALUES
('A001','Miss.','GAYATHRI NARAYANAN','Gurgaon','Java','Bachelor of Technology','Gayathri.Narayanan@hp.com','tne1@123'),
('A002','Mrs.','RADHIKA MOHAN','Kerala','Java','Bachelor of Engineering In Information Technology','Radhika.Mohan@cognizant.com','tne2@123'),
('A003','Mr.','KISHORE SRINIVAS','Chennai','Java','Bachelor of Engineering In Computers','Kishore.Srinivas@ibm.com','tne3@123'),
('A004','Mr.','ANAND RANGANATHAN','Mumbai','DotNet','Master of Computer Applications','Anand.Ranganathan@finolex.com','tne4@123'),
('A005','Miss.','LEELA MENON','Kerala','Mainframe','Bachelor of Engineering In Information Technology','Leela.Menon@microsoft.com','tne5@123'),
('A006','Mrs.','ARTI KRISHNAN','Pune','Testing','Master of Computer Applications','Arti.Krishnan@cognizant.com','tne6@123'),
('A007','Mr.','PRABHAKAR SHUNMUGHAM','Mumbai','Java','Bachelor of Technology','Prabhakar.Shunmugham@honda.com','tne7@123');


INSERT INTO Questions VALUES
('Q001','EM001','Instructor knowledgeable and able to handle all your queries'),
('Q002','EM001','All the topics in a particular course handled by the trainer without any gaps or slippages'),
('Q003','EM002','The course materials presentation, handson,  etc. refered during the training are relevant and useful.'),
('Q004','EM002','The Hands on session adequate enough to grasp the understanding of the topic.'),
('Q005','EM002','The reference materials suggested for each module are adequate.'),
('Q006','EM003','Knowledge and skills presented in this training are applicatible at your work'),
('Q007','EM003','This training increases my proficiency level'),
('Q008','EM004','The physical environment e.g. classroom space, air-conditioning was conducive to learning.'),
('Q009','EM004','The software/hardware environment provided was sufficient for the purpose of the training.'),
('Q010','EM005','This training will improve your job performance.'),
('Q011','EM005','This training align with the business priorities and goals.'),
('Q012','TM001','Participants were receptive and had attitude towards learning.'),
('Q013','TM001','All participats gained the knowledge and the practical skills after this training.'),
('Q014','TM002','The course materials presentation, handson,  etc. available for the session covers the entire objectives of the course.'),
('Q015','TM002','Complexity of the course is adequate for the particpate level.'),
('Q016','TM002','Case study and practical demos helpful in understanding of the topic'),
('Q017','TM003','The physical environment e.g. classroom space, air-conditioning was conducive to learning.'),
('Q018','TM003','The software/hardware environment provided was adequate  for the purpose of the training.');


INSERT INTO Associate_Status VALUES
('A001','O10SQL','B001','F001','2000-12-15','2000-12-25'),
('A002','O10SQL','B001','F001','2000-12-15','2000-12-25'),
('A003','O10SQL','B001','F001','2000-12-15','2000-12-25'),
('A001','O10PLSQL','B002','F002','2001-02-01','2001-02-12'),
('A002','O10PLSQL','B002','F002','2001-02-01','2001-02-12'),
('A003','O10PLSQL','B002','F002','2001-02-01','2001-02-12'),
('A001','J2SE','B003','F003','2002-08-20','2002-10-25'),
('A002','J2SE','B003','F003','2002-08-20','2002-10-25'),
('A001','J2EE','B004','F004','2005-12-01','2005-12-25'),
('A002','J2EE','B004','F004','2005-12-01','2005-12-25'),
('A003','J2EE','B004','F004','2005-12-01','2005-12-25'),
('A004','J2EE','B004','F004','2005-12-01','2005-12-25'),
('A005','JAVAFX','B005','F006','2005-12-04','2005-12-20'),
('A006','JAVAFX','B005','F006','2005-12-04','2005-12-20'),
('A006','SQL2008','B006','F007','2007-06-21','2007-06-28'),
('A007','SQL2008','B006','F007','2007-06-21','2007-06-28'),
('A002','MSBI08','B007','F006','2009-06-26','2009-06-29'),
('A003','MSBI08','B007','F006','2009-06-26','2009-06-29'),
('A004','MSBI08','B007','F006','2009-06-26','2009-06-29'),
('A002','ANDRD4','B008','F005','2010-06-05','2010-06-28'),
('A005','ANDRD4','B008','F005','2010-06-05','2010-06-28'),
('A003','ANDRD4','B009','F005','2011-08-01','2011-08-20'),
('A006','ANDRD4','B009','F005','2011-08-01','2011-08-20');

-- Update password of Trainer F004
UPDATE Trainer_Info
SET Trainer_Password = 'nn4@123'
WHERE Trainer_Id = 'F004';

/*Remove following record form associate_status table
	A003,J2EE,B004,F004,2005-12-1,2005-12-25 */
DELETE FROM Associate_Status
WHERE Associate_Id = 'A003'
  AND Module_Id = 'J2EE'
  AND Batch_Id = 'B004'
  AND Trainer_Id = 'F004'
  AND Start_Date = '2005-12-01'
  AND End_Date = '2005-12-25';
  
BEGIN;

INSERT INTO Login_Details (User_Id, User_Password) VALUES
('U001', 'Admin1@123'),
('U002', 'Admin2@123');

ROLLBACK;

SELECT * FROM Login_Details;