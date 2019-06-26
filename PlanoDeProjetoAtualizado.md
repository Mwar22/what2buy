# PLANO DE PROJETO
## CONTROLE DE ESTOQUE (What2buy)


### Histórico de Alterações
 
Data           |   Versão   |        Descrição     |   Responsável
---------------|------------|----------------------|----------------
07/06/2019     |     1.0    | Desenvolvimento      | Paula Fabiana 
08/06/2019     |     1.0    | Desenv e Modificação | Lucas de Jesus
09/06/2019     |     1.0    | Desenv e Modificação |   Miguel
09/06/2019     |     1.0    | Desenv e Modificação |  Vitor Rafael
09/06/2019     |     1.0    | Desenv e Modificação |  Fábio Jr
11/06/2019     |     1.0    |    Modificação       | Paula Fabiana
11/06/2019     |     1.0    |    Modificação       | Lucas de Jesus
25/06/2019     |     1.0    |    Modificação       | Paula Fabiana






### Introdução

Este documento fornece uma visão abrangente do projeto what2buy, um aplicativo de controle de estoque que visa  auxiliar o seu usuário no que diz respeito ao controle de mantimentos de sua residência, buscando proporcionar uma gestão mais simples e eficaz dos produtos básicos e as respectivas quantidades. O presente documento destina-se ao gerente de projeto, para acompanhar o andamento do mesmo em relação ao cronograma, e aos desenvolvedores do projeto, utilizando-o para entender o que e quais atividades fazer. Este documento provê uma visão abrangente do projeto sem se aprofundar nos detalhes das
iterações, que serão melhor definidas ao longo do processo de desenvolvimento. Nele são apresentados: a metodologia de desenvolvimento , a descrição e os objetivos do projeto, as métricas aplicadas, os objetivos das iterações, o cronograma e os produtos do desenvolvimento, a equipe de desenvolvimento e o processo de homologação, seguindo o MPS-BR nível G com a utilização do Scrum. 

2. Escopo do trabalho

-E1;
-E2;
-E3;
-E4;
-E5;
-E6.

3. Dimensionamento de tarefas e produtos de trabalho
 Para mensurar a complexidade em cada requisito, foi utilizado a sequência de Fibonacci, colocando um valor em cada requisito (estória).
 Em que um ponto equivale a quantidade de horas gasta  no desenvolvimento de cada estória, ex: 1 ponto equivale a 2 horas. 


- Estória 2: 1 ponto;
- Estória 5: 1 ponto;
- Estória 4: 2 pontos;
- Estória 1: 3 pontos;
- Estória 3: 5 pontos
- Estória 6: 8 pontos; 

4. Modelo e as fases do ciclo de vida do projeto
O modelo utilizado possui uma abordagem iterativa incremental. Com fases: Pré-game, Game e Post-game.
5. Estimativa de esforço e o custeio baseado em dados históricos ou referências técnicas
Nessa etapa é utilizada o ROI (Retorno sobre o Investimento).
ROI = ((GANHO OBTIDO – GASTOS x 100) / GASTOS)
Com estimativas através de Story Points e divisão de itens em tarefas
 
6. O orçamento e o cronograma do projeto
 Esta etapa define  em essência, como se dará o planejamento da Sprint, o qual será efetuado com base em dois pontos essenciais: 
 Como e O quê fazer.  A Primeira parte do planejamento (Também conhecida como  Sprint Planning 1) 
 concentra-se na seleção de itens preparados (Ready)  trazidos pelo cliente/usuário. Isto encerra questões remanescentes
 e define  a meta da Sprint. A Segunda parte do planejamento da Sprint (Sprint Planning 2) concentra-se na criação de
 um plano de trabalho, definindo os  estados de  “Pronto” para cada item, e lhes atribuindo uma estimativa através de story points.   

Nome da tarefa                                        |     Duração   |    Início   |   Final 
------------------------------------------------------|---------------|-------------|----------
O sistema permita o cadastro de produtos              |     4 horas   |    23/06    |    23/06
O sistema permita remoção de produtos                 |     6 horas   |    24/06    |    25/06
O sitema permita a inserção da quantidade de produtos |     6 horas   |    24/06    |    25/06



7. Riscos do projeto
Através de reuniões diárias de duração aproximada de 10 minutos (Daily Meeting) entre o time de desenvolvimento,
empecilhos para a produção dos requisitos são definidos e classificados segundo os seguintes  graus de dificuldade:

[1] Baixa
[2] Média
[3] Alta

Em que o índice que tem o maior valor de prioridade, vai ser o que terá o maior foco no desenvolvimento do produto. 

Risco                                                       | Probabilidade |  Impacto|    Prioridade
------------------------------------------------------------|---------------|---------|-------------------
Complexidade do requisito                                   |    2          |   3     |         6
Definição de cronograma não realística                      |    2          |   3     |         6
Qualidade do produto não atinge a expectativa do cliente    |    2          |   1     |         2
Falta de compromentimento e má gerência                     |    3          |   3     |         9    
 
 
8. Planejamento de recursos humanos
Nesta etapa é definida a distribuição dos recursos humanos (Time, Product Owner, Scrum Master) 
baseando-se nos perfis  definidos no documento de visão.

 Membro               |       Papel   | Conhecimento para o projeto       |Horas para aprendizado
----------------------|---------------|-----------------------------------|-----------------------
Fábio Jr              |Desenvolvedor  |   Plataforma kivy, GitHub, Pyhton |  36 horas
Lucas de Jesus        |Desenvolvedor  |   Plataforma kivy                 |  40 horas
Miguel                |Desenvolvedor  |   Plataforma kivy, GitHub         |  10 horas
Paula Fabiana         |Desenvolvedor  |   Plataforma kivy, GitHub, Pyhton |  60 horas
Vitor Rafael          |Desenvolvedor  |   Plataforma kivy, GitHub, Pyhton |  30 horas


9. Planejamento das tarefas, os recursos e o ambiente de trabalho
Nesta etapa os itens são adicionais ao Backlog do produto e às Tarefas da Sprint (Task).

Configuração mínima para desenvolvimento do projeto |Software utilizado para desenvolvimento |Configuração mínima do dispositivo para rodar o software
----------------------------------------------------|----------------------------------------|---------------------------------------------------------
Intel(R) Core(TM)i3-6100U CPU @ 2.30GHz 4096 MB RAM | Python, kivy, IDLE/Gedit, Git          |  Android 4.0 , 1000 MB RAM

 
10. Planejamento de dados relevantes do projeto (armazenamento, privacidade e segurança)
https://github.com/Mwar22/what2buy
 

 11. Planos para a execução do projeto
  Nessa etapa ocorre uma visão geral do produto.

- Product Backlog
Trata-se de uma lista definida pelo time de desenvolvimento segundo os requisitos adequados às necessidades do cliente.
Deve  contém todas os requisitos  desejados para o software:

Notificação ao usuário quando ocorrer falta de produtos (1);
Notificação quando a data de validade do produto está próxima (2);
Notificação ao usuário com base nos dados de aquisição de produtos anteriores (3);
O sistema permite o isolamento de determinados produtos em um conjunto mínimo (4);
Lista básica com os produtos mais comuns (5);
O sistema permite a inserção de uma lista de produtos, com a quantidade de cada item (6).

-Sprint planning 1
Reunião realizada entre o cliente/Product Owner e o time de desenvolvimento.
Tem como objetivo permitir que o time de desenvolvedores realize uma investigação mais profunda dos desejos  do cliente/usuário. Isto garante que o resultado de cada fase seja mais coerente com os  resultados desejados.
Possui duração de 1 à 2 horas

- Sprint planning 2
Reunião realizada somente entre os desenvolvedores. 
Expande o problema (estória) compreendido na Sprint planning 1, isto é, acontece a quebra técnica dos itens em tarefas. Neste momento o time estima os itens e tarefas do Sprint Backlog
Possui duração de 2 à 3 horas

- Sprint Backlog
Trata-se de uma tabela que codifica os resultados da divisão/especificação definidas na Sprint planning 2.

- Daily meeting
Reuniões diárias de 10 min.  Tem como objetivo responder às seguintes perguntas: O quê já foi feito?, O quê faremos neste momento? e Quais são os empecilhos atrapalham nossos objetivos?
 
12. Avaliação de viabilidade de atingir as metas do projeto
Sprint Planning (1 e 2) e definição do objetivo da iteração na elaboração da Sprint Backlog (A Sprint Backlog utilizá horas para estimar tarefas em vez de pontos de história).

13. Revisão e compromisso com o Plano do Projeto
Através das reuniões diárias (Daily meeting), melhora-se a comunicação e o engajamento da equipe, corrigindo os rumos, mitigando os riscos e ainda proporcionando o uso dos 3 pilares do Scrum: inspeção (do progresso),  adaptação (ajustes e impedimentos) e transparência (todos sabem o que está acontecendo).

14. Monitoramento de progresso do projeto
Nesta etapa é feito um Product Burndown/Sprint Burndown, onde gráficos são usados para rastrear o progresso da equipe de desenvolvimento. Ele mostra como a equipe está completando cada sprint, e auxilia na previsão de término de um produto.
Ao final de cada Sprint, realiza-se uma reunião (Sprint review) onde o time de desenvolvimento mostra o que foi alcançado durante a Sprint.  O projeto é portanto avaliado em relação aos objetivos da Sprint, os quais são  determinados durante a Sprint planning. Idealmente, a equipe completaria cada um dos itens do Backlog do produto trazidos para fazer parte do Sprint, entretanto o essencial  é que a equipe atinja o objetivo geral da Sprint.
Também realiza-se a Sprint Retrospective, um evento que ocorre ao final de uma Sprint e serve para identificar o que funcionou bem, o que pode ser melhorado e quais ações serão tomadas no próximo ciclo de desenvolvimento induziram melhoras.
