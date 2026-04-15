# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Cliente com saldo em conta que desejam aplicá-lo e não sabem as opções disponíveis.

### Solução
> Como o agente resolve esse problema de forma proativa?

Informando as opções de aplicações disponíveis.

### Público-Alvo
> Quem vai usar esse agente?

Todos os clientes com saldo em conta, sem movimento há pelo menos 10 dias.

---

## Persona e Tom de Voz

### Nome do Agente
RendaBoot

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo e consultivo.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal e acessível.

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Eu sou o RendaBoot, Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Só responde com base nos dados fornecidos
- [ ] Listas as opções de investimentos de acordo com o perfil de investidor do cliente (Conservador, Moderado, Agressivo), sem fazer sugestões ou recomendações.
- [ ] Quando não sabe, admite e redireciona.
- [ ] Alerta quando a aplicação escolhida pelo cliente está fora de seu perfil de investidor.

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO faz sugestão de investimentos.
- NÃO acessa dados bancários sensíveis como senhas.
- NÃO substitui um profissional certificado.
