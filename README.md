# MovieRecommender Application

## Project Overview
A simple movie recommender web application built on the TMDB API.

### Summary
The MovieRecommender app helps people decide what to watch. Users browse trending movies, search by title, save favorites, and get a "Recommended for you" row based on the movies they saved. The project is designed to be small enough to finish, but complete enough to show real skills: working with an external API, building a full-stack app , writing simple recommendation logic, and deploying a live product.

### Problem and Goal
**Problem:** Choosing a movie takes too long. Huge catalogs, and generic "popular" lists don't reflect personal taste.
**Goal:** Let a user get a useful short lsit of movies in under a minute, wiht no sign-up required for now.
**Personal Goal:** Ship a deployed, well-documented portfolio project that demonstratesAPI integration, clean code and basic testing.

### Core Features
1. Show trending and popular movies from TMDB
2. Search by title
3. Movie detail page (with a 'similar movies' row)
4. A heart button to save favorites
5. A 'Recommended for you' row built from the favorites' list.

### Tech Stack
|Layer        |Choice              |Why                                            |
|:------------|:------------------:|----------------------------------------------:|
| Frontend    | ReactJS and MUI    | Building cleaner components and reusable code.|
| Backend     | NodeJS and Express | To create the backend server                  |
| Data source | TMDB API           | Free rich metadata, built-in recommendations  |
| Storage     | DuckDB             | Unit tests for the recommendation function    |
| Hosting     | Netlify            | Free tier                                     |

