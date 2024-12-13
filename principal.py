from tkinter import Tk, Button, Canvas, mainloop
from os import path
from PIL import ImageTk
from model.relatorio import relatorio_pokemons


def gerir():
    from view.código_tela_de_adicionamento import Tela
    global master
    Tela(master)


def ver():
    from view.personagens import personagem
    global master
    personagem(master)


def bg_foto(qual: str) -> ImageTk:
    SEPARADOR = '\\'
    if qual == 'b':
        return ImageTk.PhotoImage(
            file=str(
                path.dirname(path.realpath(__file__)) + SEPARADOR +
                'assets' + SEPARADOR + 'pokedex.png'
            )
        )
    else:
        return ImageTk.PhotoImage(
            file=str(
                path.dirname(path.realpath(__file__)) + SEPARADOR +
                'assets' + SEPARADOR + 'powered_by.jpg'
            )
        )


if __name__ == '__main__':
    master = Tk()
    master.geometry('586x462')
    master.resizable(False, False)
    master.title('Pokedex')

    tela = Canvas(master, bg='white')

    imagens = (bg_foto('b'), bg_foto('l'))
    tela.create_image(-90, 70, image=imagens[1], anchor='nw')
    tela.create_image(0, 0, image=imagens[0], anchor='nw')

    tela.place(x=0, y=0, relwidth=1, relheight=1)
    gerenciar = Button(master,
                       text='CRUD',
                       command=gerir,
                       bg='#FFA500')
    gerenciar.place(x=358, y=360, width=79, height=30)

    visualizar = Button(master,
                        text='Biografia',
                        command=ver,
                        bg='#FFA500')
    visualizar.place(x=458, y=360, width=78, height=30)

    destruir = Button(master,
                      text='Sair',
                      command=master.destroy,
                      bg='#FFFF00')
    destruir.place(x=70, y=353, height=40, width=95)

    relatorio = Button(master,
                       text='Relatório',
                       command=relatorio_pokemons,
                       bg='#888')
    relatorio.place(x=0, y=0, relwidth=80, relheight=30)

    mainloop()
