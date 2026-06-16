# 🧭 Biomaze

O organismo humano é composto por diferentes sistemas que, relacionados entre si, possibilitam a existência da vida humana. O sistema endócrino é um deles, sendo responsável pela produção e secreção de substâncias químicas extremamente importantes para o funcionamento do corpo, chamadas hormônios. Aos serem secretados por glândulas, como a tireoide, a pituitária e a pineal, os hormônios entram na circulação sanguínea e alcançam diferentes órgãos, trazendo uma mensagem específica. Assim, pensando nesse contexto biológico, o Biomaze propõe um **labirinto endócrino**, conciliando a nobre temática da biologia com o aspecto lúdico.

No Biomaze, o jogador é um hormônio que está perambulando pelo corpo humano, e seu objetivo é passar por todos os órgãos uma única vez, sem repetição. Se isso ocorrer, o usuário será declarado vencedor, e, em caso contrário, será decretado fim de jogo. O conceito do Biomaze é simples, mas envolve a aplicação de grafos, uma estrutura de dados bastante relevante na área de computação. Define-se um grafo como um conjunto de nós e arestas (ligações) entre esses nós, o que faz com que os órgãos possam ser visualizados como nós e suas arestas como as vias sanguíneas. Ademais, um dos tópicos de destaque em grafos é o caminho hamiltoniano, que ocorre quando se tem no grafo uma trajetória em que todos os nós são visitados uma única vez, exatamente a regra que rege o Biomaze.

Com o sistema de ranqueamento, a gameplay torna-se mais sofisticada. Toda vez que um jogador finaliza uma partida com êxito, o Biomaze pergunta por seu nome de identificação e registra o tempo gasto por esse usuário na partida em um banco de dados SQLite. Dessa forma, é possível visualizar os jogadores que resolveram o desafio no menor tempo, incluindo todos os tempos obtidos por um mesmo jogador.

O jogo não requer bibliotecas adicionais para seu funcionamento, sendo necessário apenas o interpretador Python com a biblioteca padrão. Para instalar o Biomaze, deve-se executar o seguinte comando:
```
git clone https://github.com/GS-bit/biomaze.git
```

E, para jogar, estando dentro do diretório em que estão os arquivos do jogo, executa-se:
```
python3 main.py
```

Será criado um arquivo de banco de dados com o nome "biomaze.db". Deve-se mantê-lo intocável a fim de preservar os dados de ranqueamento.

## 🏠 Tela inicial do jogo:

<img width="1090" height="819" alt="Captura_de_tela_20260616_174402" src="https://github.com/user-attachments/assets/b37d1ef4-4e6f-4e05-a34f-ca834fa29a8b" />


## 🎮 Tela de jogo:

<img width="1090" height="903" alt="Captura_de_tela_20260616_174451" src="https://github.com/user-attachments/assets/fe9fd5fc-3e73-482a-be0f-1caa9895cf2f" />
