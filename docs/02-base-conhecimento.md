# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Função para o RendaBoot |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Informar aplicações disponíveis de acordo com o perfil de investidor do cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

---

## Adaptações nos Dados

Inserido o perfil de investidor recomendado para cada produto financeiro para que não seja exibido produtos acima do perfil de investidor do cliente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibiliades, injetar os dados diretamente no prompt ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv(data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='uft-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='uft-8') as f:
  produtos = json.load(f) 
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que o Agente tenha o melhor contexto possível. Para soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente para ganho de flexibilidade.

```text
DADOS DO CLIENTE (perfil_investidor.json) :

{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}


PRODUTOS DISPONIVEIS PARA APLICACAO (produtos_financeiros.json):

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "perfil_recomendado": "conservador",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "perfil_recomendado": "conservador",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo"
    "perfil_recomendado": "conservador",,
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "perfil_recomendado": "moderado",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "perfil_recomendado": "agressivo",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto montando abaixo é baseado nos dados originais, mas o sintetiza deixando apenas as informações relevantes, otimizando o consumo de tokens. Vale lembrar que mais importante que a economia de tokens, é ter todas as informações relevantes disponíveis em seu contexto.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Produtos disponíveis para aplicação:
- Tesouro Selic
- CDB Liquidez Diária
- LCI/LCA
- Fundo Multimercado

```
