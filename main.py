
#Libraries are added by extensions the build

def do_drive_forward(speed:number, duration: number):
    DFRobotMaqueenPlus.servo_run(Servos.S1, 15)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, speed)
    pause(duration)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def do_drive_backwar(speed:number, duration: number):
    music.tone_playable(Note.CSHARP, music.beat(BeatFraction.HALF))
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.YELLOW)
    DFRobotMaqueenPlus.servo_run(Servos.S1, 25)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, speed)
    pause(duration)
    music.tone_playable(Note.CSHARP, music.beat(BeatFraction.HALF))
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def do_drive_spin_right(speed:number, duration: number):
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.CYAN)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, speed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, speed)
    pause(duration)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)

def do_drive_spin_left(speed:number, duration: number):
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.CYAN)
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, speed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, speed)
        pause(duration)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)



def onIn_background():
    DFRobotMaqueenPlus.i2c_init()
    basic.show_icon(IconNames.ANGRY)
    while True:      
        if 15 > DFRobotMaqueenPlus.ultra_sonic(PIN.P1, PIN.P2):
            do_drive_backwar(100, 750)
            DFRobotMaqueenPlus.motot_stop(Motors.ALL)
            do_drive_spin_left(75,750)
            DFRobotMaqueenPlus.motot_stop(Motors.ALL)
        else:
            basic.pause(200)

control.in_background(onIn_background)

def on_logo_event_pressed():
    DFRobotMaqueenPlus.servo_run(Servos.S1, 0)
    do_drive_forward(100,1500)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    do_drive_spin_right(80,750)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    do_drive_backwar(100,1000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    do_drive_spin_left(80, 750)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    do_drive_forward(35,1000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.RED)

input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def on_button_pressed_a():
    music.built_in_playable_melody(Melodies.POWER_UP)
    DFRobotMaqueenPlus.servo_run(Servos.S1, 60)

input.on_button_pressed(Button.A, on_button_pressed_a)



basic.show_icon(IconNames.ANGRY)
music.set_volume(60)