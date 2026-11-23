#!/usr/bin/env python3
"""
generate_post.py - Geração de sínteses científicas com foco protagonista em Bioinformática.

Conectado estritamente com as 6 Linhas de Pesquisa do LaBiOmicS:
1. Genômica Estrutural e Funcional & Mitogenômica
2. Transcriptômica e Expressão Gênica
3. Microbioma e Viroma
4. Metagenômica e Resistoma
5. Biologia Computacional e Inteligência Artificial
6. Reprodutibilidade e Workflows
"""

import os
import json
import urllib.request
import urllib.parse
from typing import Dict, Any, Optional

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

SYSTEM_PROMPT = """Você é o Redator Científico Especialista em Bioinformática e Ciências Ômicas do LaBiOmicS (Laboratório de Bioinformática e Ciências Ômicas - Menegidio Lab).

ATENÇÃO AO PRINCÍPIO FUNDAMENTAL DO LABORATÓRIO:
A BIOINFORMÁTICA E A BIOLOGIA COMPUTACIONAL SÃO O ELO PRINCIPAL DE TODAS AS ANÁLISES.
O foco dos artigos deve SEMPRE destacar algoritmos, pipelines, modelos estatísticos/de IA, montagem, anotação, benchmarking, bancos de dados, ferramentas de código aberto e processamento em larga escala de dados ômicos.

O LaBiOmicS atua especificamente em 6 Linhas de Pesquisa:
1. Genômica Estrutural e Funcional & Mitogenômica (montagem de genomas nucleares/mitocondriais, anotação gênica, variação)
2. Transcriptômica e Expressão Gênica (RNA-Seq, redes de co-expressão, splicing alternativo, lncRNAs, biomarcadores)
3. Microbioma e Viroma (bacterioma, micobioma, viroma, ecologia microbiana, interação hospedeiro-microrganismo)
4. Metagenômica e Resistoma (sequenciamento shotgun, genes de resistência a antimicrobianos - ARGs, elementos genéticos móveis - MGEs, mineração de genomas/MAGs)
5. Biologia Computacional e IA (desenvolvimento de algoritmos e ferramentas, machine learning, deep learning, AlphaFold, modelos de linguagem de proteínas)
6. Reprodutibilidade e Replicabilidade (benchmarking, workflows em Nextflow/Snakemake, contêineres Docker/Singularity, ciência aberta)

Diretrizes de Redação:
1. Linguagem: Português do Brasil (pt-BR) técnico, fluído e acadêmico de alto nível, adequado para bioinformatas, biólogos moleculares e cientistas da computação.
2. Título em Português: Atraente, técnico e preciso, evidenciando o avanço computacional ou genômico/metagenômico.
3. Estrutura do Texto (Markdown):
   - Parágrafo de Introdução: Qual é a lacuna biológica ou o gargalo computacional que motivou o estudo?
   - Subseção '### O Pipeline, Algoritmo ou Abordagem Computacional': Explique a metodologia bioinformática (ferramentas utilizadas, bancos de dados, modelagem, algoritmos, validação, fluxo de dados).
   - Subseção '### Conexão com as Linhas de Pesquisa do LaBiOmicS': Explique como este trabalho dialoga diretamente com as linhas do laboratório (cite explicitamente a linha correspondente, como Metagenômica/Resistoma, Transcriptômica/lncRNAs, Mitogenômica ou Biologia Computacional/IA).
4. Categorias: Escolha 1 ou 2 entre: [bioinformatica, metagenomica, genomica, transcriptomica, microbioma, ia-em-biologia, reprodutibilidade].
5. Tags: 3 a 5 tags técnicas em minúsculas (ex: shotgun-sequencing, nextflow, alphafold, lncrna, resistome, mags, mitogenoma).

Responda ESTRITAMENTE em formato JSON com as chaves:
{
  "title": "Título em português focado no avanço bioinformático/ômico",
  "categories": ["bioinformatica", "metagenomica"],
  "tags": ["tag1", "tag2", "tag3"],
  "body_markdown": "Texto completo em Markdown formatado..."
}
"""


def generate_post_with_gemini(paper: Dict[str, Any], api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Chama a API do Google Gemini para gerar o conteúdo do post com foco em bioinformática.
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
            "temperature": 0.35,
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
    Gera um rascunho de post caso a API esteja indisponível.
    """
    title = f"Bioinformática em Foco: {paper.get('title')[:85]}..."
    
    abstract_lower = paper.get('abstract', '').lower()
    categories = ["bioinformatica"]
    if "metagenom" in abstract_lower or "microbiom" in abstract_lower:
        categories.append("metagenomica")
    elif "transcriptom" in abstract_lower or "rna-seq" in abstract_lower:
        categories.append("transcriptomica")
    elif "learning" in abstract_lower or "algorithm" in abstract_lower or "model" in abstract_lower:
        categories.append("ia-em-biologia")

    body = f"""O periódico **{paper.get('journal')}** publicou um estudo de alto impacto centrado em inovação computacional e ciências ômicas: *"{paper.get('title')}"*, por {paper.get('authors')}.

### O Desafio e o Contexto Computacional
{paper.get('abstract')}

### O Pipeline, Algoritmo ou Abordagem Computacional
- Desenvolvimento de metodologia bioinformática avançada para integração de dados biológicos em larga escala.
- Estruturação de fluxos de análise com ênfase em reprodutibilidade, validação e mineração preditiva.

### Conexão com as Linhas de Pesquisa do LaBiOmicS
O artigo conecta-se fortemente com a atuação do laboratório em biologia computacional e análise de dados ômicos massivos, ressaltando a importância do desenvolvimento de algoritmos robustos e ciência aberta.
"""

    return {
        "title": title,
        "categories": categories,
        "tags": ["bioinformatica", "ciencias-omicas", "computational-biology"],
        "body_markdown": body
    }


def format_jekyll_markdown(paper: Dict[str, Any], ai_output: Dict[str, Any], date_str: str) -> str:
    """
    Formata o artigo final no padrão Markdown com Frontmatter Jekyll.
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
