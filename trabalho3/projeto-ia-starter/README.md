# 🤖 Projeto IA - Código Starter

> Template completo para criar aplicações de IA para entretenimento com Python, FastAPI e Google Gemini!

## 📋 Sobre Este Projeto

Este é um **código starter** (base inicial) para o microprojeto de IA da disciplina de Programação Web. Ele já vem com toda a estrutura pronta para você começar a desenvolver sua aplicação de IA!

### ✨ O que já está pronto?

- ✅ Aplicação FastAPI funcionando
- ✅ Integração com Google Gemini AI
- ✅ Templates Jinja2 responsivos
- ✅ Design com Tailwind CSS
- ✅ Sistema de histórico
- ✅ Validações de formulário
- ✅ Tratamento de erros
- ✅ Código comentado e documentado

### 🎯 O que você precisa fazer?

1. **Personalizar** a aplicação para sua ideia específica
2. **Adicionar** funcionalidades únicas do seu projeto
3. **Customizar** prompts da IA para seu caso de uso
4. **Melhorar** a interface e experiência do usuário
5. **Testar** e garantir que tudo funciona perfeitamente

---

## 🛠️ Stack Tecnológica

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Python** | 3.11+ | Linguagem de programação |
| **FastAPI** | 0.104+ | Framework web moderno |
| **Jinja2** | 3.1+ | Motor de templates |
| **Requests** | 2.31+ | Cliente HTTP |
| **UV** | 0.1+ | Gerenciador de dependências |
| **Uvicorn** | 0.24+ | Servidor ASGI |
| **Tailwind CSS** | 3.3+ | Framework CSS (via CDN) |
| **Gemini API** | 1.5 Flash | Modelo de IA do Google |

---

## 🚀 Como Instalar e Rodar

### 📦 Pré-requisitos

- Python 3.11 ou superior instalado
- UV instalado ([instruções aqui](https://github.com/astral-sh/uv))
- Conta no Google AI Studio ([criar aqui](https://makersuite.google.com/app/apikey))

### 1️⃣ Clone ou Baixe o Projeto

```bash
# Se estiver usando Git
git clone <url-do-repositorio>
cd projeto-ia-starter

# Ou simplesmente extraia o ZIP baixado
```

### 2️⃣ Configure a API Key do Gemini

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua API key
# GEMINI_API_KEY=sua_api_key_aqui
```

**⚠️ IMPORTANTE:** 
- Consiga sua API key em: https://makersuite.google.com/app/apikey
- NUNCA compartilhe sua API key ou commite o arquivo `.env` no Git!

### 3️⃣ Instale as Dependências

```bash
# UV vai instalar tudo automaticamente
uv sync
```

### 4️⃣ Rode a Aplicação

```bash
# Inicia o servidor em modo desenvolvimento
uv run uvicorn main:app --reload
```

### 5️⃣ Acesse no Navegador

Abra seu navegador e vá para:
```
http://localhost:8000
```

🎉 **Pronto!** Sua aplicação está rodando!

---

## 📁 Estrutura do Projeto

```
projeto-ia-starter/
│
├── main.py                 # ❤️ Aplicação FastAPI principal
├── models.py               # 🎯 Classes POO (Interacao, Historico)
├── gemini_service.py       # 🤖 Serviço de integração com Gemini
│
├── templates/              # 🎨 Templates HTML (Jinja2)
│   ├── base.html          # Template base
│   ├── index.html         # Página inicial
│   ├── resultado.html     # Página de resultado
│   └── historico.html     # Página de histórico
│
├── static/                 # 📦 Arquivos estáticos
│   ├── style.css          # CSS customizado
│   └── script.js          # JavaScript
│
├── pyproject.toml         # 📋 Dependências (UV)
├── .env.example           # 🔑 Exemplo de variáveis de ambiente
├── .env                   # 🔒 Suas variáveis (NÃO COMMITAR!)
├── .gitignore            # 🙈 Arquivos ignorados pelo Git
└── README.md             # 📖 Este arquivo!
```

---

## 🎨 Personalizando Seu Projeto

### 1. Mudar o Nome e Descrição

Edite `main.py`:

```python
app = FastAPI(
    title="SEU TÍTULO AQUI",
    description="SUA DESCRIÇÃO AQUI",
    version="1.0.0"
)
```

### 2. Customizar Prompts da IA

Edite a função `processar_input()` em `main.py`:

```python
prompt = f"""
Você é um [SEU PERSONAGEM AQUI]!

Tarefa: {user_input}

[SUAS INSTRUÇÕES ESPECÍFICAS AQUI]
"""
```

**Exemplos de Prompts:**

Para **Gerador de Personagens RPG:**
```python
prompt = f"""
Você é um mestre de RPG experiente.

Crie um personagem completo com:
- Nome épico
- Raça: {raca}
- Classe: {classe}
- Atributos (FOR, DES, CON, INT, SAB, CAR)
- História de background (2 parágrafos)
- 3 habilidades especiais

Use criatividade!
"""
```

Para **Gerador de Histórias:**
```python
prompt = f"""
Você é um escritor criativo premiado.

Escreva uma história curta de {genero} sobre: {tema}

Palavras-chave obrigatórias: {palavras_chave}

A história deve ter:
- Início interessante
- Desenvolvimento
- Clímax
- Conclusão surpreendente

Limite: 200-300 palavras
"""
```

### 3. Adicionar Novas Rotas

Adicione em `main.py`:

```python
@app.post("/sua-nova-rota", response_class=HTMLResponse)
async def sua_funcao(request: Request, parametro: Annotated[str, Form()]):
    # Sua lógica aqui
    return templates.TemplateResponse("seu_template.html", {...})
```

### 4. Criar Novas Classes POO

Adicione em `models.py`:

```python
class Personagem:
    def __init__(self, nome: str, classe: str, nivel: int = 1):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.experiencia = 0
    
    def ganhar_experiencia(self, xp: int):
        self.experiencia += xp
        if self.experiencia >= 100 * self.nivel:
            self.subir_nivel()
    
    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
```

### 5. Customizar Visual (CSS)

Edite `static/style.css` para mudar cores, fontes, animações, etc.

Para mudar as cores principais, edite as variáveis:

```css
:root {
    --color-primary: #6366f1;    /* Cor primária */
    --color-secondary: #8b5cf6;  /* Cor secundária */
    --color-accent: #ec4899;     /* Cor de destaque */
}
```

---

## 🧪 Testando Sua Aplicação

### Teste Local

1. **Teste a página inicial:** http://localhost:8000
2. **Teste o formulário:** Digite algo e clique em "Gerar"
3. **Teste o histórico:** http://localhost:8000/historico
4. **Teste a API:** http://localhost:8000/health

### Teste em Diferentes Navegadores

- ✅ Chrome
- ✅ Firefox
- ✅ Safari
- ✅ Edge

### Teste Responsividade

Redimensione a janela do navegador ou use:
- **Chrome DevTools:** F12 → Toggle Device Toolbar

---

## 🐛 Problemas Comuns e Soluções

### ❌ "ModuleNotFoundError: No module named 'fastapi'"

**Solução:** Instale as dependências
```bash
uv sync
```

### ❌ "GEMINI_API_KEY não configurada"

**Solução:** 
1. Copie `.env.example` para `.env`
2. Adicione sua API key no arquivo `.env`

### ❌ "Address already in use"

**Solução:** Porta 8000 já está em uso. Use outra porta:
```bash
uv run uvicorn main:app --reload --port 8001
```

### ❌ "API key inválida"

**Solução:**
1. Verifique se copiou a API key corretamente
2. Crie uma nova em: https://makersuite.google.com/app/apikey

### ❌ Templates não carregam

**Solução:** Verifique se a pasta `templates/` existe e tem os arquivos HTML

---

## 📚 Recursos Úteis

### Documentação Oficial

- [FastAPI](https://fastapi.tiangolo.com/) - Framework web
- [Jinja2](https://jinja.palletsprojects.com/) - Templates
- [Gemini API](https://ai.google.dev/docs) - API de IA
- [Tailwind CSS](https://tailwindcss.com/docs) - Framework CSS
- [UV](https://github.com/astral-sh/uv) - Gerenciador Python

### Tutoriais Recomendados

- FastAPI + Jinja2 Templates
- Como usar Gemini API
- Tailwind CSS para iniciantes
- Programação Orientada a Objetos em Python

---

## 🎓 Próximos Passos

1. ✅ **Instale e rode o projeto** → Certifique-se que funciona
2. 🎨 **Customize a interface** → Deixe com a cara do seu projeto
3. 🤖 **Ajuste os prompts** → Faça a IA responder do jeito que você quer
4. ➕ **Adicione features** → Histórico de favoritos? Dark mode? Compartilhar?
5. 🧪 **Teste muito!** → Teste em diferentes situações
6. 📖 **Documente** → Atualize este README com suas mudanças
7. 🎤 **Prepare a apresentação** → Demo + explicação técnica

---

## 👥 Seu Grupo

**Integrantes:**
1. [Nome do Integrante 1]
2. [Nome do Integrante 2]
3. [Nome do Integrante 3]
4. [Nome do Integrante 4]
5. [Nome do Integrante 5]

**Nome do Projeto:** [Seu Nome Criativo Aqui]

**Descrição:** [Breve descrição do que seu projeto faz]

---

## 📝 Checklist de Entrega

Antes de entregar, verifique:

- [ ] Aplicação roda sem erros
- [ ] Integração com Gemini funciona
- [ ] Todas as rotas estão funcionando
- [ ] Design está responsivo (mobile + desktop)
- [ ] Código está comentado
- [ ] README atualizado com info do grupo
- [ ] `.env` NÃO está no repositório
- [ ] Screenshots ou GIF da aplicação
- [ ] Apresentação preparada (5-7 minutos)

---

## 🆘 Precisa de Ajuda?

- **Dúvidas técnicas:** Consulte a documentação oficial
- **Problemas com código:** Revise os comentários nos arquivos
- **Erro desconhecido:** Leia a mensagem de erro com atenção
- **API não funciona:** Verifique sua API key e limite de uso

---

## 📄 Licença

Este projeto é de código livre para fins educacionais.

---

## 🎉 Boa Sorte!

Lembre-se: **O objetivo é aprender e se divertir!** 🚀

Não tenha medo de experimentar, quebrar coisas e consertar. É assim que se aprende programação de verdade!

**Dica Final:** A melhor aplicação é aquela que FAZ AS PESSOAS SORRIREM! 😊

---

**Desenvolvido com ❤️ para a disciplina de Programação Web**

*2º Ano - Técnico em Informática*
