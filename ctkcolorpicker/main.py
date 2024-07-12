import threading
from customtkinter import *


class CTkColorPicker(CTkFrame):
    def __init__(self, master, app):
        self.master = master
        self.app    = app
        self.running = True
        super(CTkColorPicker, self).__init__(master=self.master, width=400, corner_radius=0)

        self.hex_lv_var = StringVar()
        self.rgb_lv_var = StringVar()

        self.liveview = CTkFrame(self, width=64, height=64)
        self.liveview.place(x=325, y=10)

        self.slider_r = CTkSlider(master=self, from_=0, to=255, number_of_steps=255)
        self.slider_r.place(x=30, y=25)
        self.slider_r.configure(command=self.update_liveview)

        self.slider_g = CTkSlider(master=self, from_=0, to=255, number_of_steps=255)
        self.slider_g.place(x=30, y=50)
        self.slider_g.configure(command=self.update_liveview)

        self.slider_b = CTkSlider(master=self, from_=0, to=255, number_of_steps=255)
        self.slider_b.place(x=30, y=75)
        self.slider_b.configure(command=self.update_liveview)

        self.button = CTkButton(self, text='OK', corner_radius=0, command=self.app.destroy)
        self.button.place(x=60, y=110)

        self.hex_lv = CTkEntry(self, width=100, height=20, corner_radius=0, textvariable=self.hex_lv_var)
        self.hex_lv.place(x=289, y=80)

        self.rgb_lv = CTkEntry(self, width=100, height=20, corner_radius=0, textvariable=self.rgb_lv_var)
        self.rgb_lv.place(x=289, y=105)

        self.update_liveview(self)

        self.thrd = threading.Thread(target=self.check_lvs)
        self.thrd.start()

    def rgb2hex(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def hex2rgb(self, hexcode):
        self.hexcode_rep = hexcode.replace('#', '')
        r = int(self.hexcode_rep[0:2], 16)
        g = int(self.hexcode_rep[2:4], 16)
        b = int(self.hexcode_rep[4:6], 16)
        return [str(r), str(g), str(b)]

    def update_liveview(self, test):
        self.r = self.slider_r.get()
        self.g = self.slider_g.get()
        self.b = self.slider_b.get()
        self.rgb = f"{int(self.r)}, {int(self.g)}, {int(self.b)}"
        self.hex = self.rgb2hex(r=int(self.r), g=int(self.g), b=int(self.b))

        self.rgb_lv_var.set(self.rgb)
        self.hex_lv_var.set(self.hex)

        self.liveview.configure(fg_color=self.hex)

    def stop(self):
        self.running = False

    def check_lvs(self):
        while self.running == False:
            if self.hex_lv_var.get() != self.hex:
                try:
                    self.hex_data = self.hex_lv_var.get()
                    self.new_rgb = self.hex2rgb(self.hex_data)

                    self.slider_r.set(int(self.new_rgb[0]))
                    self.slider_g.set(int(self.new_rgb[1]))
                    self.slider_b.set(int(self.new_rgb[2]))

                    self.liveview.configure(fg_color=self.hex_data)
                    self.rgb = f'{self.new_rgb[0]}, {self.new_rgb[1]}, {self.new_rgb[2]}'
                    self.hex = self.hex_data
                    self.rgb_lv_var.set(f'{self.new_rgb[0]}, {self.new_rgb[1]}, {self.new_rgb[2]}')
                except Exception as e:
                    print(e)

            if self.rgb_lv_var.get() != self.rgb:
                try:
                    self.new_rgb = self.rgb_lv_var.get().split(',')
                    self.hex_data = self.rgb2hex(r=int(self.new_rgb[0]), g=int(self.new_rgb[1]), b=int(self.new_rgb[2]))

                    self.slider_r.set(int(self.new_rgb[0]))
                    self.slider_g.set(int(self.new_rgb[1]))
                    self.slider_b.set(int(self.new_rgb[2]))

                    self.liveview.configure(fg_color=self.hex_data)
                    self.rgb = f'{self.new_rgb[0]},{self.new_rgb[1]},{self.new_rgb[2]}'
                    self.hex = self.hex_data
                    self.hex_lv_var.set(f'{self.hex_data}')
                except Exception as e:
                    print(e)


def color_picker():
    def on_close():
        colorpicker.stop()
        app.quit()
        app.destroy()

    app = CTk()
    app.geometry('400x170')
    app.resizable(False, False)
    app.protocol('WM_DELETE_WINDOW', on_close)
    app.title('Color Picker')

    colorpicker = CTkColorPicker(master=app, app=app)
    colorpicker.pack()

    app.mainloop()

    return [f'{colorpicker.rgb}', f'{colorpicker.hex}']