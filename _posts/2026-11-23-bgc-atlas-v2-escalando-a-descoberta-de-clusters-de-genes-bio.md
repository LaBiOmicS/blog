---
layout: post
title: "BGC Atlas v2: Escalando a Descoberta de Clusters de Genes Biossintéticos através de Contextualização Taxonômica e Ambiental em Larga Escala"
date: 2026-11-23 08:00:00 -0300
categories: ["bioinformatica", "metagenomica"]
tags: ["biosynthetic-gene-clusters", "metagenomica", "bancos-de-dados", "genomica-microbiana", "produtos-naturais"]
journal: "Nucleic acids research"
doi: "10.1093/nar/gkag1174"
original_url: "https://doi.org/10.1093/nar/gkag1174"
original_title: "BGC Atlas v2: biosynthetic gene clusters with taxonomic and environmental context at scale"
authors: "Bağcı C, Talamás-Tanner A, Ziemert N"
year: 2026
---

A vasta e inexplorada diversidade de metabólitos secundários produzidos por microrganismos representa uma fonte inestimável de compostos com aplicações biotecnológicas e farmacêuticas. Contudo, a caracterização experimental de uma pequena fração desse potencial biossintético é um gargalo significativo. O desafio reside em desenvolver abordagens computacionais capazes de identificar, anotar e contextualizar Clusters de Genes Biossintéticos (BGCs) em larga escala, integrando informações genômicas e ambientais para desvendar as interações microbianas e acelerar a descoberta de novos produtos naturais.

### O Pipeline, Algoritmo ou Abordagem Computacional
O BGC Atlas v2 representa um avanço computacional robusto para enfrentar o desafio da exploração de BGCs em larga escala. A plataforma expandiu sua coleção em mais de oito vezes, totalizando mais de 16 milhões de BGCs preditos. Essa expansão foi possível pela integração de dados provenientes de diversas fontes genômicas, incluindo montagens metagenômicas, Genomas Montados a partir de Metagenomas (MAGs), Genomas de Amplificação Única (SAGs) e genomas de isolados.

A metodologia bioinformática empregada no BGC Atlas v2 foca na contextualização abrangente dos BGCs. Isso inclui:
- **Atribuição Taxonômica em Larga Escala:** Quase todos os BGCs receberam atribuições taxonômicas precisas, um feito que requer pipelines eficientes de classificação taxonômica integrados a bancos de dados de referência.
- **Harmonização de Metadados Ambientais:** A padronização e integração de metadados ambientais associados aos BGCs permitem análises contextuais aprofundadas, revelando a distribuição e a relevância ecológica desses clusters.
- **Funcionalidades de Busca Aninhada:** A plataforma oferece capacidades de busca sofisticadas, permitindo consultas cruzadas e aninhadas baseadas em propriedades biossintéticas, taxonômicas, ambientais e geográficas. Isso é viabilizado por um sistema de indexação e recuperação de dados otimizado para grandes volumes.
- **Busca por Sequências de Proteínas:** Usuários podem realizar buscas por sequências de proteínas contra genes codificados nos BGCs, facilitando a identificação de homólogos e a inferência funcional.

A escala do BGC Atlas v2 não apenas catalisa a descoberta de produtos naturais, mas também revela a vasta diversidade biossintética bacteriana e arqueal que permanece inexplorada, sublinhando a importância de abordagens computacionais para mapear esse potencial.

### Conexão com as Linhas de Pesquisa do LaBiOmicS
Este trabalho se alinha diretamente com diversas linhas de pesquisa do LaBiOmicS, com destaque para:

- **Metagenômica e Resistoma:** A integração massiva de BGCs provenientes de montagens metagenômicas e MAGs é central para a linha de Metagenômica e Resistoma, que busca minerar genomas microbianos em larga escala para identificar elementos genéticos de interesse. A metodologia de contextualização de BGCs pode ser análoga à identificação e caracterização de Genes de Resistência a Antimicrobianos (ARGs) e Elementos Genéticos Móveis (MGEs) em comunidades microbianas.

- **Biologia Computacional e IA:** O desenvolvimento do BGC Atlas v2, com sua capacidade de processamento em larga escala de dados ômicos, integração de diversas fontes de dados, e funcionalidades de busca avançadas, exemplifica o foco da linha de Biologia Computacional e IA. A criação de uma ferramenta robusta e escalável para a análise de BGCs demonstra o desenvolvimento de algoritmos e ferramentas computacionais essenciais para a bioinformática moderna.

- **Genômica Estrutural e Funcional:** A inclusão de BGCs de genomas de isolados e SAGs contribui para a compreensão da genômica funcional, permitindo a anotação gênica e a exploração da variação biossintética em diferentes linhagens microbianas.
