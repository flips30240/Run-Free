from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from update import update
from createWorld import createWorld
from filters import filters
from spawnPlayer import spawnPlayer
from cameraControl import cameraControl
 
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.world = createWorld(self.render)
        self.player = spawnPlayer(self.render, 0)
        self.player_cam = cameraControl("reparent", self.render.find("player_node"))
        self.create_filter = filters()
        self.update = update(self.render)
 
app = MyApp()
app.run()