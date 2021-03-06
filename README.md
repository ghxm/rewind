# rewind

scheduled audio stream recordings using streamripper

# Installation and setup

- ```streamripper``` must be installed
- setup an SQLite database and run the following query:

``````
CREATE TABLE "scheduled_recordings" ("id" integer,"station_name" text,"show_name" text,"stream_url" text,"processed" integer,"time_start" datetime NOT NULL,"time_stop" datetime,"station_id" int,"show_id" int, "split tracks" int DEFAULT '0', PRIMARY KEY (id));
``````

- clone this repository
    - rename ```config.ini.template``` to ```config.ini```
    - adjust configurations in  ```config.ini```
- set up cronjobs for `````scheduler.py````` to run periodically (e.g. every 6 minutes, repeat time should ideall be larger than ```10/2``` as 10 minutes is the default time until the start of a scheduled recording that triggers an actual recording):

````
6 * * * * /home/<user>/rewind/venv/python /home/user/rewind/scheduler.py
````

# Usage

- In order to schedule a recording, add a new row to ```scheduled_recordings``` with ```processed```set to ```0``` and timezone-aware start and end times
