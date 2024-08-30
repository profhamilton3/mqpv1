// Libraries are added by extensions the build
function do_drive_forward(speed: number, duration: number) {
    DFRobotMaqueenPlus.servoRun(Servos.S1, 15)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, speed)
    pause(duration)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}

function do_drive_backwar(speed: number, duration: number) {
    music.tonePlayable(Note.CSharp, music.beat(BeatFraction.Half))
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.YELLOW)
    DFRobotMaqueenPlus.servoRun(Servos.S1, 25)
    DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CCW, speed)
    pause(duration)
    music.tonePlayable(Note.CSharp, music.beat(BeatFraction.Half))
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}

function do_drive_spin_right(speed: number, duration: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.CYAN)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, speed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, speed)
    pause(duration)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}

function do_drive_spin_left(speed: number, duration: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.CYAN)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, speed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, speed)
    pause(duration)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}

control.inBackground(function onIn_background() {
    DFRobotMaqueenPlus.I2CInit()
    basic.showIcon(IconNames.Angry)
    while (true) {
        if (15 > DFRobotMaqueenPlus.ultraSonic(PIN.P1, PIN.P2)) {
            do_drive_backwar(100, 750)
            DFRobotMaqueenPlus.mototStop(Motors.ALL)
            do_drive_spin_left(75, 750)
            DFRobotMaqueenPlus.mototStop(Motors.ALL)
        } else {
            basic.pause(200)
        }
        
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    DFRobotMaqueenPlus.servoRun(Servos.S1, 0)
    do_drive_forward(100, 1500)
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    do_drive_spin_right(80, 750)
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    do_drive_backwar(100, 1000)
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    do_drive_spin_left(80, 750)
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    do_drive_forward(35, 1000)
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.RED)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.builtInPlayableMelody(Melodies.PowerUp)
    DFRobotMaqueenPlus.servoRun(Servos.S1, 60)
})
basic.showIcon(IconNames.Angry)
music.setVolume(60)
