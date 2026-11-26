---
layout: post
title: "mirCCC: Aprendizado de Grafos e Análise de scRNA-Seq para Decifrar a Comunicação Célula-Célula Mediada por miRNAs"
date: 2026-11-26 08:00:00 -0300
categories: ["transcriptomica", "bioinformatica"]
tags: ["mirna", "scrna-seq", "aprendizado-de-grafos", "comunicacao-celular", "biomarcadores"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014494"
original_url: "https://doi.org/10.1371/journal.pcbi.1014494"
original_title: "mirCCC: Repression-aware graph learning for miRNA-mediated cell-cell communication inference"
authors: "Chen Y, Cui J, Zhang S, Liu E, Xie L, et al."
year: 2026
---

A compreensão da comunicação intercelular é fundamental para desvendar processos biológicos complexos e patologias como o câncer. Tradicionalmente, as análises de comunicação célula-célula têm se concentrado predominantemente em ligantes e receptores proteicos, negligenciando uma via de sinalização igualmente crucial: a transferência de microRNAs (miRNAs) via vesículas extracelulares. Essa lacuna representa um gargalo significativo, especialmente em contextos como a oncogênese, onde miRNAs desempenham papéis regulatórios vitais. A capacidade de inferir essa comunicação miRNA-mediada a partir de dados transcriptômicos de célula única (scRNA-seq) padrão é um desafio computacional que, uma vez superado, pode revolucionar nossa compreensão das interações celulares.

### O Pipeline, Algoritmo ou Abordagem Computacional
Para endereçar essa lacuna, foi desenvolvido o `mirCCC`, um framework computacional inovador projetado para estimar a comunicação célula-célula mediada por miRNAs a partir de dados de sequenciamento de RNA de célula única. A metodologia central do `mirCCC` reside na detecção de diminuições coordenadas na expressão de genes-alvo de miRNAs validados. O pipeline integra diversas etapas computacionais sofisticadas: primeiramente, estima a atividade de miRNA de forma específica para cada célula; em seguida, modela a capacidade de envio e recebimento celular para a transferência de vesículas extracelulares; e, finalmente, emprega técnicas de aprendizado de grafos para construir redes de comunicação resolvidas por miRNA a partir dos dados transcriptômicos. A robustez do `mirCCC` foi demonstrada em benchmarks sintéticos, onde, mesmo na presença de fortes sinais de confusão, o método apresentou desempenho superior, enquanto as abordagens comparativas declinaram. Sua aplicação a um atlas de câncer colorretal humano não apenas recuperou miRNAs previamente associados à doença, mas também identificou vias de comunicação estromal e mieloide para epitelial que convergem em programas de plasticidade celular ligados às vias de sinalização TGF-β e Wnt/β-catenina, fornecendo uma rota prática para estudar a comunicação mediada por vesículas extracelulares em atlas de célula única existentes.

### Conexão com as Linhas de Pesquisa do LaBiOmicS
Este trabalho se alinha diretamente com múltiplas linhas de pesquisa do LaBiOmicS. A análise de dados de sequenciamento de RNA de célula única (scRNA-seq) e a investigação do papel dos miRNAs na regulação gênica e na comunicação intercelular o conectam intrinsecamente à linha de **Transcriptômica e Expressão Gênica**. O desenvolvimento e a validação do `mirCCC` como um framework computacional, que inclui a aplicação de aprendizado de grafos e modelagem estatística avançada, o posicionam firmemente na linha de **Biologia Computacional e IA**. Além disso, a rigorosa avaliação de desempenho através de benchmarks sintéticos, comparando `mirCCC` com outros métodos, ressalta a importância da **Reprodutibilidade e Replicabilidade** na ciência, garantindo a robustez e a confiabilidade dos resultados bioinformáticos.
