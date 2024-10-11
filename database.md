# dvdrental Database Schema

## Tables and Columns

### actor
- **actor_id** (PK)
- first_name
- last_name
- last_update

### address
- **address_id** (PK)
- address
- address2
- district
- city_id (FK to **city.city_id**)
- postal_code
- phone
- last_update

### category
- **category_id** (PK)
- name
- last_update

### city
- **city_id** (PK)
- city
- country_id (FK to **country.country_id**)
- last_update

### country
- **country_id** (PK)
- country
- last_update

### customer
- **customer_id** (PK)
- store_id
- first_name
- last_name
- email
- address_id (FK to **address.address_id**)
- activebool
- create_date
- last_update
- active

### film
- **film_id** (PK)
- title
- description
- release_year (1901-2155)
- language_id (FK to **language.language_id**)
- rental_duration
- rental_rate
- length
- replacement_cost
- rating ('G', 'PG', 'PG-13', 'R', 'NC-17')
- last_update
- special_features
- fulltext

### film_actor
- **actor_id** (PK, FK to **actor.actor_id**)
- **film_id** (PK, FK to **film.film_id**)
- last_update

### film_category
- **film_id** (PK, FK to **film.film_id**)
- **category_id** (PK, FK to **category.category_id**)
- last_update

### inventory
- **inventory_id** (PK)
- film_id (FK to **film.film_id**)
- store_id
- last_update

### language
- **language_id** (PK)
- name
- last_update

### payment
- **payment_id** (PK)
- customer_id (FK to **customer.customer_id**)
- staff_id (FK to **staff.staff_id**)
- rental_id (FK to **rental.rental_id**)
- amount
- payment_date

### rental
- **rental_id** (PK)
- rental_date
- inventory_id (FK to **inventory.inventory_id**)
- customer_id (FK to **customer.customer_id**)
- return_date
- staff_id (FK to **staff.staff_id**)
- last_update

### staff
- **staff_id** (PK)
- first_name
- last_name
- address_id (FK to **address.address_id**)
- email
- store_id
- active
- username
- password
- last_update
- picture

### store
- **store_id** (PK)
- manager_staff_id (FK to **staff.staff_id**)
- address_id (FK to **address.address_id**)
- last_update

## Data Types and Constraints

- **Primary Keys (PK):** Unique identifiers for each table.
- **Foreign Keys (FK):** Define relationships between tables.
- **rating:** Enum with values ('G', 'PG', 'PG-13', 'R', 'NC-17').
- **release_year:** Integer between 1901 and 2155.

## Relationships

- **film_actor** links films and actors (many-to-many).
- **film_category** links films and categories (many-to-many).
- **customer** references **address** and **store**.
- **address** references **city**; **city** references **country**.
- **inventory** references **film** and **store**.
- **rental** references **inventory**, **customer**, and **staff**.
- **payment** references **customer**, **staff**, and **rental**.
- **staff** references **address** and **store**.
- **store** references **staff** (manager) and **address**.

This concise schema includes all necessary details to construct executable SQL queries against the **dvdrental** database.