import typing
from .utils import *
import math

mapOBJ = [
    {
        "name" : "firewall",
        "danger" : 9
    },
    {
        "name" : "via",
        "danger" : 5
    },
    {

    },{
        "name": "resistance",
        "danger" : 3
    },{
      "name" : "chest",
      "danger" : 0  
    },{
        "name": "bot",
        "danger" : 6
    },
    {
        "name" : "groundPlane",
        "danger" : 7
    }]

def detectMap(state: GameState, find: str):
    for n in range(len(state.ground.data)):
        for obj in mapOBJ:
            if state.ground.data[n] == obj["name"] and state.ground.data[n] == find:
                x=  n%7
                y = n//7
                print(f"{obj['name']} DETECTED AT POSITION {x},{y}")
                return (x,y)


def directionNormalize(direction: tuple) -> Vector:
    xNorm = (direction[0]-3)/math.sqrt(pow(direction[0]-3,2)+pow(direction[1]-3, 2))
    yNorm = (direction[1]-3)/math.sqrt(pow(direction[0]-3,2)+pow(direction[1]-3, 2))
    print(f"NEW DIRECTION {xNorm}, {yNorm}")
    return Vector(xNorm, yNorm)