-- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)
SELECT `tv_genres_name`, `rating.COUNT(*)`
FROM `hbtn_0d_tvshows_rate`
