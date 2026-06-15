import flet as ft

def main(page: ft.Page):
    page.title = "Cinema Stardust Crusaders"
    page.window.width = 1920
    page.window.height = 1080

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    salas = {
        "Backrooms": [
            ["L", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L"],
        ],

        "Obsessão": [
            ["L", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L"],
        ],

        "Michael": [
            ["L", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L"],
            ["L", "L", "L", "L", "L"],
        ]
    }
    
    def calcular_ocupacao(nome):
        livres = 0
        ocupados = 0

        for linha in range(3):
            for coluna in range(5):
                if salas[nome][linha][coluna] == "L":
                    livres += 1
                elif salas[nome][linha][coluna] == "O":
                    ocupados += 1

        total = livres + ocupados
        percentual = (ocupados / total) * 100

        return livres, ocupados, percentual

    def selecionar_assento(nome, linha, coluna):
        if salas[nome][linha][coluna] == "L":
            salas[nome][linha][coluna] = "S"

        elif salas[nome][linha][coluna] == "S":
            salas[nome][linha][coluna] = "L"

        escolher_filme(nome)

    def confirmar_compra(nome):
        escolhidos = []

        for linha in range(3):
            for coluna in range(5):
                if salas[nome][linha][coluna] == "S":
                    escolhidos.append(f"{linha + 1}-{coluna + 1}")
                    salas[nome][linha][coluna] = "O"

        page.clean()

        page.add(
            ft.Container(height=30),
            ft.Text("Compra confirmada!", size=30, weight="bold"),
            ft.Text(f"Assentos escolhidos: {', '.join(escolhidos)}"),
            ft.Button(
                "Voltar para a sala",
                on_click=lambda: escolher_filme(nome)
            ),
            ft.Button(
                "Cancelar compra",
                on_click=lambda: cancelar_compra(nome)
            )   
        )

    def escolher_filme(nome):
        page.clean()

        livres, ocupados, percentual = calcular_ocupacao(nome)

        page.add(
            ft.Container(height=30),
            ft.Text(
                nome,
                size=30,
                weight="bold"
            ),
            ft.Text("Escolha seus assentos"),
            ft.Container(height=20),
            ft.Text(f"Assentos livres: {livres}"),
            ft.Text(f"Assentos ocupados: {ocupados}"),
            ft.Text(f"Ocupação: {percentual:.0f}%"),
            ft.Container(height=40),
        ),

        mostrar_assentos(nome, salas[nome])

        page.add(
            ft.Text("-------------------------TELA-------------------------"),
            ft.Container(height=30),
            ft.Button(
                "Confirmar compra",
            on_click=lambda: confirmar_compra(nome)
        ),
        ft.Button(
            "Cancelar compra",
            on_click=lambda: cancelar_compra(nome)
        ),
        ft.Button(
            "VOLTAR",
            on_click=lambda: clique_iniciar()
        )
    )
    
    def cancelar_compra(nome):
        for linha in range(3):
         for coluna in range(5):
                if salas[nome][linha][coluna] == "O":
                   salas[nome][linha][coluna] = "L"

        escolher_filme(nome)

    def mostrar_assentos(nome, assentos):
        for linha in range(3):
            botoes = []

            for coluna in range(5):
                estado = assentos[linha][coluna]

                if estado == "S":
                    texto = "✓"
                elif estado == "O":
                    texto = "X"
                else:
                    texto = f"{linha + 1}-{coluna + 1}"

                botoes.append(
                    ft.Button(
                        texto,
                        width=70,
                        height=50,
                        disabled=estado == "O",
                        on_click=lambda e, l=linha, c=coluna: selecionar_assento(nome, l, c)
                    )
                )

            page.add(
                ft.Row(
                    controls=botoes,
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )

    def clique_iniciar():
        page.clean()
        page.add(
            ft.Container(height=30),
            ft.Text(
                "Filmes em cartaz",
                size=30,
                weight="bold"
            ),
            ft.Text(
                "Clique para escolher"
            ),
            ft.Container(height=50),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(src="assets/backrooms.jpg", width=150),
                                ft.Text(
                                    "     Backrooms",
                                    size=20,
                                )
                            ]
                        ),
                        on_click=lambda: escolher_filme("Backrooms")
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(src="assets/obsession.jpg", width=150),
                                ft.Text(
                                    "     Obsessão",
                                    size=20,
                                )
                            ]
                        ),
                        on_click=lambda: escolher_filme("Obsessão")
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(src="assets/michael.jpg", width=150),
                                ft.Text(
                                    "       Michael",
                                    size=20,
                                )
                            ]
                        ),
                        on_click=lambda: escolher_filme("Michael")
                    )
                ],
                spacing=60,
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    page.add(
        ft.Image(
            src="assets/logo.png",
            width=500,
            height=400
        ),
        ft.Button(
            "INICIAR",
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=25, weight="bold")
            ),
            width=150,
            height=50,   
            on_click=clique_iniciar
        )
    )
    
ft.run(main)