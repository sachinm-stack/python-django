-- USERS
CREATE TABLE users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(10) NOT NULL DEFAULT 'student'
);

-- TESTS
CREATE TABLE tests (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    created_by_id INTEGER NOT NULL,
    time_limit INTEGER DEFAULT 30,
    is_published BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_tests_user
        FOREIGN KEY (created_by_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

-- QUESTIONS
CREATE TABLE questions (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    test_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    question_type VARCHAR(5) NOT NULL,
    marks INTEGER DEFAULT 1,
    CONSTRAINT fk_questions_test
        FOREIGN KEY (test_id)
        REFERENCES tests(id)
        ON DELETE CASCADE
);

-- OPTIONS
CREATE TABLE options (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    question_id INTEGER NOT NULL,
    text VARCHAR(300),
    is_correct BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_options_question
        FOREIGN KEY (question_id)
        REFERENCES questions(id)
        ON DELETE CASCADE
);

-- SUBMISSIONS
CREATE TABLE submissions (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    student_id INTEGER NOT NULL,
    test_id INTEGER NOT NULL,
    score FLOAT,
    submitted_at TIMESTAMP,
    CONSTRAINT fk_submissions_user
        FOREIGN KEY (student_id)
        REFERENCES users(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_submissions_test
        FOREIGN KEY (test_id)
        REFERENCES tests(id)
        ON DELETE CASCADE
);