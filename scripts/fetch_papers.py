#!/usr/bin/env python3
"""
fetch_papers.py - Busca de artigos científicos recentes de alto impacto.

Consulta APIs abertas (Europe PMC / PubMed / OpenAlex) filtrando por termos
de interesse do laboratório LaBiOmicS e periódicos de alto fator de impacto.
"""

import urllib.request
import urllib.parse
import json
import re
import html
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

# Periódicos de alto impacto de interesse
DEFAULT_JOURNALS = [
    "Nature",
    "Science",
    "Cell",
    "Nature Biotechnology",
    "Nature Genetics",
    "Nature Methods",
    "Nature Communications",
    "Nucleic Acids Research",
    "Bioinformatics",
    "Genome Biology",
    "Microbiome",
    "The ISME Journal",
    "Briefings in Bioinformatics",
    "PLoS Computational Biology"
]

# Tópicos de pesquisa alinhados com o LaBiOmicS
DEFAULT_TOPICS = [
    "metagenomics",
    "microbiome",
    "antimicrobial resistance",
    "resistome",
    "RNA-seq",
    "single-cell transcriptomics",
    "long non-coding RNA",
    "lncRNA",
    "structural bioinformatics",
    "AlphaFold",
    "protein structure prediction",
    "deep learning biology",
    "mitogenomics"
]


def clean_html(raw_html: str) -> str:
    """Remove tags HTML, decodifica entidades e normaliza espaços."""
    if not raw_html:
        return ""
    # Decodifica entidades HTML como &lt;sup&gt; para <sup>
    unescaped = html.unescape(raw_html)
    # Remove tags HTML
    clean = re.sub(r"<.*?>", "", unescaped)
    return " ".join(clean.split())


def fetch_recent_papers_europe_pmc(
    topics: Optional[List[str]] = None,
    journals: Optional[List[str]] = None,
    days_back: int = 15,
    page_size: int = 25
) -> List[Dict[str, Any]]:
    """
    Busca artigos no Europe PMC usando queries estruturadas em periódicos de topo.
    """
    topics = topics or DEFAULT_TOPICS
    journals = journals or DEFAULT_JOURNALS

    topics_query = " OR ".join([f'"{t}"' if " " in t else t for t in topics])
    journals_query = " OR ".join([f'JOURNAL:"{j}"' for j in journals])

    start_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    query_str = f"({topics_query}) AND ({journals_query}) AND (FIRST_PDATE:[{start_date} TO 2099-12-31])"

    params = {
        "query": query_str,
        "format": "json",
        "resultType": "core",
        "pageSize": str(page_size),
        "sort": "P_PDATE_D desc"
    }

    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{urllib.parse.urlencode(params)}"
    
    headers = {
        "User-Agent": "LaBiOmicS-CuratorBot/1.0 (https://labiomics.github.io; contato@labiomics.com.br)"
    }

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"[Aviso] Falha ao consultar Europe PMC: {e}")
        return []

    results = []
    items = data.get("resultList", {}).get("result", [])

    for item in items:
        doi = item.get("doi")
        abstract = clean_html(item.get("abstractText", ""))
        title = clean_html(item.get("title", ""))

        # Exige pelo menos DOI e Abstract para conseguirmos gerar uma boa síntese
        if not doi or not abstract or len(abstract) < 150:
            continue

        journal_title = item.get("journalInfo", {}).get("journal", {}).get("title", "")
        if not journal_title:
            journal_title = item.get("journalTitle", "Revista Científica")

        pub_year = item.get("pubYear", str(datetime.now().year))
        author_string = item.get("authorString", "Vários Autores")

        results.append({
            "doi": doi.strip(),
            "title": title.rstrip("."),
            "abstract": abstract,
            "authors": author_string,
            "journal": journal_title,
            "year": pub_year,
            "url": f"https://doi.org/{doi.strip()}",
            "source": "Europe PMC"
        })

    return results


if __name__ == "__main__":
    print("Testando busca de artigos recentes no Europe PMC...")
    papers = fetch_recent_papers_europe_pmc(days_back=60, page_size=5)
    print(f"Artigos válidos encontrados: {len(papers)}")
    for i, p in enumerate(papers, 1):
        print(f"\n[{i}] {p['title']}")
        print(f"    Periódico: {p['journal']} ({p['year']})")
        print(f"    DOI: {p['doi']}")
        print(f"    Abstract: {p['abstract'][:120]}...")
