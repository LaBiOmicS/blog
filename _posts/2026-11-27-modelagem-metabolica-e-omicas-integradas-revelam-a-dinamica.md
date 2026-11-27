---
layout: post
title: "Modelagem Metabólica e Ômicas Integradas Revelam a Dinâmica da Biotransformação de Bisfenol A em Microcosmo de Lodo Ativado"
date: 2026-11-27 08:00:00 -0300
categories: ["bioinformatica", "metagenomica"]
tags: ["metagenomica", "metatranscriptomica", "gsmm", "mags", "microbioma"]
journal: "The ISME journal"
doi: "10.1093/ismejo/wrag294"
original_url: "https://doi.org/10.1093/ismejo/wrag294"
original_title: "Community-level bisphenol A biotransformation in an activated sludge microcosm"
authors: "Wu Y, Liang Y, Cui J, Jiang L, Zeng X, et al."
year: 2026
---

A contaminação ambiental por bisfenol A (BPA), um desregulador endócrino amplamente utilizado, representa um desafio significativo para a saúde pública e ecossistemas. Embora a biotransformação microbiana seja uma via crucial para a remoção do BPA, a compreensão detalhada dos mecanismos e da dinâmica em nível de comunidade microbiana permanece limitada. A complexidade das interações metabólicas e a necessidade de integrar dados de diversas plataformas ômicas para desvendar os atores e as rotas de degradação constituem um gargalo computacional. Este estudo aborda essa lacuna, empregando uma abordagem bioinformática e computacional multifacetada para elucidar as vias de biotransformação do BPA e as interações microbianas em um microcosmo de lodo ativado, fornecendo insights cruciais sobre o destino ambiental desse poluente.

### O Pipeline, Algoritmo ou Abordagem Computacional

Para desvendar a biotransformação do BPA em nível de comunidade, o estudo empregou um pipeline integrativo de bioinformática e biologia computacional. Inicialmente, a técnica de **Sondagem de Isótopos Estáveis de DNA (DNA-SIP)** com 13C-BPA foi utilizada para identificar os microrganismos metabolicamente ativos na degradação. O DNA enriquecido com 13C foi sequenciado, e análises bioinformáticas de composição taxonômica e abundância diferencial foram aplicadas para pinpointar os táxons degradadores.

Concomitantemente, foram realizadas **Metagenômica** e **Metatranscriptômica** de shotgun. Os dados metagenômicos foram processados para montagem de genomas (utilizando ferramentas como MEGAHIT ou metaSPAdes), binning para a reconstrução de **Genomas Montados a partir de Metagenomas (MAGs)** (com ferramentas como MaxBin ou MetaBAT) e anotação funcional (via eggNOG, KEGG, etc.) para caracterizar o potencial metabólico da comunidade. Os dados metatranscriptômicos, por sua vez, foram mapeados aos MAGs e genes anotados (com ferramentas como HISAT2 ou STAR, e quantificação via Salmon ou Kallisto) para avaliar a expressão gênica diferencial, revelando quais genes e vias estavam ativamente transcritos durante a biotransformação do BPA.

O ponto culminante da abordagem computacional foi a aplicação de **Modelagem Metabólica em Larga Escala (GSMM)**, guiada pelos dados metatranscriptômicos. Modelos de redes metabólicas foram construídos para os MAGs identificados, permitindo a simulação de fluxos metabólicos e a predição de interações interespécies, como a troca de metabólitos. A metatranscriptômica foi crucial para refinar e constranger esses modelos, inferindo como MAGs não degradadores poderiam suportar a comunidade fornecendo metabólitos essenciais, enquanto os degradadores alteravam seu perfil metabólico de captação para secreção de metabólitos durante o processo. A espectrometria de massas de alta resolução complementou essas análises, validando as rotas de degradação inferidas computacionalmente e identificando metabólitos intermediários.

### Conexão com as Linhas de Pesquisa do LaBiOmicS

Este trabalho se alinha intrinsecamente com diversas linhas de pesquisa do LaBiOmicS, demonstrando a centralidade da bioinformática e biologia computacional:

*   **Metagenômica e Resistoma:** A utilização de sequenciamento shotgun para metagenômica e a subsequente mineração de genomas (MAGs) para caracterizar a composição e o potencial funcional da comunidade microbiana no lodo ativado são pilares desta linha. A identificação de táxons-chave e genes envolvidos na biotransformação de BPA, como os genes `cyp` em Sphingomonadaceae, exemplifica a análise funcional de comunidades complexas.
*   **Transcriptômica e Expressão Gênica:** A aplicação de metatranscriptômica para monitorar a expressão gênica em tempo real durante a degradação do BPA é fundamental. A identificação de genes up-regulados e a inferência de cooperação metabólica entre diferentes guilds bacterianas, baseada em seus perfis de expressão, dialogam diretamente com a análise de redes de co-expressão e a busca por biomarcadores de atividade metabólica.
*   **Microbioma e Viroma:** A caracterização aprofundada da ecologia microbiana do lodo ativado, a identificação dos principais degradadores (Sphingomonadaceae, Rhizobiaceae e Comamonadaceae) e a elucidação das interações metabólicas entre os membros da comunidade são aspectos centrais desta linha. O estudo fornece um modelo para entender como comunidades microbianas complexas respondem e se adaptam a estressores ambientais.
*   **Biologia Computacional e IA:** A aplicação de Modelagem Metabólica em Larga Escala (GSMM) representa uma abordagem sofisticada de biologia computacional para simular e prever o comportamento de sistemas biológicos complexos. A integração de dados metatranscriptômicos para guiar e validar esses modelos ilustra o desenvolvimento e a aplicação de modelos computacionais avançados para desvendar mecanismos biológicos, um foco primordial desta linha de pesquisa.
