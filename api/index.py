import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from pydantic import BaseModel
from typing import Optional

# Configuração de Ambiente
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise EnvironmentError("Variáveis SUPABASE_URL ou SUPABASE_KEY não encontradas.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI(title="Censo Hospitalar API - Supabase Edition")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para validação de dados
class AtualizacaoLeito(BaseModel):
    n: str  # Identificador do leito
    p: Optional[str] = None # Paciente
    a: Optional[str] = None # Atendimento
    sx: Optional[str] = None # Sexo
    o: Optional[str] = None # Origem
    s: Optional[str] = None # Status
    obs: Optional[str] = None # Observação

@app.get("/api/v1/censo")
async def listar_leitos():
    # Busca ordenada para manter a estrutura do hospital correta
    response = supabase.table("movimentacao_leitos").select("*").order("id").execute()
    return response.data

@app.post("/api/v1/atualizar")
async def atualizar_leito(dados: AtualizacaoLeito):
    field_map = {
        'p': 'paciente_nome', 'a': 'atendimento', 
        'sx': 'sexo', 'o': 'origem', 
        's': 'status', 'obs': 'observacao'
    }
    
    update_data = {field_map[k]: v for k, v in dados.dict().items() if v is not None and k != 'n'}
    
    result = supabase.table("movimentacao_leitos")\
        .update(update_data)\
        .eq("identificador", dados.n)\
        .execute()
    
    if not result.data:
        raise HTTPException(status_code=404, detail="Leito não encontrado")
    
    return {"status": "sucesso", "data": result.data}
