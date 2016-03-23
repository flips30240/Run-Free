from direct.task import Task

from math import pi, sin, cos

class update():

	def __init__(self, render):

		self.render_copy = render
		self.createTask()

	def createTask(self):

		taskMgr.add(self.globalUpdate, "globalUpdate")

	def globalUpdate(self, task):
		#do stuff
		return Task.cont

