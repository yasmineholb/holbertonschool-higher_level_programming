-- task 15
SELECT title
FROM tv_genres
LEFT JOIN tv_show_genres ON genre_id = tv_genres.id
LEFT JOIN tv_shows ON show_id = tv_shows.id
WHERE name = "Comedy"
ORDER BY title ASC;
