import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

kivy.config.Config.set('graphics', 'width', '400')
kivy.config.Config.set('graphics', 'height', '200')

class MyApp(App):
    def build(self):
        # Создаем главный GridLayout для размещения всех элементов
        main_layout = GridLayout(cols=1, spacing=10, padding=(10, 10))

        # Создаем ScrollView для размещения вертикального GridLayout с кнопками
        scrollview = ScrollView(size_hint=(1, 1))

        # Создаем вертикальный GridLayout для кнопок
        button_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)

        # Устанавливаем минимальную высоту для вертикального GridLayout
        button_layout.bind(minimum_height=button_layout.setter('height'))

        # Создаем текстовое поле для поиска
        search_input = TextInput(text='Поиск', size_hint_y=None, height=50)
        button_layout.add_widget(search_input)

        # Создаем промежуток между поиском и первой кнопкой
        button_layout.add_widget(Button(size_hint_y=None, height=20))

        # Создаем кнопки
        buttons = ['Терминалы', 'Прошивка терминалов', 'Настройка терминалов']
        for text in buttons:
            button = Button(text=text, size_hint_y=None, height=50, background_normal='', background_color=(0.2, 0.6, 1, 1))
            button.background_disabled_normal = ''
            button.background_disabled_down = ''
            button_layout.add_widget(button)

            # Создаем промежуток между кнопками
            button_layout.add_widget(Button(size_hint_y=None, height=20))

        # Добавляем вертикальный GridLayout с кнопками в ScrollView
        scrollview.add_widget(button_layout)

        # Добавляем ScrollView в главный GridLayout
        main_layout.add_widget(scrollview)

        return main_layout

if __name__ == '__main__':
    MyApp().run()
