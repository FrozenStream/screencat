
import pynput.mouse as pm
import tkinter as tk


class childWindow:

    def locate(self):
        self.win = tk.Tk()
        self.start = False
        self.creating = True
        self.begin_x, self.begin_y = 0, 0
        self.x, self.y, self.width, self.height = 0, 0, 0, 0

        print("window begin")
        self.win.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        # 设置窗口背景色为透明
        self.win.wm_attributes('-alpha', 0.8)
        self.win.attributes('-topmost', 'true')
        # 隐藏标题栏
        self.win.overrideredirect(True)

        listener = pm.Listener(on_move=self.on_move, on_click=self.on_click)
        listener.start()

        def check():
            if not self.creating:
                self.win.after(100, lambda:self.win.destroy())
            else:
                self.win.after(20, check)

        check()
        self.win.mainloop()

    def on_click(self, x, y, button, pressed):
        if pressed and button == pm.Button.right:
            print("按下坐标")
            self.begin_x, self.begin_y = x, y
            print(f"{x},{y}")
            print(button)
            self.start = True

        if (not pressed) and button == pm.Button.right:
            print("松开坐标")
            print(f"{x},{y}")
            print(button)
            self.creating = False
            return False

    def on_move(self, x, y):
        if self.start and self.creating:
            self.width = abs(self.begin_x - x)
            self.height = abs(self.begin_y - y)
            self.x = min(self.begin_x, x)
            self.y = min(self.begin_y, y)
            self.win.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
            print("moving!")
