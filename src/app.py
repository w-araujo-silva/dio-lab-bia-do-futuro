import json
import pandas as pd
import requests
import streamlit as st

# ============= CHAMAR OLLAMA =================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

# ============= CARREGAR DADOS =================
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============= MONTAR CONTEXTO =================
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============= SYSTEM PROMPT =================
SYSTEM_PROMPT = """Você é o RendaBoot, um agente financeiro inteligente especializado em investimentos.

OBJETIVO: Seu objetivo é informar ao cliente as possibilidades de investimento adequadas ao seu perfil de investidor.

REGRAS:
- Sempre baseie suas respostas nos dados fornecidos
- Nunca invente informações financeiras
- Se não souber algo, admita e ofereça alternativas
- Nunca apresente um produto de investimento cujo perfil de investidor é acima do cadastrado para o cliente
"""

# ============= CHAMAR OLLAMA =================
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============= INTERFACE =================
st.title("Oi! Sou o RendaBoot, seu assistente de investimentos")

if pergunta := st.chat_input("Sua dúvida sobre investimentos..."):
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
