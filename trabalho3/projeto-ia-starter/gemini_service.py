"""
gemini_service.py - Serviço para integração com API do Google Gemini

Este arquivo é responsável por toda a comunicação com a IA do Google.
É como um "tradutor" entre sua aplicação e a API.

Analogia: Imagine que a API Gemini é uma pessoa que só fala inglês técnico.
         Este serviço é seu intérprete que traduz seus pedidos e as respostas!
"""

import os
import requests
from typing import Optional
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()


class GeminiService:
    """
    Serviço para comunicação com API do Google Gemini.
    
    Essa classe encapsula toda a complexidade de fazer chamadas HTTP
    para a API, tratar erros e processar respostas.
    """
    
    def __init__(self):
        """
        Inicializa o serviço com configurações da API.
        """
        # Pega a API key do arquivo .env
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        # Valida se a API key existe
        if not self.api_key or self.api_key == "sua_api_key_aqui":
            raise ValueError(
                "❌ API key do Gemini não configurada! "
                "Copie .env.example para .env e adicione sua API key."
            )
        
        # URL base da API Gemini
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
        
        # Modelo a ser usado (gemini-1.5-flash é rápido e barato!)
        self.model = "gemini-2.5-flash"




        
        # Timeout para requisições (30 segundos)
        self.timeout = 30
    
    def gerar_conteudo(
        self, 
        prompt: str, 
        temperatura: float = 0.9,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Gera conteúdo usando o modelo Gemini.
        
        Analogia: É como fazer uma pergunta para um amigo muito inteligente
                 e criativo, e ele te responder!
        
        Args:
            prompt: O texto/pergunta que você quer enviar para IA
            temperatura: Controla criatividade (0.0-1.0)
                        - 0.0 = Respostas mais previsíveis e focadas
                        - 1.0 = Respostas mais criativas e variadas
            max_tokens: Limite de tokens na resposta (None = sem limite)
        
        Returns:
            Texto gerado pela IA
            
        Raises:
            Exception: Se algo der errado na comunicação com API
        """
        
        # URL completa da API
        url = f"{self.base_url}/{self.model}:generateContent"
        
        # Parâmetros da requisição
        params = {"key": self.api_key}
        
        # Corpo da requisição (payload)
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": temperatura,
                "topK": 40,
                "topP": 0.95,
            }
        }
        
        # Adiciona limite de tokens se especificado
        if max_tokens:
            payload["generationConfig"]["maxOutputTokens"] = max_tokens
        
        # Headers da requisição
        headers = {"Content-Type": "application/json"}
        
        try:
            # 🚀 Faz a requisição POST para API
            response = requests.post(
                url,
                params=params,
                json=payload,
                headers=headers,
                timeout=self.timeout
            )
            
            # Verifica se deu erro HTTP (404, 500, etc)
            response.raise_for_status()
            
            # Converte resposta JSON em dicionário Python
            data = response.json()
            
            # Extrai o texto da resposta
            # (A estrutura é meio complexa, mas sempre segue esse padrão)
            texto_gerado = data["candidates"][0]["content"]["parts"][0]["text"]
            
            return texto_gerado
            
        except requests.exceptions.Timeout:
            raise Exception(
                "⏱️ A API demorou muito para responder (timeout). "
                "Tente novamente!"
            )
            
        except requests.exceptions.ConnectionError:
            raise Exception(
                "🌐 Erro de conexão com a API. "
                "Verifique sua internet!"
            )
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                raise Exception(
                    "🚫 Você excedeu o limite de requisições da API. "
                    "Aguarde alguns minutos!"
                )
            elif response.status_code == 401:
                raise Exception(
                    "🔑 API key inválida! "
                    "Verifique se copiou corretamente."
                )
            else:
                raise Exception(f"❌ Erro HTTP {response.status_code}: {str(e)}")
                
        except KeyError:
            raise Exception(
                "🤔 Resposta da API em formato inesperado. "
                "Pode ser que o modelo esteja indisponível."
            )
            
        except Exception as e:
            raise Exception(f"💥 Erro inesperado: {str(e)}")
    
    def gerar_com_contexto(
        self, 
        mensagens: list[dict],
        temperatura: float = 0.9
    ) -> str:
        """
        Gera conteúdo mantendo contexto de conversas anteriores.
        
        Útil para criar chatbots que "lembram" do que foi dito antes!
        
        Args:
            mensagens: Lista de mensagens no formato:
                      [
                          {"role": "user", "text": "Olá!"},
                          {"role": "model", "text": "Oi! Como posso ajudar?"},
                          {"role": "user", "text": "Me conte uma piada"}
                      ]
            temperatura: Controla criatividade (0.0-1.0)
        
        Returns:
            Resposta da IA considerando todo o contexto
        """
        
        url = f"{self.base_url}/{self.model}:generateContent"
        params = {"key": self.api_key}
        
        # Formata mensagens para o formato esperado pela API
        conteudo_formatado = []
        for msg in mensagens:
            conteudo_formatado.append({
                "role": msg["role"],
                "parts": [{"text": msg["text"]}]
            })
        
        payload = {
            "contents": conteudo_formatado,
            "generationConfig": {
                "temperature": temperatura,
                "topK": 40,
                "topP": 0.95,
            }
        }
        
        headers = {"Content-Type": "application/json"}
        
        try:
            response = requests.post(
                url,
                params=params,
                json=payload,
                headers=headers,
                timeout=self.timeout
            )
            
            response.raise_for_status()
            data = response.json()
            
            return data["candidates"][0]["content"]["parts"][0]["text"]
            
        except Exception as e:
            raise Exception(f"Erro ao gerar com contexto: {str(e)}")


# 💡 EXEMPLO DE USO:
#
# from gemini_service import GeminiService
#
# # Criar instância do serviço
# gemini = GeminiService()
#
# # Gerar conteúdo simples
# resposta = gemini.gerar_conteudo("Me conte uma piada de programação")
# print(resposta)
#
# # Gerar com contexto (chatbot)
# mensagens = [
#     {"role": "user", "text": "Olá, meu nome é João"},
#     {"role": "model", "text": "Olá João! Prazer em conhecê-lo!"},
#     {"role": "user", "text": "Qual é meu nome?"}
# ]
# resposta = gemini.gerar_com_contexto(mensagens)
# print(resposta)  # Deve responder "João"!
