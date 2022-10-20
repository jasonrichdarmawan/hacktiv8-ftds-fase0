# dataset 3

https://drive.google.com/file/d/1jx3NVT-WpZhYvghu6jOv1m1HBoIUDk8D/view?usp=sharing

https://drive.google.com/file/d/1h-0bMZpzP8NqaXi0ss3Rb1bdpm9Ma3JJ/view?usp=sharing

```
SELECT * FROM hacktiv8.teams;
SELECT * FROM hacktiv8.players;

SELECT teams.conference AS conference,
       players.year,
       COUNT(1) AS players
  FROM hacktiv8.players players
  JOIN hacktiv8.teams teams
    ON teams.school_name = players.school_name
# 1, 2 == index columns from SELECT
GROUP BY 1, 2
ORDER BY conference, year;

SELECT conference,
	   SUM(CASE WHEN year = 'FR' THEN players ELSE NULL END) AS fr,
       SUM(CASE WHEN year = 'SO' THEN players ELSE NULL END) AS so,
       SUM(CASE WHEN year = 'JR' THEN players ELSE NULL END) AS jr,
       SUM(CASE WHEN year = 'SR' THEN players ELSE NULL END) AS sr
 FROM (
  SELECT teams.conference AS conference,
         players.year,
         COUNT(1) AS players
  FROM hacktiv8.players players
  JOIN hacktiv8.teams teams
   ON teams.school_name = players.school_name
  GROUP BY 1,2
 ) sub
GROUP BY 1
ORDER BY 1;

SELECT conference,
       SUM(players) AS total_players,
       SUM(CASE WHEN year = 'FR' THEN players ELSE NULL END) AS fr,
       SUM(CASE WHEN year = 'SO' THEN players ELSE NULL END) AS so,
       SUM(CASE WHEN year = 'JR' THEN players ELSE NULL END) AS jr,
       SUM(CASE WHEN year = 'SR' THEN players ELSE NULL END) AS sr
FROM (
 SELECT teams.conference AS conference,
		players.year,
		COUNT(1) AS players
 FROM hacktiv8.players players
 JOIN hacktiv8.teams teams
  ON teams.school_name = players.school_name
 GROUP BY 1,2
) sub
GROUP BY 1
ORDER BY 2 DESC;
```