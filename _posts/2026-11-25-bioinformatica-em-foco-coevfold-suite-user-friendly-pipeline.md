---
layout: post
title: "Bioinformática em Foco: CoEVFold suite: User friendly pipelines to visually represent protein coevolution..."
date: 2026-11-25 08:00:00 -0300
categories: ["bioinformatica", "ia-em-biologia"]
tags: ["bioinformatica", "ciencias-omicas", "computational-biology"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014968"
original_url: "https://doi.org/10.1371/journal.pcbi.1014968"
original_title: "CoEVFold suite: User friendly pipelines to visually represent protein coevolution"
authors: "Graham CLB, Cremona L, Little R, Rodrigues CDA"
year: 2026
---

O periódico **PLoS computational biology** publicou um estudo de alto impacto centrado em inovação computacional e ciências ômicas: *"CoEVFold suite: User friendly pipelines to visually represent protein coevolution"*, por Graham CLB, Cremona L, Little R, Rodrigues CDA.

### O Desafio e o Contexto Computacional
Multiple sequence alignment (MSA) data underlies current principles in protein folding and protein-protein interaction prediction, from which deep-learning models trained on protein sequence and structure datasets can predict protein structure. However, what is missing are user-friendly tools that enable researchers to identify and visualise coevolution, the principal signal that these MSAs encode. Here we present tools to identify and visualize coevolution, through a pipeline (CoEVFold) that uses basic direct coupling algorithms derived from GREMLIN and an input alignment of sequences from MMseqs2. We also provide notebooks to calculate coevolution with alternative methods such as CCMpred or plmc. The pipeline generates a visual representation of coevolution for a single protein but can also represent coevolution of homomeric or heteromeric protein complexes, as well as coevolution within protein networks. The input for this pipeline can be an amino acid sequence, or protein structures from AlphaFold/RoseTTAFold, the user's own files or the PDB. Using proteins from well-studied prokaryotic and eukaryotic model systems (Bacillus subtilis, Escherichia coli and Saccharomyces cerevisiae), as well as phage proteins, we show that CoEVFold detects coevolution between proteins known to interact, between protomers of known oligomers, and within known protein complexes. Benchmarked against 18 heteromeric complexes of known structure, the top-ranked inter-protein couplings identified interface contacts with a precision of 0.8 or more in 7 complexes, and CoEVMapper rankings agreed with STRING associations for an Escherichia coli cell-wall synthesis network (ROC AUC 0.72-0.74). For homo-oligomers, the top-ranked coevolution pairs not explained by the monomer structure were protomer-protomer contacts in 25% (SpoIIIE) and 47% (MlaD) of cases, against 2% or less expected by chance. The coupling calculation for a ~ 950-residue complex took 114 s with GREMLIN, compared with 116 s for CCMpred and 2,060 s for plmc. Collectively, this suite of tools, named 'CoEVFold suite', has broad applicability and provide a useful toolkit to those interested in dissecting protein-protein interactions and networks.

### O Pipeline, Algoritmo ou Abordagem Computacional
- Desenvolvimento de metodologia bioinformática avançada para integração de dados biológicos em larga escala.
- Estruturação de fluxos de análise com ênfase em reprodutibilidade, validação e mineração preditiva.

### Conexão com as Linhas de Pesquisa do LaBiOmicS
O artigo conecta-se fortemente com a atuação do laboratório em biologia computacional e análise de dados ômicos massivos, ressaltando a importância do desenvolvimento de algoritmos robustos e ciência aberta.
