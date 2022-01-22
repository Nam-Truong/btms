# Basketball Tournament Management System - BTMS
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
| View scoreboard                               | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| View player's personal details                | :white_check_mark: _only self details_ | :white_check_mark: _only his team_ | :heavy_check_mark: |
| View list of players of a team                | | :white_check_mark: _only his team_ | :heavy_check_mark: |
| View list of 90-percentile avg-scores players | | :white_check_mark: _only his team_ | |
| View Website usage statistics                 | | | :heavy_check_mark: |


_Note: this is a fun project_

## Terminologies and Definitions:

  - **Average score of player**: sum of total scores divided by the number of gaems in which he played.
  - **90th percentile average scores**: the scores which are better than 90 percent of all the others.
  - **Scoreboard**: display of all games, final scores, current round result, winners/losers
  - Website usage statistics:
    + # of times each user logged into the system
    + How much time each user spends on the website totally
    + Which user is currently online (logged-in and viewing the site in a browser) 

 
