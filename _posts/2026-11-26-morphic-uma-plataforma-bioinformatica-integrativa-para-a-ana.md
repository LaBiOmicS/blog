---
layout: post
title: "MorPhiC: Uma Plataforma Bioinformática Integrativa para a Análise em Larga Escala de Fenótipos Moleculares de Alelos Nulos Humanos"
date: 2026-11-26 08:00:00 -0300
categories: ["bioinformatica", "genomica"]
tags: ["integracao-omica", "genomica-funcional", "rna-seq", "portais-de-dados", "alelos-nulos"]
journal: "Nucleic acids research"
doi: "10.1093/nar/gkag1238"
original_url: "https://doi.org/10.1093/nar/gkag1238"
original_title: "The molecular phenotypes of null alleles in cells (MorPhiC) data resource"
authors: "Wilson R, Orges Koci A, Shivalikanjli A, Vidović D, Yordanova G, et al."
year: 2026
---

A compreensão das consequências moleculares e celulares da inativação gênica em humanos é um pilar fundamental para desvendar mecanismos de doenças e funções biológicas essenciais. No entanto, a complexidade e a heterogeneidade dos dados ômicos gerados em larga escala, provenientes de diversas plataformas (como RNA-seq, single-cell RNA-seq, metabolômica) e estratégias de perturbação, representam um gargalo significativo. A ausência de recursos integrados e padronizados dificulta a análise comparativa robusta e a extração de conhecimento acionável sobre os fenótipos moleculares associados a alelos nulos. O MorPhiC Data Portal surge como uma resposta computacional a essa necessidade, fornecendo uma infraestrutura bioinformática abrangente para consolidar, analisar e disponibilizar dados de inativação gênica em células humanas, permitindo uma exploração escalável e sistemática dos efeitos da perda de função gênica.

### O Pipeline, Algoritmo ou Abordagem Computacional

O MorPhiC Data Portal é uma plataforma computacional robusta que integra e padroniza uma vasta gama de dados ômicos e de fenotipagem funcional para o estudo de alelos nulos em células humanas. A abordagem computacional centraliza-se na harmonização e análise uniforme de dados provenientes de diversas tecnologias, incluindo RNA-seq (tanto bulk quanto single-cell), Perturb-seq, SLAM-seq, perfil de acessibilidade da cromatina e metabolômica. Os dados brutos e processados são submetidos a pipelines de análise uniformes, desenvolvidos para garantir consistência e comparabilidade entre os experimentos, um aspecto crucial para a reprodutibilidade e replicabilidade dos resultados em estudos de larga escala.

Um dos avanços computacionais centrais do portal é a sua navegação gene-centrada. Para cada gene, a plataforma consolida de forma inteligente o contexto experimental, as estratégias de perturbação (visando produtos de DNA, RNA ou proteína), os modelos celulares utilizados (como células-tronco pluripotentes induzidas humanas, corpos embrionários e organoides), os conjuntos de dados associados, as evidências de fenotipagem e os resultados de análises padronizadas. Além disso, o MorPhiC oferece visualizações interativas que expõem de forma clara resultados de expressão diferencial, enriquecimento de vias e resultados específicos de ensaios, facilitando a interpretação e a exploração dos dados por parte dos usuários.

Para enriquecer o contexto biológico, o portal integra os conjuntos de dados MorPhiC com anotações externas sobre essencialidade gênica, associações com doenças mendelianas e fenótipos de mamíferos. A padronização de metadados, saídas de análise e fluxos de trabalho de submissão a arquivos públicos é um pilar fundamental da arquitetura do MorPhiC, tornando-o um recurso reutilizável e escalável para a comunidade científica interessada em estudos de perda de função em humanos.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com múltiplas linhas de pesquisa do LaBiOmicS, com um foco proeminente na **Genômica Estrutural e Funcional** e na **Reprodutibilidade e Replicabilidade**.

Na linha de **Genômica Estrutural e Funcional**, o MorPhiC aborda diretamente a variação gênica (alelos nulos) e sua anotação funcional em larga escala, investigando as consequências moleculares da inativação gênica em diversos sistemas celulares. A análise de expressão gênica e perfis de acessibilidade da cromatina contribui diretamente para a compreensão da função gênica e dos mecanismos regulatórios em resposta a perturbações genéticas.

Adicionalmente, a ênfase na utilização de pipelines de análise uniformes, a padronização de metadados e a disponibilização de um recurso reutilizável para a comunidade científica ressoa fortemente com a linha de **Reprodutibilidade e Replicabilidade**. A iniciativa MorPhiC serve como um excelente exemplo de ciência aberta e de como a padronização computacional é essencial para garantir a validade, a comparabilidade e a reutilização dos resultados em estudos ômicos de grande escala, um princípio fundamental defendido pelo LaBiOmicS.

Por fim, a integração e análise de dados de RNA-seq (tanto bulk quanto single-cell) estabelece uma conexão direta com a linha de **Transcriptômica e Expressão Gênica**, especialmente na identificação de biomarcadores e na compreensão de redes de co-expressão alteradas pela inativação gênica, fornecendo insights valiosos sobre a regulação gênica em diferentes contextos celulares.
