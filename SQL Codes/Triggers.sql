-- Trigger to keep track of popularity score updation

-- CREATE TABLE popularity_log (
--     tmdb_id INT PRIMARY KEY,
--     old_popularity FLOAT,
--     new_popularity FLOAT,
--     updated_at DATETIME
-- );

DROP TRIGGER IF EXISTS log_popularity_update

DELIMITER //
CREATE TRIGGER log_popularity_update
AFTER UPDATE ON movie_metadata
FOR EACH ROW
BEGIN
    IF OLD.popularity <> NEW.popularity THEN
        INSERT INTO popularity_log (tmdb_id, old_popularity, new_popularity, updated_at)
        VALUES (NEW.tmdb_id, OLD.popularity, NEW.popularity, NOW());
    END IF;
END //
DELIMITER ;

-- Trigger to add limit number of Genres linked to a movie

DROP TRIGGER IF EXISTS CheckGenreLimit

DELIMITER //

CREATE TRIGGER CheckGenreLimit
BEFORE INSERT ON movie_genres
FOR EACH ROW
BEGIN
    DECLARE genre_count INT;
    
    SELECT COUNT(*) INTO genre_count
    FROM movie_genres
    WHERE tmdb_id = NEW.tmdb_id;
    
    IF genre_count >= 10 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot add more than 10 genres for a movie.';
    END IF;
END //

DELIMITER ;

-- Trigger to keep track of ratings deletion

-- CREATE TABLE rating_deletion_audit (
--     user_id INT,
--     movie_id INT,
--     rating FLOAT,
--     deleted_at DATETIME,
--     PRIMARY KEY (user_id , movie_id)
-- );

DROP TRIGGER IF EXISTS LinkDeletionAudit

DELIMITER //

CREATE TRIGGER RatingDeletionAudit
AFTER DELETE ON ratings
FOR EACH ROW
BEGIN
    INSERT INTO rating_deletion_audit (user_id, movie_id, rating, deleted_at)
    VALUES (OLD.user_id, OLD.movie_id, OLD.rating, NOW());
END //

DELIMITER ;
