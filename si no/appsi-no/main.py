import flet as ft


def main(page: ft.Page):
    page.title = "¿regresamos?"
    page.bgcolor ="pink"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    lbl1=ft.Text("¿regresamos?",
                style=ft.TextStyle(size=40,weight="bold"))
    ing1=ft.Image(src="triste.png",width=200,height=200)
    
    btnSI=ft.ElevatedButton("si",
                            color="green",
                            width=100,
                            height=50)
    btnNO=ft.ElevatedButton("no",
                            color="red",
                            width=100,
                            height=50
                            ) 
    def no(e):
        btnSI.width+=30
        btnNO.height+=10
        page.update()
    def si(e):
        ing1.src="feliz.png"
        page.update()
        
    
    btnNO.on_click=no
    btnSI.on_click=si
    page.add (
        ft.Column(
            [
                lbl1,
                ing1,
                ft.Row(
                    [btnSI,btnNO],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing = 20
        )
    )


ft.app(main)
