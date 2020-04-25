import time
import datetime
import subprocess
import utilities
import re
import pytz
config = utilities.get_config()

class Recording:
    def __init__(self, stream_url, station_name, show_name, time_start = None, time_stop = None, show_length = None, split_tracks = False):
        # @TODO if stations is known automatically select stream url/fallback etc
        self.stream_url = stream_url
        self.station_name = station_name
        self.show_name = show_name
        if time_start == None:
            self.time_start = datetime.datetime.now(pytz.utc)
        else:
            self.time_start = time_start
        self.time_stop = time_stop
        if show_length is not None:
            self.show_length = int(show_length) # calculate if not given
            self.time_stop = self.time_start + datetime.timedelta(seconds = show_length)
        else:
            self.show_length = abs(self.time_start-self.time_stop).total_seconds()
        self.split_tracks = split_tracks

    def record(self):
        # wait for show to start
        if datetime.datetime.now(pytz.utc) < self.time_start: # if recording start is in the future
            while abs(datetime.datetime.now(pytz.utc) - self.time_start).seconds > 30: # wait until 30 seconds before show
                time.sleep(1)
        # start ripping
        print("starting recording")
        return subprocess.Popen(f'{config.get("STREAMRIPPER", "path")} '
                                f'{self.stream_url} -d {config.get("STREAMRIPPER", "outdir")} '
                                f'-a %d__{re.sub(" ", "_", self.station_name)}__{re.sub(" ", "_", self.show_name)} '
                                f'{"-A" if not self.split_tracks else ""} -l {self.show_length+30}',
                                shell = True)




