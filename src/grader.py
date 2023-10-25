import csv
import piazza_api
from piazza_api import Piazza


def main():  
    p = Piazza()
    
    # Prompt for email and password
    p.user_login()

    # Replace with class code (whatever comes after "class/" in the url)
    csc110 = p.network("llbcl58pjkd113")

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
    student_names_map = {}

    init_scores(csc110, scores, student_names_map),
    grade(post, scores) # should update scores
    scores_to_csv(scores, student_names_map)

# Initializes all maps (all scores to zero and map user ids to users' names)
def init_scores(course, user_score_map, user_to_name_map):
    global_users = course.get_all_users()
    for user in global_users:
        # if user is not staff
        if not user.get('admin'):
            # Set everyone's score to zero
            user_score_map[user.get('id')] = 0
            # Map user's id to their name
            user_to_name_map[user.get('id')] = user.get('name')

# Grades post
def grade(post, user_score_map):
    # Search change_log for user ids that made changes to the thread
    for change in post.get('change_log'):
        curr_id = change.get('uid')
        if curr_id is not None:
            curr_score = user_score_map.get(curr_id)
            # If no posts made, set score to 70, if one already made, set to 100
            user_score_map[curr_id] = 70 if curr_score == 0 else 100

# Outputs scores to a csv with headers: Name | Score
def scores_to_csv(user_score_map, user_to_name_map):
    scores_list=[]
    for uid in user_score_map:
        scores_list.append({'Name':user_to_name_map.get(uid), 'Score': user_score_map.get(uid)})

    # Output scores csv
    fields = ['Name', 'Score']
    with open('scores.csv', 'w') as csvf:
        writer = csv.DictWriter(csvf, fieldnames = fields)
        writer.writeheader()
        writer.writerows(scores_list)

main()
