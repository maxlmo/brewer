let minTemperature = 50;
let maxTemperature = 100;

setInterval(() => {
    fetch("/temp").then(r => r.json()).then(newTempValue => {
        document.getElementById("temperatureValue").textContent = newTempValue;
        if (newTempValue < minTemperature) {
            setTempBackgroundColor("#275DAD");
        } else if(newTempValue > maxTemperature) {
            setTempBackgroundColor("#FF5E5B")
        }
        else {
            setTempBackgroundColor("#20BF55")
        }
    })
}, 2000);

const setRange = (min, max) => {
    document.getElementById("min-temperature").value = min.toString();
    document.getElementById("max-temperature").value = max.toString();
}

const updateRange = () => {
    minTemperature = document.getElementById("min-temperature").value;
    maxTemperature = document.getElementById("max-temperature").value;
    console.log("update");
}

const setTempBackgroundColor = (color) => {
    document.getElementsByClassName("temperature-card")[0].style.backgroundColor = color;
}

setRange(minTemperature, maxTemperature);

document.getElementById("set-range-btn").onclick = updateRange;
