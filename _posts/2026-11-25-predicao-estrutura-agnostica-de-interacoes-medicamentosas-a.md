---
layout: post
title: "Predição Estrutura-Agnóstica de Interações Medicamentosas: A Fusão de Semântica MeSH e Topologia de Grafos de Conhecimento em Bioinformática"
date: 2026-11-25 08:00:00 -0300
categories: ["bioinformatica", "ia-em-biologia"]
tags: ["drug-drug-interaction", "knowledge-graph", "machine-learning", "mesh-semantics", "drug-discovery"]
journal: "BMC bioinformatics"
doi: "10.1186/s12859-026-06746-z"
original_url: "https://doi.org/10.1186/s12859-026-06746-z"
original_title: "Integrating MeSH semantics and knowledge graph topology for structure-agnostic drug-drug interaction prediction"
authors: "Yılmaz A, Taheri G"
year: 2026
---

As interações medicamentosas (DDIs) adversas representam um desafio significativo na prática clínica, sendo uma causa evitável de hospitalizações. A triagem experimental exaustiva de todas as possíveis combinações de fármacos é inviável devido à sua complexidade combinatória e aos altos custos associados. Além disso, muitos preditores computacionais existentes para DDIs dependem de representações estruturais de pequenas moléculas, o que limita drasticamente sua aplicabilidade a terapêuticas biológicas, uma classe de medicamentos em crescente desenvolvimento e importância. Diante dessa lacuna, surge a necessidade premente de desenvolver abordagens computacionais robustas, versáteis e estrutura-agnósticas que possam prever DDIs de forma eficiente e abrangente, independentemente da natureza química do fármaco.

### O Pipeline, Algoritmo ou Abordagem Computacional

Este estudo apresenta um *framework* inovador e estrutura-agnóstico para a predição de interações medicamentosas, superando as limitações das abordagens baseadas em estrutura. A metodologia central reside na combinação sinérgica de duas fontes de informação distintas: representações semânticas e topologia de grafos. Primeiramente, são utilizadas representações semânticas derivadas dos *Medical Subject Headings* (MeSH), que fornecem uma rica taxonomia hierárquica para descrever drogas e seus efeitos. A profundidade da anotação MeSH foi examinada para entender sua associação com o desempenho preditivo, revelando variações sistemáticas na performance. Em paralelo, é construído um grafo de conhecimento Drug-Target-Protein, integrando dados de bancos de dados biomédicos de referência como DrugBank e UniProt. Este grafo captura as relações complexas entre drogas, seus alvos proteicos e as proteínas em si, fornecendo uma visão topológica das interações biológicas.

A fusão dessas duas fontes de informação é realizada através de uma abordagem de fusão latente com *gating* (latent gated fusion). Este algoritmo de *machine learning* é projetado para aprender a combinar de forma otimizada as características semânticas do MeSH com as características topológicas do grafo de conhecimento. A validação do modelo foi rigorosa, empregando avaliações transdutivas e indutivas (seen-unseen). Na avaliação transdutiva, o modelo alcançou um AUROC geral de 0.988, superando significativamente abordagens baseadas apenas em MeSH em todas as seis categorias de interação. Na avaliação indutiva, onde pares de teste incluíam uma droga não vista, o AUROC geral foi de 0.937, demonstrando a robustez e a capacidade de generalização do *framework*. Ganhos notáveis foram observados para interações de baixa a média e média a média profundidade de anotação MeSH, com evidências adicionais para interações de média a profunda em avaliação transdutiva.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com a linha de pesquisa **Biologia Computacional e IA** do LaBiOmicS. O desenvolvimento e a aplicação de um algoritmo de *machine learning* avançado (fusão latente com *gating*) para a predição de interações complexas, a construção e mineração de grafos de conhecimento a partir de bancos de dados como DrugBank e UniProt, e a exploração de representações semânticas (MeSH) são pilares fundamentais desta linha. A abordagem estrutura-agnóstica representa um avanço significativo na modelagem computacional, expandindo a aplicabilidade de preditores para além das pequenas moléculas, e demonstra o potencial da IA para resolver problemas críticos na descoberta e segurança de fármacos.

Adicionalmente, o rigor na avaliação e *benchmarking* do modelo, com análises transdutivas e indutivas, e a aplicação de correção estatística (Holm), ressoa com os princípios de **Reprodutibilidade e Replicabilidade**. A ênfase na robustez e na capacidade de generalização dos resultados computacionais é crucial para garantir a confiabilidade e o impacto translacional da bioinformática na saúde.
