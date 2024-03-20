-- Top 5 Collaborations of Director and Actors based on count

DROP PROCEDURE IF EXISTS GetDirectorCollaborations

DELIMITER //

CREATE PROCEDURE GetDirectorCollaborations(IN director_name VARCHAR(255))
BEGIN
SELECT 
    casts.name AS 'Cast Name',
    GROUP_CONCAT(title) AS 'Collaborated Movies',
    COUNT(*) AS 'Total Number of Collaborations'
FROM
    casts
        JOIN
    movie_casts ON casts.credit_id = movie_casts.credit_id
        JOIN
    movie_crews ON movie_casts.tmdb_id = movie_crews.tmdb_id
        JOIN
    crews ON crews.credit_id = movie_crews.credit_id
        JOIN
    movie_metadata ON movie_metadata.tmdb_id = movie_crews.tmdb_id
WHERE
    crews.name = director_name
        AND department = 'Directing'
GROUP BY casts.name
ORDER BY COUNT(*) DESC
LIMIT 10;
END //

DELIMITER ;

CALL GetDirectorCollaborations('Aki Kaurismäki');

-- Filter the movies by genre and language

DROP PROCEDURE IF EXISTS GenreFilter

DELIMITER //

CREATE PROCEDURE GenreFilter(IN genre_name VARCHAR(255), IN language_code VARCHAR(255), IN lim int)
BEGIN
SELECT 
    original_title AS 'Movie Title', release_date AS 'Release Date', overview AS 'Synopsis', runtime AS 'Runtime'
FROM
    movie_metadata
        JOIN
    movie_genres ON movie_genres.tmdb_id = movie_metadata.tmdb_id
        JOIN
    genres ON genres.genres_id = movie_genres.genres_id
WHERE
    genres.name = genre_name
        AND movie_metadata.original_language = language_code
ORDER BY popularity desc
LIMIT lim;
END //
DELIMITER ;

CALL GenreFilter('Action', 'ja', 5);
 

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

