from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from PIL import Image as PILImage, ImageEnhance
import io


class ImageFilterApp(App):
    def build(self):
        self.img_widget = Image()
        self.file_chooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'])
        self.file_chooser.bind(on_selection=self.load_image)

        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.img_widget)

        button_layout = BoxLayout(size_hint_y=None, height=50)
        self.choose_button = Button(text='Choose Image', on_press=self.open_file_chooser)
        self.filter_button = Button(text='Apply Filter', on_press=self.apply_filter)
        button_layout.add_widget(self.choose_button)
        button_layout.add_widget(self.filter_button)

        self.layout.add_widget(button_layout)

        return self.layout

    def open_file_chooser(self, instance):
        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(self.file_chooser)
        close_button = Button(text='Close', size_hint_y=None, height=50)
        close_button.bind(on_press=lambda x: self.file_chooser_popup.dismiss())
        popup_layout.add_widget(close_button)
        self.file_chooser_popup = Popup(title='Choose an Image', content=popup_layout, size_hint=(0.9, 0.9))
        self.file_chooser_popup.open()

    def load_image(self, filechooser, selection):
        if selection:
            self.image_path = selection[0]
            print(f"Selected image path: {self.image_path}")  # Debugging line
            self.img_widget.source = self.image_path
            self.img_widget.reload()  # Ensure the image is reloaded
            self.file_chooser_popup.dismiss()

    def apply_filter(self, instance):
        if hasattr(self, 'image_path'):
            pil_image = PILImage.open(self.image_path)
            enhancer = ImageEnhance.Color(pil_image)
            filtered_image = enhancer.enhance(0.5)  # Apply a simple desaturation filter

            # Convert PIL image to Kivy texture
            data = io.BytesIO()
            filtered_image.save(data, format='png')
            data.seek(0)
            self.img_widget.texture = Image(source=data).texture


if __name__ == '__main__':
    ImageFilterApp().run()
