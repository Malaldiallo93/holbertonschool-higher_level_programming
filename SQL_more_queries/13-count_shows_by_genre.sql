-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_genres.genre_id AS genre, 
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
ORDER BY number_of_shows DESC;