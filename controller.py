from firstscreen import FirstScreen
from secondscreen import SecondScreen, window

first_screen = FirstScreen()
second_screen = SecondScreen()

class Controller:
    def firstscreen_button_check():
        if first_screen.first_screen_button_pressed:
            first_screen.first_screen_button_pressed = False
            first_screen.hide_canvas()
            second_screen.show_canvas()
        window.after(70, Controller.firstscreen_button_check)

    def secondscreen_button_check():
        if second_screen.second_screen_button_pressed:
            second_screen.second_screen_button_pressed = False
            second_screen.hide_canvas()
            first_screen.show_canvas()
        window.after(70, Controller.secondscreen_button_check)

Controller.firstscreen_button_check()
Controller.secondscreen_button_check()