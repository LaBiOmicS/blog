#!/usr/bin/env python3
"""
generate_post.py - Geração automatizada do artigo de divulgação científica via IA.

Utiliza a API do Google Gemini (ou fallback) para gerar um post curto, elegante
e tecnicamente preciso em português com base nos metadados e no abstract do artigo.
"""

import os
import json
import urllib.request
import urllib.parse
from typing import Dict, Any, Optional

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


SYSTEM_PROMPT = """Você é o Redator Científico Especialista do LaBiOmicS (Laboratório de Bioinformática e Ciências Ômicas).
Sua missão é ler os metadados e o abstract de um artigo científico de alto impacto e escrever uma síntese de divulgação científica em Português do Brasil (pt-BR) de alto nível para o blog do laboratório.

Diretrizes de Redação:
1. Tom: Cientificamente rigoroso, moderno, acessível a pesquisadores e estudantes de pós-graduação em bioinformática, biotecnologia e ciências biológicas. Não use clichês vazios de IA ("em um mundo onde...", "um divisor de águas revolucionário").
2. Título em Português: Crie um título claro, cativante e preciso (NÃO faça tradução literal do inglês, mas resuma a descoberta ou inovação principal).
3. Estrutura do Texto:
   - Parágrafo de Abertura: Qual o problema biológico, de saúde ou metodológico abordado?
   - Subseção '### Principais Inovações Metodológicas': Detalhe a estratégia experimental ou computacional (sequenciamento shotgun, single-cell, algoritmos, aprendizado profundo, bancos de dados, etc.).
   - Subseção '### Por que isso é relevante para o LaBiOmicS e para a Área?': O impacto prático da descoberta e como dialoga com as pesquisas de genômica, metagenômica e bioinformática aberta.
4. Categorias: Escolha 1 a 2 categorias principais entre: [metagenomica, genomica, transcriptomica, ia, bioinformatica, microbioma].
5. Tags: 3 a 5 tags técnicas em letras minúsculas (ex: resistoma, alphafold, rna-seq, docker).

Responda ESTRITAMENTE em formato JSON com as chaves:
{
  "title": "Título em português",
  "categories": ["categoria1", "categoria2"],
  "tags": ["tag1", "tag2", "tag3"],
  "body_markdown": "Texto completo em Markdown formatado..."
}
"""


def generate_post_with_gemini(paper: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Chama a API do Google Gemini para gerar o conteúdo do post.
    """
    api_key = api_key or os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("[Aviso] GEMINI_API_KEY não encontrada. Gerando post estruturado com modelo de fallback.")
        return generate_post_fallback(paper)

    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

    user_content = f"""Artigo Original:
Título: {paper.get('title')}
Periódico: {paper.get('journal')} ({paper.get('year')})
Autores: {paper.get('authors')}
DOI: {paper.get('doi')}
Link: {paper.get('url')}

Resumo (Abstract):
{paper.get('abstract')}
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": SYSTEM_PROMPT},
                    {"text": user_content}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.4,
            "responseMimeType": "application/json"
        }
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=40) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            candidate = res_data["candidates"][0]["content"]["parts"][0]["text"]
            post_json = json.loads(candidate)
            return post_json
    except Exception as e:
        print(f"[Erro] Falha ao comunicar com a API do Gemini ({e}). Usando fallback.")
        return generate_post_fallback(paper)


def generate_post_fallback(paper: Dict[str, Any]) -> Dict[str, Any]:
    """
    Gera um rascunho de post sem depender da chave de API da IA (útil para testes locais).
    """
    title = f"Avanços Recentes em {paper.get('journal')}: {paper.get('title')[:80]}..."
    
    # Classificação heurística simples
    abstract_lower = paper.get('abstract', '').lower()
    categories = []
    if "metagenom" in abstract_lower or "microbiom" in abstract_lower:
        categories.append("metagenomica")
    if "transcriptom" in abstract_lower or "rna-seq" in abstract_lower:
        categories.append("transcriptomica")
    if "structure" in abstract_lower or "alphafold" in abstract_lower or "protein" in abstract_lower:
        categories.append("bioinformatica")
    if "machine learning" in abstract_lower or "deep learning" in abstract_lower:
        categories.append("ia")
    if not categories:
        categories = ["bioinformatica"]

    body = f"""O periódico **{paper.get('journal')}** publicou recentemente um estudo de grande impacto intitulado *"{paper.get('title')}"*, desenvolvido por {paper.get('authors')}.

### Contexto do Estudo
{paper.get('abstract')}

### Principais Inovações Metodológicas
- Investigação detalhada combinando abordagens experimentais avançadas com modelagem computacional.
- Estratégia de análise voltada para desvendar sistemas biológicos complexos e interação molecular.

### Relevância para a Comunidade LaBiOmicS
O trabalho dialoga diretamente com as linhas de pesquisa do laboratório, reforçando a importância do uso de pipelines reprodutíveis e análise de grandes volumes de dados ômicos para gerar novas hipóteses biológicas.
"""

    return {
        "title": title,
        "categories": categories,
        "tags": ["ciencias-omicas", "bioinformatica", "artigo-recente"],
        "body_markdown": body
    }


def format_jekyll_markdown(paper: Dict[str, Any], ai_output: Dict[str, Any], date_str: str) -> str:
    """
    Formata o artigo final no padrão Markdown com Frontmatter aceito nativamente pelo Jekyll.
    """
    title = ai_output.get("title", paper.get("title", "Novo Artigo")).replace('"', '\\"')
    categories = ai_output.get("categories", ["bioinformatica"])
    tags = ai_output.get("tags", ["bioinformatica"])
    body = ai_output.get("body_markdown", "").strip()

    frontmatter = f"""---
layout: post
title: "{title}"
date: {date_str} 08:00:00 -0300
categories: {json.dumps(categories)}
tags: {json.dumps(tags)}
journal: "{paper.get('journal', '')}"
doi: "{paper.get('doi', '')}"
original_url: "{paper.get('url', '')}"
original_title: "{paper.get('title', '').replace('"', '\\"')}"
authors: "{paper.get('authors', '').replace('"', '\\"')}"
year: {paper.get('year', 2026)}
---

{body}
"""
    return frontmatter
