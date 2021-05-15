from instapy import InstaPy
import pandas as pd
from datetime import datetime
import os

input = pd.read_csv('input_credentials.csv')

session = InstaPy(username=input.Username[0], password=input.Password[0], headless_browser=True)
session.login()

user_following = session.grab_following(username="ab", amount="full")
##now, `lazySmurf_following` variable which is a list- holds the `Following` data of "lazy.smurf" at requested time

today_date = datetime.now()
d_time = today_date.strftime("%d-%m-%Y")

d = {'followers': user_following}
output = pd.DataFrame(data=d)
output.to_csv('list_follower' + d_time + '.csv')


# difference --> new follower
main_dir = os.getcwd()
new_path = main_dir + str('\\'+'list_follower_old.csv')
old_list = pd.read_csv(new_path)

diff_list_new = set(output.followers.tolist()) - set(old_list.followers.tolist())

diff_list_lost = set(old_list.followers.tolist()) - set(output.followers.tolist())

