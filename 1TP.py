## Primeiro Trabalho Parcial: Parametrização de um FT.
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import step

def plot_step_response(ta):
    # Verifica se o tempo de assentamento está dentro do intervalo permitido
    if not (2e-3 <= ta <= 10e-3):
        raise ValueError('O tempo de assentamento deve estar entre 2ms e 10ms.')
    
    # Definindo o tempo de assentamento desejado
    final_settling_time = ta

    # Ajuste inicial da constante de tempo tau
    tau = ta / 3  # Ajuste conforme necessário para atender aos requisitos

    # Ganho do sistema
    K = 1

    # Numerador e denominador da função de transferência
    numerator = [K]
    denominator = [tau, 1]

    # Criando a função de transferência
    sys = (numerator, denominator)

    # Definindo os limites de tempo
    t = np.linspace(0, 5*final_settling_time, 1000)

    # Obtendo a resposta ao degrau da função de transferência usando scipy.signal.step
    t, y = step(sys, T=t)

    # Plotando o gráfico da resposta ao degrau
    plt.plot(t, y, 'b', linewidth=2)
    plt.grid(True)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Resposta ao Degrau')
    plt.title('Resposta ao Degrau de uma Função de Transferência de 1ª Ordem')

    # Exibindo o tempo de assentamento final
    final_settling_time_message = f'Tempo de Assentamento Final: {final_settling_time:.2f} segundos'
    print(final_settling_time_message)

    plt.show()

# Exemplo de uso
plot_step_response(5e-3)
