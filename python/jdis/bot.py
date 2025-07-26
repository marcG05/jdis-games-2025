import typing
from .utils import *
import math

TOKEN = "p647772y"

lastMove =(0,0)

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

async def on_tick(state: GameState) -> typing.Union[MoveAction, PhaseAction, OpenChestAction, UseItemAction, SegFaultAction, SkipAction]:
    """
    fr: Cette fonction est appelée à chaque tick. C'est ici que vous programmez
        le fonctionnement de votre agent en retournant l'action qui sera executée
        sur le serveur.

    en: This function is called every tick. Program the behaviour of your agent
        here by returning the action to be executed on the server.
    """


    print(state.ground.data)
    
            
    
    return move(lastMove)
    



async def on_game_start():
    """
    fr: Cette fonction est appelée une seule fois au début de chaque parti.

    en: This function is called at the beginning of each game.
    """
    pass

