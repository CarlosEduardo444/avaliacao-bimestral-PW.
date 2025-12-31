"""
main.py - Aplicação FastAPI principal
Agora configurada para gerar POEMAS
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

from gemini_service import GeminiService
from models import Interacao, HistoricoInteracoes


# 🚀 Cria a aplicação FastAPI
app = FastAPI(
    title="Projeto IA Entretenimento",
    description="Aplicação de IA para entretenimento desenvolvida por [SEU GRUPO]",
    version="1.0.0"
)

# 📁 Arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# 🎨 Templates
templates = Jinja2Templates(directory="templates")

# 🤖 Serviço Gemini
gemini = GeminiService()

# 📝 Histórico
historico = HistoricoInteracoes(limite=50)


# 🏠 Página inicial
@app.get("/", response_class=HTMLResponse)
async def pagina_inicial(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "titulo": "Gerador de Poemas com IA",
            "descricao": "Transforme ideias em poesia com Inteligência Artificial ✨"
        }
    )


# 🎯 Processar input → GERAR POEMA
@app.post("/processar", response_class=HTMLResponse)
async def processar_input(
    request: Request,
    user_input: Annotated[str, Form()],
    temperatura: Annotated[float, Form()] = 0.9
):
    try:
        if not user_input or len(user_input.strip()) < 3:
            return templates.TemplateResponse(
                "resultado.html",
                {
                    "request": request,
                    "erro": "❌ Digite um tema com pelo menos 3 caracteres.",
                    "user_input": user_input
                }
            )

        # 📝 PROMPT PARA POEMA
        prompt = f"""
Você é um poeta criativo e sensível.

Crie um poema original em português do Brasil.

TEMA: {user_input}

Regras do poema:
- Linguagem poética
- Emoção e imagens fortes
- Ritmo agradável
- Entre 12 e 20 versos
- Pode usar rimas (não obrigatório)

Escreva apenas o poema:
"""

        resposta_ia = gemini.gerar_conteudo(
            prompt=prompt,
            temperatura=temperatura
        )

        interacao = Interacao(
            usuario_input=user_input,
            ia_resposta=resposta_ia,
            categoria="poema"
        )
        historico.adicionar(interacao)

        return templates.TemplateResponse(
            "resultado.html",
            {
                "request": request,
                "user_input": user_input,
                "resultado": resposta_ia,
                "temperatura": temperatura,
                "total_interacoes": historico.total()
            }
        )

    except Exception as e:
        return templates.TemplateResponse(
            "resultado.html",
            {
                "request": request,
                "erro": f"Ops! Algo deu errado: {str(e)}",
                "user_input": user_input
            }
        )


# 📜 Histórico
@app.get("/historico", response_class=HTMLResponse)
async def ver_historico(request: Request):
    return templates.TemplateResponse(
        "historico.html",
        {
            "request": request,
            "interacoes": historico.obter_todas(),
            "total": historico.total()
        }
    )


# 🗑️ Limpar histórico
@app.post("/limpar-historico")
async def limpar_historico():
    historico.limpar()
    return {"mensagem": "Histórico limpo com sucesso!", "total": 0}


# 🏥 Health check
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "mensagem": "Aplicação rodando 🚀",
        "versao": "1.0.0",
        "total_interacoes": historico.total()
    }


# ▶️ Rodar com:
# python -m uvicorn main:app --reload
# http://localhost:8000