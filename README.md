# PPS - Pogs Per Second
## Structure  
REQ: https://github.com/PetterKraabol/Twitch-Chat-Downloader
```mermaid
sequenceDiagram
tcd-->cron: Pull recent chat logs
break only pull vods once
tcd-->cron: stop pull
end
cron-->api: pass chat logs
db-->api: record transformed logs

```
- need good way to insightfully represent emotes in a time period  
- identify high emote density moments  
- a good way to transform and store emote data from a vod, along with its time data  
- endpoints to return insightful data / moments

