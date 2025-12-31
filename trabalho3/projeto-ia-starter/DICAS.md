# 💡 Dicas Práticas para o Projeto

## 🎯 Dicas de Produtividade

### 1. Organização do Grupo

#### Divisão de Tarefas Sugerida:

**Pessoa 1 - Backend Master** 🐍
- Foco: Python, FastAPI, integração Gemini
- Responsável por: Rotas, lógica de negócio, API
- Habilidades: Python, POO, APIs

**Pessoa 2 - Frontend Master** 🎨
- Foco: HTML, CSS, JavaScript, Tailwind
- Responsável por: Templates, estilos, responsividade
- Habilidades: Design, UX/UI, CSS

**Pessoa 3 - IA Engineer** 🤖
- Foco: Prompts, Gemini API, qualidade das respostas
- Responsável por: Otimizar prompts, testar IA
- Habilidades: Prompt engineering, criatividade

**Pessoa 4 - QA/Tester** 🧪
- Foco: Testes, validações, bugs
- Responsável por: Garantir qualidade, testar edge cases
- Habilidades: Atenção aos detalhes, testes

**Pessoa 5 - DevOps/Documentação** 📚
- Foco: Git, README, apresentação
- Responsável por: Repositório, docs, demo
- Habilidades: Comunicação, organização

**⚠️ Importante:** Todos devem entender TODO o código!

---

## 🚀 Git & GitHub - Guia Rápido

### Fluxo de Trabalho Recomendado

```bash
# 1. Clone o repositório
git clone <url-do-repo>
cd projeto-ia

# 2. Crie uma branch para sua feature
git checkout -b feature/minha-funcionalidade

# 3. Faça suas mudanças e commit
git add .
git commit -m "feat: adiciona gerador de personagens"

# 4. Push para o GitHub
git push origin feature/minha-funcionalidade

# 5. Crie Pull Request no GitHub
# (Outra pessoa do grupo revisa antes de dar merge)
```

### Boas Práticas de Commit

✅ **BOM:**
```
feat: adiciona validação de formulário
fix: corrige erro na API do Gemini
docs: atualiza README com instruções
style: melhora layout da página inicial
```

❌ **RUIM:**
```
mudanças
fixes
atualizei
teste
```

### Resolução de Conflitos

Se der conflito no merge:
```bash
# 1. Atualize sua branch com a main
git pull origin main

# 2. Resolva conflitos manualmente nos arquivos
# (Git marca os conflitos com <<< === >>>)

# 3. Commit das resoluções
git add .
git commit -m "resolve: conflitos de merge"
```

---

## 🤖 Prompt Engineering - Como Fazer a IA te Obedecer

### Estrutura de Prompt Eficaz

```python
prompt = f"""
[1. CONTEXTO - Quem a IA deve ser]
Você é um [PERSONAGEM/ESPECIALISTA]

[2. TAREFA - O que fazer]
Sua tarefa é [AÇÃO ESPECÍFICA]

[3. RESTRIÇÕES - Regras a seguir]
- Restrição 1
- Restrição 2
- Restrição 3

[4. FORMATO - Como responder]
Formate sua resposta como:
[ESTRUTURA ESPERADA]

[5. EXEMPLOS - Mostre o que quer]
Exemplo de saída:
[EXEMPLO CONCRETO]

[6. INPUT - Dados do usuário]
Input do usuário: {user_input}
"""
```

### Exemplos Práticos

#### Para Gerador de Histórias:
```python
prompt = f"""
Você é um escritor best-seller de ficção científica.

Escreva uma história curta e envolvente baseada neste tema: "{tema}"

Regras:
- Máximo 300 palavras
- Deve ter início, meio e fim
- Inclua um plot twist
- Use linguagem acessível

Estrutura:
1. Introdução (2 parágrafos)
2. Desenvolvimento (2-3 parágrafos)
3. Clímax e conclusão (1 parágrafo)

Tema fornecido pelo usuário: {user_input}
"""
```

#### Para Quiz Generator:
```python
prompt = f"""
Você é um professor criativo e especialista em {assunto}.

Crie 5 perguntas de múltipla escolha sobre: {user_input}

Cada pergunta deve ter:
- Enunciado claro e interessante
- 4 alternativas (A, B, C, D)
- Apenas 1 resposta correta
- Explicação da resposta correta

Dificuldade: {nivel}

Formato de saída (JSON):
{{
  "perguntas": [
    {{
      "pergunta": "...",
      "alternativas": ["A) ...", "B) ...", "C) ...", "D) ..."],
      "resposta_correta": "A",
      "explicacao": "..."
    }}
  ]
}}
"""
```

### Controlando a Temperatura

- **0.0 - 0.3:** Respostas muito focadas, previsíveis (bom para tarefas técnicas)
- **0.4 - 0.7:** Equilíbrio entre criatividade e foco (uso geral)
- **0.8 - 1.0:** Muito criativo, variado (histórias, arte, poesia)

---

## 🎨 Dicas de Design (Tailwind CSS)

### Paleta de Cores Harmoniosa

```html
<!-- Gradientes modernos -->
<div class="bg-gradient-to-r from-purple-600 via-pink-500 to-red-500"></div>
<div class="bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500"></div>

<!-- Cores para diferentes estados -->
<button class="bg-green-500 hover:bg-green-600">Sucesso</button>
<button class="bg-red-500 hover:bg-red-600">Erro</button>
<button class="bg-blue-500 hover:bg-blue-600">Info</button>
```

### Sombras e Profundidade

```html
<!-- Níveis de sombra -->
<div class="shadow-sm">Leve</div>
<div class="shadow-md">Média</div>
<div class="shadow-lg">Grande</div>
<div class="shadow-2xl">Enorme</div>

<!-- Sombra colorida -->
<div class="shadow-lg shadow-purple-500/50">Com cor!</div>
```

### Animações Simples

```html
<!-- Hover effects -->
<div class="transform hover:scale-105 transition-all duration-300">
    Cresce ao passar o mouse
</div>

<div class="hover:rotate-2 transition-transform">
    Rotaciona levemente
</div>

<!-- Loading spinner -->
<div class="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>

<!-- Pulse animation -->
<div class="animate-pulse bg-indigo-100 h-4 w-full rounded"></div>
```

### Responsividade Fácil

```html
<!-- Mobile first! -->
<div class="text-sm md:text-base lg:text-lg">
    Texto cresce em telas maiores
</div>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    <!-- 1 coluna mobile, 2 tablet, 3 desktop -->
</div>

<!-- Esconder/mostrar por tamanho -->
<div class="hidden md:block">
    Visível apenas em tablet+
</div>
```

---

## 🐛 Debug: Como Resolver Problemas

### Técnicas de Debug

#### 1. Console.log é seu amigo!

```javascript
// Frontend (JavaScript)
console.log('Valor da variável:', minhaVariavel);
console.table(meuObjeto); // Mostra objeto formatado
console.error('Erro aqui!'); // Mostra em vermelho
```

```python
# Backend (Python)
print(f"Valor: {variavel}")
print(f"Tipo: {type(variavel)}")
import json
print(json.dumps(objeto, indent=2))  # JSON formatado
```

#### 2. Use o Debugger do Browser

- Aperte **F12** no navegador
- Vá na aba **Console** para ver erros
- Aba **Network** mostra requisições HTTP
- Aba **Elements** para inspecionar HTML/CSS

#### 3. Verifique Status Codes HTTP

- **200:** ✅ Sucesso
- **400:** ❌ Erro no cliente (dados inválidos)
- **404:** ❌ Rota não encontrada
- **500:** ❌ Erro no servidor (bug no código)

#### 4. Teste APIs Isoladamente

Use o **Thunder Client** (VS Code) ou **Postman** para testar suas rotas sem frontend.

### Erros Comuns e Soluções

#### ❌ "CORS Error"
**Solução:**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
```

#### ❌ "Template not found"
**Solução:** Verifique se:
- Pasta `templates/` existe
- Arquivo tem extensão `.html`
- Nome está correto (case-sensitive!)

#### ❌ "Rate limit exceeded" (Gemini)
**Solução:**
- Você excedeu o limite gratuito da API
- Espere alguns minutos
- Crie nova API key se necessário

---

## 🎯 Features Extras para Impressionar

### Fáceis de Implementar

1. **Dark Mode** 🌙
   - Toggle entre claro/escuro
   - Salvar preferência no localStorage

2. **Histórico de Favoritos** ⭐
   - Marcar gerações favoritas
   - Filtrar favoritos

3. **Compartilhar Resultado** 📤
   - Botão de compartilhar para redes sociais
   - Copiar link

4. **Export/Download** 💾
   - Baixar resultado como TXT
   - Salvar como PDF

### Médias

5. **Modo Criativo vs Focado** 🎚️
   - Presets de temperatura
   - Explicar diferença pro usuário

6. **Múltiplas Variações** 🔄
   - Gerar 3 versões diferentes
   - Usuário escolhe a melhor

7. **Estatísticas** 📊
   - Total de gerações
   - Média de caracteres
   - Gráficos simples

### Avançadas (Desafio!)

8. **Sistema de Usuários** 👤
   - Login/registro simples
   - Histórico por usuário

9. **Refinar Resultado** 🔧
   - "Tornar mais criativo"
   - "Encurtar"
   - "Adicionar mais detalhes"

10. **Voice Input** 🎤
    - Gravar áudio
    - Converter para texto
    - Enviar para IA

---

## ⚡ Performance: Deixe Rápido!

### Frontend

```javascript
// Debounce para evitar muitos requests
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func(...args), wait);
    };
}

// Uso:
input.addEventListener('input', debounce(function() {
    // Sua função aqui
}, 500));
```

### Backend

```python
# Use async quando possível
@app.post("/processar")
async def processar_input(...):
    # async/await para I/O
    resposta = await gemini.gerar_conteudo_async(prompt)
```

### Otimizações Gerais

- ✅ Minimize chamadas à API
- ✅ Cache respostas comuns
- ✅ Comprima imagens
- ✅ Use CDN para Tailwind
- ✅ Lazy load de conteúdo

---

## 🎤 Apresentação - Dicas

### Estrutura Sugerida (5-7 min)

**1. Introdução (30s)**
- Nome do projeto
- Integrantes
- Problema que resolve

**2. Demo ao Vivo (2min)**
- Mostre funcionando!
- Prepare exemplo interessante
- Tenha backup (vídeo) se der problema

**3. Tecnologias (1min)**
- Stack usado
- Por que essas escolhas

**4. Código Interessante (2min)**
- Mostre algo legal que fizeram
- Explique uma funcionalidade complexa
- POO, integração API, etc

**5. Desafios e Aprendizados (1min)**
- O que foi difícil
- Como resolveram
- O que aprenderam

**6. Perguntas (1min)**
- Estejam preparados!

### Dicas de Apresentação

✅ **Faça:**
- Ensaie antes!
- Teste tudo funcionando
- Prepare slides simples
- Fale devagar e claro
- Mostre entusiasmo

❌ **Não Faça:**
- Ler slides
- Desculpas ("não deu tempo...")
- Culpar outros do grupo
- Ficar sem testar antes

---

## 📚 Recursos Extras

### Canais YouTube Recomendados

- **Python:** Corey Schafer, Real Python
- **FastAPI:** ArjanCodes, Patrick Loeber
- **Web Dev:** Traversy Media, Fireship
- **Tailwind:** Tailwind Labs (oficial)

### Ferramentas Úteis

- **Design:** Figma (mockups)
- **Ícones:** Heroicons, Lucide
- **Fontes:** Google Fonts
- **Cores:** Coolors.co
- **APIs Test:** Thunder Client, Postman
- **Git GUI:** GitHub Desktop, GitKraken

---

## 🎓 Checklist Final

### Antes de Entregar

- [ ] Código funciona 100%
- [ ] Sem erros no console
- [ ] README atualizado
- [ ] Screenshots/GIF adicionado
- [ ] Tudo commitado no Git
- [ ] `.env` não está no repo
- [ ] Código comentado
- [ ] Apresentação pronta
- [ ] Demo testada
- [ ] Todos sabem explicar código

### No Dia da Apresentação

- [ ] Chegar cedo
- [ ] Testar tudo de novo
- [ ] Ter backup (vídeo, prints)
- [ ] Água para apresentadores
- [ ] Todos participam

---

## 💪 Mensagem Final

**Lembre-se:**

> "Não é sobre código perfeito, é sobre aprender, colaborar e criar algo legal!"

Não se estressem muito! O importante é:
1. Funcionar ✅
2. Vocês entenderem o código 🧠
3. Se divertir no processo 🎉

**BOA SORTE! VOCÊS CONSEGUEM! 🚀**

---

**Dúvida? Problema? Trave no código?**

1. Google o erro (sério, isso funciona!)
2. Pergunte pro ChatGPT/Claude
3. Consulte documentação oficial
4. Peça ajuda pro professor
5. Ajude seus colegas de grupo

*"O melhor debugger é ter outra pessoa olhando seu código!"*
