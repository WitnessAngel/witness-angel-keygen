from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, ILeftBody, MDList
from kivymd.uix.selectioncontrol import MDCheckbox
from key_device import list_available_key_devices
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import Label



class MyCheckbox(IRightBodyTouch, MDCheckbox):
    pass


class MyAvatar(ILeftBody, Image):
    pass


class MainApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "Witness Angel - WardProject"
        self.theme_cls.primary_palette = "Teal"
        super().__init__(**kwargs)

    def show_validate(self):
        #
        if (self.list.ids.textfield1.text is not "" )and(self.list.ids.textfield2.text is not "" ):
            print("initialize_key_USB()")
            #user_error = self.list.ids.textfield1.text + " user does not exist.\n" + self.list.ids.textfield1.text + " is current."
        elif (self.list.ids.textfield1.text is "" )and(self.list.ids.textfield2.text is "" ):
            user_error = "Please enter a username and a passphrase"
            self.open_dialog(user_error)
        elif(self.list.ids.textfield1.text is "" ):
            user_error = "Please enter a username"
            self.open_dialog(user_error)
        elif (self.list.ids.textfield2.text is ""):
            user_error = "Please enter a passphrase"
            self.open_dialog(user_error)

    def open_dialog(self,user_error):
        self.dialog = MDDialog(title='Please fill in the empty field',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                               )
        #else:
            #initialize_key_device(key_device, self.username.text)
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def createList(self):
        self.list = Factory.Lists()
        self.screen.add_widget(self.list)
        self.list = Factory.Lists()
        list_devices = list_available_key_devices()
        for index, usb in enumerate(list_devices):
            self.lineCheck = Factory.ListItemWithCheckbox(text="Path :%s " % (str(usb["path"])),secondary_text="Label : %s" % (str(usb["label"])))
            self.lineCheck.bind(on_release=self.key_device_selected_fct)
            self.list.ids.scroll.add_widget(self.lineCheck)
            self.screen.add_widget(self.list)




    def initialize_USB(self):
        print('initialize_USB()')
        self.show_validate()
        #print(self.key_device_selected)
        #self.l = Label(text="self.list.ids.checkbo0.text", font_size='20sp')
        #self.list.ids.scroll.add_widget(self.l)
        list_devices = list_available_key_devices()
        for index, usb in enumerate(list_devices):
            print("Path :"+str(usb["path"]))
            print(self.key_device_selected)
            self.l = Label(
                #text="Path :%s |Size :%s |Fst :%s  " % (str(usb["path"])) % (str(usb["size"])) % (str(usb["type"])),
                text="Path :%s " % (str(usb["path"])),
                font_size='20sp')
            self.list.ids.scroll.add_widget(self.l)
            if str(self.key_device_selected)=="Path :"+str(usb["path"]):
                print('ok')
                self.l = Label(text="Path :%s |Size :%s |Fst :%s  " % (str(usb["path"])) % (str(usb["size"])) % (str(usb["type"])), font_size='20sp')
                self.list.ids.scroll.add_widget(self.l)
    def retry_initialisation(self):
        print('retry_initialisation')







    def build(self):
        self.key_device_selected = None
        self.orientation = 'vertical'
        self.screen = Screen()
        self.createList()
        return self.screen

    def key_device_selected_fct(self,linelist):
        self.key_device_selected = linelist.text





if __name__ == "__main__":
    MainApp().run()