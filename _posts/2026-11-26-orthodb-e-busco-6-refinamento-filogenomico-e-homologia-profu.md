---
layout: post
title: "OrthoDB e BUSCO 6: Refinamento Filogenômico e Homologia Profunda Impulsionados por Modelos de Linguagem de Proteínas e IA"
date: 2026-11-26 08:00:00 -0300
categories: ["bioinformatica", "ia-em-biologia"]
tags: ["orthodb", "busco", "filogenomica", "modelos-de-linguagem-de-proteinas", "mags"]
journal: "Nucleic acids research"
doi: "10.1093/nar/gkag1250"
original_url: "https://doi.org/10.1093/nar/gkag1250"
original_title: "OrthoDB and BUSCO update: broader phylogenomic sampling, deeper homology searches, and AI-agent support"
authors: "Kriventseva EV, Tegenfeldt F, Kuznetsov D, Manni M, Berkeley M, et al."
year: 2026
---

A identificação precisa de ortólogos é um pilar fundamental para a inferência funcional e evolutiva em genômica comparativa. No entanto, o desafio de detectar homologia remota entre sequências altamente divergentes, especialmente em linhagens eucarióticas basais e em genomas recém-sequenciados ou incompletos como os Metagenome-Assembled Genomes (MAGs), representa um gargalo computacional significativo. A complexidade e o volume crescentes dos dados ômicos exigem abordagens bioinformáticas cada vez mais sofisticadas para garantir a cobertura e a acurácia das anotações, bem como a integração de novas tecnologias como a inteligência artificial para otimizar esses processos.

### O Pipeline, Algoritmo ou Abordagem Computacional

Esta atualização do OrthoDB (https://www.orthodb.org) e BUSCO (https://busco.ezlab.org) representa um avanço substancial na anotação evolutiva e funcional de genes ortólogos. A recomputação dos grupos ortólogos (OGs) foi realizada *de novo* utilizando o OrthoLoger, que se baseia em buscas de homologia candidatas do MMseqs2 com parâmetros otimizados. Para superar a dificuldade de recuperar homologia remota, particularmente na raiz dos Eukaryota e entre sequências de protistas divergentes, os pesquisadores empregaram o The Embedded Alphabet (TEA) – um alfabeto derivado de modelos de linguagem de proteínas. Esta inovação computacional resultou em um aumento significativo na atribuição de OGs e uma melhor representação de ortólogos menos divergentes, aprimorando a sensibilidade das buscas.

Os datasets de linhagem do BUSCO foram reconstruídos para eucariotos, incorporando uma amostragem de espécies mais ampla e uniformemente distribuída. Essa melhoria é crucial para estender o valor do BUSCO na avaliação da completude de genomas, especialmente para Metagenome-Assembled Genomes (MAGs) e eucariotos microbianos, onde a representatividade taxonômica é vital. Adicionalmente, a interface web do OrthoDB foi aprimorada com a inclusão de um assistente conversacional com links para fontes e uma camada de Model Context Protocol, que expõe *endpoints* de API públicos para agentes de IA externos. A acessibilidade das ferramentas e dados é mantida através da interface web, downloads em massa, REST, SPARQL/RDF, e pacotes para Python e R/Bioconductor, promovendo a integração em diversos workflows bioinformáticos.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha diretamente com diversas linhas de pesquisa do LaBiOmicS, reforçando o princípio fundamental de que a bioinformática é o elo principal de todas as análises:

*   **Genômica Estrutural e Funcional & Mitogenômica:** A recomputação de OGs e a anotação de 5768 genomas eucarióticos, incluindo 132 genomas de mamíferos reanotados com Tiberius, são cruciais para a anotação gênica e a compreensão da variação e evolução genômica. A identificação precisa de ortólogos é a base para inferir funções e relações evolutivas entre genes e genomas.

*   **Metagenômica e Resistoma:** A extensão do valor dos datasets BUSCO para Metagenome-Assembled Genomes (MAGs) é de suma importância. A capacidade de avaliar a completude e a qualidade de MAGs é essencial para a mineração de genomas e a caracterização de comunidades microbianas, incluindo a identificação de genes de resistência a antimicrobianos (ARGs) e elementos genéticos móveis (MGEs) em ambientes complexos.

*   **Biologia Computacional e IA:** O uso de modelos de linguagem de proteínas (TEA) para buscas de homologia profunda e a integração de agentes de IA na interface web do OrthoDB demonstram um compromisso com o desenvolvimento e aplicação de algoritmos avançados e técnicas de *machine learning* e *deep learning* na biologia. A exposição de APIs para agentes de IA externos abre novas avenidas para a automação e análise inteligente de dados ômicos.

*   **Reprodutibilidade e Replicabilidade:** A disponibilidade de OrthoDB e BUSCO como ferramentas de código aberto, juntamente com a acessibilidade via APIs, Python e R/Bioconductor, facilita a integração em workflows robustos e reprodutíveis. Isso é fundamental para o *benchmarking* e a promoção da ciência aberta, permitindo que outros pesquisadores validem e estendam os achados.
