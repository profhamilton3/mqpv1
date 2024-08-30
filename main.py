
#Libraries are added by extensions the build
DFRobotMaqueenPlus.i2c_init()
basic.show_icon(IconNames.ANGRY)
DFRobotMaqueenPlus.servo_run(Servos.S1, 0)


def doDriveForward(speed:number, duration: number):
    DFRobotMaqueenPlus.servo_run(Servos.S1, 15)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, speed)
    pause(duration)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def doDriveBackwar(speed:number, duration: number):
    music.tone_playable(Note.CSHARP, music.beat(BeatFraction.HALF))
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.YELLOW)
    DFRobotMaqueenPlus.servo_run(Servos.S1, 25)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, speed)
    pause(duration)
    music.tone_playable(Note.CSHARP, music.beat(BeatFraction.HALF))
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def doDriveSpinRight(speed:number, duration: number):
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.CYAN)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, speed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, speed)
    pause(duration)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def doDriveSpinLeft(speed:number, duration: number):
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.CYAN)
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, speed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, speed)
        pause(duration)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)



def on_button_pressed_a():
    doDriveForward(75,1000)
    doDriveSpinLeft(50,500)
    doDriveBackward(75,1000)
    doDriveSpinRight(50, 500)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)

input.on_button_pressed(Button.A, on_button_pressed_a)