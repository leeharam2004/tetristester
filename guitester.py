import random

from Settings import Settings
#from environment.AutoPlayEnvironment import AutoPlayEnvironment
from environment.ManualPlayEnvironment import ManualPlayer
from graphics.DummyGraphicModule import DummyGraphicModule
from graphics.GraphicModule import GraphicModule

settings = Settings()

def random_tetromino():
    return random.randrange(0, settings.ACTIONS)
TETROMINO_AGENT = random_tetromino

graphic_interface = GraphicModule(settings)

env_model = ManualPlayer(settings, graphic_interface)

turns = 0
while True:
    turns += 1
    _, _, end = env_model.action(TETROMINO_AGENT())
    if end:
        print("Turns: " + str(turns))
        turns = 0
