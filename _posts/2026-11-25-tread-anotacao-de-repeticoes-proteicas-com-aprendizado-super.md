---
layout: post
title: "TREAD: Anotação de Repetições Proteicas com Aprendizado Supervisionado e Embeddings de Modelos de Linguagem, Superando Abordagens Baseadas em Perfis"
date: 2026-11-25 08:00:00 -0300
categories: ["ia-em-biologia", "bioinformatica"]
tags: ["protein-embeddings", "protein-language-models", "repeat-annotation", "machine-learning", "alphafold"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014994"
original_url: "https://doi.org/10.1371/journal.pcbi.1014994"
original_title: "Beyond profiles: Supervised repeat annotation using protein embeddings"
authors: "Qiu K, Ludwiczak J, Lupas AN, Dunin-Horkawicz S"
year: 2026
---

Repetições proteicas são elementos estruturais e funcionais fundamentais, mas sua detecção baseada em sequência é um desafio persistente devido à alta divergência entre as unidades repetidas. Métodos convencionais, que dependem de perfis de sequência explícitos, frequentemente enfrentam limitações de flexibilidade e escalabilidade, dificultando a anotação precisa em cenários de dados escassos ou alta variabilidade. Essa lacuna impede uma compreensão completa da evolução e função dessas estruturas, tornando crucial o desenvolvimento de abordagens computacionais mais robustas e adaptáveis.

### O Pipeline, Algoritmo ou Abordagem Computacional

O TREAD (Transfer learning-based REpeat Annotation using Protein EmbeDdings) é uma estrutura supervisionada inovadora que reformula a detecção de repetições proteicas como um problema de anotação em nível de resíduo. Em vez de construir perfis probabilísticos explícitos, como o amplamente utilizado HMMER, o TREAD opera diretamente sobre *embeddings* gerados por modelos de linguagem de proteínas. Essa abordagem permite que o algoritmo aprenda implicitamente características específicas de repetições, resultando em uma pontuação resolvida por resíduo e uma extração flexível de segmentos repetidos. A metodologia foi validada extensivamente utilizando *benchmarks* complementares baseados em RepeatsDB e Pfam, demonstrando desempenho superior ou equivalente ao HMMER, especialmente em contextos de dados limitados e alta divergência de sequência. A robustez do modelo a diferentes limiares de pontuação e sua capacidade de generalização para conjuntos de teste independentes, incluindo famílias remotamente relacionadas, foram pontos cruciais. A utilidade prática do TREAD foi ilustrada pela sua aplicação na análise de proteínas beta-hélice (*β-propeller*) na AlphaFold Database e em proteomas representativos, revelando padrões de expansão específicos de linhagem e novas relações entre dobras de repetição.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com a linha de pesquisa de **Biologia Computacional e IA** do LaBiOmicS. O desenvolvimento do TREAD representa um avanço significativo na aplicação de *machine learning* e modelos de linguagem de proteínas para a anotação de sequências, uma área central para o laboratório. A utilização de *embeddings* de proteínas e a reformulação da detecção de repetições como um problema de anotação em nível de resíduo demonstram a inovação algorítmica e a capacidade de processamento de dados em larga escala. Além disso, a aplicação do TREAD na análise de proteínas beta-hélice na AlphaFold Database estabelece uma conexão com a **Genômica Estrutural e Funcional**, ao fornecer insights sobre a diversidade e evolução de estruturas proteicas, que são cruciais para a compreensão da função gênica e da variação.
