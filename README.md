
# Cronômetro e Temporizador

## Descrição
Este é um aplicativo desenvolvido em Python com interface gráfica, que permite utilizar um cronômetro ou temporizador, registrar tempos, e salvar o histórico em um arquivo. O programa é interativo, fácil de usar e visualmente organizado.

---

## Funcionalidades
- **Cronômetro**:
  - Realiza contagem progressiva no formato `HH:MM:SS`.
  - Pode ser pausado, redefinido ou salvo.
  
- **Temporizador**:
  - Realiza contagem regressiva até zero no formato `HH:MM:SS`.
  - Pode ser pausado, redefinido ou salvo.
  
- **Histórico de Tempos**:
  - Permite salvar tempos com nomes personalizados.
  - Exibe os tempos registrados em uma janela separada.

- **Salvar em Arquivo**:
  - O histórico pode ser salvo em um arquivo `.txt` de sua escolha.

- **Exibição de Hora e Data**:
  - Exibe a hora e a data atualizadas em tempo real.

---

## Instalação

1. **Requisitos**:
   - Python 3.9 ou superior.
   - Biblioteca `customtkinter`.

2. **Instalação do `customtkinter`**:
   Execute o comando abaixo no terminal:
   ```bash
   pip install customtkinter
   ```

3. **Execução**:
   - Baixe o código e salve em um arquivo `cronometro.py`.
   - Execute o programa com:
     ```bash
     python cronometro.py
     ```

---

## Como Usar

1. **Selecionar uma Opção**:
   - Escolha entre "Cronômetro" (`⏱✡`) ou "Temporizador" (`⏳✡`).

2. **Adicionar Nome**:
   - Insira um nome no campo "Nome do Tempo" para identificar o tempo.

3. **Iniciar**:
   - Clique no botão "Iniciar" para começar o cronômetro ou temporizador.

4. **Parar/Redefinir**:
   - Use os botões "Parar" ou "Redefinir" conforme necessário.

5. **Salvar Tempo**:
   - Clique em "Salvar Tempo" para registrar o tempo atual no histórico.
   - Escolha onde salvar o arquivo no formato `.txt`.

6. **Visualizar Histórico**:
   - Clique em "Visualizar Tempos" para abrir uma janela com o histórico registrado.

---

## Estrutura do Código

### Arquivo Principal: `cronometro.py`
- **Funções principais**:
  - `iniciar()`: Inicia o cronômetro ou temporizador.
  - `parar()`: Pausa o tempo atual.
  - `redefinir()`: Reseta o tempo para `00:00:00`.
  - `salvar()`: Salva o histórico em um arquivo `.txt`.
  - `visualizar()`: Exibe os tempos salvos.
  - `atualizar_hora_data()`: Atualiza a hora e data em tempo real.

---

## Contribuição

Contribuições são bem-vindas! Siga os passos:
1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade: `git checkout -b feature/nova-funcionalidade`.
3. Faça um commit das alterações: `git commit -m 'Adiciona nova funcionalidade'`.
4. Faça um push para a branch: `git push origin feature/nova-funcionalidade`.
5. Abra um pull request.

---

## Licença

Este projeto é de uso livre e aberto sob a licença MIT.
