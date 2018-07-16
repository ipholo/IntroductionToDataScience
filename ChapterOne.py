from __future__ import division


def number_of_friends(user):
    return len(user["friends"])


def number_total_connections(users):
    return sum(number_of_friends(user) for user in users)


def possible_friends(users):
    for user in users:
        user["possible_friend"] = []
        for friend in user["friends"]:
            for possible_friend in users[friend]["friends"]:
                if possible_friend not in user["friends"] and \
                   possible_friend not in user["possible_friend"] and \
                   possible_friend != user["id"]:
                    user["possible_friend"].append(possible_friend)


def mutual_friends_count(users):
    for user in users:
        user["mutual_friends_count"] = {}
        for user_temp in users:
            if user["id"] != user_temp["id"]:
                for friend in user_temp["friends"]:
                    if friend in user["friends"]:
                        if user_temp["id"] in user["mutual_friends_count"]:
                            user["mutual_friends_count"][user_temp["id"]] += 1
                        else:
                            user["mutual_friends_count"][user_temp["id"]] = 1


# List of users each is represented by a dict that contains for each user
# his or her id (which is a number) and name
users = [
    {"id": 0, "name": "Azaraf"},
    {"id": 1, "name": "Armandito"},
    {"id": 2, "name": "Karlita"},
    {"id": 3, "name": "Monse"},
    {"id": 4, "name": "Steve"},
    {"id": 5, "name": "Cesar"},
    {"id": 6, "name": "Julio"},
    {"id": 7, "name": "Jalipe"},
    {"id": 8, "name": "Dany"},
    {"id": 9, "name": "Alex"},
    {"id": 10, "name": "Omi"},
    {"id": 11, "name": "Zavala"},
    {"id": 12, "name": "Salvador"},
    {"id": 13, "name": "Chucho"},
    {"id": 14, "name": "Angel"},
    {"id": 15, "name": "Lydia"},
    {"id": 16, "name": "Mary"},
    {"id": 17, "name": "Sai"},
    {"id": 18, "name": "Xia"},
    {"id": 19, "name": "Riky"}
]

# List of pairs that represents the friendship between users.
friendships = [(0, 1), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 19),
               (1, 2), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 19),
               (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (6, 7),
               (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 19), (7, 8),
               (7, 19), (8, 9), (8, 10), (9, 10), (9, 19), (10, 19), (11, 12),
               (11, 13), (11, 14), (12, 13), (12, 14), (13, 14), (14, 15),
               (15, 16), (15, 17)]

# List of pairs that represents the interests of each user.
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
    (10, "Hadoop"), (10, "Big Data"), (10, "HBase"), (10, "Java"),
    (11, "Spark"), (12, "Storm"), (12, "Cassandra"),
    (13, "NoSQL"), (13, "MongoDB"), (13, "Cassandra"), (13, "HBase"),
    (14, "Postgres"), (14, "Python"), (14, "scikit-learn"), (14, "scipy"),
    (15, "numpy"), (15, "statsmodels"), (15, "pandas"), (15, "R"), (15, "Python"),
    (16, "statistics"), (16, "regression"), (16, "probability"),
    (17, "machine learning"), (17, "regression"), (17, "decision trees"),
    (18, "libsvm"), (18, "Python"), (18, "R"), (18, "Java"), (18, "C++"),
    (19, "Haskell"), (19, "programming languages"), (19, "statistics")
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j]["id"])
    users[j]["friends"].append(users[i]["id"])

num_users = len(users)
avg_connections = number_total_connections(users) / num_users

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

num_friends_by_id = sorted(num_friends_by_id,
                           key=lambda (user_id, num_friends): num_friends,
                           reverse=True)

possible_friends(users)
mutual_friends_count(users)
for user in users:
    print(user)