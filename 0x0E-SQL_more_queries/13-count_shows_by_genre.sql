-- Script to list all genres in hbtn_0d_tvshows and display the number of shows linked to each
SELECT tv_genres.name AS "genre", COUNT(*) AS "number_shows"
FROM tv_genres JOIN tv_show_genres
WHERE tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
