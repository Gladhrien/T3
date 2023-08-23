# Alunos:
* Eduarda Carvalho Waechter - 00304585 - Turma A
* Giulia Chimini Stefainski - 00289108 - Turma A
* Matheus Henrique Sabadin  - 00228729 - Turma A

# Agente MARIA
Monte-carlo-minimax
Advanced
Recursive
Ingenious
Algorithm

# Tic-tac-toe misere
## (i) O minimax sempre ganha do randomplayer? 
Não. Em 20 partidas rodadas, houveram 13 ganhos e 7 empates, o que, em uma estatística muito simplificada, gira em torno 53,8% de ganho para o minimax.

## (ii) O minimax sempre empata consigo mesmo? 
Aparentemente sim. Houve empate em todas partidas de uma amostragem de 20 rodadas.

## (iii) O minimax sempre empata contra as jogadas perfeitas recomendadas pelo https://nyc.cs.berkeley.edu/uni/games/ttt/variants/misere ? Para verificar isso, use o humanplayer. No link, faça as jogadas do minimax, e no servidor do kit, faça as jogadas recomendadas (amarelo ou verde) do link.
Sim. De 10 partidas jogadas, todas resultaram em um empate com o minimax fazendo uma das jogadas sugeridas pelo site.

## Othello:
# Descrição da função de avaliação customizada:
Na função de avaliação customizada utilizamos uma heurística baseada no potencial. Dispõe-se da contagem das opções de movimento disponíveis, assim como da quantificação dos movimentos potenciais e da valoração dos estados mediante a aplicação da máscara proveniente da outra heurística. Os movimentos potenciais referem-se à quantidade de casas desocupadas contíguas às peças adversárias, ainda que não necessariamente conformem movimentos legalmente admissíveis.

# Descrição do critério de parada:
O critério de parada adotado foi uma profundidade máxima fixa de 4.

# Resultado da avaliação:
python server.py othello advsearch/maria/othello_minimax_mask.py advsearch/maria/othello_minimax_count.py
mask x count
  10 x 0

python server.py othello advsearch/maria/othello_minimax_mask.py advsearch/maria/othello_minimax_custom.py
mask x custom
   0 x 10

python server.py othello advsearch/maria/othello_minimax_mask.py advsearch/maria/mcts.py
mask x monte-carlo
   ? x ?

python server.py othello advsearch/maria/othello_minimax_count.py advsearch/maria/othello_minimax_custom.py
count x custom
    10 x 0

python server.py othello advsearch/maria/othello_minimax_count.py advsearch/maria/mcts.py
count x monte-carlo
    ? x ?

python server.py othello advsearch/maria/othello_minimax_custom.py advsearch/maria/mcts.py
custom x monte-carlo
     ? x ?

# Implementação escolhida para o torneio e se houve implementação de alguma melhoria no minimax ou no MCTS:
A implementação escolhida para o torneio foi a de minimax com heurística customizada pois foi a que apresentou o melhor desempenho. 
Não foram feitas melhorias nos algoritmos.

## Feedback:
# Quão fácil ou difícil foi realizar o trabalho? como foi trabalhar com o auxílio da IA? quais sugestões teria para melhorar o trabalho?
* O trabalho foi relativamente difícil de ser realizado essencialmente por uma questão de prazo e conflito de obrigações com outras matérias do que pelo conteúdo em si. Uma sugestão é que este trabalho (e talvez o conteúdo) fosse adiantado para um período anterior do semestre e fosse deixado um trabalho mais simples para o final.
* Quanto às ferramentas de IA, houve algum auxílio do GitHub Copilot, do GitHub Copilot Chat e do ChatGPT. O GitHub Copilot Chat e o ChatGPT foram muito úteis no auxilío de aspectos em que tipicamente não há problemas em uma linguagem fortemente tipada (erros em tipos, passagem de argumentos, etc.), os quais em linguagens fortemente tipadas normalmente são notificados durante a compilação, mas que em python só acabam sendo descobertos em runtime. 
O GitHub Copilot foi muito útil para a implementação de linhas simples de código, em que se sabia a estrutura de dados que se desejava implementar, mas não se dominava a sintaxe para tal. 
Para a avaliação de corretude dos algoritmos estas ferramentas não foram tão precisas, indicando muitas vezes que os algoritmos estavam coerentes quando na verdade haviam pequenos erros que não permitiam a execução. 