---
layout: post
title: "spotGLM e SPARROW: Um Framework Bioinformático Unificado para Análise Diferencial Escalável em Ômicas Espaciais"
date: 2026-11-24 08:00:00 -0300
categories: ["bioinformatica", "transcriptomica"]
tags: ["spatial-omics", "spotglm", "glm", "rna-seq", "scalability"]
journal: "Nature biotechnology"
doi: "10.1038/s41587-026-03284-0"
original_url: "https://doi.org/10.1038/s41587-026-03284-0"
original_title: "A unified framework for scalable differential testing for spatial omics"
authors: "Mason K, Jiang Y, Klötzer KA, Huang S, Zhang NR"
year: 2026
---

A análise de dados ômicos espaciais representa um avanço crucial para desvendar a complexidade biológica dos tecidos, permitindo a identificação de características cujos valores variam não apenas pelo tipo celular, mas também pelo nicho celular circundante. Contudo, um gargalo significativo reside na limitação das metodologias existentes, que frequentemente são otimizadas para dados baseados em contagens (como transcriptômica) e falham em generalizar eficientemente para outras modalidades ômicas ou em escalar para os volumes massivos de dados gerados atualmente. Este estudo aborda essa lacuna, introduzindo um framework computacional unificado e escalável para a análise diferencial em diversas modalidades ômicas espaciais.

### O Pipeline, Algoritmo ou Abordagem Computacional
Os pesquisadores desenvolveram o **spotGLM**, um framework de modelagem linear generalizada (GLM) que considera misturas, projetado para testes diferenciais específicos de tipo celular em múltiplas modalidades espaciais. O spotGLM é notavelmente versátil, acomodando diversos tipos de dados, incluindo expressão gênica baseada em contagens, proporções de isoformas binomiais e pontuações contínuas de acessibilidade da cromatina, tudo dentro de uma estrutura estatística unificada. Complementarmente, foi introduzido o **SPARROW**, uma estratégia de destilação de dados que preserva o poder estatístico, fundamental para inferência escalável.

A eficácia do framework foi demonstrada em diversas aplicações de ômicas espaciais. Em dados Visium HD de câncer colorretal e rim de camundongo, o spotGLM e o SPARROW permitiram a recuperação de efeitos de nicho específicos de tipo celular, com validação multiplataforma em cortes seriais. Em dados de RNA-seq espacial de leitura longa, o framework revelou a troca de isoformas específica de tipo celular no bulbo olfatório de camundongo. Adicionalmente, em dados de ATAC-seq espacial do cérebro de camundongo, foi possível identificar variações espaciais específicas de tipo celular na acessibilidade de motivos regulatórios.

### Conexão com as Linhas de Pesquisa do LaBiOmicS
Este trabalho se alinha diretamente com diversas linhas de pesquisa do LaBiOmicS, reforçando o princípio fundamental de que a bioinformática e a biologia computacional são o elo principal de todas as análises.

*   **Biologia Computacional e IA:** O desenvolvimento do spotGLM e do SPARROW representa um avanço significativo na criação de algoritmos e ferramentas computacionais robustas. A utilização de modelagem linear generalizada e estratégias de destilação de dados para inferência escalável exemplifica a aplicação de modelos estatísticos avançados para resolver desafios complexos em larga escala.
*   **Transcriptômica e Expressão Gênica:** A capacidade do framework de analisar expressão gênica baseada em contagens e, crucialmente, de resolver a troca de isoformas específica de tipo celular em dados de RNA-seq espacial, demonstra sua relevância direta para a compreensão da regulação gênica e do splicing alternativo em contextos espaciais.
*   **Genômica Estrutural e Funcional:** A aplicação bem-sucedida do spotGLM em dados de ATAC-seq espacial para identificar variações na acessibilidade de motivos regulatórios estabelece uma conexão clara com a genômica funcional, permitindo a exploração de elementos regulatórios do genoma em alta resolução espacial.
