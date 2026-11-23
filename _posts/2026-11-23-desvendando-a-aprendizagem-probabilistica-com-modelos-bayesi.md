---
layout: post
title: "Desvendando a Aprendizagem Probabilística com Modelos Bayesianos: Uma Abordagem Computacional para a Dinâmica Pupilar"
date: 2026-11-23 08:00:00 -0300
categories: ["bioinformatica", "ia-em-biologia"]
tags: ["modelagem-bayesiana", "neurociencia-computacional", "aprendizagem-maquina", "pupilometria", "inferencia-estatistica"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014064"
original_url: "https://doi.org/10.1371/journal.pcbi.1014064"
original_title: "Pupil dynamics reflect uncertainty-driven adjustments of probability learning"
authors: "Greenhouse-Tucknott A, Foucault C, Buot A, Meyniel F"
year: 2026
---

A compreensão dos mecanismos adaptativos da aprendizagem em ambientes dinâmicos é um desafio central na neurociência computacional. Embora a pupillometria seja uma ferramenta promissora para inferir estados de excitação e incerteza, a integração de modelos computacionais robustos para decifrar como a incerteza modula a aprendizagem probabilística, especialmente em cenários de difícil detecção de mudanças, ainda representa um gargalo significativo. Este estudo aborda essa lacuna ao empregar uma abordagem computacional avançada para modelar a relação complexa entre a dinâmica pupilar e os ajustes impulsionados pela incerteza na aprendizagem.

### O Pipeline, Algoritmo ou Abordagem Computacional

O cerne desta investigação reside na aplicação de um **modelo bayesiano de observador ideal** (Bayesian ideal observer model). Este algoritmo foi projetado para estimar, em cada tentativa (trial-by-trial), as taxas de aprendizagem e dois fatores críticos associados à incerteza: a probabilidade de um ponto de mudança (change point probability) e a incerteza prévia (prior uncertainty) sobre as crenças atuais do processo generativo. A metodologia envolveu a coleta de dados de pupillometria e desempenho em uma tarefa de aprendizagem probabilística, onde participantes humanos estimavam uma probabilidade geradora oculta de estímulos que mudavam abrupta e imprevisivelmente.

O modelo bayesiano atua como um framework computacional robusto para inferir estados latentes (taxas de aprendizagem e incerteza) a partir de dados observáveis (respostas comportamentais e dinâmica pupilar). A validação do modelo foi realizada ao demonstrar que os participantes, em linha com a teoria normativa, ajustavam suas taxas de aprendizagem com base na incerteza prévia. Além disso, análises de mediação foram empregadas para quantificar como os sinais pupilares fásicos (rastreando a probabilidade de ponto de mudança) e tônicos (rastreando a incerteza prévia) mediavam os efeitos desses fatores na aprendizagem. Este fluxo de dados e modelagem computacional permitiu uma compreensão aprofundada da integração racional de fatores de incerteza latentes na atualização de crenças, regulada por respostas associadas à excitação.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com a linha de pesquisa **Biologia Computacional e IA** do LaBiOmicS. A aplicação de um modelo bayesiano de observador ideal para inferir processos cognitivos complexos, como a aprendizagem probabilística e a percepção de incerteza, exemplifica o desenvolvimento e a aplicação de algoritmos avançados para desvendar fenômenos biológicos. A modelagem de sistemas dinâmicos, a inferência de estados latentes e a análise de dados fisiológicos em larga escala (pupilometria) são pilares da biologia computacional, e este estudo demonstra como essas ferramentas podem ser utilizadas para construir modelos preditivos e explicativos do comportamento adaptativo. Além disso, a exploração da "racionalidade computacional" subjacente à integração de fatores de incerteza na atualização de crenças ressoa com o foco do laboratório em desenvolver e aplicar modelos de IA para compreender a complexidade biológica.
