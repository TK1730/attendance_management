import datetime

class Timer(object):
    def __init__(self):
        t_delta = datetime.timedelta(hours=9)
        self.JST = datetime.timezone(t_delta, 'JST')

    def GetDate(self):
        self.now = datetime.datetime.now(self.JST)
        return self.now
