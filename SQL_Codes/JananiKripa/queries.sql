-- Count the number of movies produced by each production company:
select pc.name as production_company, COUNT(*) as movie_count from Movie_metadata m join Movie_Production_Companies mpc on m.tmdb_id = mpc.tmdb_id join Production_Companies pc 
on mpc.production_companies_id = pc.production_companies_id group by pc.name;


-- Retrieve movies with their associated production companies:
select m.title, pc.name as production_company from Movie_metadata m join Movie_Production_Companies mpc 
on m.tmdb_id = mpc.tmdb_id join Production_Companies pc on mpc.production_companies_id = pc.production_companies_id

-- Retrieve all search history records for a specific user:
select * from SearchHistory where user_id = 123; -- Replace 123 with the actual user ID


-- Retrieve all view history records for a specific user:
select * from ViewHistory where user_id = 456; -- Replace 456 with the actual user ID

-- Delete all search history records older than 6 months:
delete from SearchHistory where search_date < DATE_SUB(NOW(), INTERVAL 6 MONTH);


-- Retrieve the top 10 users with the highest number of view history records:
select u.user_id, u.username, u.email, COUNT(vh.view_id) AS total_views from Users u left join ViewHistory vh on u.user_id = vh.user_id group by u.user_id order by total_views desc limit 10;
