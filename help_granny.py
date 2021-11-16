import math

def tour(friends, friend_towns, home_to_town_distances):
    visitedFriends = []
    
    for i in friends:
        for j in friend_towns:
            if i in j and j not in visitedFriends:
                visitedFriends.append(i)
    
    friend_towns = dict(friend_towns)
    
    total = 0
    
    for i in range(len(visitedFriends) - 1):
        a = home_to_town_distances[friend_towns[visitedFriends[i]]]
        c = home_to_town_distances[friend_towns[visitedFriends[i + 1]]]
        print(c)
        total += returnOpp(a, c)
        
    x1Dist = home_to_town_distances[friend_towns[visitedFriends[0]]]
    xLast = home_to_town_distances[friend_towns[visitedFriends[-1]]]
    total += x1Dist + xLast
    
    return math.floor(total)
        


def returnOpp(a, c):
    return math.sqrt(c**2 - a**2)
