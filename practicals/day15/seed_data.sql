-- Teacher
INSERT INTO users (name, email, password, role)
VALUES ('Ravi Kumar', 'ravi@besant.com', 'hashed_pw', 'teacher');

-- Students
INSERT INTO users (name, email, password)
VALUES 
('Arjun', 'arjun@student.com', 'hashed_pw'),
('Priya', 'priya@student.com', 'hashed_pw'),
('Meena', 'meena@student.com', 'hashed_pw');

-- Test
INSERT INTO tests (title, created_by_id, time_limit, is_published)
VALUES ('Python Basics Quiz', 1, 30, TRUE);

-- Questions
INSERT INTO questions (test_id, text, question_type, marks)
VALUES
(1, 'Python is a _____ language.', 'mcq', 2),
(1, 'What is a class?', 'text', 5);

-- Options
INSERT INTO options (question_id, text, is_correct)
VALUES
(1, 'Compiled', FALSE),
(1, 'Interpreted', TRUE),
(1, 'Assembly', FALSE);