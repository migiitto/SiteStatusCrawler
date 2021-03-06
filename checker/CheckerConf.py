import json


class CheckerConf:
    id = 0
    name = ""
    url = ""
    period = 60  # in seconds
    regex = None  # regex pattern for html start and end tags

    def __init__(self, id=0, name="", url="", period=60, regex=None):
        self.id = id
        self.name = name
        self.url = url
        if period < 60:
            self.period = 60
        else:
            self.period = period
        self.regex = regex

    def __unicode__(self):
        return "%i. %s - %s - %i (%s)" % (self.id, self.name, self.url, self.period, self.regex)

    def __str__(self):
        return "%i. %s - %s - %i (%s)" % (self.id, self.name, self.url, self.period, self.regex)

    def hasRegex(self):
        return self.regex is None

    def toJSON(self):
        return json.dumps({"id":self.id, "name":self.name, "url":self.url, "period":self.period, "regex":self.regex})

    @staticmethod
    def fromJSON(jsondata):
        parsed = json.loads(jsondata)
        return CheckerConf(parsed["id"], parsed["name"], parsed["url"], parsed["period"], parsed["regex"])

    @staticmethod
    def fromSQL(row):
        return CheckerConf(row[0], row[1], row[2], row[3], row[4])
