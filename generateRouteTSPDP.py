
import numpy as np
import sys
import json
from urllib import request


@dataclass
class Waypoint:
    latitude: float
    longitude: float
    stayTime: float



def getTimeMap(Info, waypoints):
    time_precision = np.float
    url = Info.prefix + Info.profile + "/"
    stayTimes = np.zeros(len(waypoints), dtype=time_precision)

    for index, waypoint in enumerate(waypoints):
        url += f"{waypoint.longitude},{waypoint.latitude};"
        stayTimes[index] = waypoint.stayTime

    url = url[:-1] + "?access_token=" + Info.access_token

    response = request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    timeMap = np.array(data['durations'], dtype=time_precision)
    timeMap += stayTimes.repeat(len(waypoints), axis=0)

    return timeMap
    

def travelSalesmanProblemUsingBottomUpDynamicProgramming(source, num_points):
    # dp[visited_stated][curent]
    # meaning : the shortest path from current to source and the path go through visited_state
    # visited_stated represents which waypoints are visited, if waypoint 1 is visited then
    # For example : if waypoint 1 is visited then visited = 0...01 
    #               if waypoint 2 is visited then visited = 0...10, and so on
    # current represents the current waypoints travel salesman stays
    # Math representation : 
    #   if visited == 0(never visit waypoint) :  dp[0][waypoint] = weight[waypoint][source]
    #   else : dp[visited_state][current] = min(dp[visited_state - {waypoint}] + weight[current][waypoint])
    
    

    # Init
    dp = np.ones((2**(num_points - 1), num_points)) * -1
    for current in range(num_points):
        dp[0][current] = timeMap[current][source]

    # Bottom up dynamic programming
    for visited_status in range(1, 2**(num_points-1)):
        for current in range(num_points):
            minimum = float("Inf")
            
            # check minimum time through all connected waypoints
            # Since we are complete graph
            for i in range(1, num_points):
                if (visited_status & (1<<(i-1))) and ((timeMap[current][i] + dp[visited_status & ~(i-1)][i]) < minimum):
                    minimum = (timeMap[current][i] + dp[visited_status & ~(i-1)][i])
            
            dp[visited_status][current] = minimum

    return dp[2**(num_points-1)-1, 0]

source = 0
mapbox_info = MapboxInfo()
timeMap = getTimeMap(mapbox_info, waypoints)
travelSalesmanProblemUsingBottomUpDynamicProgramming(source, len(waypoints))