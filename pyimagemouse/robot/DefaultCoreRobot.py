class DefaultCoreRobot():
  def click(self, point, waitTime=500):
    raise NotImplementedError( )

  def move(self, point, waitTime=500 ):
    raise NotImplementedError( )

  def capture(self, path):
    raise NotImplementedError( )
