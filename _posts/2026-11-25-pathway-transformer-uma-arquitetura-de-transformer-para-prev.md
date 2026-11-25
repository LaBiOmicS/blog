---
layout: post
title: "Pathway-Transformer: Uma Arquitetura de Transformer para Previsão de Fenótipos de Câncer via Integração de Variantes de Transcritos e Vias Biológicas"
date: 2026-11-25 08:00:00 -0300
categories: ["bioinformatica", "transcriptomica"]
tags: ["transformer", "rna-seq", "splicing-alternativo", "predicao-de-cancer", "redes-biologicas"]
journal: "Bioinformatics (Oxford, England)"
doi: "10.1093/bioinformatics/btag864"
original_url: "https://doi.org/10.1093/bioinformatics/btag864"
original_title: "Pathway-Transformer: Integrating Transcript Variants and Biological Pathways for Cancer Phenotype Prediction"
authors: "Baul S, Sun J, Fahmi NA, Zhang W"
year: 2026
---

A compreensão aprofundada das funções biológicas e dos mecanismos regulatórios que moldam os desfechos do câncer é crucial tanto para elucidar a progressão da doença quanto para guiar terapias direcionadas. A análise integrativa de dados multiômicos tem se estabelecido como uma abordagem robusta para fornecer uma visão molecular mais completa do câncer. No entanto, um gargalo computacional persistente reside na incapacidade de muitos métodos existentes de incorporar explicitamente as variantes de transcritos geradas por eventos pós-transcricionais, como o splicing alternativo e a poliadenilação alternativa. Tais eventos são reconhecidamente drivers de anomalias proteicas e, consequentemente, de mudanças fenotípicas, mas são frequentemente negligenciados em favor da expressão gênica agregada, perdendo informações cruciais para a predição precisa de desfechos clínicos. Este cenário motivou o desenvolvimento de uma nova abordagem computacional capaz de preencher essa lacuna, capitalizando sobre a riqueza informacional das variantes de transcritos.

### O Pipeline, Algoritmo ou Abordagem Computacional

Para superar as limitações mencionadas, foi proposto o **Pathway-Transformer**, uma estrutura computacional inovadora que integra variantes de transcritos e expressão gênica, ambos derivados dos mesmos dados de RNA-seq, para a predição de fenótipos de câncer, utilizando vias biológicas como conhecimento prévio. A metodologia do Pathway-Transformer é intrinsecamente bioinformática e baseada em inteligência artificial:

1.  **Codificação de Redes de Vias:** O framework inicia codificando as propriedades estruturais das redes de vias biológicas (ex: vias KEGG), transformando-as em representações que podem ser processadas por modelos de aprendizado de máquina.
2.  **Encoder Transformer:** No coração do Pathway-Transformer está um **encoder Transformer**, uma arquitetura de deep learning conhecida por sua capacidade de modelar dependências de longo alcance e capturar relações complexas em dados sequenciais ou estruturados. Este encoder é empregado para aprender representações específicas de vias da regulação transcricional, onde as variantes de transcritos e a expressão gênica são contextualizadas dentro do arcabouço das vias biológicas.
3.  **Agregação e Predição:** As representações aprendidas por cada via são então agregadas de forma inteligente para realizar a predição do fenótipo de câncer. Este processo permite que o modelo capture a interação e a contribuição combinada de múltiplas vias e seus respectivos perfis de variantes de transcritos.
4.  **Validação e Interpretabilidade:** A eficácia do Pathway-Transformer foi avaliada em amostras de pacientes com câncer de mama do TCGA e validada de forma independente na coorte METABRIC, demonstrando desempenho superior na predição de desfechos clínicos quando comparado a perfis de expressão gênica isolados. Os resultados consistentemente indicam que as variantes de transcritos fornecem assinaturas moleculares mais informativas. Adicionalmente, a análise dos scores de atenção computados a partir dos parâmetros aprendidos pelo Transformer permitiu a identificação de programas de receptores hormonais e sinalização biologicamente relevantes, conferindo interpretabilidade ao modelo e reforçando sua aplicabilidade clínica. O código-fonte do Pathway-Transformer está disponível publicamente em https://github.com/compbiolabucf/PathwayTransformer, promovendo a reprodutibilidade e a ciência aberta.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha perfeitamente com duas das principais linhas de pesquisa do LaBiOmicS:

*   **Biologia Computacional e IA:** O desenvolvimento e a aplicação do **Pathway-Transformer**, uma arquitetura de rede neural baseada em **Transformers**, representam um avanço significativo no campo da inteligência artificial aplicada à biologia. A capacidade de modelar dados ômicos complexos e extrair padrões preditivos a partir de variantes de transcritos demonstra o potencial da IA para resolver desafios biológicos complexos, alinhando-se diretamente com o desenvolvimento de algoritmos e ferramentas de machine learning e deep learning no laboratório.
*   **Transcriptômica e Expressão Gênica:** O foco central do estudo na integração e análise de **variantes de transcritos** (resultantes de splicing alternativo e poliadenilação alternativa) e dados de expressão gênica provenientes de RNA-seq para a identificação de **biomarcadores** e predição de fenótipos de câncer, dialoga diretamente com a linha de pesquisa em Transcriptômica. A ênfase na informação contida nas variantes de transcritos, muitas vezes negligenciada, destaca a importância de abordagens computacionais avançadas para desvendar a complexidade da regulação gênica pós-transcricional.
