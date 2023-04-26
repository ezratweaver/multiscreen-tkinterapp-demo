from tkinter import Canvas, Button
from firstscreen import window, Assets

class SecondScreen():

    def __init__(self):
        self.second_screen_canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 333,
            width = 551,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.button_bg = self.second_screen_canvas.create_image(
            275.0,
            246.0,
            image=Assets.image_button_bg
        )
        self.secondscreen = self.second_screen_canvas.create_image(
            275.0,
            75.0,
            image=Assets.image_secondscreen
        )
        self.second_screen_button_pressed = False
        self.second_screen_button = Button(
            self.second_screen_canvas,
            image=Assets.image_arrow_left,
            borderwidth=0,
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            highlightthickness=0,
            command=lambda: setattr(
                self, "second_screen_button_pressed", 
                not self.second_screen_button_pressed),
            relief="flat"
        )
        self.second_screen_button.place(
            x=244,
            y=222,
            width=60,
            height=46
        )

    def show_canvas(self):
        self.second_screen_canvas.pack()

    def hide_canvas(self):
        self.second_screen_canvas.pack_forget()