#!/usr/bin/env python3
"""
fetch_papers.py - Busca direcionada de artigos em Bioinformática e Ciências Ômicas via PubMed.

Foco estrito e protagonista em Bioinformática e nas 6 Linhas de Pesquisa do LaBiOmicS:
1. Genômica Estrutural e Funcional & Mitogenômica
2. Transcriptômica e Expressão Gênica (RNA-Seq, redes gênicas, lncRNAs)
3. Microbioma e Viroma (diversidade microbiana/viral, interações patógeno-hospedeiro)
4. Metagenômica e Resistoma (shotgun metagenomics, genes de resistência a antimicrobianos - ARGs, MGEs)
5. Biologia Computacional e Inteligência Artificial (algoritmos, machine/deep learning, ferramentas abertas, AlphaFold)
6. Reprodutibilidade e Workflows (benchmarking de pipelines, Nextflow, Snakemake, contêineres)
"""

import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import html
import re
from typing import List, Dict, Any, Optional

# Periódicos de referência mundial em Bioinformática, Métodos e Ciências Ômicas
TARGET_JOURNALS_QUERY = (
    '("Bioinformatics"[Journal] OR "Brief Bioinform"[Journal] OR "Nat Methods"[Journal] OR '
    '"PLoS Comput Biol"[Journal] OR "Genome Biol"[Journal] OR "Nucleic Acids Res"[Journal] OR '
    '"Microbiome"[Journal] OR "ISME J"[Journal] OR "Gigascience"[Journal] OR "Database (Oxford)"[Journal] OR '
    '"BMC Bioinformatics"[Journal] OR "BMC Genomics"[Journal] OR '
    '(("Nat Biotechnol"[Journal] OR "Nat Genet"[Journal] OR "Nat Commun"[Journal] OR '
    '"Nature"[Journal] OR "Science"[Journal] OR "Cell"[Journal]) AND '
    '(bioinformatics OR "computational biology" OR "machine learning" OR "deep learning" OR '
    'metagenom* OR "RNA-seq" OR "genome assembly" OR resistome OR mitogenom* OR lncRNA OR '
    '"AlphaFold" OR pipeline OR workflow OR benchmark)))'
)

# Termos das 6 Linhas de Pesquisa do LaBiOmicS
RESEARCH_LINES_QUERY = (
    '("mitogenomics" OR "mitogenome" OR "genome assembly" OR "structural variation" OR '
    '"transcriptome" OR "RNA-Seq" OR "co-expression network" OR "long non-coding RNA" OR "lncRNA" OR '
    '"microbiome" OR "virome" OR "viral diversity" OR "host-microbe" OR '
    '"metagenomics" OR "shotgun metagenomics" OR "metagenome-assembled genomes" OR "MAGs" OR '
    '"resistome" OR "antimicrobial resistance" OR "antimicrobial resistance genes" OR "mobile genetic elements" OR '
    '"computational biology" OR "machine learning" OR "deep learning" OR "AlphaFold" OR '
    '"protein language model" OR "Nextflow" OR "Snakemake" OR "benchmarking" OR "bioinformatics tool")'
)

# Palavras-chave obrigatórias para assegurar o elo de bioinformática
BIOINFO_INDICATORS = [
    "bioinformatics", "computational", "algorithm", "pipeline", "tool", "software",
    "machine learning", "deep learning", "in silico", "neural network", "database",
    "genome assembly", "rna-seq", "metagenom", "shotgun", "resistome", "mitogenom",
    "lncrna", "benchmark", "workflow", "nextflow", "snakemake", "alphafold", "mags"
]


def clean_text(raw_text: Optional[str]) -> str:
    """Decodifica entidades HTML e limpa espaços redundantes."""
    if not raw_text:
        return ""
    unescaped = html.unescape(raw_text)
    clean = re.sub(r"<.*?>", "", unescaped)
    return " ".join(clean.split())


def has_bioinformatics_focus(title: str, abstract: str) -> bool:
    """Verifica se o artigo tem a bioinformática como elo central."""
    combined = f"{title} {abstract}".lower()
    matches = sum(1 for ind in BIOINFO_INDICATORS if ind in combined)
    return matches >= 1


def fetch_recent_papers_pubmed(limit: int = 50) -> List[Dict[str, Any]]:
    """
    Busca artigos recentes no PubMed alinhados às linhas de pesquisa do LaBiOmicS.
    """
    full_term = f"({TARGET_JOURNALS_QUERY}) AND ({RESEARCH_LINES_QUERY})"
    
    esearch_url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
        f"db=pubmed&term={urllib.parse.quote(full_term)}&retmax={limit * 2}&sort=pub_date&retmode=json"
    )

    headers = {
        "User-Agent": "LaBiOmicS-CuratorBot/3.0 (https://labiomics.github.io/blog; labiomics@bioinformatica.com.br)"
    }

    try:
        req = urllib.request.Request(esearch_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as res:
            search_data = json.loads(res.read().decode("utf-8"))
            id_list = search_data.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"[Aviso] Erro no esearch do PubMed: {e}")
        return []

    if not id_list:
        return []

    # Busca os detalhes via efetch em lote (máximo 50 por vez)
    ids_str = ",".join(id_list[:limit])
    efetch_url = (
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
        f"db=pubmed&id={ids_str}&retmode=xml"
    )

    try:
        req = urllib.request.Request(efetch_url, headers=headers)
        with urllib.request.urlopen(req, timeout=25) as res:
            xml_content = res.read()
    except Exception as e:
        print(f"[Aviso] Erro no efetch do PubMed: {e}")
        return []

    results = []
    try:
        root = ET.fromstring(xml_content)
    except Exception as e:
        print(f"[Aviso] Erro ao parsear XML do PubMed: {e}")
        return []

    for art in root.findall(".//PubmedArticle"):
        try:
            medline = art.find(".//MedlineCitation")
            article = medline.find(".//Article") if medline is not None else None
            if article is None:
                continue

            title = clean_text(article.findtext(".//ArticleTitle"))
            
            # Concatena partes do abstract
            abstract_parts = []
            abstract_elem = article.find(".//Abstract")
            if abstract_elem is not None:
                for text_elem in abstract_elem.findall(".//AbstractText"):
                    label = text_elem.get("Label")
                    content = text_elem.text or ""
                    if label:
                        abstract_parts.append(f"{label}: {content}")
                    else:
                        abstract_parts.append(content)
            abstract = clean_text(" ".join(abstract_parts))

            # Validação mínima
            if not title or not abstract or len(abstract) < 180:
                continue

            if not has_bioinformatics_focus(title, abstract):
                continue

            # Periódico
            journal_title = article.findtext(".//Journal/Title") or "Periódico Científico"

            # Ano
            pub_date = article.find(".//JournalIssue/PubDate")
            year = "2026"
            if pub_date is not None:
                year_elem = pub_date.find("Year")
                if year_elem is not None and year_elem.text:
                    year = year_elem.text

            # DOI
            doi = None
            article_id_list = art.find(".//PubmedData/ArticleIdList")
            if article_id_list is not None:
                for aid in article_id_list.findall(".//ArticleId"):
                    if aid.get("IdType") == "doi":
                        doi = aid.text.strip()
                        break

            if not doi:
                # Tenta DOI dentro da MedlineCitation
                for eid in article.findall(".//ELocationID"):
                    if eid.get("EIdType") == "doi":
                        doi = eid.text.strip()
                        break

            if not doi:
                continue

            # Autores
            authors_list = []
            author_group = article.find(".//AuthorList")
            if author_group is not None:
                for a in author_group.findall(".//Author")[:5]:
                    last = a.findtext("LastName") or ""
                    initials = a.findtext("Initials") or ""
                    if last:
                        authors_list.append(f"{last} {initials}".strip())
                if len(author_group.findall(".//Author")) > 5:
                    authors_list.append("et al.")
            author_str = ", ".join(authors_list) or "Vários Autores"

            results.append({
                "doi": doi,
                "title": title.rstrip("."),
                "abstract": abstract,
                "authors": author_str,
                "journal": journal_title,
                "year": year,
                "url": f"https://doi.org/{doi}",
                "source": "PubMed / NCBI"
            })
        except Exception as err:
            continue

    return results


# Função de compatibilidade
def fetch_recent_papers_europe_pmc(topics=None, journals=None, days_back=45, page_size=50):
    """Encaminha para a busca PubMed de alta precisão em bioinformática."""
    return fetch_recent_papers_pubmed(limit=page_size)


if __name__ == "__main__":
    print("Testando busca no PubMed focada nas 6 linhas de pesquisa do LaBiOmicS...")
    papers = fetch_recent_papers_pubmed(limit=15)
    print(f"\nArtigos de bioinformática encontrados: {len(papers)}")
    for i, p in enumerate(papers[:5], 1):
        print(f"\n[{i}] {p['title']}")
        print(f"    Periódico: {p['journal']} ({p['year']})")
        print(f"    DOI: {p['doi']}")
        print(f"    Abstract: {p['abstract'][:140]}...")
