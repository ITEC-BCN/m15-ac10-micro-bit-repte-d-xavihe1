input.onButtonPressed(Button.A, function () {
    if (input.temperature() > 22) {
        basic.showString("Calor")
    } else {
        basic.showString("Fred")
    }
})
input.onButtonPressed(Button.B, function () {
    if (input.lightLevel() > 200) {
        music.play(music.stringPlayable("- - - - - - - - ", 120), music.PlaybackMode.UntilDone)
    } else if (input.lightLevel() < 50) {
        music.play(music.stringPlayable("- - - - - - - - ", 120), music.PlaybackMode.UntilDone)
    }
})
