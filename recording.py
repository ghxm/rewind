import time
import datetime
import subprocess
import utilities

config = utilities.get_config()

class Recording:
    def __init__(self, stream_url, station_name, show_name, time_start, time_stop = None, show_length = None, split_tracks = False):
        # @TODO if stations is known automatically select stream url/fallback etc
        self.stream_url = stream_url
        self.station_name = station_name
        self.show_name = show_name
        self.time_start = time_start
        self.time_stop = time_stop
        self.show_length = show_length # calculate if not given
        self.split_tracks = split_tracks

        if self.show_length is None:
            self.show_length = abs(self.time_start-self.time_stop).seconds

    def record(self):
        # wait for show to start
        while abs(datetime.datetime.now(datetime.timezone.utc) - self.time_start).seconds < 30: # seconds before show
            time.sleep(1)
        # start ripping
        return subprocess.Popen(f'{config.get("STREAMRIPPER", "path")} {self.stream_url} -d {config.get("STREAMRIPPER", "outpath")} -a %d_%S {"-A" if not self.split_tracks else ""} -l {self.show_length+30}', shell = True)




