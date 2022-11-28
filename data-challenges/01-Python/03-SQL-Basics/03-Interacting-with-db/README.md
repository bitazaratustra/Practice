## Background & Objectives

The goal of this challenge is to explore a [SQLite](http://en.wikipedia.org/wiki/SQLite) database to understand its schema.

## Tool

Download and install [DBeaver](https://dbeaver.io/), a free and open source powerful tool to connect to any database, explore the schema and even **run SQL queries**.

## Data

The data for SQL challenges is stored online and can be accessed through a URL.

In each SQL challenge you will find an empty directory named `data`.

As a good practice all data files, `.csv`, `.sqlite`, etc. should be stored in these folders.

Your first task is to download the databases so that you can work with them locally.

As a reminder of Data Sourcing yesterday, here are two ways of doing so:

*User's way:* through the Web Browser
1. Open your web browser
2. Navigate to the URL provided
3. When prompted to, choose to save the file on your computer
4. If needed, find the file and move/copy it in the challenge `data` directory

*Hacker's way:* through the CLI
1. Open your terminal
2. `curl <URL> > <target-path>`

### Movies Database
We will work with the `movies.sqlite` database, available at this URL:
`https://wagon-public-datasets.s3.amazonaws.com/sql_databases/movies.sqlite`

In your terminal, Copy/paste and execute the curl command below to download the database into the `data` directory of this challenge.
```bash
curl https://wagon-public-datasets.s3.amazonaws.com/sql_databases/movies.sqlite \
> ~/code/<user.github_nickname>/{{local_path_to("01-Python/03-SQL-Basics/03-Interacting-with-db")}}/data/movies.sqlite
```

<details>
  <summary markdown='span'>
    <strong>⚠️ For Windows/WSL2 Users </strong>
    <span class="icon"> ⚠️👈 (Click me!)</span>
  </summary>

  DBeaver is installed on Windows and by default does not have enough rights to access files on your Ubuntu file system.

  As a workaround for this, you can simply copy the downloaded file onto your Windows file system.

  Here is an [article](https://lewagon.notion.site/Ubuntu-x-WSL2-x-Windows-7675feb26a644306881b7365d5154204) on how to easily copy or move files between Windows and Ubuntu.

  ---
</details>
<br>

## Specs

### Database schema

Open DBeaver and connect to the `data/movies.sqlite` database. Then explore the different tables to answer the following questions:

- What are the tables and the relationships between tables?
- What are the columns and their types?

Use [db.lewagon.com](http://db.lewagon.com/) to draw this movies database schema.
To check your solution, click on "Save / Load", then "Save XML", copy/paste the generated XML code in `movies.xml`. You can then `make` to check your solution.

### Run SQL queries

Open a new SQL editor and run some SQL queries to anwer to following question:

How many rows does each table contain?
