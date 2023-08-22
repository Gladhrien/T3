# Alunos:
* Eduarda Carvalho Waechter - 00304585 - Turma A
* Giulia Chimini Stefainski - 00289108 - Turma A
* Matheus Henrique Sabadin  - 00228729 - Turma A

# Tic-tac-toe misere
## (i) O minimax sempre ganha do randomplayer? 
Não. Em 20 partidas rodadas, houveram 13 ganhos e 7 empates, o que, em uma estatística muito simplificada, gira em torno 53,8% de ganho para o minimax.

## (ii) O minimax sempre empata consigo mesmo? 
Aparentemente sim. Houve empate em todas partidas de uma amostragem de 20 rodadas.

## (iii) O minimax sempre empata contra as jogadas perfeitas recomendadas pelo https://nyc.cs.berkeley.edu/uni/games/ttt/variants/misere ? Para verificar isso, use o humanplayer. No link, faça as jogadas do minimax, e no servidor do kit, faça as jogadas recomendadas (amarelo ou verde) do link.
Sim. De 10 partidas jogadas, todas resultaram em um empate com o minimax fazendo uma das jogadas sugeridas pelo site.

## Othello:
Para o Othello, faça um mini-torneio entre os algoritmos. Observe e relate qual implementação foi a mais bem-sucedida.
* descrição da função de avaliação customizada;
* descrição do critério de parada (profundidade máxima fixa? aprofundamento iterativo?)
* implementação escolhida para o torneio e se houve implementação de alguma melhoria no minimax ou no MCTS.

## Feedback:
# Quão fácil ou difícil foi realizar o trabalho? como foi trabalhar com o auxílio da IA? quais sugestões teria para melhorar o trabalho?
* O trabalho foi relativamente difícil de ser realizado essencialmente por uma questão de prazo e conflito de obrigações com outras matérias do que pelo conteúdo em si. Uma sugestão é que este trabalho (e talvez o conteúdo) fosse adiantado para um período anterior do semestre e fosse deixado um trabalho mais simples para o final.
* Quanto às ferramentas de IA, houve algum auxílio do GitHub Copilot, do GitHub Copilot Chat e do ChatGPT. O GitHub Copilot Chat e o ChatGPT foram muito úteis no auxilío de aspectos em que tipicamente não há problemas em uma linguagem fortemente tipada (erros em tipos, passagem de argumentos, etc.), os quais em linguagens fortemente tipadas normalmente são notificados durante a compilação, mas que em python só acabam sendo descobertos em runtime. 
O GitHub Copilot foi muito útil para a implementação de linhas simples de código, em que se sabia a estrutura de dados que se desejava implementar, mas não se dominava a sintaxe para tal. 
Para a avaliação de corretude dos algoritmos estas ferramentas não foram tão precisas, indicando muitas vezes que os algoritmos estavam coerentes quando na verdade haviam pequenos erros que não permitiam a execução. 