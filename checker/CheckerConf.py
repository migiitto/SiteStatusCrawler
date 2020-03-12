class CheckerConf:
    url = ""
    period = 60  # in seconds
    regex = None  # regex pattern for html start and end tags

    def __init__(self, url="", period=60, regex=None):
        self.url = url
        if period < 60:
            self.period = 60
        else:
            self.period = period
        self.regex = regex

    def hasRegex(self):
        return self.regex is None

    @staticmethod
    def fromSQL(url, period, regex):
        return CheckerConf(url, period, regex)
