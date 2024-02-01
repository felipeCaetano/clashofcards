import flet as ft
from flet_core import Page

import pokerequest


def main(page: Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = ft.colors.RED
    image = create_image()
    info = create_info()
    skills = create_skills()
    layout = create_layout(image, info, skills)
    page.data = 1

    def back_click(e: ft.ControlEvent):
        print(e.control.data)
        if page.data > 1:
            print("back")
            page.data -= 1
            poke = pokerequest.hows_pokemon(page.data)
            update_layout(poke)

    def update_layout(poke):
        image = create_image(poke[-1])
        info = create_info(poke[0], poke[1])
        layout.content.controls[0] = image
        layout.content.controls[1] = info
        page.update()

    def forward_click(e):
        if page.data < 1010:
            page.data += 1
            poke = pokerequest.hows_pokemon(page.data)
            update_layout(poke)

    page.add(
        ft.Row([
            ft.IconButton(icon=ft.icons.ARROW_BACK,
                          icon_color=ft.colors.YELLOW,
                          icon_size=50,
                          on_click=back_click
                          ),
            layout,
            ft.IconButton(icon=ft.icons.ARROW_FORWARD,
                          icon_color=ft.colors.YELLOW,
                          icon_size=50,
                          on_click=forward_click
                          )
        ])
    )
    # page.update()


def create_layout(image, info, skills):
    return ft.Container(
        height=650,
        width=400,
        bgcolor=ft.colors.WHITE,
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.BROWN),
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.all(30),
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills
            ]
        )
    )


def create_skills():
    return ft.Container(
        expand=1,
        bgcolor=ft.colors.ORANGE,
        border_radius=ft.border_radius.vertical(bottom=20),
        padding=ft.padding.symmetric(horizontal=20),
        content=ft.Row(
            [
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Atk.",
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20),
                        ft.Text("49",
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20
                                ),
                    ]
                ),
                ft.VerticalDivider(color=ft.colors.WHITE, opacity=.5),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Vel.",
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20
                                ),
                        ft.Text("45",
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20
                                ),
                    ]
                ),
                ft.VerticalDivider(color=ft.colors.WHITE, opacity=.5),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Def.",
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20
                                ),
                        ft.Text("49",
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=20
                                ),
                    ]
                )
            ]
        )
    )


def create_info(poke_num=1, poke_name='Bulbassaur'):
    return ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(f'N° {poke_num:03}', color=ft.colors.YELLOW_600,
                        size=30),
                ft.Text(f'{poke_name}', weight=ft.FontWeight.BOLD, size=40),
                ft.Row([
                    ft.Text(
                        "Grama",
                        weight=ft.FontWeight.BOLD,
                        size=20,
                        bgcolor=ft.colors.GREEN
                    ),
                    ft.Text("Venenoso",
                            weight=ft.FontWeight.BOLD,
                            size=20,
                            bgcolor=ft.colors.PURPLE)
                ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                ft.Text(
                    "Uma semente estranha foi plantada nas suas costas"
                    " quando nasceu. A planta brota e cresce com este "
                    "Pokémon.",
                    text_align=ft.TextAlign.CENTER
                ),
            ]
        )
    )


def create_image(url_poke_image='https://assets.pokemon.com/assets/cms2/img/pokedex/full/001'
                '.png'):
    return ft.Container(
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        expand=2,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.TEAL, ft.colors.SURFACE]
        ),
        content=ft.Image(
            src=url_poke_image,
            scale=1.5
        ),
        alignment=ft.alignment.center
    )


if __name__ == "__main__":
    ft.app(target=main)
