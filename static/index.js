/* JavaScript for game.html page */

/* Configuring "show ranking" and "how to play" buttons: */

const showRankingBtn = document.getElementById("show-ranking-btn");
const howToPlayBtn = document.getElementById("how-to-play-btn");

showRankingBtn.addEventListener("click", () => {
    document.getElementById("ranking-modal").style.display = "flex";
});

howToPlayBtn.addEventListener("click", () => {
    document.getElementById("help-modal").style.display = "flex";
});