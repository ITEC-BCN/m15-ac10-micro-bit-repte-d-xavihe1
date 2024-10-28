def on_button_pressed_a():
    if input.temperature() > 22:
        basic.show_string("Calor")
    else:
        basic.show_string("Fred")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if input.light_level() > 200:
        music.play(music.string_playable("- - - - - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif input.light_level() < 50:
        music.play(music.string_playable("- - - - - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)
