---
layout: post
title: "TFRegDB v2.0: Curadoria Computacional e Integração Ômica de Domínios Efetores de Fatores de Transcrição Humanos para a Genômica Funcional"
date: 2026-11-26 08:00:00 -0300
categories: ["bioinformatica", "ia-em-biologia"]
tags: ["transcription-factors", "effector-domains", "database", "language-models", "alphafold"]
journal: "Nucleic acids research"
doi: "10.1093/nar/gkag1248"
original_url: "https://doi.org/10.1093/nar/gkag1248"
original_title: "TFRegDB v2.0: an integrated database of human transcription factor effector domains"
authors: "Carmen-Sifuentes S, Munoz-Esquivel G, Hualpa-Rodriguez PF, Plaza E, Andaluz A, et al."
year: 2026
---

A compreensão da regulação gênica é fundamental para desvendar os mecanismos biológicos e patológicos. Os fatores de transcrição (TFs) desempenham um papel central nesse processo, reconhecendo sequências de DNA específicas através de seus domínios de ligação ao DNA. No entanto, a capacidade de um TF em ativar ou reprimir a transcrição depende intrinsecamente de seus domínios efetores. Historicamente, o mapeamento desses domínios tem sido um desafio, realizado predominantemente por ensaios de repórter de baixa vazão, resultando em anotações dispersas e fragmentadas em uma vasta literatura. Essa lacuna de conhecimento e o gargalo computacional na consolidação e integração desses dados impedem uma análise sistêmica da função dos TFs e do impacto de isoformas alternativas e variações genéticas na regulação gênica. A necessidade de uma base de dados centralizada, abrangente e curada, que integre dados experimentais e computacionais de domínios efetores de TFs humanos, motivou o desenvolvimento do TFRegDB v2.0.

### O Pipeline, Algoritmo ou Abordagem Computacional

O TFRegDB v2.0 representa um avanço significativo na curadoria e integração de dados de domínios efetores de fatores de transcrição humanos. A abordagem metodológica empregada combinou o poder da inteligência artificial com a rigorosa validação manual. Inicialmente, foi realizada uma triagem assistida por modelos de linguagem (AI) da literatura científica publicada, permitindo a identificação em larga escala de informações relevantes sobre domínios efetores. Cada registro identificado por este processo foi submetido a uma verificação manual meticulosa, garantindo a alta qualidade e confiabilidade dos dados. Posteriormente, essas anotações curadas foram mescladas com dados de mapeamento de domínios de alta vazão, consolidando um compêndio robusto.

O resultado é uma base de dados que compreende 5277 relatórios de domínios experimentalmente suportados, abrangendo 1268 TFs humanos de 64 famílias, curados a partir de 1072 publicações. Esta versão representa uma expansão de 8.7 vezes em relação ao compêndio anterior. Para cada anotação de domínio de ativação e repressão, o TFRegDB v2.0 fornece uma riqueza de informações integradas, incluindo: modelos estruturais pré-computados gerados pelo AlphaFold; dados de conservação por resíduo em resolução de aminoácidos e nucleotídeos; previsões computacionais de função; motivos lineares curtos (SLiMs); perfis biofísicos e de desordem; modificações pós-traducionais (PTMs); variantes de linhagem germinativa; e a estrutura éxon-íntron que codifica o domínio. Essa integração de dados permite aos usuários avaliar como isoformas alternativas e variações genéticas podem comprometer a integridade e a função dos domínios efetores. O TFRegDB v2.0 é livremente acessível através de um portal interativo, uma REST API pública e downloads em massa, e aceita anotações submetidas pela comunidade para futuras atualizações.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha de forma intrínseca e multifacetada com diversas linhas de pesquisa do LaBiOmicS, evidenciando o papel central da bioinformática e da biologia computacional.

Primeiramente, a metodologia empregada no TFRegDB v2.0 dialoga diretamente com a linha **Biologia Computacional e IA**. A utilização de modelos de linguagem para a triagem assistida da literatura e a integração de modelos estruturais do AlphaFold demonstram a aplicação de algoritmos avançados e ferramentas de inteligência artificial para a curadoria e enriquecimento de dados biológicos em larga escala. Este é um exemplo paradigmático de como o desenvolvimento e a aplicação de IA podem transformar a forma como organizamos e interpretamos informações complexas.

Em segundo lugar, a curadoria detalhada e a anotação dos domínios efetores, incluindo a estrutura éxon-íntron e a incorporação de variantes genéticas, estabelecem uma forte conexão com a linha **Genômica Estrutural e Funcional**. Ao fornecer insights sobre como a variação genômica e as isoformas alternativas afetam a integridade e a função regulatória dos TFs, o TFRegDB v2.0 é uma ferramenta valiosa para a compreensão da arquitetura e da função do genoma humano.

Por fim, ao elucidar os mecanismos de ativação e repressão transcricional e ao integrar dados que permitem a avaliação do impacto de isoformas e variantes, a TFRegDB v2.0 contribui significativamente para a linha **Transcriptômica e Expressão Gênica**. Esta base de dados oferece um recurso fundamental para a identificação de biomarcadores, a análise de redes de co-expressão e a compreensão aprofundada das complexas redes regulatórias que governam a expressão gênica.
