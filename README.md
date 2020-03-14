# SiteStatusCrawler
A simple site status crawler with database backed site configuration.

#Test coverage

Name                     Stmts   Miss  Cover
--------------------------------------------
checker\CheckerConf.py      28      4    86%
checker\__init__.py          0      0   100%
checker\checker.py          31      9    71%
config.py                   17      0   100%
database\__init__.py         0      0   100%
database\database.py        12      2    83%
sites\__init__.py            0      0   100%
sites\sites.py              32      6    81%
tests.py                    69      3    96%
--------------------------------------------
TOTAL                      189     24    87%


# Running the crawler
- Configure environment parameters in config.py. The tests will validate if the given settings are valid.
- Add a couple of sites into db e.g.
`INSERT INTO sites(name, url, frequency, regex) VALUES("Google", "https://www.google.com", 120, "<title[^>]*>(.*?)</title>")`
- Run consumer with "python3 consumer.py"
- Run producer with "python3 producer.py"