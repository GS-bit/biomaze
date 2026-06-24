# 🧭 Biomaze

O organismo humano é composto por diferentes sistemas que, relacionados entre si, possibilitam a existência da vida humana. O sistema endócrino é um deles, sendo responsável pela produção e secreção de substâncias químicas extremamente importantes para o funcionamento do corpo, chamadas hormônios. Aos serem secretados por glândulas, como a tireoide, a pituitária e a pineal, os hormônios entram na circulação sanguínea e alcançam diferentes órgãos, trazendo uma mensagem específica. Assim, pensando nesse contexto biológico, o Biomaze propõe um **labirinto endócrino**, conciliando a nobre temática da biologia com o aspecto lúdico.

No Biomaze, o jogador é um hormônio que está perambulando pelo corpo humano, e seu objetivo é passar por todos os órgãos uma única vez, sem repetição. Se isso ocorrer, o usuário será declarado vencedor, e, em caso contrário, será decretado fim de jogo. O conceito do Biomaze é simples, mas envolve a aplicação de grafos, uma estrutura de dados bastante relevante na área de computação. Define-se um grafo como um conjunto de nós e arestas (ligações) entre esses nós, o que faz com que os órgãos possam ser visualizados como nós e suas arestas como as vias sanguíneas. Ademais, um dos tópicos de destaque em grafos é o caminho hamiltoniano, que ocorre quando se tem no grafo uma trajetória em que todos os nós são visitados uma única vez, exatamente a regra que rege o Biomaze.

Com o sistema de ranqueamento, a gameplay torna-se mais sofisticada. Toda vez que um jogador finaliza uma partida com êxito, o Biomaze pergunta por seu nome de identificação e registra o tempo gasto por esse usuário na partida em um banco de dados SQLite. Dessa forma, é possível visualizar os jogadores que resolveram o desafio no menor tempo, incluindo todos os tempos obtidos por um mesmo jogador.

O jogo requer a biblioteca Flask para seu funcionamento. Portanto, para instalá-la, use o seguinte comando: 
```
pip install Flask
```

Uma vez presente o Flask no computador, deve-se baixar o repositório do Biomaze:
```
git clone https://github.com/GS-bit/biomaze.git
```

E, para jogar, estando dentro do repositório baixado, executa-se:
```
python3 app.py
```

Assim, deve aparecer uma mensagem no terminal com algumas informações, dentre elas algo como "* Running on [address]". Ao abrir o navegador de internet, insere-se o [address] apresentado, como http://127.0.0.1:5000, e o jogo estará disponível.

Será criado um arquivo de banco de dados com o nome "biomaze.db" no repositório. Deve-se mantê-lo intocável a fim de preservar os dados de ranqueamento.

## 🏠 Tela inicial do jogo:

<img width="1920" height="1080" alt="Captura_de_tela_20260624_140642" src="https://github.com/user-attachments/assets/6cdab406-a6e7-4f0b-998f-8c37cfb949dd" />



## 🎮 Tela de jogo:

<img width="1920" height="1080" alt="Captura_de_tela_20260624_140725" src="https://github.com/user-attachments/assets/569a4e5e-c8c5-48f5-b0b0-a46c262a153e" />
