import operator
from stat import ST_CTIME
import os, sys, time


class LatestJpg:

    def __init__(self, mydir: str = None):
        if mydir is None:
            self.path = str(os.getcwd()) + '/'
        else:
            os.chdir(mydir)
            self.path = str(os.getcwd()) + '/'

        self.files = os.listdir(self.path)

    def mostrecentfile(self):
        all_files = os.listdir(self.path)
        file_times = dict()
        for e in all_files:
            filename, file_extension = os.path.splitext(e)
            file_extension = file_extension.strip().upper()
            if file_extension in ["JPG","JPEG"]:
                file_times[e] = time.time() - os.stat(e).st_ctime
        if len(file_times) > 0:
            return sorted(file_times.items(), key=operator.itemgetter(1))[0][0]
        else:
            return ""


