from tkinter import Canvas, Button
from window import window
from assets import Assets

class FirstScreen:
        
    def __init__(self):
        self.first_screen_canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 333,
            width = 551,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.button_bg = self.first_screen_canvas.create_image(
            275.0,
            246.0,
            image=Assets.image_button_bg
        )
        self.first_screen = self.first_screen_canvas.create_image(
            275.0,
            75.0,
            image=Assets.image_firstscreen
        )
        self.first_screen_button_pressed = False
        self.first_screen_button = Button(
            self.first_screen_canvas,
            image=Assets.image_arrow_right,
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: setattr(
                self, "first_screen_button_pressed", 
                not self.first_screen_button_pressed),
            relief="flat"
        )
        self.first_screen_button.place(
            x=245.0,
            y=223.0,
            width=60.0,
            height=46.0
        )
    
    def show_canvas(self):
        self.first_screen_canvas.pack()

    def hide_canvas(self):
        self.first_screen_canvas.pack_forget()