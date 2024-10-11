    Here are 10 SQL queries, starting from a simple select and progressively getting more complex, utilizing the **dvdrental** database schema.

### 1. Simple `SELECT`
```sql
SELECT first_name, last_name
FROM actor
LIMIT 10;
```
This query retrieves the first 10 actors' first and last names from the `actor` table.

### 2. `SELECT` with `WHERE` clause
```sql
SELECT title, rental_rate
FROM film
WHERE rental_rate > 2.99
ORDER BY rental_rate DESC;
```
This query retrieves films where the rental rate is greater than $2.99, sorted by rental rate in descending order.

### 3. `SELECT` with `JOIN`
```sql
SELECT f.title, c.name AS category_name
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
ORDER BY f.title;
```
This query retrieves the titles of films and their corresponding categories, sorted by film title.

### 4. `SELECT` with Aggregation (`COUNT`)
```sql
SELECT c.name AS category, COUNT(f.film_id) AS total_films
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
ORDER BY total_films DESC;
```
This query retrieves the number of films in each category, sorted by the category with the most films.

### 5. `SELECT` with `LEFT JOIN` and `COALESCE`
```sql
SELECT cu.first_name, cu.last_name, COALESCE(cu.email, 'No Email') AS email
FROM customer cu
LEFT JOIN payment p ON cu.customer_id = p.customer_id
WHERE cu.activebool = true
ORDER BY cu.last_name;
```
This query retrieves all active customers, showing their email if available, or 'No Email' if not.

### 6. `SELECT` with Date Function (`NOW()`)
```sql
SELECT r.rental_id, r.rental_date, r.return_date, 
       CASE 
           WHEN r.return_date IS NULL THEN 'Still Rented'
           ELSE 'Returned'
       END AS rental_status
FROM rental r
WHERE r.rental_date >= NOW() - INTERVAL '1 month';
```
This query retrieves rentals made within the last month, indicating whether the rental has been returned or not.

### 7. `JOIN` with Multiple Conditions
```sql
SELECT f.title, l.name AS language, f.rental_duration, f.rental_rate
FROM film f
JOIN language l ON f.language_id = l.language_id
WHERE f.rental_duration > 5 AND l.name = 'English'
ORDER BY f.title;
```
This query retrieves English films with a rental duration greater than 5 days, sorted by title.

### 8. `SUM` Aggregation with `JOIN`
```sql
SELECT s.store_id, s.manager_staff_id, SUM(p.amount) AS total_sales
FROM store s
JOIN payment p ON s.store_id = p.staff_id
GROUP BY s.store_id, s.manager_staff_id
ORDER BY total_sales DESC;
```
This query calculates the total sales for each store and displays the store's manager ID.

### 9. Complex Query with `HAVING` Clause
```sql
SELECT cu.customer_id, cu.first_name, cu.last_name, SUM(p.amount) AS total_payments
FROM customer cu
JOIN payment p ON cu.customer_id = p.customer_id
GROUP BY cu.customer_id, cu.first_name, cu.last_name
HAVING SUM(p.amount) > 100
ORDER BY total_payments DESC;
```
This query retrieves customers who have made payments totaling more than $100, sorted by total payments.

### 10. Nested Subquery with `IN`
```sql
SELECT f.title
FROM film f
WHERE f.film_id IN (
    SELECT r.inventory_id
    FROM rental r
    WHERE r.customer_id = 1
);
```
This query retrieves all films rented by a specific customer with `customer_id = 1`.
