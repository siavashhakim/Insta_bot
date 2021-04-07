from instapy import InstaPy
import pandas as pd

input = pd.read_csv('input_credentials.csv')

session = InstaPy(username=input.Username[0], password=input.Password[0], headless_browser=True)
session.login()
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.set_relationship_bounds(enabled=True, max_followers=18000)
session.like_by_tags(["puppy", "husky", "cutepuppy","huskylife","huskylovers","huskyphotography",'puppylife'], amount=10)
session.set_dont_like(["naked", "nsfw"])
# session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Cute! :heart_eyes:", "lovely! :heart_eyes:", "Beautiful :heart_eyes:"])
session.end()