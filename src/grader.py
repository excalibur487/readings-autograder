import csv
import piazza_api
from piazza_api import Piazza

p = Piazza()
# Prompt for email and password
p.user_login()

# Replace with class code (whatever comes after "class/" in the url)
csc110 = p.network("llbcl58pjkd113")
post_output = open("OUT.txt", "w")

while True:
    post_num = input("Enter reading post number: ")
    try:
        # get the post dictionary
        post = csc110.get_post(post_num)
        break
    except piazza_api.exceptions.RequestError as error:
        print("Oops! Post does not exist")

# dictionary to keep track of scores {userid:score}
scores = {}
# maps student uid to student name
studentmap = {}

# get all students
global_users = csc110.get_all_users()
for user in global_users:
    # if user is not staff
    if not user.get('admin'):
        scores[user.get('id')] = 0
        studentmap[user.get('id')] = user.get('name')

# Count posts per user in thread
for change in post.get('change_log'):
    curr_id = change.get('uid')
    if curr_id is not None:
        curr_score = scores.get(curr_id)
        # If no posts made, set score to 70, if one already made, set to 100
        scores[curr_id] = 70 if curr_score == 0 else 100

# List of dictionaries with name, score as key value pairs (to work with csv files)
scores_list=[]
for uid in scores:
    scores_list.append({'Name':studentmap.get(uid), 'Score': scores.get(uid)})

# Output scores csv
fields = ['Name', 'Score']
with open('scores.csv', 'w') as csvf:
    writer = csv.DictWriter(csvf, fieldnames = fields)
    writer.writeheader()
    writer.writerows(scores_list)
