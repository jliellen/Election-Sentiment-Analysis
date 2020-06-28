TRACK_TERMS = ["trump", "biden", "joe biden", "donald trump", "republican", "democratic"]
CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass
