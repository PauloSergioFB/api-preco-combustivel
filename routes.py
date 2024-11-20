from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

from services import *


app = FastAPI(title="API Preço dos Combustí veis", description="API para consultar preços de combustíveis por estado.", version="1.0.0")


class State(str, Enum):
    """
    Enum que representa os estados brasileiros e a opção 'br' para o Brasil como um todo.
    """
    br = "br"
    ac = "ac"
    al = "al"
    ap = "ap"
    am = "am"
    ba = "ba"
    ce = "ce"
    df = "df"
    es = "es"
    go = "go"
    ma = "ma"
    mt = "mt"
    ms = "ms"
    mg = "mg"
    pa = "pa"
    pb = "pb"
    pr = "pr"
    pe = "pe"
    pi = "pi"
    rj = "rj"
    rn = "rn"
    rs = "rs"
    ro = "ro"
    rr = "rr"
    sc = "sc"
    sp = "sp"
    se = "se"
    to = "to"


class FuelType(str, Enum):
    """
    Enum que representa os tipos de combustível suportados pela API.
    """
    gasoline = "gasolina"
    diesel = "diesel"
    ethanol = "etanol"
    energy = "energia"


class FuelPrice(BaseModel):
    """
    Modelo que define o formato dos dados de entrada para a rota de preço de combustível.
    """
    fuel_type: FuelType
    state: State = State.br


@app.get("/")
def root():
    """
    Rota inicial para testar se a API está funcionando.
    Retorna uma mensagem simples de boas-vindas.
    """
    return {"message": "Hello World!"}


@app.get("/gasolina")
def get_gasoline_average_price():
    """
    Retorna o preço médio nacional da gasolina.
    """
    price = get_gasoline_price("br")
    return {"preco": price}


@app.get("/gasolina/{state}")
def get_gasoline_state_price(state: State):
    """
    Retorna o preço da gasolina para um estado específico.
    """
    price = get_gasoline_price(state.value)
    return {"preco": price}


@app.get("/diesel")
def get_diesel_average_price():
    """
    Retorna o preço médio nacional do diesel.
    """
    price = get_diesel_price("br")
    return {"preco": price}


@app.get("/diesel/{state}")
def get_diesel_state_price(state: State):
    """
    Retorna o preço do diesel para um estado específico.
    """
    price = get_diesel_price(state.value)
    return {"preco": price}


@app.get("/etanol")
def get_ethanol_average_price():
    """
    Retorna o preço médio nacional do etanol.
    """
    price = get_ethanol_price()
    return {"preco": price}


@app.get("/etanol/{state}")
def get_ethanol_state_price(state: State):
    """
    Retorna o preço do etanol para um estado específico.
    Observação: atualmente retorna o preço fixo nacional.
    """
    price = get_ethanol_price()
    return {"preco": price}


@app.get("/energia")
def get_energy_average_price():
    """
    Retorna o preço médio nacional da energia elétrica.
    """
    price = get_energy_price()
    return {"preco": price}


@app.get("/energia/{state}")
def get_energy_state_price(state: State):
    """
    Retorna o preço da energia elétrica para um estado específico.
    Observação: atualmente retorna o preço fixo nacional.
    """
    price = get_energy_price()
    return {"preco": price}


@app.post("/combustivel")
def post_get_fuel_price(data: FuelPrice):
    """
    Retorna o preço do combustível especificado (gasolina, diesel, etanol ou energia) para um estado.
    Dados de entrada:
    - `fuel_type`: Tipo de combustível (gasolina, diesel, etanol, energia).
    - `state`: Estado para consulta (default: Brasil como um todo).
    """
    match (data.fuel_type.value):
        case "gasolina": price = get_gasoline_price(data.state.value)
        case "diesel": price = get_diesel_price(data.state.value)
        case "etanol": price = get_ethanol_price()
        case "energia": price = get_energy_price()

    return {"preco": price}
