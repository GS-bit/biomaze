const modals = [...document.getElementsByClassName("modal")];
modals.forEach(element => {
    element.children[0].insertAdjacentHTML('afterbegin', '<div style="display: flex; justify-content: flex-end"><span style="font-size: 24px; cursor: pointer">X</span></div>');
    element.children[0].children[0].children[0].addEventListener('click', e => {
        element.style.display = 'none';
    });
});