# rewind

small tool to record online radio on a schedule using streamripper


# Installation and setup

- streamripper must be installed
- setup an SQLite database and run the following query:

``````
CREATE TABLE "scheduled_recordings" ("id" integer,"station_name" text,"show_name" text,"stream_url" text,"processed" integer,"time_start" datetime NOT NULL,"time_stop" datetime,"station_id" int,"show_id" int, "split tracks" int DEFAULT '0', PRIMARY KEY (id));
``````

- set up cronjobs for `````scheduler.py````` to run periodically (e.g. every 5 minutes):

````
python3 scheduler.py
````