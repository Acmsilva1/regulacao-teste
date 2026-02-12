import os
from supabase import create_client, Client

# Configuração via Secrets (GitHub)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Variáveis SUPABASE_URL ou SUPABASE_KEY não configuradas.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def popular_banco():
    # O mapa completo conforme seu original
    leitos_mapa = [
        # SETOR D (2° ANDAR)
        {"setor": "SETOR D (2° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 202-A", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR D (2° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 202-B", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR D (2° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 204-A", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR D (2° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 204-B", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR D (2° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 205-A", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR D (2° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 205-B", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR D (2° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 207-A", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR D (2° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 207-B", "tipo": "ENF", "status": "FORRADO"},
        # SETOR A (3° ANDAR)
        {"setor": "SETOR A (3° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 302-A", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR A (3° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 302-B", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR A (3° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 304-A", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR A (3° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 304-B", "tipo": "ENF", "status": "FORRADO"},
        # SETOR B (3° ANDAR)
        {"setor": "SETOR B (3° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 314-A", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR B (3° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 314-B", "tipo": "ENF", "status": "FORRADO"},
        # SETOR C (4° ANDAR)
        {"setor": "SETOR C (4° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 402-A", "tipo": "ENF", "status": "FORRADO"},
        {"setor": "SETOR C (4° ANDAR)", "sub_header": "ENFERMARIA", "identificador": "ENF 402-B", "tipo": "ENF", "status": "FORRADO"},
        # UTI GERAL (4° ANDAR)
        {"setor": "UTI GERAL (4° ANDAR)", "sub_header": "POSTO 1", "identificador": "BOX 01", "tipo": "UTI", "status": "LIVRE"},
        {"setor": "UTI GERAL (4° ANDAR)", "sub_header": "POSTO 1", "identificador": "BOX 02", "tipo": "UTI", "status": "LIVRE"},
        {"setor": "UTI GERAL (4° ANDAR)", "sub_header": "POSTO 1", "identificador": "BOX 03", "tipo": "UTI", "status": "LIVRE"},
        {"setor": "UTI GERAL (4° ANDAR)", "sub_header": "POSTO 1", "identificador": "ISOL 04", "tipo": "UTI", "status": "LIVRE"},
        {"setor": "UTI GERAL (4° ANDAR)", "sub_header": "POSTO 1", "identificador": "ISOL 05", "tipo": "UTI", "status": "LIVRE"},
        {"setor": "UTI GERAL (4° ANDAR)", "sub_header": "POSTO 2", "identificador": "BOX 18", "tipo": "UTI", "status": "LIVRE"},
        {"setor": "UTI GERAL (4° ANDAR)", "sub_header": "POSTO 2", "identificador": "ISOL 20", "tipo": "UTI", "status": "LIVRE"},
        {"setor": "UTI GERAL (4° ANDAR)", "sub_header": "POSTO 2", "identificador": "BOX 26", "tipo": "UTI", "status": "LIVRE"},
    ]

    try:
        print("🛠️  Limpando regulação anterior...")
        # Deleta tudo para evitar duplicidade no teste
        supabase.table("movimentacao_leitos").delete().neq("identificador", "RESET").execute()
        
        print(f"📡 Injetando {len(leitos_mapa)} leitos no Supabase...")
        supabase.table("movimentacao_leitos").insert(leitos_mapa).execute()
        
        print("✅ Censo Vivo populado com sucesso!")
    except Exception as e:
        print(f"❌ Erro estratégico: {e}")

if __name__ == "__main__":
    popular_banco()
