// Libraries are added by extensions the build
DFRobotMaqueenPlus.I2CInit()
function doDriveForward(speed: number, duration: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.GREEN)
    DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, speed)
    pause(duration)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}

function doDriveBackwar(speed: number, duration: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.YELLOW)
    DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CCW, speed)
    pause(duration)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}

function doDriveSpinRight(speed: number, duration: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.CYAN)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, speed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, speed)
    pause(duration)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}

function doDriveSpinLeft(speed: number, duration: number) {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.CYAN)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, speed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, speed)
    pause(duration)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
})
