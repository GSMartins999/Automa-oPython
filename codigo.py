# Utilizamos a biblioteca pyautogui para automatizar as tarefas.

# Com ela iremos conseguir fazer o clique do mouse, a digitação de teclas e também pressionar teclas com a biblioteca.

# comandos para isso -> .click = clicar com o mouse, .write -> escreve um texto, .press -> pressiona uma tecla,.hotkey -> pressiona um conjunto de teclas(ctrl + C, ctrl + V..), .position -> verifica a posição do mouse

import pyautogui
import time 
# time -> Serve para fazer o código dormir por um determinado tempo(não precisa ser instalada, ela já vem no próprio python.)

# PAUSE, serve para dar uma pausa para executar um trecho do código
pyautogui.PAUSE = 0.5

# Abrir o navegador:
pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")

time.sleep(3)

# Abrir o site para inserir os dados:
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# Usando o time.sleep
time.sleep(3)
# clicou no campo de email:
pyautogui.click(x=693, y=461)
pyautogui.write("y@gmail.com")
# passou para o input de senha:
pyautogui.press("tab")
pyautogui.write("12345678")
# aqui podemos ou dar tab e enter depois ou então clicar novamente no botão de logar, fiz a segunda opção abaixo
pyautogui.click(x=968, y=667)

time.sleep(2)


## Vamos começar a trabalhar com a biblioteca pandas, onde ela irá ler nossa base de dados e atráves dela conseguiremos fazer nossa automação:


import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Clicar no campo código do produto:

pyautogui.click(x=1854, y=122)
time.sleep(2)

# usamos o for para cadastrar todos os dados no formulário:
for linha in tabela.index:

    # aqui, estamos fazendo a troca de código de acordo com a linha
    # loc é uma das funções do pandas que servem para resgatar dados, primeiro devemos colocar a linha e depois a coluna na função:
    codigo = str(tabela.loc[linha, "codigo"])

    pyautogui.click(x=847, y=314)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)