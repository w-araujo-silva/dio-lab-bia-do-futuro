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

Inserido o perfil de investidor recomendado para cada produto financeiro para que não seja exibido produtos fora do perfil do cliente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos serão carregados via código, como no exemplo abaixo:

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

```text
DADOS DO CLIENTE:

PRODUTOS DISPONIVEIS PARA APLICACAO:
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
