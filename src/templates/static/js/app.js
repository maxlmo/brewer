setInterval(() => {
    fetch("/temp").then(r => r.json()).then(newTempValue => {
        document.getElementById("temperatureValue").textContent = newTempValue;
    })
}, 1000);