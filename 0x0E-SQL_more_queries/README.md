# Project: 0x0E SQL - More Queries

## Overview

The 0x0E SQL - More Queries project is a hands-on learning experience focused on deepening your understanding of SQL, specifically using MySQL. The project covers various tasks related to user management, database creation, and executing complex queries.

## Key Objectives

- Manage MySQL users and implement privileges
- Work with constraints like PRIMARY KEY and FOREIGN KEY
- Utilize advanced SQL techniques, including subqueries, joins, and unions
- Design and create tables with specific constraints

## Project Structure

| Script                   | Description                                                                                   |
|--------------------------|-----------------------------------------------------------------------------------------------|
| 0-privileges.sql         | Lists all privileges of MySQL users `user_0d_1` and `user_0d_2`.                               |
| 1-create_user.sql        | Creates the MySQL server user `user_0d_1` with full privileges.                                 |
| 2-create_read_user.sql   | Creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege.                |
| 3-force_name.sql         | Creates the table `force_name` with specific constraints.                                       |
| 4-never_empty.sql        | Creates the table `id_not_null` with a default value for `id`.                                  |
| 5-unique_id.sql          | Creates the table `unique_id` with a unique constraint on `id`.                                  |
| 6-states.sql             | Creates the database `hbtn_0d_usa` and the table `states`.                                      |
| 7-cities.sql             | Creates the database `hbtn_0d_usa` and the table `cities` with a foreign key constraint.        |
| 8-cities_of_california_subquery.sql | Lists all cities of California without using JOIN.                                  |
| 9-cities_by_state_join.sql           | Lists all cities with their respective states using JOIN.                              |
| 10-genre_id_by_show.sql              | Lists shows from `hbtn_0d_tvshows` with at least one genre linked.                       |
| 11-genre_id_all_shows.sql            | Lists all shows from `hbtn_0d_tvshows` with their respective genre IDs.                |
| 12-no_genre.sql                      | Lists shows from `hbtn_0d_tvshows` without a linked genre.                              |
| 13-count_shows_by_genre.sql          | Displays the number of shows linked to each genre.                                      |
| 14-my_genres.sql                     | Lists all genres of the show "Dexter".                                                  |
| 15-comedy_only.sql                   | Lists all Comedy shows.                                                                  |
| 16-shows_by_genre.sql                | Lists all shows and linked genres.                                                      |
| 100-not_my_genres.sql                | Lists genres not linked to the show "Dexter".                                           |
| 101-not_a_comedy.sql                 | Lists shows without the genre "Comedy".                                                 |
| 102-rating_shows.sql                 | Lists shows from `hbtn_0d_tvshows_rate` by their rating.                                 |

