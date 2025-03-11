function showFact(fact) {
    document.getElementById("fact-text").innerText = fact;
    document.getElementById("fact-box").style.display = "block";
}

function hideFact() {
    document.getElementById("fact-box").style.display = "none";
}
