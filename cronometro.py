import time
from datetime import datetime
from tkinter import filedialog  # Para salvar arquivos

import customtkinter as ctk

# Configuração do tema
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

# Configuração da janela principal
app = ctk.CTk()
app.title("Cronômetro e Temporizador")
app.geometry("600x600")  # Aumentado o tamanho da janela

# Variáveis globais
opcao = ctk.StringVar(value="Cronômetro")
tempo_total = 0
rodando = False
historico = []  # Lista para armazenar os tempos

# Configuração de cores e fontes
COR_TEXTO = "#4169E1"  # Azul Real
COR_BOTAO = "#1E90FF"  # Azul Médio Brilhante
COR_BOTAO_PARAR = "#FF4500"  # Laranja avermelhado
COR_BOTAO_REDEFINIR = "#696969"  # Cinza Escuro
FONTE_TITULO = ("Arial", 30, "bold")
FONTE_TEXTO = ("Arial", 16)
FONTE_TEMPO = ("Arial", 40, "bold")
FONTE_ICONE = ("Arial", 20)

# Funções
def atualizar_hora_data():
    """Atualiza a hora e a data local."""
    agora = datetime.now()
    hora_atual = agora.strftime("%H:%M:%S")
    data_atual = agora.strftime("%d/%m/%Y")
    hora_label.configure(text=f"Hora: {hora_atual}")
    data_label.configure(text=f"Data: {data_atual}")
    app.after(1000, atualizar_hora_data)  # Atualiza a cada 1 segundo

def iniciar():
    """Inicia o cronômetro ou temporizador com nome opcional."""
    global rodando
    rodando = True
    nome = nome_entrada.get().strip() or "Sem Nome"
    if opcao.get() == "Cronômetro":
        iniciar_cronometro(nome)
    elif opcao.get() == "Temporizador":
        iniciar_temporizador(nome)

def iniciar_cronometro(nome):
    global tempo_total, rodando
    while rodando:
        mins, secs = divmod(tempo_total, 60)
        horas, mins = divmod(mins, 60)
        tempo_label.configure(text=f"{horas:02}:{mins:02}:{secs:02}")
        app.update()
        time.sleep(1)
        tempo_total += 1

def iniciar_temporizador(nome):
    global tempo_total, rodando
    while rodando and tempo_total > 0:
        mins, secs = divmod(tempo_total, 60)
        horas, mins = divmod(mins, 60)
        tempo_label.configure(text=f"{horas:02}:{mins:02}:{secs:02}")
        app.update()
        time.sleep(1)
        tempo_total -= 1
    if tempo_total <= 0:
        tempo_label.configure(text="00:00:00")

def parar():
    """Para o cronômetro ou temporizador."""
    global rodando
    rodando = False

def redefinir():
    """Redefine o cronômetro ou temporizador."""
    global tempo_total, rodando
    rodando = False
    tempo_total = 0
    tempo_label.configure(text="00:00:00")

def salvar():
    """Salva o tempo atual no histórico com nome opcional."""
    global tempo_total
    nome = nome_entrada.get().strip() or "Sem Nome"
    mins, secs = divmod(tempo_total, 60)
    horas, mins = divmod(mins, 60)
    tempo_formatado = f"{horas:02}:{mins:02}:{secs:02}"
    historico.append(f"{nome} ({opcao.get()}): {tempo_formatado}")
    
    # Salvar em arquivo escolhido pelo usuário
    caminho_arquivo = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Arquivo de Texto", "*.txt")]
    )
    if caminho_arquivo:
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write("\n".join(historico))
        ctk.CTkLabel(app, text="Tempo salvo com sucesso!", text_color="green", font=FONTE_TEXTO).pack(pady=5)

def visualizar():
    """Exibe os tempos salvos em uma nova janela."""
    janela_historico = ctk.CTkToplevel(app)
    janela_historico.title("Histórico de Tempos")
    janela_historico.geometry("400x300")

    titulo_historico = ctk.CTkLabel(janela_historico, text="Histórico de Tempos", font=FONTE_TITULO, text_color=COR_TEXTO)
    titulo_historico.pack(pady=10)

    for tempo in historico:
        ctk.CTkLabel(janela_historico, text=tempo, font=FONTE_TEXTO, text_color=COR_TEXTO).pack()

# Layout da interface

# Título principal
titulo = ctk.CTkLabel(
    app, text="SCHAEDLER", font=FONTE_TITULO, text_color=COR_TEXTO
)
titulo.pack(pady=10)

# Hora e data
hora_label = ctk.CTkLabel(
    app, text="Hora: --:--:--", font=FONTE_TEXTO, text_color=COR_TEXTO
)
hora_label.pack()

data_label = ctk.CTkLabel(
    app, text="Data: --/--/----", font=FONTE_TEXTO, text_color=COR_TEXTO
)
data_label.pack()

linha = ctk.CTkLabel(
    app, text="─" * 50, font=FONTE_TEXTO, text_color=COR_TEXTO
)
linha.pack(pady=5)

# Entrada para nome
nome_label = ctk.CTkLabel(app, text="Nome do Tempo:", font=FONTE_TEXTO, text_color=COR_TEXTO)
nome_label.pack(pady=5)
nome_entrada = ctk.CTkEntry(app, placeholder_text="Digite um nome...", font=FONTE_TEXTO)
nome_entrada.pack(pady=5)

# Opções de escolha
opcao_label = ctk.CTkLabel(
    app, text="Escolha uma opção:", font=FONTE_TEXTO, text_color=COR_TEXTO
)
opcao_label.pack(pady=10)

# Botão com ícone - Cronômetro
cronometro_frame = ctk.CTkFrame(app, fg_color="transparent")
cronometro_frame.pack(pady=5)

cronometro_icone = ctk.CTkLabel(
    cronometro_frame, text="⏱✡", font=FONTE_ICONE, text_color=COR_TEXTO
)
cronometro_icone.grid(row=0, column=0, padx=5)

radio_cronometro = ctk.CTkRadioButton(
    cronometro_frame, text="Cronômetro", variable=opcao, value="Cronômetro", text_color=COR_TEXTO
)
radio_cronometro.grid(row=0, column=1, padx=5)

# Botão com ícone - Temporizador
temporizador_frame = ctk.CTkFrame(app, fg_color="transparent")
temporizador_frame.pack(pady=5)

temporizador_icone = ctk.CTkLabel(
    temporizador_frame, text="⏳✡", font=FONTE_ICONE, text_color=COR_TEXTO
)
temporizador_icone.grid(row=0, column=0, padx=5)

radio_temporizador = ctk.CTkRadioButton(
    temporizador_frame, text="Temporizador", variable=opcao, value="Temporizador", text_color=COR_TEXTO
)
radio_temporizador.grid(row=0, column=1, padx=5)

# Exibição do tempo
tempo_label = ctk.CTkLabel(
    app,
    text="00:00:00",
    font=FONTE_TEMPO,
    text_color=COR_TEXTO
)
tempo_label.pack(pady=20)

# Botões de controle
botoes_frame = ctk.CTkFrame(app)
botoes_frame.pack(pady=10)

botao_iniciar = ctk.CTkButton(
    botoes_frame, text="Iniciar", command=iniciar, fg_color=COR_BOTAO, text_color="white"
)
botao_iniciar.grid(row=0, column=0, padx=10)

botao_parar = ctk.CTkButton(
    botoes_frame, text="Parar", command=parar, fg_color=COR_BOTAO_PARAR, text_color="white"
)
botao_parar.grid(row=0, column=1, padx=10)

botao_redefinir = ctk.CTkButton(
    botoes_frame, text="Redefinir", command=redefinir, fg_color=COR_BOTAO_REDEFINIR, text_color="white"
)
botao_redefinir.grid(row=0, column=2, padx=10)

# Botões para salvar e visualizar tempos
botao_salvar = ctk.CTkButton(
    app, text="Salvar Tempo", command=salvar, fg_color=COR_BOTAO, text_color="white"
)
botao_salvar.pack(pady=10)

botao_visualizar = ctk.CTkButton(
    app, text="Visualizar Tempos", command=visualizar, fg_color=COR_BOTAO, text_color="white"
)
botao_visualizar.pack(pady=10)

# Inicia a atualização da hora e data
atualizar_hora_data()

# Inicia o loop principal da interface
app.mainloop()
