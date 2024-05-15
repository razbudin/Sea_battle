# from kivy.config import Config
from kivy.app import App
from kivymd.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# Config.set("graphics", "resizable", 0)
# Config.set("graphics", "width", 1250)
# Config.set("graphics", "height", 1050)


class SeaBattleApp(App):

    def build(self):

        superbl = BoxLayout(orientation='vertical',
                            padding=10)

        box_pole = BoxLayout(orientation='horizontal')

        # self.button_color = []
        pole_1 = GridLayout(cols=10, rows=10,
                            size_hint=(None, None),
                            width=390,
                            height=390)
        for i in range(10):
            for j in range(10):
                button = Button(background_color=(0.1, 0.3, 0.2, 1),
                                text=str(i) + ' ' + str(j))
                button.bind(on_press=self.on_target)
                pole_1.add_widget(button)

        pole_2 = GridLayout(cols=10, rows=10,
                            size_hint=(None, None),
                            width=390,
                            height=390)
        for i in range(10):
            for j in range(10):
                button = Button(background_color=(0.1, 1, 0, 1),
                                text=str(i) + ' ' + str(j))
                pole_2.add_widget(button)

        box_pole.add_widget(pole_1)
        box_pole.add_widget(pole_2)

        box_label = BoxLayout(orientation='horizontal',
                              padding=10,
                              size_hint_y=0.3)
        lb_player = Label(text='Player score')
        lb_step = Label(text='Step')
        lb_comp = Label(text='Comp score')
        box_label.add_widget(lb_player)
        box_label.add_widget(lb_step)
        box_label.add_widget(lb_comp)

        superbl.add_widget(box_pole)
        superbl.add_widget(box_label)

        return superbl

    def on_target(self, instanse):
        # Если пусто сделать стреляной
        # Если корабль нарисовать красный квадрат
        #
        pass


# if __name__ == '__main__':
#     SeaBattleApp().run()

    # return Builder.load_file("seabattle.kv")


SeaBattleApp().run()
