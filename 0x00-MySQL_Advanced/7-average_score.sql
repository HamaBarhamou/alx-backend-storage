-- create procedure
-- computes the average score of a student from all their projects
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    SELECT SUM(score) / COUNT(score) INTO @avg_score
    FROM corrections WHERE corrections.user_id=user_id;
    UPDATE users SET average_score=@avg_score WHERE id=user_id;
END;//