import schedule
import time
import ponto  # Importando o arquivo ponto.py

# Função para iniciar a automação
def iniciar_automacao():
    print("Automação iniciada...")

# Agendamento de horários de registro de ponto (de segunda a sexta-feira)
schedule.every().monday.at("08:00").do(ponto.registrar_ponto)  # Registro do ponto às 08:00
schedule.every().monday.at("12:30").do(ponto.registrar_ponto)  # Registro do ponto às 12:30
schedule.every().monday.at("13:30").do(ponto.registrar_ponto)  # Registro do ponto às 13:30
schedule.every().monday.at("17:00").do(ponto.registrar_ponto)  # Registro do ponto às 17:00

# Agendando a automação para iniciar às 07:55
schedule.every().monday.at("07:55").do(iniciar_automacao)

# Agendando para desligar a automação às 17:05
schedule.every().monday.at("17:05").do(ponto.desligar_automacao)

# Loop para manter a execução do agendamento
if __name__ == "__main__":
    while True:
        schedule.run_pending()  # Executa as tarefas agendadas
        time.sleep(1)  # Espera 1 segundo entre as verificações
