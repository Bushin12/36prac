from random import uniform
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup



Window.size = (360, 640)


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(uniform(0.5, 1), uniform(0.5, 1), uniform(0.5, 1))
            d = 30.
            #Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size = (d, d))
            touch.ud['line'] = Line (points = (touch.x, touch.y), width = 3)

    def on_touch_move(self, touch):
        touch.ud['line']. points += [touch.x, touch.y]
   

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        parent.add_widget(self.painter)

        clearbtn = Button(text = 'Очистить', size = (75, 50), on_press = self.clear_canvas)
        colorbtn = Button(text = 'Цвет', size = (75, 50), on_press = self.change_color )

        parent.add_widget(clearbtn)
        parent.add_widget(colorbtn)

        return parent


    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def change_color(self, obj):
        clr_picker = ColorPicker()

if __name__=='__main__':
    MyPaintApp().run()
