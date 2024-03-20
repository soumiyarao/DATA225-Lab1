-- Top 5 Collaborations of Director and Actors based on count

DROP PROCEDURE IF EXISTS GetDirectorCollaborations

DELIMITER //

CREATE PROCEDURE GetDirectorCollaborations(IN director_name VARCHAR(255))
BEGIN
SELECT 
    casts.name AS 'Cast Name', COUNT(*) AS 'Number of Collaborations'
FROM
    casts
        JOIN
    movie_casts ON casts.credit_id = movie_casts.credit_id
        JOIN
    movie_crews ON movie_casts.tmdb_id = movie_crews.tmdb_id
        JOIN
    crews ON crews.credit_id = movie_crews.credit_id
WHERE
    crews.name = 'Aki Kaurismäki'
        AND department = 'Directing'
GROUP BY casts.name
ORDER BY COUNT(*) DESC
LIMIT 5;
END //

DELIMITER ;

CALL GetDirectorCollaborations('Aki Kaurismäki');


 

-- Get Cast List for a movie

DROP PROCEDURE IF EXISTS GetActors;

DELIMITER //

CREATE PROCEDURE GetActors(IN movie_name VARCHAR(255))
BEGIN
SELECT 
    casts.name AS 'Cast Name'
FROM
    casts
        JOIN
    movie_casts ON casts.credit_id = movie_casts.credit_id
        JOIN
    movie_metadata ON movie_metadata.tmdb_id = movie_casts.tmdb_id
WHERE
    movie_metadata.title = movie_name
ORDER BY casts.order_num;
END //
DELIMITER ;

CALL GetActors('Jumanji');

