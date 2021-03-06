# Basketball Tournament Management System - BTMS
_Note: this is a fun project_

Suppose there are 16 basketball teams, each of which is comprised of 10 players, playing a tournament with 4 rounds as follows:

| Round | # of Teams | # of Games |
|-------|------------|------------|
| 1     | 16         | 8          |
| 2     | 8          | 4          |
| 3     | 4          | 2          |
| 4     | 2          | 1          |

BTMS will monitor the following statistics:
  - Team rankings
  - Player's average scores
  - Player's personal details: name, height, average score, number of participated games
  - Website usage 

There are 3 types of user with role-based access control as below:

|                                               | Player | Coach | Tournament Admin | 
|-----------------------------------------------|--------|-------|------------------|
| View scoreboard                               | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| View player's personal details                | :white_check_mark: <br />_only self details_ | :white_check_mark: <br />_only own team_ | :white_check_mark: |
| View list of players of a team                | | :white_check_mark: <br />_only own team_ | :white_check_mark: |
| View list of 90-percentile avg-scores players | | :white_check_mark: <br />_only own team_ | |
| View Website usage statistics                 | | | :white_check_mark: |




## Terminologies and Definitions:

  - **Average score of player**:
    + Sum of total scores divided by the number of gaems in which he played.
  - **90th percentile average scores**:
    + The scores which are better than 90 percent of all the others.
  - **Scoreboard**:
    + Display of all games, final scores, current round result, winners/losers
  - **Website usage statistics**:
    + Number of times each user logged into the system
    + How much time each user spends on the website totally
    + Which user is currently online (logged-in and viewing the site in a browser) 

 
## Development

1. Postgres (PostgreSQL) 13.3
2. Python 3.9.7
3. Django 3.2.7


### 1. Create a DEV database
1. Log into PostgreSQL using default user `postgres`:
  - `psql -U postgres`

    _Note: enter your predefined password which was set during PostgreSQL installation_

2. Enter the following commands:
  ```
  CREATE DATABASE btms;
  CREATE ROLE btms WITH PASSWORD 'password' LOGIN;
  GRANT ALL PRIVILEGES ON DATABASE btms TO btms;
  ```

3. To simulate data of players, coaches, admin, games, scores, etc., use the following commands:
  ```
  cd BTMS
  python3 manage.py simulate_db 4
  ```
  _Note: The tournament has totally 4 rounds. So, the above command will simulate entire tournament results, i.e. the tournament ended. However, if execute **simulate_db 2**, it will simuate data showing that the tournament has just completed the 2nd round._

4. To delete all database data, use this command:
  `python3 manage.py delete_db`
## Reference
https://docs.djangoproject.com/en/4.0/intro/tutorial02/
