
#Libraries are added by extensions the build
DFRobotMaqueenPlus.i2c_init()

DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 30)
DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 30)
pause(1300)
basic.show_string("Hello!")
DFRobotMaqueenPlus.motot_stop(Motors.ALL)