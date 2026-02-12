import os
from supabase import create_client, Client

# Configuração via Secrets do GitHub
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Variáveis SUPABASE_URL ou SUPABASE_KEY não configuradas.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def popular_banco():
    leitos_raw = [
        # --- SETOR D (2° ANDAR) ---
        {"s": "SETOR D (2° ANDAR)", "h": "ENFERMARIA", "n": "ENF 202-A", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "ENFERMARIA", "n": "ENF 202-B", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "ENFERMARIA", "n": "ENF 204-A", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "ENFERMARIA", "n": "ENF 204-B", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "ENFERMARIA", "n": "ENF 205-A", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "ENFERMARIA", "n": "ENF 205-B", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "ENFERMARIA", "n": "ENF 207-A", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "ENFERMARIA", "n": "ENF 207-B", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "APARTAMENTO", "n": "APT 209", "t": "ENF"},
        {"s": "SETOR D (2° ANDAR)", "h": "APARTAMENTO", "n": "APT 210", "t": "ENF"},

        # --- SETOR A (3° ANDAR) ---
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 301", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 302", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 303", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 304", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 305", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 306", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 307", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "ISOL 308", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 309", "t": "ENF"},
        # Mudança para ENFERMARIA (Gera o título no front)
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 310-A", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 310-B", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 311-A", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 311-B", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 312-A", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 312-B", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 313-A", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 313-B", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 314-A", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 314-B", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 315-A", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 315-B", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 316-A", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 316-B", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 317-A", "t": "ENF"},
        {"s": "SETOR A (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 317-B", "t": "ENF"},
        # Volta para APARTAMENTO
        {"s": "SETOR A (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 318", "t": "ENF"},

        # --- SETOR B (3° ANDAR) ---
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 319-A", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 319-B", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 320-A", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 320-B", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 321-A", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 321-B", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 322-A", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 322-B", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 323-A", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 323-B", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 324-A", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 324-B", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 325-A", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 325-B", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 326-A", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "ENFERMARIA", "n": "ENF 326-B", "t": "ENF"},
        # Mudança para APARTAMENTO (Gera o título no front)
        {"s": "SETOR B (3° ANDAR)", "h": "APARTAMENTO", "n": "ISOL 327", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "APARTAMENTO", "n": "APT 328", "t": "ENF"},
        {"s": "SETOR B (3° ANDAR)", "h": "APARTAMENTO", "n": "ISOL 329", "t": "ENF"},

        # --- SETOR C (3° ANDAR) ---
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 330-A", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 330-B", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 331-A", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 331-B", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 332-A", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 332-B", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 333-A", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 333-B", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 334-A", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 334-B", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 335-A", "t": "ENF"},
        {"s": "SETOR C (3° ANDAR) - CIRÚRGICO", "h": "ENFERMARIA", "n": "ENF 335-B", "t": "ENF"},

        # --- UTI GERAL (4° ANDAR) ---
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 01", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 02", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 03", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 04", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 05", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 06", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 07", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 08", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 27", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 28", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 1", "n": "BOX 29", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 09", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 10", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 11", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 12", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 13", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 14", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 15", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 16", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 17", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 18", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 19", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "ISOL 20", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "ISOL 21", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 22", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 23", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 24", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 25", "t": "UTI"},
        {"s": "UTI GERAL (4° ANDAR)", "h": "POSTO 2", "n": "BOX 26", "t": "UTI"},
    ]

    leitos_final = []
    for item in leitos_raw:
        leitos_final.append({
            "setor": item['s'],
            "sub_header": item['h'],
            "identificador": item['n'],
            "tipo": item['t'],
            "status": "LIVRE" if item['t'] == "UTI" else "FORRADO"
        })

    try:
        # Deleta tudo para evitar duplicidade e garantir a nova ordem
        supabase.table("movimentacao_leitos").delete().neq("identificador", "RESET_FIX").execute()
        supabase.table("movimentacao_leitos").insert(leitos_final).execute()
        print(f"✅ Sucesso: {len(leitos_final)} leitos mapeados estrategicamente.")
    except Exception as e:
        print(f"❌ Erro no seed: {e}")

if __name__ == "__main__":
    popular_banco()