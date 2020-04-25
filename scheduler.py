# run this every 5 minutes
import utilities
import datetime
from recording import Recording
import time
import pytz

# connect to database
cur = utilities.get_cursor()

# select all future scheduled recordings not yet processed
cur.execute('SELECT id, station_name, show_name, time_start, time_stop, stream_url FROM scheduled_recordings WHERE processed = 0')
scheduled_recordings = [{'id': row[0], 'station_name': row[1], 'show_name': row[2], 'time_start': datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M %z'), 'time_stop': datetime.datetime.strptime(row[4], '%Y-%m-%d %H:%M %z'), 'stream_url': row[5]} for row in list(cur)]

now = datetime.datetime.now(pytz.utc)

# if any recording scheduled within the next 10 minutes, create Recording object and start record()
recordings=[]
for rec in scheduled_recordings:
    if rec['time_stop'] < now: # if show has already ended
        continue
    if rec['time_start'] < now or abs(rec['time_start'] - now).seconds < 100:
        id = rec['id']
        recordings.append(Recording(stream_url=rec['stream_url'], station_name=rec['station_name'], show_name=rec['show_name'], time_start=rec['time_start'], time_stop=rec['time_stop']).record())
        # Update entry with processed = True
        cur.execute (f'UPDATE scheduled_recordings SET processed = 1 WHERE id={id}')
# wait until all reacordings are finished to keep streamripper process running
while not all([rec.poll() is not None for rec in recordings]):
    time.sleep(1)





