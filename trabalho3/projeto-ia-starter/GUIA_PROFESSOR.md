# 👨‍🏫 Guia do Professor - Microprojeto de IA

## 📋 Visão Geral da Avaliação

Este documento fornece orientações para conduzir a avaliação do microprojeto de IA de forma eficaz e justa.

---

## 🎯 Objetivos Pedagógicos

### Competências Técnicas
- Programação Orientada a Objetos (POO) em Python
- Desenvolvimento web fullstack (frontend + backend)
- Integração com APIs externas (Gemini AI)
- Template engines (Jinja2)
- Framework CSS moderno (Tailwind)
- Trabalho com requisições HTTP

### Competências Transversais
- Trabalho em equipe
- Gestão de tempo
- Resolução de problemas
- Comunicação técnica
- Criatividade aplicada

---

## 📅 Cronograma de Acompanhamento Sugerido

### Semana 1 - Setup e Estrutura

**Checkpoint 1 (Dia 3):**
- ✅ Grupos formados
- ✅ Ideia definida
- ✅ Repositório Git criado
- ✅ Ambiente de desenvolvimento funcionando
- ✅ Primeira versão do README

**O que verificar:**
- Todos têm acesso ao repositório?
- API key do Gemini configurada?
- Código starter rodando?

**Checkpoint 2 (Dia 7):**
- ✅ Backend básico funcionando
- ✅ Integração com Gemini testada
- ✅ Templates básicos criados
- ✅ Primeiros commits no Git

**O que verificar:**
- Rotas FastAPI funcionando?
- Chamada à API retorna resposta?
- Divisão de tarefas clara?

### Semana 2 - Refinamento e Finalização

**Checkpoint 3 (Dia 10):**
- ✅ Funcionalidades principais completas
- ✅ Frontend estilizado
- ✅ Validações implementadas
- ✅ Testes realizados

**O que verificar:**
- Código está limpo?
- POO sendo usado adequadamente?
- Interface funciona em mobile?

**Entrega Final (Dia 14):**
- ✅ Aplicação completa
- ✅ README atualizado
- ✅ Apresentação preparada

---

## 🔍 Como Avaliar - Guia Detalhado

### 1. Funcionalidade e Integração (3,5 pontos)

#### O que avaliar:

**Integração com Gemini (1,5 pontos)**
- [ ] API key configurada corretamente
- [ ] Chamadas à API funcionam
- [ ] Resposta da IA é exibida corretamente
- [ ] Erros de API são tratados
- [ ] Timeout configurado

**Rotas FastAPI (1,0 ponto)**
- [ ] Mínimo de 3 rotas diferentes
- [ ] Rota GET para página inicial
- [ ] Rota POST para processar
- [ ] Rota adicional (histórico, favoritos, etc)
- [ ] Todas retornam status HTTP correto

**Templates Jinja2 (0,5 pontos)**
- [ ] Pelo menos 2 templates
- [ ] Usa herança (extends base.html)
- [ ] Dados passados do backend aparecem no frontend
- [ ] Lógica de template (if, for) usada adequadamente

**Tratamento de Erros (0,5 pontos)**
- [ ] Validação de input do usuário
- [ ] Mensagens de erro amigáveis
- [ ] Não quebra com input inválido
- [ ] Try/except usado adequadamente

#### Critérios de Pontuação:

| Pontos | Descrição |
|--------|-----------|
| 3,5 | Tudo funciona perfeitamente, trata todos os erros, integração impecável |
| 2,5 | Funciona bem, pequenos bugs não críticos |
| 1,5 | Funciona parcialmente, alguns problemas na integração |
| 0,5 | Não funciona ou muitos erros críticos |

---

### 2. Qualidade do Código (2,5 pontos)

#### O que avaliar:

**Programação Orientada a Objetos (1,0 ponto)**
- [ ] Pelo menos 1 classe criada
- [ ] Classe tem construtor (`__init__`)
- [ ] Métodos implementados corretamente
- [ ] Atributos e métodos fazem sentido
- [ ] Encapsulamento adequado
- [ ] Uso de herança ou composição (se aplicável)

**Exemplo de Boa Classe:**
```python
class Personagem:
    def __init__(self, nome: str, nivel: int = 1):
        self.nome = nome
        self.nivel = nivel
        self.vida = 100
    
    def atacar(self, alvo):
        dano = self.nivel * 10
        alvo.receber_dano(dano)
        return f"{self.nome} atacou!"
    
    def receber_dano(self, quantidade: int):
        self.vida -= quantidade
        if self.vida < 0:
            self.vida = 0
```

**Organização e Limpeza (0,8 pontos)**
- [ ] Código indentado corretamente
- [ ] Nomes de variáveis descritivos
- [ ] Funções com propósito único
- [ ] Sem código comentado desnecessário
- [ ] Imports organizados
- [ ] Segue PEP 8 (Python style guide)

**Comentários e Documentação (0,7 pontos)**
- [ ] Funções têm docstrings
- [ ] Comentários explicam o "porquê", não o "o quê"
- [ ] Código complexo está explicado
- [ ] README está completo

#### Critérios de Pontuação:

| Pontos | Descrição |
|--------|-----------|
| 2,5 | Código limpo, POO excelente, muito bem comentado |
| 1,8 | Código organizado, POO básico, alguns comentários |
| 1,0 | Código funcional mas desorganizado |
| 0,3 | Código confuso, sem padrão, POO inadequado |

---

### 3. Criatividade e Valor de Entretenimento (2,0 pontos)

#### O que avaliar:

**Originalidade da Ideia (0,8 pontos)**
- [ ] Ideia diferente dos colegas
- [ ] Abordagem criativa do problema
- [ ] Aplicação interessante da IA

**Qualidade da Experiência (0,7 pontos)**
- [ ] Realmente diverte/entretém
- [ ] Interface convidativa
- [ ] Feedback ao usuário é bom
- [ ] Resultados são interessantes

**Prompts e IA (0,5 pontos)**
- [ ] Prompts bem construídos
- [ ] IA responde adequadamente
- [ ] Temperatura ajustada corretamente
- [ ] Resultados consistentes

#### Critérios de Pontuação:

| Pontos | Descrição |
|--------|-----------|
| 2,0 | Ideia original, muito divertido, surpreendente |
| 1,5 | Boa ideia, entretém bem |
| 1,0 | Ideia comum mas bem executada |
| 0,5 | Pouco criativo ou entediante |

---

### 4. Interface e Experiência do Usuário (1,5 pontos)

#### O que avaliar:

**Design Visual (0,6 pontos)**
- [ ] Interface bonita e moderna
- [ ] Cores harmoniosas
- [ ] Tipografia legível
- [ ] Uso adequado de espaçamento
- [ ] Tailwind bem aplicado

**Responsividade (0,4 pontos)**
- [ ] Funciona em desktop
- [ ] Funciona em tablet
- [ ] Funciona em mobile
- [ ] Sem quebra de layout

**UX/Usabilidade (0,5 pontos)**
- [ ] Fácil de usar
- [ ] Fluxo intuitivo
- [ ] Botões bem posicionados
- [ ] Feedback visual de ações
- [ ] Mensagens claras

#### Critérios de Pontuação:

| Pontos | Descrição |
|--------|-----------|
| 1,5 | Interface profissional, intuitiva, responsiva perfeita |
| 1,0 | Interface boa, pequenos problemas de UX |
| 0,6 | Interface básica mas funcional |
| 0,2 | Interface confusa ou quebrada |

---

### 5. Apresentação e Documentação (0,5 pontos)

#### O que avaliar:

**Apresentação Oral (0,3 pontos)**
- [ ] Todos os membros participam
- [ ] Demo ao vivo funciona
- [ ] Explicam código
- [ ] Respondem perguntas adequadamente
- [ ] Dentro do tempo (5-7 minutos)

**Documentação (0,2 pontos)**
- [ ] README completo
- [ ] Instruções de instalação
- [ ] Screenshots ou GIF
- [ ] Integrantes identificados

#### Critérios de Pontuação:

| Pontos | Descrição |
|--------|-----------|
| 0,5 | Apresentação excelente, README completo, demo perfeita |
| 0,3 | Boa apresentação, documentação básica |
| 0,1 | Apresentação fraca, sem documentação |

---

## 🚨 Critérios de Desclassificação (Nota 0)

Zere o projeto se:

1. **Plágio Confirmado**
   - Código copiado integralmente de terceiros
   - Sem atribuição adequada
   - Não souber explicar o próprio código

2. **Não Usa Stack Obrigatória**
   - Não usa Python/FastAPI
   - Não integra com Gemini
   - Não usa templates Jinja2

3. **Não Funciona**
   - Aplicação não roda
   - Erros impedem uso básico
   - Nem parcialmente funcional

4. **Participação Desigual**
   - Membros que claramente não participaram
   - Só 1 ou 2 pessoas fizeram tudo
   - Não sabem explicar o código na apresentação

---

## 🎯 Observações Durante a Avaliação

### Sinais de Bom Projeto

✅ Commits bem distribuídos entre membros
✅ Código está no Git, não só localmente
✅ README foi atualizado (não é o padrão)
✅ Classe POO faz sentido no contexto
✅ Tratam erros de forma adequada
✅ Interface funciona sem bugs visuais
✅ Prompts da IA são customizados
✅ Todos sabem explicar o código

### Red Flags (Sinais de Alerta)

⚠️ Apenas 1 ou 2 commits no Git
⚠️ Todos os commits de 1 pessoa só
⚠️ Código extremamente complexo para nível
⚠️ Membros não sabem explicar o código
⚠️ README não foi modificado
⚠️ Classe POO "forçada" sem propósito
⚠️ Código idêntico entre grupos
⚠️ Nenhum erro tratado

---

## 💡 Como Dar Feedback Construtivo

### Durante os Checkpoints

**Ao invés de:** "Isso está errado"
**Diga:** "Que tal tentar dessa forma? [sugestão]"

**Ao invés de:** "Vocês estão atrasados"
**Diga:** "Vejo que vocês estão em X, vamos ajustar o cronograma?"

**Ao invés de:** "Esse código é ruim"
**Diga:** "Aqui poderia ser melhorado fazendo [exemplo]"

### Na Apresentação Final

**Faça Perguntas que Revelam Compreensão:**
- "Por que escolheram usar essa estrutura de classe?"
- "Como vocês tratam quando a API não responde?"
- "Explique como funciona essa parte do código"
- "Se tivessem mais tempo, o que adicionariam?"

**Valorize:**
- Criatividade
- Esforço de aprendizado
- Colaboração
- Resolução de problemas

---

## 📊 Planilha de Avaliação Sugerida

```
Grupo: ____________________
Projeto: __________________
Data: ____________________

┌──────────────────────────────────────────┬────────┐
│ Critério                                 │ Nota   │
├──────────────────────────────────────────┼────────┤
│ 1. Funcionalidade e Integração          │ /3,5   │
│   - Integração Gemini                    │        │
│   - Rotas FastAPI                        │        │
│   - Templates Jinja2                     │        │
│   - Tratamento de erros                  │        │
├──────────────────────────────────────────┼────────┤
│ 2. Qualidade do Código                  │ /2,5   │
│   - POO                                  │        │
│   - Organização                          │        │
│   - Comentários                          │        │
├──────────────────────────────────────────┼────────┤
│ 3. Criatividade e Entretenimento        │ /2,0   │
│   - Originalidade                        │        │
│   - Qualidade da experiência             │        │
│   - Prompts e IA                         │        │
├──────────────────────────────────────────┼────────┤
│ 4. Interface e UX                        │ /1,5   │
│   - Design visual                        │        │
│   - Responsividade                       │        │
│   - Usabilidade                          │        │
├──────────────────────────────────────────┼────────┤
│ 5. Apresentação e Documentação          │ /0,5   │
│   - Apresentação oral                    │        │
│   - README                               │        │
├──────────────────────────────────────────┼────────┤
│ NOTA FINAL                               │ /10,0  │
└──────────────────────────────────────────┴────────┘

Observações:
_____________________________________________
_____________________________________________
_____________________________________________

Destaques Positivos:
_____________________________________________
_____________________________________________

Pontos de Melhoria:
_____________________________________________
_____________________________________________
```

---

## 🎓 Sugestões de Extensão (Opcional)

Se algum grupo terminar antes, sugira:

1. **Sistema de favoritos** - Salvar gerações preferidas
2. **Histórico persistente** - Usar SQLite
3. **Compartilhamento** - Link para resultado
4. **Dark mode** - Toggle tema
5. **Export PDF** - Salvar resultado
6. **Múltiplas variações** - Gerar 3 versões
7. **Refinar resposta** - "Tornar mais criativo", etc
8. **Voice input** - Gravar áudio
9. **Autenticação** - Sistema de login
10. **Deploy** - Colocar online (Vercel, Railway)

---

## 📚 Recursos para o Professor

### Para Tirar Dúvidas

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Gemini API Docs](https://ai.google.dev/docs)
- [Jinja2 Docs](https://jinja.palletsprojects.com/)
- [Tailwind Docs](https://tailwindcss.com/)

### Videos Tutoriais

- FastAPI Tutorial (YouTube)
- Prompt Engineering Basics
- Git/GitHub para Professores

---

## 🤝 Lidando com Situações Comuns

### "Não conseguimos fazer rodar"

1. Verificar se Python 3.11+ instalado
2. Confirmar que UV está instalado
3. Checar se `.env` está configurado
4. Testar em máquina do professor

### "A API não funciona"

1. Verificar API key válida
2. Checar limite gratuito da API
3. Testar com conta do professor
4. Ver logs de erro completos

### "Tivemos conflitos no grupo"

1. Ouvir todos os lados
2. Verificar commits no Git
3. Propor divisão clara de tarefas
4. Avaliar participação individual

### "Está muito difícil"

1. Identificar dificuldade específica
2. Revisar conceitos necessários
3. Sugerir recursos de apoio
4. Ajustar expectativas se necessário

---

## ✅ Checklist do Professor

### Antes de Começar
- [ ] Material disponibilizado aos alunos
- [ ] Grupos formados
- [ ] Cronograma comunicado
- [ ] Rubrica explicada

### Durante o Projeto
- [ ] Checkpoint 1 realizado (Dia 3)
- [ ] Checkpoint 2 realizado (Dia 7)
- [ ] Checkpoint 3 realizado (Dia 10)
- [ ] Dúvidas respondidas
- [ ] Grupos acompanhados

### No Dia da Apresentação
- [ ] Planilha de avaliação pronta
- [ ] Ordem das apresentações definida
- [ ] Tempo controlado (5-7 min)
- [ ] Perguntas preparadas
- [ ] Feedback anotado

### Após as Apresentações
- [ ] Notas calculadas
- [ ] Feedback individualizado
- [ ] Repositórios verificados
- [ ] Notas lançadas no sistema

---

## 📝 Feedback Final aos Alunos

Após a avaliação, forneça:

1. **Nota com justificativa**
2. **Pontos positivos** (pelo menos 3)
3. **Áreas de melhoria** (pelo menos 2)
4. **Sugestões de estudo** (tópicos para aprofundar)
5. **Comentário motivacional**

**Exemplo de Feedback:**

```
Nota: 8,5

Pontos Positivos:
✅ Excelente integração com Gemini
✅ Interface muito criativa
✅ Código bem organizado e comentado
✅ Apresentação clara e objetiva

Pontos de Melhoria:
🔄 POO poderia ser mais aprofundada
🔄 Alguns erros não foram tratados

Sugestões:
📚 Estudar mais sobre herança e polimorfismo
📚 Revisar try/except e tratamento de exceções

Comentário:
Parabéns pelo projeto! Vocês demonstraram
grande criatividade e trabalho em equipe.
Continue praticando POO que é fundamental!
```

---

**Bom trabalho, professor! 🎓**

*Este guia foi feito para facilitar sua vida e garantir uma avaliação justa e construtiva!*
