class cameraControl():

    def __init__(self, action, np):

        if action == "reparent":

            self.reparentCamera(np)

        else:
            print("From cameraControl.py: Action" + " " + action + " is not recognozed!")

    def reparentCamera(self, parent):

        base.camera.reparentTo(parent)