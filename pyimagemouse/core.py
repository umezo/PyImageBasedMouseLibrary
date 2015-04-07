from robot import DefaultCoreRobot

robot = DefaultCoreRobot()
def click(point, waitTime=500):
  robot.click(point, waitTime)

def move(point, waitTime=500):
  robot.move(point, waitTime)

def capture(path):
  robot.capture(path)



import cv
import logging as logger


def detect ( templatePath, targetPath, threshold = 0.8 ):

  target = cv.LoadImage( targetPath )
  template = cv.LoadImage( templatePath )

  dstSize = (target.width - template.width + 1, target.height - template.height + 1)
  dstImg = cv.CreateImage(dstSize, cv.IPL_DEPTH_32F, 1)

  cv.MatchTemplate (target, template, dstImg , cv.CV_TM_CCOEFF_NORMED);
  minMaxLoc = cv.MinMaxLoc (dstImg);
  logger.debug( "%s, %.2f%%" % ( templatePath, minMaxLoc[1]*100 ) )
  if minMaxLoc[1] < threshold :
    return False

  maxLoc = minMaxLoc[3]
  
  x = maxLoc[0] + template.width/2 
  y = maxLoc[1] + template.height/2

  return (x,y)

