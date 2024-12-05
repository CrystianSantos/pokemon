from tkinter import Tk, Label, Button, CENTER, mainloop


def gerir():
    from view.código_tela_de_adicionamento import Tela
    global master
    Tela(master)


def ver():
    from view.personagens import personagem
    global master
    personagem(master)


if __name__ == '__main__':
    master = Tk()
    master.geometry('720x480')

    titulo = Label(master, text='Pokedex')
    titulo.pack()

    gerenciar = Button(master, text='Tela de CRUD', command=gerir)
    gerenciar.place(relx=0.3, rely=0.5, anchor=CENTER)

    visualizar = Button(master, text='Ver pokemons', command=ver)
    visualizar.place(relx=0.7, rely=0.5, anchor=CENTER)

    mainloop()
