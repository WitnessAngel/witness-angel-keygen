from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox
from key_device import list_available_key_devices
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog

Builder.load_string(
    """

<ListItemWithCheckbox@ThreeLineAvatarIconListItem>:

    MyAvatar:
        source: "IconsWitnessAngel\PNG\Witness_Angel_Logotype1.png"
    MyCheckbox:
        group: "radio"



<Lists@BoxLayout>

    name: "lists"
    orientation: "vertical"
    canvas.before:
        Color:
            rgba: 0.1372, 0.2862, 0.5294, 1
        Rectangle:
            pos: self.pos
            size: self.size

    GridLayout:
        cols:2
        spacing: [20,40]
        GridLayout:
            size_hint: 0.9, 1
            rows:5

            MDToolbar:
                title:"Select a USB"
                size_hint: 0.9, 0.1
                md_bg_color: [0.1372, 0.2862, 0.5294, 1]
                elevation: 3

            ScrollView:
                size_hint: 0.9, 0.9

                MDList:
                    id: scroll
        AnchorLayout:
            padding: [0, 20, 20, 0]
            size_hint: 0.5, 0.9

            Button:
                id: btn
                background_color: (51, 23, 186.0, 1)
                color: 0.1372, 0.2862, 0.5294, 1
                text: "Refresh"
                size: 200, 70
                size_hint: None, None




    GridLayout:
        rows:2
        GridLayout:
            cols:2
            spacing: [20,20]

            GridLayout:
                padding: [0, 20, 0, 0]
                rows: 2
                MDTextField:
                    id: textfield1
                    size_hint_x: -0.5
                    hint_text: 'Enter username'
                    helper_text: 'Personal ID'
                    helper_text_mode: 'on_focus'
                    width: 50
                    color_mode: 'custom'
                    line_color_focus: 1, 1, 1, 1
                    mode: "rectangle"
                    current_hint_text_color: 1, 1, 1, 1

                MDTextField:
                    id: textfield2
                    size_hint_x: -0.5
                    hint_text: 'Enter passphrase'
                    helper_text: 'A sentence to memorize'
                    helper_text_mode: 'on_focus'
                    width: 50
                    color_mode: 'custom'
                    line_color_focus: 1, 1, 1, 1
                    mode: "rectangle"
                    current_hint_text_color: 1, 1, 1, 1


            AnchorLayout:
                padding: [0, 20, 20, 0]
                size_hint: 0.5, 0.9

                Button:
                    id: btn
                    background_color: (51, 23, 186.0, 1)
                    color: 0.1372, 0.2862, 0.5294, 1
                    text: "Initialize"
                    size: 200, 70
                    size_hint: None, None
                    on_release:
                        app.change()
        GridLayout:
            cols:2

            Label:
                size_hint: 1, .1
                text: 'Errors'


            AnchorLayout:
                padding: [0, 20, 20, 0]
                size_hint: 0.5, 0.9

                Button:
                    id: btn
                    background_color: (51, 23, 186.0, 1)
                    color: 0.1372, 0.2862, 0.5294, 1
                    text: "Retry"
                    size: 200, 70
                    size_hint: None, None

"""
)


class Container(GridLayout):
    pass


class MyCheckbox(IRightBodyTouch, MDCheckbox):
    pass


class MyAvatar(ILeftBody, Image):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Witness Angel - WardProject"
        self.theme_cls.primary_palette = "Teal"
        super().__init__(**kwargs)

    def change(self):
        print('ok')
        if (self.username.text is not "") and (self.passphrase.text is not ""):
            user_error = self.username.text + " user does not exist.\n" + self.passphrase.text + " is current."
        elif (self.username.text is "") and (self.passphrase.text is ""):
            user_error = "Please enter a username and a passphrase"
        elif (self.username.text is ""):
            user_error = "Please enter a username"
        elif (self.passphrase.text is ""):
            user_error = "Please enter a passphrase"
        self.dialog = MDDialog(title='Check !!',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                        MDFlatButton(text='More')]
                               )
        # else:
        # initialize_key_device(key_device, self.username.text)
        self.dialog.open()

    def show_validate(self, obj):
        # print(self.username.text)
        # print(self.passphrase.text)
        if (self.username.text is not "") and (self.passphrase.text is not ""):
            user_error = self.username.text + " user does not exist.\n" + self.passphrase.text + " is current."
        elif (self.username.text is "") and (self.passphrase.text is ""):
            user_error = "Please enter a username and a passphrase"
        elif (self.username.text is ""):
            user_error = "Please enter a username"
        elif (self.passphrase.text is ""):
            user_error = "Please enter a passphrase"
        self.dialog = MDDialog(title='Check !!',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                        MDFlatButton(text='More')]
                               )
        # else:
        # initialize_key_device(key_device, self.username.text)
        self.dialog.open()

    def build(self):
        self.orientation = 'vertical'
        list = Factory.Lists()
        screen = Screen()
        list_devices = list_available_key_devices()
        row_data_devices = []
        for index, usb in enumerate(list_devices):
            list.ids.scroll.add_widget(
                Factory.ListItemWithCheckbox(text="Label : %s   |   Path :%s " % (str(usb["label"]), str(usb["path"])),
                                             secondary_text="Size in bytes :%s " % (str(usb["size"])),
                                             tertiary_text="File system type : %s  " % (str(usb["format"]))))
        screen.add_widget(list)

        return screen


if __name__ == "__main__":
    MainApp().run()