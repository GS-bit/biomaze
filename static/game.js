function drawMap(){
    fetch('gamestatus')
        .then(response => response.json())
        .then(game_data => {
            let nodes = [];
            let edges = [];

            for(const organ in game_data.connections){
                nodes.push({id: organ, label: organ});

                for(connection of game_data.connections[organ]){
                    edges.push({from: organ, to: connection});
                }
            }

            const data = {
                nodes: new vis.DataSet(nodes),
                edges: new vis.DataSet(edges)
            };

            const options = {
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
                    font: { size: 16, face: ['Elms Sans', 'sans-serif'], multi: false, bold: { color: '#000000', size: 16, face: ['Elms Sans', 'sans-serif'], vadjust: 0 } }
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

                stabilization: {
                    enabled: true,
                    iterations: 100,
                    updateInterval: 25,
                    onlyDynamicEdges: false,
                    fit: true
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

            const network = new vis.Network(container, data, options);
        })
        .catch(error => alert("Erro ao gerar o mapa do labirinto!", error));
}

const btns = [...document.getElementsByClassName('movement-btn')];

btns.forEach(function sendMovement(element){
    element.addEventListener("click", () => {
        fetch('gamemovement', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain'
            },
            body: element.innerHTML.trim()
        })
        .then(response => response.json())
        .then(game_data => {
            document.getElementById("cur-organ").innerText = game_data.cur_organ;
            document.getElementById("activated-organs").innerText = game_data.activated_organs.length;

            const movement_btns = document.getElementById("movement-btns");

            movement_btns.innerHTML = "";
            for(organ of game_data.connections[game_data.cur_organ]){
                movement_btns.innerHTML += `<button class="movement-btn">${ organ }</button>`;
            }
        })
        .catch(error => alert("Erro ao enviar movimento ao servidor!", error))
    });
});

drawMap();