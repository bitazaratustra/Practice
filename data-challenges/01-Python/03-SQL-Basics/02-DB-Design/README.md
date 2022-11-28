
## Background & Objectives

The goal of this challenge is to become familiar with database design, a crucial skill to explore a database.

## Specs

### Movie database design

There are many ways to build a movie database, but let's start by building a basic system with `users`, `movies` and `views`.

Here are the requirements of our system:

- A `user` has a `first_name`, `last_name`, an `age` and an `email`.
- A `movie` has a `title`, a `release_year` and a `rating`.
- A `user` can `view` many `movies`.
- A `movie` can be `viewed` by many `users`.
- A `view` is defined by a `date`.

Which columns are primary keys? Which are foreign keys? What is the relationship between tables? How do we call the `views` table?

### Design the schema

Design the database schema for a movie database that meets these requirements.
For this, you must use the [SQL Designer](http://db.lewagon.com).
To check your solution, click on "Save / Load", then "Save XML", copy/paste the generated XML code in `movies.xml`. You can then `make` to check your solution.
If you see a weird error, double check the syntax of your named columns and tables.

## Key learning points

- Become comfortable with using the [SQL Designer](http://db.lewagon.com) tool to build a multi-table database schema.
- Understand the difference between primary key and foreign key.
- Understand the difference between [`1:N` and `N:N` relationships](https://en.wikipedia.org/wiki/Cardinality_(data_modeling))
