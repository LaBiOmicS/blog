---
layout: post
title: "Bioinformática na Oncologia: Um Pipeline Computacional Inovador para Desvendar Drivers Emergentes em Modelos Agente-Baseados de Tumores"
date: 2026-11-27 08:00:00 -0300
categories: ["bioinformatica", "ia-em-biologia"]
tags: ["modelagem-agente-baseada", "aprendizado-de-maquina", "abc-smc", "heterogeneidade-tumoral", "analise-de-parametros"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014995"
original_url: "https://doi.org/10.1371/journal.pcbi.1014995"
original_title: "A discovery of emergent drivers pipeline uncovers parameter hierarchies in spatiotemporal agent-based tumor models"
authors: "Chiu PH, Evarts JI, Cain JY, Bagheri N"
year: 2026
---

A heterogeneidade tumoral representa um dos maiores desafios na oncologia, dificultando o desenvolvimento de terapias eficazes. Esta complexidade decorre de decisões celulares individuais, da regulação entre diversas células e da interação destas com o microambiente tumoral. Identificar os fatores celulares e microambientais que impulsionam essa heterogeneidade é crucial para o direcionamento terapêutico. Contudo, os métodos experimentais atuais frequentemente obscurecem as contribuições relativas do microambiente e das propriedades intrínsecas das células. Paralelamente, os métodos padrão de estimação de parâmetros para modelos espaciais-temporais falham em classificar a importância dos parâmetros ou em resolver a equifinalidade – a propriedade pela qual diferentes combinações de parâmetros podem gerar comportamentos emergentes equivalentes. Esta lacuna computacional e biológica exige abordagens mais sofisticadas para desvendar as complexas interações que governam a progressão tumoral.

### O Pipeline, Algoritmo ou Abordagem Computacional

Para superar as limitações existentes, o estudo apresenta um pipeline inovador de descoberta de drivers emergentes, livre de verossimilhança, projetado para identificar combinações de distribuições de parâmetros que levam a dinâmicas teciduais emergentes observadas. Este pipeline integra o poder da Computação Bayesiana Aproximada (ABC) com o Monte Carlo Sequencial (SMC) e Random Forests Distribuídas. A combinação dessas técnicas permite ajustar métricas-alvo e caracterizar as associações entre parâmetros e saídas dentro de modelos agente-baseados espaciais-temporais. A análise de informação mútua é empregada para comparar perfis de dependência entre diferentes regiões de parâmetros ajustados. Para otimizar o espaço de busca de parâmetros sem comprometer o ajuste às métricas-alvo emergentes, o pipeline utiliza correlações entre partículas de geração-4, aplicando substituição por regressão linear pareada e agrupamento baseado em clusterização hierárquica. A aplicação a dados de câncer de mama demonstrou a capacidade do pipeline de identificar regiões de parâmetros ajustados que, embora reproduzam métricas-alvo semelhantes, exibem perfis de dependência parâmetro-saída distintos, fornecendo insights valiosos sobre redundâncias mecanísticas.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com a Linha de Pesquisa 5 do LaBiOmicS: **Biologia Computacional e IA**. O desenvolvimento de um pipeline computacional complexo que integra algoritmos avançados como Computação Bayesiana Aproximada (ABC-SMC) e Random Forests Distribuídas para modelagem de sistemas biológicos (neste caso, modelos agente-baseados de tumores) é um exemplo claro de desenvolvimento de algoritmos e ferramentas inovadoras. A abordagem de aprendizado de máquina para caracterizar a importância e a dependência de parâmetros, bem como a otimização do espaço de busca, reflete o foco do laboratório em aplicar e desenvolver métodos de machine learning e deep learning para resolver problemas biológicos complexos. A capacidade de desvendar hierarquias de parâmetros e equifinalidade em modelos biológicos representa um avanço significativo na aplicação de IA para a compreensão de sistemas biológicos dinâmicos.
