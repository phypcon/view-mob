"""
My first application
"""
import toga
from toga.style.pack import CENTER, COLUMN, ROW, Pack


class ViewMob(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow()

        self.webview = toga.WebView(
            on_webview_load=self.on_webview_loaded, style=Pack(flex=1)
        )
        self.url_input = "https://phypcon.blogspot.com/"

        box = toga.Box(
            children=[
                self.webview,
            ],
            style=Pack(direction=COLUMN),
        )

        self.main_window.content = box
        self.webview.url = self.url_input

        # Show the main window
        self.main_window.show()

    def load_page(self, widget):
        self.webview.url = self.url_input

    def on_webview_loaded(self, widget):
        self.url_input = self.webview.url


def main():
    return ViewMob()

if __name__ == "__main__":
    main().main_loop()
