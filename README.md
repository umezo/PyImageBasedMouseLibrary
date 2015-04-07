PyImageBasedMouseLibrary
========================

emulate mouse pointing operation by image like button, logo, checkbox and more.



# Requirement
- PyUserInput
 - emulate mouse input
 - https://github.com/SavinaRoja/PyUserInput
- PyScreenShot
 - capture desktop
 - https://github.com/ponty/pyscreenshot
- OpenCV
 - detect target UI position 
 - http://opencv.org/ 

# Install
- install requirements
 - PyUserInput
 - PyScreenShot
  - PIL or pillow
  - one on PyScreenShot backends 
 - OpenCV

```
python setup.py install
```

# Usage

```
from pyimagemouse import batch
from pyimagemouse import core
from pyimagemouse import robot

core.robot = robot.PILCoreRobot()

batch.click('path/to/button.png')
```

