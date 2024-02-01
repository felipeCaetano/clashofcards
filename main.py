import flet as ft
from flet_core import Page


def main(page: Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = ft.colors.RED
    image = ft.Container(
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        expand=2,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.TEAL, ft.colors.SURFACE]
        ),
        content=ft.Image(
            src='https://assets.pokemon.com/assets/cms2/img/pokedex/full/001'
                '.png',
            scale=1.5
        ),
        alignment=ft.alignment.center
    )
    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text('N° 001', color=ft.colors.YELLOW_600, size=30),
                ft.Text('Bulbassauro', weight=ft.FontWeight.BOLD, size=40),
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
    skills = ft.Container(
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
    layout = ft.Container(
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
    page.add(layout)
    # page.update()


if __name__ == "__main__":
    ft.app(target=main)
