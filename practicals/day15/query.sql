SELECT id, title, time_limit
FROM tests
WHERE is_published = TRUE;


SELECT text, question_type, marks
FROM questions
WHERE test_id = 1
ORDER BY id;

SELECT u.name, s.score, s.submitted_at
FROM submissions s
JOIN users u ON s.student_id = u.id
WHERE s.test_id = 1
ORDER BY s.score DESC;


INSERT INTO submissions (student_id, test_id, score, submitted_at)
VALUES (2, 1, 6.5, NOW());

DELETE FROM tests
WHERE id = 1;


SELECT * FROM tests;
SELECT * FROM questions;
SELECT * FROM options;
SELECT * FROM submissions;