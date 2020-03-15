# SiteStatusCrawler
A simple site status crawler with database backed site configuration. Tested and developed for python3(.7).

# Test coverage

Name / Stmts / Miss / Cover

TOTAL / 189 / 24 / 87%


# Running the crawler
- Configure environment parameters in config.py. The tests will validate if the given settings are valid.
- Install requirements `pip(3) install -r requirements.txt`
- Add a couple of sites into db e.g.
`INSERT INTO sites(name, url, frequency, regex) VALUES("Google", "https://www.google.com", 120, "<title[^>]*>(.*?)</title>")`
- Run consumer with "python3 consumer.py"
- Run producer with "python3 producer.py"
- Exiting works with Ctrl-C on both pieces, do note that some editors (such as PyCharm) won't pass the signal correctly on all platforms. 
# Running the tests
No coverage: `python3 tests.py`

Coverage: `coverage run -m unittest discover` (remember to install coverage first!) 
