import time

from pymouse import PyMouse
import pyscreenshot as ImageGrab

from DefaultCoreRobot import DefaultCoreRobot

class PILCoreRobot(DefaultCoreRobot):
  def click(self, point, waitTime=500 ):
    PyMouse().click( point[0] , point[1] )
    time.sleep( waitTime * 0.001 )

  def move(self, point, waitTime=500 ):
    PyMouse().move( point[0] , point[1] )
    time.sleep( waitTime * 0.001 )

  def capture(self, path):
    ImageGrab.grab().save( path , "PNG" );


