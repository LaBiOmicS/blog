---
layout: post
title: "Modelos de Linguagem e Decodificação Probabilística: PSALM Redefine a Anotação de Domínios Proteicos em Escala Ômica"
date: 2026-11-26 08:00:00 -0300
categories: ["ia-em-biologia", "bioinformatica"]
tags: ["modelos-de-linguagem-de-proteinas", "anotacao-de-dominios", "deep-learning", "esm-2", "hmmer"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014969"
original_url: "https://doi.org/10.1371/journal.pcbi.1014969"
original_title: "Protein sequence domain annotation using a language model"
authors: "Sarkar A, Krishnan K, Eddy SR"
year: 2026
---

A anotação de domínios proteicos é um pilar fundamental para a inferência funcional em larga escala, permitindo a compreensão das funções biológicas e das interações moleculares. Tradicionalmente, essa tarefa tem sido dominada por métodos baseados em modelos ocultos de Markov de perfil (HMMs), como o HMMER, que escaneiam sequências contra bibliotecas de perfis conhecidos. Embora eficazes, a crescente avalanche de dados de sequenciamento e a complexidade inerente das proteínas demandam abordagens computacionais mais sofisticadas e sensíveis. A lacuna reside na capacidade de capturar padrões contextuais e sutis nas sequências proteicas que podem ser cruciais para a delimitação precisa de domínios, um gargalo que as novas arquiteturas de inteligência artificial, como os modelos de linguagem, prometem superar.

### O Pipeline, Algoritmo ou Abordagem Computacional

O artigo apresenta o PSALM (Protein Sequence Annotation using Language Models), uma metodologia inovadora para a anotação de domínios proteicos que integra o poder dos modelos de linguagem com técnicas de classificação e decodificação estruturada. O pipeline do PSALM é composto por três componentes principais:

1.  **Modelo de Linguagem de Proteínas Pré-treinado (ESM-2):** No cerne do PSALM, o modelo ESM-2 é utilizado para gerar representações vetoriais contextuais de cada resíduo na sequência proteica. Essas representações capturam informações complexas sobre o ambiente local e global de cada aminoácido, superando as limitações de abordagens baseadas em alinhamento.
2.  **Classificador de Estado de Domínio por Resíduo:** As representações do ESM-2 são então alimentadas a um classificador que prevê o estado de domínio para cada resíduo. Este classificador é treinado para discernir se um resíduo pertence a um domínio específico ou a uma região não-domínio, fornecendo uma probabilidade por resíduo.
3.  **Decodificador Probabilístico Estruturado:** O componente final e crucial do PSALM é um decodificador probabilístico estruturado. Ele processa as previsões por resíduo do classificador para produzir um conjunto único e não sobreposto de chamadas de domínio, com limites explícitos e pontuações de confiança. Este decodificador garante a coerência e a delimitação precisa dos domínios, resolvendo ambiguidades e sobreposições.

Em um *benchmark* massivo de 76.9 milhões de sequências proteicas contendo 107 milhões de domínios anotados, o PSALM demonstrou um *trade-off* de sensibilidade-especificidade na detecção de domínios comparável ao HMMER. Notavelmente, o PSALM alcança maior cobertura de sequências e resíduos em contagens de falsos positivos esperados (valores-E) mais relaxados, enquanto o HMMER mantém a liderança em valores-E mais rigorosos, sugerindo uma complementaridade entre as abordagens. Para promover a ciência aberta e a reprodutibilidade, os autores disponibilizaram o código para processamento de dados, treinamento e inferência, juntamente com os pesos do modelo e os conjuntos de dados utilizados para treinamento, validação e *benchmarking*.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com múltiplas linhas de pesquisa do LaBiOmicS, com destaque para a **Biologia Computacional e IA** e a **Genômica Estrutural e Funcional**. O desenvolvimento do PSALM é um exemplo paradigmático do uso de *machine learning* e *deep learning*, especificamente modelos de linguagem de proteínas, para resolver problemas complexos em bioinformática. A aplicação de modelos como o ESM-2 para a anotação de domínios representa um avanço significativo no desenvolvimento de algoritmos e ferramentas, ecoando o impacto de modelos como o AlphaFold na predição de estrutura. Além disso, a capacidade de realizar anotação de domínios em larga escala é crucial para a **Genômica Estrutural e Funcional**, fornecendo a base para a inferência de função gênica e a caracterização de variações. A liberação completa do código, pesos do modelo e dados de treinamento e *benchmarking* também reforça o compromisso do LaBiOmicS com a **Reprodutibilidade e Replicabilidade**, promovendo a ciência aberta e a validação independente de resultados computacionais.
