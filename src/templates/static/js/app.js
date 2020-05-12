import {setTemperatureValue, updateRange} from "./temperature.ctrl.js";

document.getElementById("set-range-btn").onclick = updateRange;

setInterval(() => {
    fetch("/temp").then(r => r.json()).then(newTempValue => {
        setTemperatureValue(newTempValue);
    })
}, 2000);
