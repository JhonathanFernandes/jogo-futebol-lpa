# Chute Certo — Jogo 2D de Futebol

Projeto acadêmico desenvolvido para a atividade de **Design de Interação**, com o objetivo de explorar a interação entre jogador e sistema por meio de um jogo de futebol em duas dimensões.

O jogo foi desenvolvido em Python com a biblioteca Pygame. A proposta é permitir que o jogador controle o personagem, prepare a força do chute e tente marcar gols contra um goleiro controlado pelo sistema.

## Objetivo do projeto

Aplicar conceitos iniciais de design de interação em uma experiência jogável, considerando os comandos disponíveis, o retorno visual das ações e a compreensão das regras durante a partida.

## Funcionalidades

- Movimentação do jogador pelo campo.
- Preparação da força do chute antes de soltar a bola.
- Física básica da bola, com movimento e colisões.
- Goleiro com comportamento automatizado para tentar defender os chutes.
- Contagem de gols e defesas.
- Feedback visual para gols, defesas e força do chute.
- Reinício da posição da bola durante a partida.

## Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Pygame** — biblioteca para janela do jogo, desenho, controles e atualização da partida.

## Controles

| Tecla | Ação |
| --- | --- |
| **W, A, S, D** ou **setas** | Movimentar o jogador |
| **Barra de espaço** | Segurar para carregar a força e soltar para chutar |
| **R** | Reposicionar a bola |

Para carregar o chute, o jogador precisa estar próximo da bola.

## Como executar

1. Instale o Python 3.
2. Instale a dependência Pygame:

   ```bash
   python -m pip install pygame
   ```

3. Abra o terminal na pasta do projeto.
4. Execute o arquivo principal do jogo. Caso ele se chame `game.py`, use:

   ```bash
   python game.py
   ```

> Se o arquivo principal tiver outro nome, substitua `game.py` pelo nome correto.

## Imagens do jogo

As imagens abaixo são referências visuais do jogo original que serviu de base para este projeto. Elas não devem ser interpretadas como capturas de tela da versão acadêmica, a menos que correspondam exatamente à versão presente neste repositório.

![Referência visual do jogo 2D de futebol](https://github.com/androfly/Python-2D-Football-Game/blob/master/ss1.png)

![Segunda referência visual do jogo 2D de futebol](https://github.com/androfly/Python-2D-Football-Game/blob/master/ss2.png)

## Relação com Design de Interação

O projeto permite observar aspectos como:

- **Mapeamento:** associação entre teclas e ações do personagem.
- **Feedback:** indicadores de força, placar e mensagens de gol ou defesa.
- **Affordances e instruções:** elementos visuais e textos que ajudam o jogador a entender como agir.
- **Aprendizagem e usabilidade:** clareza dos comandos e facilidade para começar a jogar.

Esses pontos podem orientar uma avaliação crítica da experiência, identificando melhorias para tornar os controles e os retornos do jogo mais claros.

## Contexto acadêmico

Trabalho desenvolvido para uma atividade da faculdade na área de **Design de Interação**.

**Autor:** Jhonathan Fernandes