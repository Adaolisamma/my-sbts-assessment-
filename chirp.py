users = {}
posts = {}
def create_user(username):
    username = username.lower().strip()
    if username == "":
        return{"message": "username cannot be empty", "data" : "error"}
    if username in users:
        
        return {"message": "username already exist, please choose another name"}
    users[username] = {}

    return {"message": "username craeted successfully"}

       
# print(create_user("Ada"))
# print(create_user("Ken"))
# print(users)
# print(create_user(""))

def create_post(username, text):
    username = username.strip().lower()

    # username = 
    text = text.strip()
    if username not in users:
        return{"Error": "You dont exist in our database3, please register"}
    post_id = len(posts) +1
    posts[post_id] = {"author":username, "text":text, "likes" : 0}
    x = {"message" : "your post has been added", "post_id": post_id, **posts[post_id]}
    return(x)

# print(create_post("users", "details"))
# print(create_post)
# 
print(create_user("Ada"))         
print(create_post("Ada", "This is my first post"))

def liking_posts(post_id):
    try:
        post_id = int(post_id)
    except ValueError:
        return {"error_message": "post_id can only be an integer"}
    if post_id not in posts:
        return{"Error_message": "posts not in our database"}
    posts[post_id]["likes"] +=1
    return{"post":{"id": post_id, **posts[post_id]}}
    
    
        
print(liking_posts(1))


def follow(follower, followee):
    follower = follower.lower().strip()
    followee = followee.lower().strip()
#     if followee not in users:
#         return{"Error message": "not a registered user"}
#     if follower not in users:
#         return{"Error message": "not a registered user in our DBMS"}
#     if followee in users:
#         return{"message": "you are a registered user"}
#     if follower in users:
#         return{"message": "thank you for resgistering"}
#     if followee == follower:
#         return{"message": "we are mutuals"}

# print(follow)

def create_profile(username):
    username = username.strip().lower()
    if username not in users:
        return{"error message":"You are not a user,please create a profile"}
    user_posts = []
    for post_id, posts in posts.items():
        if posts["author"] == username:
            user_posts.append({"id":post_id, **posts})
        return{"user":username, "following": users[username]["following"], "posts": user_posts}
    
print(users)
print(create_profile("username"))
def get_feed(username):
    username =""

    if username not in users:
        return{"error": "user not in the database"}
    feed = []
    following = users[username]["following"]
    for post_id, post_id in posts.items():
        if posts["author"] in following:
            feed.append({"id": post_id, **posts})

            return{"feed":feed}
print(get_feed(users))