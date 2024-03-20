-- Task 7 Average score
-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_score DECIMAL(10, 2);
    
    -- Compute the average score
    SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = user_id;
    
    -- Store the average score
    UPDATE users SET average_score = average_score WHERE id = user_id;
END;
//

DELIMITER ;
