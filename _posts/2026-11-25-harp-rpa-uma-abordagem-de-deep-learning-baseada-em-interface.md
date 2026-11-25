---
layout: post
title: "HARP-RPA: Uma Abordagem de Deep Learning Baseada em Interfaces para a Predição Precisa da Afinidade de Ligação Proteína-RNA"
date: 2026-11-25 08:00:00 -0300
categories: ["bioinformatica", "ia-em-biologia"]
tags: ["protein-rna-binding", "deep-learning", "modelos-de-linguagem", "afinidade-de-ligacao", "rna-binding-proteins"]
journal: "Bioinformatics (Oxford, England)"
doi: "10.1093/bioinformatics/btag859"
original_url: "https://doi.org/10.1093/bioinformatics/btag859"
original_title: "HARP-RPA: Interface-Aware HeteroPairFormer for Protein-RNA Binding Affinity Prediction"
authors: "Wang B, Xie X"
year: 2026
---

A predição da afinidade de ligação proteína-RNA é um pilar fundamental para a compreensão da regulação pós-transcricional e para o desenvolvimento de terapias direcionadas ao RNA. No entanto, esta tarefa apresenta um gargalo computacional significativo: a força da ligação não é determinada apenas pelas sequências isoladas de proteína ou RNA, mas sim por contatos quimicamente heterogêneos entre resíduos e bases, formados em interfaces tridimensionais flexíveis. Modelos existentes, que se concentram predominantemente em sequências ou em descritores estruturais predefinidos, frequentemente falham em capturar a complexidade da interface local enquanto integram informações contextuais ricas fornecidas por modelos de linguagem modernos de proteínas e RNA. Esta lacuna impede uma compreensão completa das interações moleculares e limita o avanço no design de intervenções terapêuticas mais eficazes.

### O Pipeline, Algoritmo ou Abordagem Computacional
Para superar os desafios na predição da afinidade de ligação proteína-RNA, foi desenvolvido o HARP-RPA (Interface-aware HeteroPairFormer). Este modelo inovador de *deep learning* aborda o problema através da modelagem de complexos proteína-RNA como pares heterogêneos de resíduos/bases, com uma consciência explícita das interfaces de ligação. A metodologia central do HARP-RPA integra duas fontes de informação cruciais:

1.  **Embeddings de Modelos de Linguagem Pré-treinados:** Utiliza representações contextuais de proteínas e RNAs geradas por modelos de linguagem avançados, capturando informações semânticas e estruturais intrínsecas às sequências de maneira global.
2.  **Características de Pares Estruturais com Consciência Relacional:** Incorpora características de pares que distinguem explicitamente as relações intra-proteína, intra-RNA e, crucialmente, as relações *cross-interface* (entre proteína e RNA), além de tokens especiais. Esta abordagem permite que o modelo aprenda padrões de interação específicos da interface de ligação, que são determinantes para a afinidade.

As representações de tokens e pares são refinadas conjuntamente, garantindo que o modelo aprenda a partir de uma visão holística e detalhada. A etapa final de *readout* integra evidências globais do complexo com sinais locais da interface, resultando em uma predição robusta da afinidade de ligação. O desempenho do HARP-RPA foi validado em benchmarks rigorosos, como PRA310 e PRA201, onde alcançou valores de PCC/SCC de 0.621/0.633 e 0.580/0.598, respectivamente, com RMSE e MAE competitivos. Além disso, a representação aprendida demonstrou transferibilidade para o benchmark de efeitos de mutação mCSM-RNA, atingindo RMSE/MAE de 0.962/0.839 e PCC/SCC de 0.563/0.581 após *fine-tuning* supervisionado. A robustez do modelo e a contribuição de seus componentes foram corroboradas por análises estratificadas, de casos difíceis e de ablação. O código-fonte do HARP-RPA está disponível publicamente no GitHub (https://github.com/wbw176-netizen/HARP-RPA) e arquivado no Zenodo (https://doi.org/10.5281/zenodo.23486566), promovendo a reprodutibilidade e a ciência aberta.

### Conexão com as Linhas de Pesquisa do LaBiOmicS
Este trabalho se alinha diretamente com as prioridades do LaBiOmicS, especialmente nas linhas de pesquisa de **Biologia Computacional e IA** e **Transcriptômica e Expressão Gênica**.

Na linha de **Biologia Computacional e IA**, o HARP-RPA representa um avanço significativo no desenvolvimento de algoritmos e ferramentas baseadas em *machine learning* e *deep learning*. A utilização de modelos de linguagem pré-treinados e a arquitetura HeteroPairFormer para modelar interações complexas proteína-RNA exemplificam a aplicação de IA para resolver problemas biológicos desafiadores. O foco na modelagem de interfaces e na integração de diferentes tipos de dados (sequência e estrutura) reflete a expertise do laboratório em abordagens computacionais inovadoras para a predição de interações moleculares.

Adicionalmente, o estudo tem uma forte conexão com a **Transcriptômica e Expressão Gênica**. A predição precisa da afinidade de ligação proteína-RNA é fundamental para desvendar os mecanismos de regulação pós-transcricional, incluindo o papel de lncRNAs, o splicing alternativo e a identificação de biomarcadores. Ao melhorar a capacidade de prever essas interações, o HARP-RPA contribui diretamente para uma compreensão mais profunda de como a expressão gênica é controlada e como essas interações podem ser moduladas para fins terapêuticos. A disponibilidade de código aberto também ressoa com o compromisso do laboratório com a **Reprodutibilidade e Replicabilidade**, promovendo a transparência e a validação de métodos computacionais.
