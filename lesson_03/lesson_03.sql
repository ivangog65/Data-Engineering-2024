/*
 Завдання на SQL до лекції 03.
 */

/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
SELECT c.name AS category_name, COUNT(1) AS films_count
FROM film f
         INNER JOIN film_category fc ON f.film_id = fc.film_id
         INNER JOIN category c ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY films_count DESC;

/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
SELECT a.actor_id AS actor_id, a.first_name AS first_name, a.last_name AS last_name
FROM actor a
         JOIN film_actor fa ON a.actor_id = fa.actor_id
         JOIN film f ON fa.film_id = f.film_id
         JOIN inventory i ON f.film_id = i.film_id
         JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY a.actor_id
ORDER BY COUNT(1) DESC
LIMIT 10;

/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
SELECT c.name AS category_name
FROM category c
         JOIN film_category fc ON c.category_id = fc.category_id
         JOIN film f ON fc.film_id = f.film_id
         JOIN inventory i ON f.film_id = i.film_id
         JOIN rental r ON i.inventory_id = r.inventory_id
         JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY SUM(p.amount) DESC;

/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
SELECT f.title AS title
FROM film f
         LEFT JOIN inventory i ON f.film_id = i.film_id
WHERE i.film_id IS NULL;

/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
SELECT a.actor_id AS actor_id, a.first_name AS first_name, a.last_name AS last_name
FROM actor a
         JOIN film_actor fa ON a.actor_id = fa.actor_id
         JOIN film f ON fa.film_id = f.film_id
         JOIN film_category fc ON f.film_id = fc.film_id
         JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Children'
GROUP BY a.actor_id
ORDER BY COUNT(1) DESC
LIMIT 3;
