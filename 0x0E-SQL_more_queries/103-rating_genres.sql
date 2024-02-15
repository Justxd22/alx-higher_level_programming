-- genre
SELECT tv_genres.name, COALESCE(SUM(tv_show_genres_ratings.rating), 0) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres_ratings ON tv_genres.id = tv_show_genres_ratings.genre_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;