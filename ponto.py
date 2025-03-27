import requests
import sys
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da API
BASE_URL = "https://centraldofuncionario.com.br/api"
LOGIN_ENDPOINT = "/auth/login"
PONTO_ENDPOINT = "/registrar_ponto"

# Suas credenciais
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Função para autenticar e obter o token de acesso
def obter_token():
    response = requests.post(f"{BASE_URL}{LOGIN_ENDPOINT}", json={"username": USERNAME, "password": PASSWORD})
    if response.status_code == 200:
        return response.json().get("token")
    else:
        print("Erro ao obter token:", response.text)
        return None

# Função para registrar o ponto
def registrar_ponto():
    token = obter_token()
    if not token:
        print("Não foi possível obter o token. Tentando novamente depois.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}{PONTO_ENDPOINT}", headers=headers)

    if response.status_code == 200:
        print("Ponto registrado com sucesso:", response.json())
    else:
        print("Erro ao registrar ponto:", response.text)

# Função para desligar a automação
def desligar_automacao():
    print("Desligando automação...")
    sys.exit()  # Interrompe a execução do script
