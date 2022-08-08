from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
from config import settings


L = instaloader.Instaloader()


PROFILE = settings.insta_username
L.load_session_from_file(PROFILE)

def local_get_profile(USER):
    profile = instaloader.Profile.from_username(L.context, USER)
    return profile

def user_finder(usernames):
    must_be_active_users = []
    for username in usernames:
        string_username = str(username)
        final_username = string_username.replace("(","").replace(")","").replace(",","").replace("'","")
        must_be_active_users.append(final_username)
    return must_be_active_users

def local_get_comments(USER,limit):
    profile = local_get_profile(USER)
    comments = set()
    commenters_dict = {}
    for count,post in enumerate(profile.get_posts()):
        #print(post)
        count = count + 1
        if count <= limit:
            comments = set(post.get_comments())
            commenters = []
            for comment in comments:
                for item in comment:
                    res = isinstance(item, instaloader.structures.Profile)
                    if res == True:
                        commenters.append(item.username)
            commenters_dict[count] = commenters
        else:
            break
    return commenters_dict

def validate_commenters(userslist,commenters_dict):
    final_dict = {}
    for key1 in commenters_dict.keys():
        uncommenters = []
        for user in userslist:
            if user not in commenters_dict[key1]:
                uncommenters.append(user)
        final_dict[key1] = uncommenters
    return final_dict
