---
layout: post
title: "AlphaFold na Vanguarda: Modelagem Estrutural em Larga Escala Desvenda Mimetismo Molecular em Interações Hospedeiro-Patógeno"
date: 2026-11-24 08:00:00 -0300
categories: ["ia-em-biologia", "bioinformatica"]
tags: ["alphafold", "ppi", "mimetismo-molecular", "biologia-estrutural", "deep-learning"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014932"
original_url: "https://doi.org/10.1371/journal.pcbi.1014932"
original_title: "AlphaFold models of host-pathogen interactions elucidate the prevalence and structural modes of molecular mimicry"
authors: "Baptista D, Gomez-Lucas L, Jänes J, Krogan NJ, Amorim MJ, et al."
year: 2026
---

A compreensão das interações proteína-proteína (PPIs) entre hospedeiros e patógenos é crucial para desvendar os mecanismos de infecção e defesa. No entanto, a ausência de informações estruturais em larga escala para essas interações representa um gargalo significativo, limitando nossa capacidade de estudar fenômenos como o mimetismo molecular e a evolução convergente de interfaces de ligação. Métodos experimentais tradicionais para determinação estrutural são frequentemente custosos e demorados, inviabilizando análises em escala genômica ou proteômica e aprofundando essa lacuna de conhecimento fundamental.

### O Pipeline, Algoritmo ou Abordagem Computacional

Para superar a lacuna estrutural, este estudo empregou uma abordagem computacional robusta baseada em inteligência artificial, utilizando os modelos AlphaFold2 e AlphaFold3. Inicialmente, foi realizado um benchmarking rigoroso dessas ferramentas para avaliar sua acurácia na predição de estruturas de PPIs hospedeiro-patógeno. Observou-se que, apesar de uma performance geral que poderia ser melhorada, modelos acurados podiam ser recuperados ao se priorizar as predições com maior confiança. Em seguida, a metodologia foi escalada para prever as estruturas de 6.782 PPIs entre patógenos e proteínas humanas, resultando em 803 modelos de alta confiança. A análise desses modelos permitiu identificar que a maioria das proteínas patogênicas que interagem com uma proteína humana comum o fazem através da mesma interface, sugerindo uma forte evolução convergente. Além disso, ao comparar modelos estruturais de interações hospedeiro-patógeno com interações hospedeiro-hospedeiro, verificou-se que a maioria das proteínas patogênicas mimetiza interfaces de PPIs humanas já existentes. O trabalho categorizou o mimetismo em diferentes modos estruturais: via a mesma família de domínio (menos comum), via um motivo estrutural similar, e via um peptídeo linear similar (mais comum). A validação experimental de 12 interações de peptídeos lineares confirmou 8 delas, incluindo 3 interações virais, reforçando a capacidade do AlphaFold em modelar interações complexas e os mecanismos subjacentes ao mimetismo molecular.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com a linha de pesquisa de **Biologia Computacional e IA** do LaBiOmicS. A aplicação em larga escala do AlphaFold2 e AlphaFold3 para predição de estruturas de interações proteína-proteína hospedeiro-patógeno demonstra o uso avançado de modelos de inteligência artificial para resolver problemas biológicos complexos. O benchmarking das ferramentas, a análise de confiança dos modelos e a categorização de modos de mimetismo molecular são exemplos claros do desenvolvimento e aplicação de algoritmos e ferramentas computacionais. Além disso, a capacidade de gerar insights sobre a evolução convergente e os mecanismos de infecção através da modelagem estrutural ressalta o potencial do *machine learning* e *deep learning* na compreensão de sistemas biológicos em escala molecular.
