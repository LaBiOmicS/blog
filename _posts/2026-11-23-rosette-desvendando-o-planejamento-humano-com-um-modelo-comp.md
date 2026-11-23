---
layout: post
title: "ROSETTE: Desvendando o Planejamento Humano com um Modelo Computacional Analiticamente Tratável Baseado em Cadeias de Markov"
date: 2026-11-23 08:00:00 -0300
categories: ["ia-em-biologia", "bioinformatica"]
tags: ["modelagem-computacional", "cadeias-de-markov", "planejamento-cognitivo", "algoritmos"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014945"
original_url: "https://doi.org/10.1371/journal.pcbi.1014945"
original_title: "Rollout models of human planning with exact action probabilities"
authors: "Olieslagers J, Ma WJ"
year: 2026
---

A capacidade de planejar é uma das características mais sofisticadas da cognição humana, frequentemente atribuída à simulação mental de sequências de ações potenciais para avaliar resultados futuros, um processo conhecido como 'rollout'. Embora modelos baseados em rollout tenham alcançado grande sucesso em inteligência artificial, sua aplicação para descrever como os humanos utilizam essa estratégia tem sido limitada. O principal gargalo reside na dificuldade de ajustar esses modelos a dados comportamentais, pois as abordagens existentes dependem de simulações computacionalmente intensivas que geram estimativas aproximadas e ruidosas dos parâmetros de planejamento latentes. Essa limitação compromete a precisão e a interpretabilidade dos modelos cognitivos, dificultando uma compreensão aprofundada dos mecanismos subjacentes ao planejamento humano.

### O Pipeline, Algoritmo ou Abordagem Computacional

Para superar as barreiras computacionais na modelagem do planejamento humano, Olieslagers e Ma introduziram o ROSETTE (Rollouts with Stochastic Early Termination and Tractable Estimation), um modelo inovador baseado em rollout que oferece um ajuste analiticamente tratável e livre de simulações. O ROSETTE aborda o planejamento como uma sequência de simulações mentais formalizadas como uma cadeia de Markov absorvente. Esta abordagem permite que o modelo acumule deterministicamente evidências de rollout esperadas, calculadas analiticamente, e execute um número variável de ciclos de atualização de política. Ao invés de depender de simulações Monte Carlo que introduzem ruído e exigem alto poder computacional, o ROSETTE utiliza propriedades matemáticas das cadeias de Markov absorventes para derivar probabilidades de ação exatas e tempos de primeira passagem, tornando a inferência de parâmetros muito mais eficiente e precisa. A validação do ROSETTE foi realizada ajustando-o a dados de participantes humanos em duas tarefas de planejamento multietapas, demonstrando que o modelo conseguiu explicar de forma robusta um rico conjunto de estatísticas sumárias do comportamento observado. Essa metodologia não apenas simplifica o processo de modelagem, mas também aumenta a confiabilidade das estimativas dos parâmetros cognitivos.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha intrinsecamente com a linha de pesquisa de **Biologia Computacional e IA** do LaBiOmicS. O desenvolvimento do ROSETTE representa um avanço significativo na criação de algoritmos e modelos computacionais para decifrar processos biológicos complexos, neste caso, o planejamento cognitivo humano. A ênfase na tratabilidade analítica e na eliminação de simulações intensivas ressoa diretamente com o nosso foco em otimizar o processamento de dados em larga escala e desenvolver abordagens computacionais eficientes. Embora o contexto seja a cognição, a metodologia de modelagem baseada em cadeias de Markov e a busca por soluções analíticas para problemas complexos são princípios que aplicamos no LaBiOmicS para desvendar padrões em dados ômicos, desde a predição de estruturas proteicas até a análise de redes de co-expressão gênica. A capacidade de desenvolver modelos que fornecem estimativas exatas e robustas, como o ROSETTE, é fundamental para a interpretabilidade e a reprodutibilidade na ciência computacional, pavimentando o caminho para futuras aplicações em sistemas biológicos.
