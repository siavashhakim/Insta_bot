from instapy import InstaPy
import pandas as pd

input = pd.read_csv('input_credentials.csv')

session = InstaPy(username=input.Username[0], password=input.Password[0], headless_browser=True)
session.login()

user_following = session.grab_following(username="30avashhe", amount="full")
##now, `lazySmurf_following` variable which is a list- holds the `Following` data of "lazy.smurf" at requested time