DROP TABLE IF EXISTS Attends;
DROP TABLE IF EXISTS Lecture;
DROP TABLE IF EXISTS Module;
DROP TABLE IF EXISTS Student;



-- ======================
-- Student
-- ======================
CREATE TABLE Student (
    studentID INTEGER PRIMARY KEY,
    attendedLectures INTEGER
);

-- ======================
-- Module
-- ======================
CREATE TABLE Module (
    moduleID INTEGER PRIMARY KEY,
    numLectures INTEGER
);

-- ======================
-- Lecture
-- ======================
CREATE TABLE Lecture (
    lectureID INTEGER PRIMARY KEY,
    moduleID INTEGER NOT NULL,
    lecturerID INTEGER NOT NULL,
    wordStart TEXT NOT NULL,
    wordEnd TEXT NOT NULL,

    FOREIGN KEY (moduleID) REFERENCES Module(moduleID)
);

-- ======================
-- Attends (attendance event)
-- ======================
CREATE TABLE Attends (
    lectureID INTEGER NOT NULL,
    studentID INTEGER NOT NULL,
    seatNum INTEGER NOT NULL,

    PRIMARY KEY (lectureID, studentID),

    FOREIGN KEY (lectureID) REFERENCES Lecture(lectureID),
    FOREIGN KEY (studentID) REFERENCES Student(studentID),

    UNIQUE (lectureID, seatNum)
);