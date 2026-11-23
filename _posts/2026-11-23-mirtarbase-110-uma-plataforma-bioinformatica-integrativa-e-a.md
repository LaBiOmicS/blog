---
layout: post
title: "miRTarBase 11.0: Uma Plataforma Bioinformática Integrativa e Assistida por IA para Desvendar Interações miRNA-Alvo"
date: 2026-11-23 08:00:00 -0300
categories: ["bioinformatica", "transcriptomica"]
tags: ["mirna", "banco-de-dados", "curadoria-de-dados", "ia-generativa", "regulacao-genica"]
journal: "Nucleic acids research"
doi: "10.1093/nar/gkag1254"
original_url: "https://doi.org/10.1093/nar/gkag1254"
original_title: "miRTarBase 11.0: an evidence-centred resource for experimentally supported microRNA-target interactions"
authors: "Li X, Dong D, Wan J, Yu S, Zhang L, et al."
year: 2026
---

A compreensão da regulação gênica pós-transcricional mediada por microRNAs (miRNAs) é fundamental para desvendar processos biológicos complexos e mecanismos de doenças. No entanto, a diversidade de abordagens experimentais para identificar interações miRNA-alvo (MTIs) resulta em dados fragmentados e heterogêneos, criando um gargalo computacional significativo na integração e interpretação dessas informações. A ausência de um recurso centralizado e de alta confiança que consolide e contextualize essas interações dificulta a pesquisa e a descoberta de novos biomarcadores e alvos terapêuticos.

### O Pipeline, Algoritmo ou Abordagem Computacional

O miRTarBase 11.0 surge como uma solução robusta para esse desafio, consolidando um vasto repositório de 9.771.947 registros de MTIs, abrangendo 5.010 miRNAs e 31.539 genes-alvo. A metodologia bioinformática empregada é multifacetada e altamente sofisticada. A base de dados integra dados de curadoria literária manual, informações de pareamento quimérico do CLASHub e dados processados de imunoprecipitação e reticulação de Argonaute (AGO-CLIP). Para garantir uma interpretação aprofundada, o recurso distingue explicitamente diferentes tipos de evidência, como pareamento direto, ocupação de AGO, validação funcional e suporte contextual.

Um dos pilares computacionais do miRTarBase 11.0 é a integração de dados de alta resolução. O CLASHub fornece evidências de pareamento direto miRNA-alvo com resolução de sítio de ligação, enquanto o processamento atualizado de dados AGO-CLIP define classes de interação de alta confiança e conservadas. Um sistema de pontuação baseado em regras sumariza métodos de direcionamento ou ligação anotados, ensaios relacionados a proteínas e RNA, experimentos de resgate e ensaios funcionais, com níveis complementares que distinguem combinações de métodos. Para contextualizar as MTIs, o RNA2Immune as posiciona em contextos de células imunes e doenças. A harmonização das anotações de miRNAs é garantida pela integração com Rfam 15.0 e miRBase v23, e o NPInter v5.0 conecta reguladores de RNA não codificadores a redes de miRNA-alvo.

Um avanço notável é a implementação de um fluxo de trabalho de curadoria assistido por Inteligência Artificial, utilizando o modelo Qwen3.6-27B. Este modelo auxilia na curadoria de texto completo e baseada em figuras, com verificação humana subsequente, otimizando a eficiência e a precisão da coleta de dados. A plataforma foi redesenhada utilizando Django e Nginx, garantindo operação segura, implantação estável e acesso responsivo a buscas ranqueadas por evidência, navegação contextual, visualização de redes e download de dados em larga escala.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com múltiplas linhas de pesquisa do LaBiOmicS, com um foco proeminente na **Transcriptômica e Expressão Gênica** e na **Biologia Computacional e IA**.

Na linha de **Transcriptômica e Expressão Gênica**, o miRTarBase 11.0 é um recurso indispensável. Ele permite a exploração aprofundada de redes de co-expressão de miRNAs e seus genes-alvo, a identificação de novos lncRNAs que podem modular a atividade de miRNAs (através da integração com NPInter), e a descoberta de potenciais biomarcadores baseados em padrões de regulação pós-transcricional. A capacidade de distinguir diferentes tipos de evidência experimental é crucial para a validação e interpretação de dados de RNA-Seq e outras abordagens transcriptômicas.

Em relação à **Biologia Computacional e IA**, o projeto exemplifica o desenvolvimento e a aplicação de algoritmos e ferramentas de ponta. O sistema de pontuação baseado em regras para MTIs, o processamento em larga escala de dados AGO-CLIP, a integração complexa de múltiplas fontes de dados e, notavelmente, a implementação de um fluxo de trabalho de curadoria assistido por modelos de linguagem de IA (Qwen3.6-27B), demonstram a aplicação de machine learning e deep learning para resolver desafios de curadoria de dados em bioinformática. A arquitetura da plataforma baseada em Django e Nginx também reflete o compromisso com o desenvolvimento de ferramentas computacionais robustas e escaláveis, essenciais para o processamento e análise de dados ômicos em larga escala.
