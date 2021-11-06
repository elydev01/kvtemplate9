from kivy.uix.screenmanager import ScreenManager


class NavigationManager(ScreenManager):
    pages = []

    def push(self, page):
        self.pages.append(self.current)
        self.transition.direction = "down"
        self.current = page

    def pop(self):
        if len(self.pages) > 0:
            self.transition.direction = "up"
            back_page = self.pages[-1]
            del self.pages[-1]
            self.current = back_page
            return True
        else: quit()
