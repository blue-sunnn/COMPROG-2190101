# load users' watching info
users = dict()
users["Pop"] = {"minion", "spiderman"}
users["Tim"] = {"ju-on", "minion"}
users["Pun"] = {"minion"}
users["Puk"] = {"avenger", "batman", "spiderman"}
users["Tan"] = {"spiderman"}

def calculate_user_scores(query, users):
    # query: a dictionary of watching histories for a specific user
    # users: a dictionary of watching histories for all users
    # Return: a dictionary of all user's scores (round 2 decimal points)
    user_scores = dict()
    # fill your code here!
    for user, mov in users.items():
        total_movies = query | mov
        watched_with_query = query & mov
        if mov.issubset(query) or watched_with_query == set():
            user_scores[user] = 0
        else:
            n = len(watched_with_query)
            d = len(total_movies)
            user_scores[user] = round(n / d, 2)
    return user_scores


def recommend_movies(query, users, user_scores):
    # query: a dictionary of watching histories for a specific user
    # users: a dictionary of watching histories for all users
    # user_scores: a dictionary of all user's scores (round 2 decimal points)
    # Return: a list of recommend movies in alphabetically order
    recommend = set()
    # fill your code here!
    max_score = max(user_scores.values())
    if max_score == 0:
        return 'No recommendation'
    for user, mov in users.items():
        if user_scores[user] == max_score:
            recommend = recommend | mov - query
    return sorted(recommend)


def main():
    n = int(input())
    query = set()
    for _ in range(n):
        query.add(input().lower())
    user_scores = calculate_user_scores(query, users)
    print(sorted(user_scores.items()))
    recommend = recommend_movies(query, users, user_scores)
    print(recommend)


main()
