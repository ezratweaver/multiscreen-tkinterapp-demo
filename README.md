# Multiscreen Modulated Tkinter App

This showcase's my idea of multiple screens in tkinter using different files for each screen, using a controller file to check for a variable to change and then calling a function to show or hide the respective canvas.

The program should be structured as such

![Screenshot 2023-04-26 142247](https://user-images.githubusercontent.com/101545981/234681573-df569200-ff43-433c-b2c8-2138a45e1d4f.png)

The window file holds the window variable:

```python
window = Tk()
```

The assets file holds all of the PhotoImage() variables, in a class called Assets(). Putting these in a high order in the the script list allows for easy access to any assets you might need to reuse. you can then access them by using the Assets.*. Heres an example.

```python
Assets.image_button_bg
```

The first and second screen files hold all your GUI element code, such as your images, buttons, and any other widget needed. The tkinter screens should be in a class structure, with two public methods to show and hide the canvas or frame that your elements are on.

```python
def show_screen(self):
   firstscreen_canvas.pack()
   
def hide_screen(self):
   firstscreen_canvas.pack_forget()
```

every button that changes to screen should instead of calling these, change a boolean variable. your button should change this variable.

```python
self.first_screen_button_pressed = False
self.first_screen_button = Button(
            self.first_screen_canvas,
            image=Assets.image_arrow_right,
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            command=lambda: setattr(
                self, "first_screen_button_pressed", 
                not self.first_screen_button_pressed),
            relief="flat"
           )
```

Next, the controller file imports all of your screens, in this case the first and second screen, aswell as your window variable

```python
from firstscreen import FirstScreen, window
from secondscreen import SecondScreen
```

The controller then constantly checks for a change in the variable, using the .after() method, when the variable is changed, it will then call the respective hide/show canvas methods.

![Screenshot 2023-04-23 174744](https://user-images.githubusercontent.com/101545981/234685123-eb8bd731-11c7-493b-a8b4-a6eb9d871af7.png)

Check the example code aswell to see how this works in action. This is just an example, and I am sure there is another way to do this that is more effective and less resource heavy then constantly checking for a variable. If you have ideas or way to improve this code, I would love to hear/see your feedback!
