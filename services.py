import requests
from bs4 import BeautifulSoup


# Função para obter o preço da gasolina em um estado específico.
def get_gasoline_price(state):
    try:
        url = f"https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/gasolina/{state}"

        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        # Procura o elemento HTML que contém o preço final da gasolina.
        price = soup.find(id="telafinal-precofinal").text
        
        # Verifica se o preço encontrado é "0,0" (indicativo de dados inválidos).
        if price == "0,0": 
            return  # Retorna None se o preço for inválido.
    except:
        # Captura exceções e retorna None em caso de erro.
        return

    # Converte o preço para um número float, substituindo a vírgula por ponto.
    price = float(price.replace(",", "."))
    return price


# Função para obter o preço do diesel em um estado específico.
def get_diesel_price(state):
    try:
        url = f"https://precos.petrobras.com.br/web/precos-dos-combustiveis/w/diesel/{state}"

        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        # Procura o elemento HTML com o preço final do diesel (busca por tag e atributo).
        price = soup.find('p', {'data-lfr-editable-id': 'telafinal-precofinal'}).text
        
        # Verifica se o preço encontrado é "0,0" (indicativo de dados inválidos).
        if price == "0,0": 
            return  # Retorna None se o preço for inválido.
    except:
        # Captura exceções e retorna None em caso de erro.
        return

    # Converte o preço para um número float, substituindo a vírgula por ponto.
    price = float(price.replace(",", "."))
    return price
    
# Função para obter o preço fixo do etanol (não foi possível encontrar um serviço confiável para fornecer esse dado).
def get_ethanol_price():
    return 3.86


# Função para obter o preço fixo da energia elétrica (não foi possível encontrar um serviço confiável para fornecer esse dado).
def get_energy_price():
    return 0.57
