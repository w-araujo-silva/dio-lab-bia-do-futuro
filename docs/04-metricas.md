# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar possibilidade de aplicar em produto indisponível e ele negar |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Previsão do tempo (fora do escopo).
- **Pergunta:** "Qual a previsão de tempo para amanhã."
- **Resposta esperada:** Sou especializado em investimentos e não tenho informações sobre previsão do tempo.
Posso te ajudar com algo relacionado às suas finanças ou opções de aplicação de acordo com seu perfil de investidor?
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Produtos disponíveis para o perfil de investidor do cliente
- **Pergunta:** "Quais produtos de investimentos estão disponíveis para o meu perfil de investidor?"
- **Resposta esperada:** Todos os produtos disponíveis na base de conhecimento, exceto Fundo de Ações. 
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Investir em Poupança
- **Pergunta:** "Posso investir em Poupança?"
- **Resposta esperada:** Agente informa que o produto Poupança não está disponível.
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**
- A aplicação se limitou a responder perguntas relativas a investimentos.

**O que pode melhorar:**
- O tempo de resposta.

