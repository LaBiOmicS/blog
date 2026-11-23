---
layout: post
title: "MIsoTEx: Um Framework Bioinformático para Classificação e Análise Abrangente de Isoformas de Transcritos em Tecidos Mamíferos"
date: 2026-11-23 08:00:00 -0300
categories: ["bioinformatica", "transcriptomica"]
tags: ["rna-seq", "isoformas-de-transcritos", "expressao-genica", "banco-de-dados"]
journal: "Nucleic acids research"
doi: "10.1093/nar/gkag1261"
original_url: "https://doi.org/10.1093/nar/gkag1261"
original_title: "MIsoTEx: a mammalian transcript-isoform classification framework and database for exploring tissue distribution, expression stability, and abundance patterns"
authors: "Balagannavar G, Basavaraju K, Manivelan V, Bm S, Hanna K, et al."
year: 2026
---

A complexidade da expressão gênica em mamíferos é amplificada pelo splicing alternativo, que gera uma vasta gama de isoformas de transcritos com padrões de expressão tecidual distintos. Apesar de sua importância fundamental na regulação biológica e na patogênese de doenças, a integração de dados sobre a distribuição tecidual, a consistência da abundância e os padrões de abundância relativa dessas isoformas em uma plataforma unificada e sistematicamente classificada tem sido um gargalo computacional significativo. A ausência de um recurso abrangente que permita a exploração detalhada desses perfis de expressão em larga escala dificulta a identificação de biomarcadores e a compreensão dos mecanismos regulatórios subjacentes.

### O Pipeline, Algoritmo ou Abordagem Computacional

O estudo apresenta o MIsoTEx (Mammalian Isoform Tissue Expression Resource), um framework bioinformático e um banco de dados inovador projetado para a classificação e exploração de isoformas de transcritos codificadoras de proteínas em humanos, camundongos e ratos. A abordagem computacional envolveu a curadoria e o processamento de extensos conjuntos de dados de RNA-seq provenientes de fontes públicas como GTEx, ARCHS4 e SRA, com uma seleção rigorosa de amostras de tecidos adultos normais para construir catálogos de expressão. O cerne do MIsoTEx reside em seu algoritmo de classificação baseado em padrões de expressão. As isoformas detectadas ubiquamente foram categorizadas como uniformemente abundantes (UUni) ou variavelmente abundantes (UVar). Para isoformas associadas a tecidos específicos, foram definidas classes como predominantes em tecido (TPred), exclusivas de tecido (TExcl), com baixa expressão em tecido (TPoor) ou ausentes em tecido (TAbsn). Cada uma dessas classes foi refinada em cinco subclasses de abundância relativa, e escores de confiança foram atribuídos às classificações associadas a tecidos, garantindo a robustez dos resultados. O banco de dados resultante compreende aproximadamente 147.000 isoformas de transcritos codificadoras de proteínas e oferece funcionalidades avançadas, incluindo consultas baseadas em genes e transcritos, buscas por padrões de expressão tecidual, comparação entre espécies de ortólogos com expressão concordante e a capacidade de analisar dados de expressão fornecidos pelo usuário para identificar isoformas de controle candidatas. A validação do framework foi realizada através de comparações com conjuntos de dados independentes de RNA-seq, RT-PCR e dados de expressão previamente publicados, enquanto análises de enriquecimento funcional revelaram associações biológicas distintas entre as categorias de expressão identificadas.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho estabelece uma conexão direta e fundamental com a linha de pesquisa de **Transcriptômica e Expressão Gênica** do LaBiOmicS. A metodologia empregada, baseada em extensos dados de RNA-seq e focada na identificação e classificação de isoformas de transcritos geradas por splicing alternativo, é central para a compreensão dos mecanismos de regulação gênica em nível pós-transcricional. A capacidade de identificar biomarcadores potenciais e explorar padrões de expressão tecidual de isoformas é um pilar dessa linha. Adicionalmente, o desenvolvimento de um framework computacional robusto e um banco de dados abrangente, como o MIsoTEx, alinha-se perfeitamente com a linha de **Biologia Computacional e IA**, que visa o desenvolvimento de algoritmos e ferramentas bioinformáticas avançadas para o processamento e a interpretação de dados ômicos em larga escala. A validação rigorosa e a arquitetura do banco de dados demonstram o compromisso com a ciência de dados e a inovação computacional.
