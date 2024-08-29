// Libraries are added by extensions the build
DFRobotMaqueenPlus.I2CInit()
DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, 30)
DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 30)
pause(1300)
basic.showString("Hello!")
DFRobotMaqueenPlus.mototStop(Motors.ALL)
