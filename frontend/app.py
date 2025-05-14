import gi, requests, markdown2
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, WebKit

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Tool Repo")
        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)
        # Sidebar and WebView setup goes here...
        self.show_all()

if __name__ == "__main__":
    MainWindow()
    Gtk.main()
