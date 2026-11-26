---
layout: post
title: "Bulk2SC: Desvendando a Resolução de Célula Única em Dados RNA-seq Bulk com Autoencoders Variacionais de Mistura Gaussiana"
date: 2026-11-26 08:00:00 -0300
categories: ["transcriptomica", "ia-em-biologia"]
tags: ["scrna-seq", "rna-seq-bulk", "autoencoder-variacional", "ia-generativa", "desconvolucao-celular"]
journal: "PLoS computational biology"
doi: "10.1371/journal.pcbi.1014979"
original_url: "https://doi.org/10.1371/journal.pcbi.1014979"
original_title: "Generating scRNA-seq data from bulk RNA-seq using a Gaussian mixture variational autoencoder"
authors: "Kim M, Williams CM, Xiong G, Cho HJ, Siadaty S, et al."
year: 2026
---

A transcriptômica de célula única (scRNA-seq) revolucionou nossa compreensão da heterogeneidade celular, fornecendo perfis de expressão gênica em resolução sem precedentes. No entanto, a scRNA-seq permanece uma tecnologia dispendiosa e com amostras limitadas, mesmo em estudos extensivos de doenças humanas. Em contraste, os dados de RNA-seq bulk são abundantes, mas perdem detalhes específicos de células ao fornecer uma média da expressão gênica em todas as populações celulares. Essa lacuna entre a riqueza de dados bulk e a necessidade de resolução de célula única representa um gargalo computacional significativo. Embora modelos de IA generativa tenham sido desenvolvidos para expandir conjuntos de dados scRNA-seq existentes ou inferir dados espaciais, faltava uma ferramenta dedicada à geração representativa de dados scRNA-seq completos a partir de dados RNA-seq bulk.

### O Pipeline, Algoritmo ou Abordagem Computacional
Para preencher essa lacuna, foi desenvolvido o Bulk2SC, uma estrutura modular inovadora que capitaliza o poder das abordagens de IA generativa e dados scRNA-seq existentes para sintetizar dados scRNA-seq representativos a partir de amostras bulk. No cerne do Bulk2SC está um **autoencoder variacional de mistura gaussiana (GMVAE)**. Este modelo de IA generativa é treinado para aprender as distribuições subjacentes da expressão gênica em nível de célula única, utilizando dados scRNA-seq de referência e informações sobre as proporções de tipos celulares inferidas de dados bulk (obtidas por qualquer ferramenta de desconvolução de tipos celulares).

O fluxo de trabalho do Bulk2SC envolve:
1.  **Inferência de Proporções Celulares**: Utiliza ferramentas existentes para estimar as proporções de diferentes tipos celulares presentes na amostra RNA-seq bulk.
2.  **Treinamento do GMVAE**: O GMVAE é treinado com um conjunto de dados scRNA-seq de referência, aprendendo a mapear as características de expressão gênica de cada tipo celular para um espaço latente.
3.  **Geração de scRNA-seq Sintético**: Com base nas proporções celulares inferidas do RNA-seq bulk e no modelo GMVAE treinado, o Bulk2SC gera um conjunto de dados scRNA-seq sintético que reflete a composição celular e os perfis de expressão da amostra bulk original, mas com a resolução de célula única.

A modularidade do Bulk2SC é uma de suas forças, permitindo a integração flexível com diversas ferramentas de predição de proporções celulares e sua implementação em frameworks computacionais mais amplos. A validação demonstrou o desempenho superior do Bulk2SC em comparação com ferramentas que geram scRNA-seq a partir de bulk como parte de frameworks computacionais mais amplos, utilizando conjuntos de dados publicados de múltiplos tipos de tecido e um conjunto de dados de desconvolução de benchmark com dados pareados de bulk e single-nucleus RNA-seq.

### Conexão com as Linhas de Pesquisa do LaBiOmicS
Este trabalho se alinha diretamente com múltiplas linhas de pesquisa do LaBiOmicS. Primeiramente, a abordagem é fundamental para a **Transcriptômica e Expressão Gênica**, pois visa superar as limitações da RNA-seq bulk para obter insights sobre a expressão gênica em nível de célula única, o que é crucial para a identificação de biomarcadores e a compreensão de redes de co-expressão específicas de tipos celulares. Em segundo lugar, e de forma proeminente, o desenvolvimento do Bulk2SC é um exemplo clássico da **Biologia Computacional e IA**, envolvendo a concepção e aplicação de um algoritmo de aprendizado de máquina avançado (autoencoder variacional de mistura gaussiana) para resolver um problema biológico complexo de geração de dados. A utilização de modelos de IA generativa para inferir e sintetizar dados ômicos de alta resolução a partir de dados de menor resolução é um pilar central desta linha de pesquisa. Finalmente, a ênfase na modularidade e no benchmarking rigoroso do desempenho do Bulk2SC ressoa com a linha de **Reprodutibilidade e Replicabilidade**, promovendo a criação de ferramentas robustas e validáveis para a comunidade científica.
