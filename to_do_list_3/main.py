# Flet to do app mobile ios/android
import flet as ft

# Lets separate the sheet for the components in the dict

_dark: str = ft.colors.with_opacity(0.5, "white")
_light: str = ft.colors.with_opcaity(1, "black")




toggle_style_sheet: dict ={ "icon": ft.icons.DARK_MODE_ROUNDED,"icon_size": 18}
add_style_sheet: dict ={ "icon": ft.icons.ADD_ROUNDED,"icon_size": 18}


# main content area
class Hero(ft.SafeArea):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(minimum=10, maintain_bottom_view_padding=True)
        self.page = page
        self.title: ft.Text = ft.Text("Todo List", size=20, weight="w800")
        self.toggle: ft.IconButton = ft.IconButton()

        self.main: ft.Column = ft.Column(
            control=[
                ft.Row(
                    controls=[self.title],
                )
            ]
        )


        self.content = self.main




def main (page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.Dark 
    theme = ft.Theme()
    page.theme = theme
    
    hero: object = Hero(page)
    page.theme_mode = ft.ThemeMode.DARK
    theme = ft.Theme()
    page.theme = theme

    hero: object = Hero(page)
    page.add(hero)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

