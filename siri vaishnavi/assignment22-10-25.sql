create database assignment;
use assignment;
create table Trainer_Info (
Trainer_Id VARCHAR(50) PRIMARY KEY,
Salutation VARCHAR(50),
Trainer_name VARCHAR(50),
Trainer_Location VARCHAR(50),
Trainer_Track VARCHAR(50),
Trainer_Qualification VARCHAR(100),
Trainer_Experiance varchar(50),
Trainer_Email VARCHAR(100),
Trainer_Password VARCHAR(50)
);
create table Batch_Info(
Batch_Id varchar(50) PRIMARY KEY,
Batch_Owner varchar(50),
Batch_BU_Name varchar(50)
);
create table Module_Info(
Module_Id varchar(50) PRIMARY KEY,
Module_Name varchar(50),
Module_Duration int
);
create table Associate_Info(
Associate_Id varchar(50) PRIMARY KEY,
Salutation VARCHAR(50),
Associate_Name varchar(50),
Associate_Location varchar(50),
Associate_Track varchar(50),
Associate_Qualification varchar(50),
Associate_Email varchar(50),
Associate_Password varchar(50)
);
create table Questions(
Question_Id varchar(50) PRIMARY KEY,
Module_Id varchar(50),
Question_Text varchar(50),
FOREIGN KEY(Module_Id) REFERENCES Module_Info(Module_Id)
);
create table Associate_Status(
Associate_Id varchar(50),
Module_Id varchar(50),
Batch_Id varchar(50),
Trainer_Id varchar(50),
Start_Date DATE,
End_Date DATE,
AFeedbackGiven varchar(50),
TFeedbackGiven varchar(50),
FOREIGN KEY(Module_Id) REFERENCES Module_Info(Module_Id),
FOREIGN KEY(Associate_Id) REFERENCES Associate_Info(Associate_Id),
FOREIGN KEY(Batch_Id) REFERENCES Batch_Info(Batch_Id),
FOREIGN KEY(Trainer_Id) REFERENCES Trainer_Info(Trainer_Id)
); 
Insert into Trainer_Info(Trainer_Id,Salutation,Trainer_Name,
Trainer_Location,Trainer_Track,Trainer_Qualification,
Trainer_Experiance,Trainer_Email,Trainer_Password) 
 VALUES('F001','Mr.','PANKAJ GHOSH', 'Pune','Java','Bachelor of Technology',12,'Pankaj.Ghosh@alliance.com', 'fac1@123'),
('F002','Mr.','SANJAY RADHAKRISHNAN','Bangalore','DotNet','Bachelor of Technology',12,'Sanjay.Radhakrishnan@alliance.com','fac2@123'),
('F003','Mr.','VIJAY MATHUR','Chennai','Mainframe','Bachelor of Technology',10,'Vijay.Mathur@alliance.com','fac3@123'),
('F004','Mrs.','NANDINI NAIR','Kolkata','Java','Master of Computer Applications',9,'Nandini.Nair@alliance.com','fac4@123'),
('F005','Miss.','ANITHA PAREKH','Hyderabad','Testing','Master of Computer Applications',6,'Anitha.Parekh@alliance.com','fac5@123'),
('F006','Mr.','MANOJ AGRAWAL' ,'Mumbai','Mainframe','Bachelor of Technology',9,'Manoj.Agrawal@alliance.com','fac6@123'),
('F007','Ms.','MEENA KULKARNI','Coimbatore','Testing','Bachelor of Technology',5,'Meena.Kulkarni@alliance.com','fac7@123'),
('F009','Mr.','SAGAR MENON','Mumbai','Java','Master of Science In Information Technology',12,'Sagar.Menon@alliance.com','fac8@123');

alter table Trainer_Info
modify column Trainer_Experiance int;


Insert into Batch_Info(Batch_Id,Batch_Owner,Batch_BU_Name)
Values('B001','MRS.SWATI ROY','MSP'),
('B002','MRS.ARURNA K','HEALTHCARE'),
('B003','MR.RAJESH KRISHNAN','LIFE SCIENCES'),
('B004','MR.SACHIN SHETTY','BFS'),
('B005','MR.RAMESH PATEL','COMMUNICATIONS'),
('B006','MRS.SUSAN CHERIAN','RETAIL & HOSPITALITY'),
('B007','MRS.SAMPADA JAIN','MSP'),
('B008','MRS.KAVITA REGE','BPO'),
('B009','MR.RAVI SEJPAL','MSP');

INSERT INTO Module_info(Module_Id,Module_Name,Module_Duration)
VALUES ('O10SQL','Oracle 10g SQL' ,16),
('O10PLSQL','Oracle 10g PL/ SQL' ,16),
('J2SE','Core Java SE 1.6',288),
('J2EE','Advanced Java EE 1.6',80),
('JAVAFX','JavaFX 2.1',80),
('DOTNT4','.Net Framework 4.0' ,50),
('SQL2008','MS SQl Server 2008',120),
('MSBI08','MS BI Studio 2008',158),
('SHRPNT','MS Share Point' ,80),
('ANDRD4','Android 4.0',200),
('EM001','Instructor',0),
('EM002','Course Material',0),
('EM003','Learning Effectiveness',0),
('EM004','Environment',0),
('EM005','Job Impact',0),
('TM001','Attendees',0),
('TM002','Course Material',0),
('TM003','Environment',0);
 insert into Associate_Info
(Associate_Id,Salutation,Associate_Name,Associate_Location,Associate_Track,Associate_Qualification,Associate_Email,Associate_Password) values 
('A001', 'Miss.', 'GAYATHRI NARAYANAN', 'Gurgaon', 'Java', 'Bachelor of Technology', 'Gayathri.Narayanan@hp.com', 'tne1@123'),
('A002', 'Mrs.', 'RADHIKA MOHAN', 'Kerala', 'Java', 'Bachelor of Engineering In Information Technology', 'Radhika.Mohan@cognizant.com', 'tne2@123'),
('A003', 'Mr.', 'KISHORE SRINIVAS', 'Chennai', 'Java', 'Bachelor of Engineering In Computers', 'Kishore.Srinivas@ibm.com', 'tne3@123'),
('A004', 'Mr.', 'ANAND RANGANATHAN', 'Mumbai', 'DotNet', 'Master of Computer Applications', 'Anand.Ranganathan@finolex.com', 'tne4@123'),
('A005', 'Miss.', 'LEELA MENON', 'Kerala', 'Mainframe', 'Bachelor of Engineering In Information Technology', 'Leela.Menon@microsoft.com', 'tne5@123'),
('A006', 'Mrs.', 'ARTI KRISHNAN', 'Pune', 'Testing', 'Master of Computer Applications', 'Arti.Krishnan@cognizant.com', 'tne6@123');
INSERT INTO Questions (Question_Id, Module_Id, Question_Text) VALUES
('Q001', 'EM001', 'Instructor knowledgeable and able to handle all your queries'),
('Q002', 'EM001', 'All the topics in a particular course handled by the trainer without any gaps or slippages'),
('Q003', 'EM002', 'The course materials presentation, handson, etc. refered during the training are relevant and useful.'),
('Q004', 'EM002', 'The Hands on session adequate enough to grasp the understanding of the topic.'),
('Q005', 'EM002', 'The reference materials suggested for each module are adequate');
INSERT INTO Associate_Status (Associate_Id, Module_Id, Batch_Id, Trainer_Id, Start_Date, End_Date) VALUES
('A001', 'O10SQL', 'B001', 'F001', '2000-12-15', '2000-12-25'),
('A002', 'O10SQL', 'B001', 'F001', '2000-12-15', '2000-12-25'),
('A003', 'O10SQL', 'B001', 'F001', '2000-12-15', '2000-12-25'),
('A001', 'O10PLSQL', 'B002', 'F002', '2001-02-01', '2001-02-12'),
('A002', 'O10PLSQL', 'B002', 'F002', '2001-02-01', '2001-02-12'),
('A003', 'O10PLSQL', 'B002', 'F002', '2001-02-01', '2001-02-12'),
('A001', 'J2SE', 'B003', 'F003', '2002-08-20', '2002-10-25'),
('A002', 'J2SE', 'B003', 'F003', '2002-08-20', '2002-10-25'),
('A001', 'J2EE', 'B004', 'F004', '2005-12-01', '2005-12-25'),
('A002', 'J2EE', 'B004', 'F004', '2005-12-01', '2005-12-25'),
('A003', 'J2EE', 'B004', 'F004', '2005-12-01', '2005-12-25');
 update Trainer_Info 
 set Trainer_Password= 'nn4@123'
 where Trainer_Id='F004';
 
 delete from Associate_Status
 where
 Associate_Id='A003'
 and Module_Id='J2EE'
 and Batch_Id='B004'
 and Start_Date = '2005-12-01'
 and  End_Date = '2005-12-25';
 BEGIN;












