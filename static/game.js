function drawMap(){
    fetch('gamestatus')
        .then(response => response.json())
        .then(game_data => {
            let nodes = [];
            let edges = [];

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
                if(game_data.gameover){
                    document.getElementById("gameover-modal").style.display = "flex";
                }

                else{
                    document.getElementById("won-modal").style.display = "flex";
                    document.getElementById("won-modal").getElementsByClassName("modal-content")[0].innerHTML += `<p>⏳ Tempo gasto: ${game_data.time_spent}s</p>`;
                }

                //window.location.href = '/';
            }
        })
        .catch(error => alert("Erro ao enviar movimento ao servidor!", error));
    }
});

drawMap();