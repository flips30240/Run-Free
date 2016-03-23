from shapeGenerator import Cube

class spawnPlayer():

    def __init__(self, render, respawn):

        self.render_copy = render

        if respawn == 0:

            self.createPlayer()

        else:

            self.respawnPlayer()

    def createPlayer(self):

        self.player_node = self.render_copy.attachNewNode("player_node")
        self.player_geom = Cube(1, 1, 6)
        self.player_geom.reparentTo(self.player_node)
        self.player_node.setColorScale(1, 0, 0, 1)

    def respawnPlayer(self):

        #create when needed
        print("")

