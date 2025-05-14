import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyApp")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        window = Gtk.ApplicationWindow(application=app)
        window.set_title("Tool Repo")
        window.set_default_size(800, 600)
        window.present()

app = MyApplication()
app.run()
