import pyautogui
import time
import sys

print("Pressione Ctrl+C para encerrar o programa.")

try:
    while True:
        # Pega a posição atual do mouse (x, y)
        x, y = pyautogui.position()

        # Cria uma string formatada. O ljust/rjust garante que o texto
        # mantenha um tamanho fixo, evitando que restos de números fiquem na tela.
        posicao = f"X: {str(x).ljust(4)} Y: {str(y).ljust(4)}"

        # Imprime na mesma linha usando o caractere de retorno '\r'
        # sys.stdout.flush() garante que o texto apareça imediatamente
        print(posicao, end='\r')
        sys.stdout.flush()

        # Pequena pausa para não sobrecarregar o processador desnecessariamente
        time.sleep(0.1)

except KeyboardInterrupt:
    # Tratamento para sair graciosamente quando apertar Ctrl+C
    print("\nPrograma encerrado.")
