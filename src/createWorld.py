from shapeGenerator import Cube

from pandac.PandaModules import Material, VBase4

class createWorld():

    def __init__(self, render):

        self.world_node = render.attachNewNode("world_node")

        self.testGeom(5, 5, 5)

    def testGeom(self, l, w, h):

        test_cube_geom = Cube(l, w, h)
        test_cube_geom_node = self.world_node.attachNewNode("test_cube_geom_node")
        test_cube_geom.reparentTo(test_cube_geom_node)
        test_cube_geom_node.setColorScale(0, 1, 0, 1)