# API Preços dos Combustíveis

Uma API para consultar preços de combustíveis (gasolina, diesel, etanol e energia elétrica) no Brasil. A API utiliza web scraping para buscar os preços diretamente da fonte oficial e oferece valores médios nacionais ou específicos por estado.

---

## 📜 Proposta

O objetivo desta API é facilitar o acesso a informações atualizadas sobre preços de combustíveis no Brasil, permitindo consultas rápidas e integráveis com outras aplicações. Ideal para sistemas de comparação de custos, análises de consumo, ou até mesmo para usuários finais que buscam economia.

---

## 🚀 Setup Local (Como Rodar)

### Pré-requisitos
- **Python 3.9 ou superior**
- Gerenciador de pacotes `pip`
- Ambiente virtual (opcional, mas recomendado)
- Biblioteca `FastAPI`, `BeautifulSoup4`, e `requests`

### Passos para executar localmente:

1. Clone o repositório:
   ```bash
   git clone https://github.com/PauloSergioFB/api-preco-combustivel.git
   cd api-preco-combustivel
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # No Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o servidor local:
   ```bash
   fastapi dev main.py
   ```

5. Acesse a documentação interativa da API:
   - Abra o navegador e vá para [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🛠️ Web Scraping (Fonte dos Dados)

A API utiliza a biblioteca `BeautifulSoup` para realizar web scraping na página oficial da **Petrobras**:

- **Gasolina e Diesel**: Os preços são obtidos diretamente da [tabela de preços da Petrobras](https://precos.petrobras.com.br/sele%C3%A7%C3%A3o-de-estados-gasolina).
- **Etanol e Energia Elétrica**: Esses preços são fixados, mas podem ser atualizados conforme necessário.

### Detalhes técnicos:
- Os dados são extraídos dos elementos HTML específicos nas páginas, utilizando identificadores e atributos.
- Caso não seja possível obter os dados (e.g., mudanças na página), a API retorna `None` para evitar informações inconsistentes.
