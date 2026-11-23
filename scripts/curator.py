#!/usr/bin/env python3
"""
curator.py - Orquestrador principal do Robô Curador Científico do LaBiOmicS.

Fluxo:
1. Carrega histórico de DOIs já publicados (data/history.json).
2. Consulta Europe PMC/PubMed por artigos recentes de alto impacto.
3. Filtra artigos duplicados.
4. Gera a síntese em português via IA (scripts/generate_post.py).
5. Salva o novo post em _posts/YYYY-MM-DD-slug.md.
6. Atualiza data/history.json.
"""

import os
import sys
import json
import re
import unicodedata
import argparse
from datetime import datetime
from pathlib import Path

from fetch_papers import fetch_recent_papers_europe_pmc
from generate_post import generate_post_with_gemini, format_jekyll_markdown

# Caminhos base
BASE_DIR = Path(__file__).resolve().parent.parent
HISTORY_FILE = BASE_DIR / "data" / "history.json"
POSTS_DIR = BASE_DIR / "_posts"


def slugify(text: str) -> str:
    """Converte um título em um slug de URL limpo e legível."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:60].rstrip("-")


def load_history() -> dict:
    """Carrega o histórico de DOIs já processados."""
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Aviso] Erro ao ler {HISTORY_FILE}: {e}")
    return {"processed_dois": [], "articles": []}


def save_history(history: dict) -> None:
    """Salva o histórico atualizado em disco."""
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def run_curator(limit: int = 5, dry_run: bool = False, days_back: int = 30) -> None:
    """Executa a rotina de curadoria diária."""
    print("=" * 60)
    print(f"🤖 LaBiOmicS Radar Bot - Iniciando Curadoria [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print("=" * 60)

    history = load_history()
    processed_dois = set(history.get("processed_dois", []))
    print(f"📦 DOIs já catalogados no histórico: {len(processed_dois)}")

    print(f"🔍 Buscando publicações recentes nos periódicos alvo (últimos {days_back} dias)...")
    candidates = fetch_recent_papers_europe_pmc(days_back=days_back, page_size=30)
    print(f"📄 Artigos brutos retornados: {len(candidates)}")

    # Filtra artigos inéditos
    new_candidates = [p for p in candidates if p["doi"] not in processed_dois]
    print(f"✨ Candidatos inéditos para publicação: {len(new_candidates)}")

    if not new_candidates:
        print("✅ Nenhum novo artigo de alto impacto para publicar hoje. O blog está atualizado!")
        return

    selected = new_candidates[:limit]
    today_str = datetime.now().strftime("%Y-%m-%d")

    for idx, paper in enumerate(selected, 1):
        print(f"\n--- Processando Artigo [{idx}/{len(selected)}] ---")
        print(f"Título Original: {paper['title']}")
        print(f"Periódico: {paper['journal']} ({paper['year']})")
        print(f"DOI: {paper['doi']}")

        print("🧠 Gerando síntese em português com IA...")
        ai_output = generate_post_with_gemini(paper)
        print(f"Título Gerado: {ai_output.get('title')}")

        post_markdown = format_jekyll_markdown(paper, ai_output, today_str)

        slug = slugify(ai_output.get("title", paper["title"]))
        filename = f"{today_str}-{slug}.md"
        filepath = POSTS_DIR / filename

        if dry_run:
            print(f"\n[DRY-RUN] O arquivo seria salvo em: {filepath}")
            print("[DRY-RUN] Prévia do conteúdo:")
            print("-" * 40)
            print(post_markdown[:400] + "\n... [truncado]")
            print("-" * 40)
        else:
            POSTS_DIR.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(post_markdown)
            print(f"💾 Post salvo com sucesso em: {filepath}")

            # Atualiza histórico
            history["processed_dois"].append(paper["doi"])
            history["articles"].append({
                "doi": paper["doi"],
                "title": paper["title"],
                "post_file": filename,
                "published_at": today_str
            })
            save_history(history)
            print(f"📝 Histórico atualizado com DOI {paper['doi']}")

    print("\n🎉 Ciclo de curadoria concluído com sucesso!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Curador Diário do LaBiOmicS Blog")
    parser.add_argument("--limit", type=int, default=5, help="Número máximo de posts a gerar (padrão: 5)")
    parser.add_argument("--dry-run", action="store_true", help="Executa sem salvar arquivos em disco")
    parser.add_argument("--days", type=int, default=30, help="Janela de dias para busca (padrão: 30)")

    args = parser.parse_args()
    run_curator(limit=args.limit, dry_run=args.dry_run, days_back=args.days)
