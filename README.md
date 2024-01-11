# WorkDayLeagueBot

Adds you to the @League Discord role at 5 PM and removes it at 9 AM ;)

```
0 0 * * 2-6 docker run --env DISCORD_BOT_TOKEN="YOUR TOKEN" workdayleaguebot main.py add
0 16 * * 1-5 docker run --env DISCORD_BOT_TOKEN="YOUR TOKEN" workdayleaguebot main.py remove
```

<sup>(example in UTC for my timezone)</sup>
