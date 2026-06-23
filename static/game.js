/* JavaScript for game.html page */

function drawMap(){
    /*
    It draws the game map on the page.
    */

    fetch('gamestatus')
        .then(response => response.json())
        .then(game_data => {
            let nodes = [];
            let edges = [];

            /* Inserting nodes into the nodes array, including the color if they are activated: */
            for(const organ in game_data.connections){
                if(game_data.activated_organs.includes(organ)){
                    nodes.push({id: organ, label: organ, color: 'green', font: {color: 'white'}});
                }
                else{
                    nodes.push({id: organ, label: organ});
                }

                for(connection of game_data.connections[organ]){
                    edges.push({from: organ, to: connection});
                }
            }

            const data = {
                nodes: new vis.DataSet(nodes),
                edges: new vis.DataSet(edges)
            };

            const options = {
                layout: {
                    randomSeed: game_data.random_seed
                },

                nodes: {
                    shape: 'circle',
                    size: 30,
                    color: {
                        background: '#ffffff',
                        border: '#000000',
                        highlight: { background: '#ffffff', border: '#000000' }
                    },
                    borderWidth: 1,
                    borderWidthSelected: 1,
                    font: { size: 16, face: 'Elms Sans' }
                },

                edges: {
                    selectionWidth: function (width){
                        return width;
                    },

                    smooth: {
                        enabled: false 
                    },

                    color: '#000000',
                    width: 1
                },

                physics: {
                    enabled: true,
                    solver: 'repulsion',

                    repulsion: {
                        nodeDistance: 250,
                        centralGravity: 0.25,
                        springLength: 100,
                        springConstant: 0.05,
                        damping: 0.10
                    }
                },

                interaction: {
                    dragNodes: false,
                    dragView: false,
                    selectable: false
                }
            };

            const container = document.getElementById('maze');

            container.style.border = "none";
            container.style.outline = "none";

            network = new vis.Network(container, data, options);
        })
        .catch(error => alert("Erro ao gerar o mapa do labirinto!", error));
}

function resetGame(){
    /* 
    It resets the game data, so the user can play multiple games.
    */

    return fetch('/resetgame', {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'
        },
        body: ''
    })
    .then(response => {})
    .catch(error => console.log("Erro ao reiniciar o jogo!", error));
}

function saveScore(playersName, timeSpent){
    /* 
    It saves the player's score on the database.
    */

    return fetch('/savescore', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"name": playersName, "time_spent": timeSpent})
    })
    .then(response => {})
    .catch(error => console.log("Erro ao enviar dados ao servidor!", error));
}

/* Adding event to the movement buttons, so the user can tell the server the movement he/she
desires to choose: */

const movementBtns = document.getElementById('movement-btns');

movementBtns.addEventListener("click", event => {
    if(event.target && event.target.classList.contains('movement-btn')){
        const element = event.target;

        fetch('gamemovement', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain'
            },
            body: element.innerHTML.trim()
        })
        .then(response => response.json())
        .then(game_data => {
            /* Updating textual info on the page: */

            document.getElementById("cur-organ").innerText = game_data.cur_organ;
            document.getElementById("activated-organs").innerText = game_data.activated_organs.length;

            const movement_btns = document.getElementById("movement-btns");

            movement_btns.innerHTML = "";
            for(let organ of game_data.connections[game_data.cur_organ]){
                movement_btns.innerHTML += `<button class="movement-btn">${ organ }</button>`;
            }

            /* Updating map: */
            drawMap();

            /* Showing modals on the page, if necessary: */

            if(!game_data.running){
                resetGame();

                if(game_data.gameover){ // Game over modal
                    const gameoverModal = document.getElementById("gameover-modal");
                    gameoverModal.style.display = "flex";
                    gameoverModal.getElementsByTagName("span")[0].addEventListener("click", event => {
                        // Sending the player to the home page:
                        window.location.href = '/';
                    });
                }

                else{ // Won game modal
                    const wonModal = document.getElementById("won-modal");
                    wonModal.style.display = "flex";

                    let new_html = "";
                    
                    new_html += `<p>⏳ Tempo gasto: ${game_data.time_spent}s</p>`;
                    new_html += "<hr />"
                    new_html += "<p>🪪  Digite seu nome, por favor:</p>";
                    new_html += '<input type="text" id="players-name" autofocus />';
                    new_html += '<button id="save-score-btn" style="padding-top: 1px; padding-bottom: 1px; margin-left: 5px">Registrar pontuação</button>';

                    wonModal.getElementsByClassName("modal-content")[0].innerHTML += new_html;

                    wonModal.getElementsByTagName("span")[0].addEventListener("click", event => {
                        // Sending the player to the home page:
                        window.location.href = '/';
                    });

                     document.getElementById("save-score-btn").addEventListener("click", event => {
                        const playersName = document.getElementById("players-name");
                        saveScore(playersName.value, game_data.time_spent)
                        .then(() => {window.location.href = '/'}); // Sending the player to the home page. 
                    });
                }
            }
        })
        .catch(error => alert("Erro ao enviar movimento ao servidor!", error));
    }
});

/* Drawing the map on the screen: */

drawMap();