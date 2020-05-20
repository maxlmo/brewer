import {setTemperatureValue, updateRange, setRange} from "./temperature.ctrl.js";

document.getElementById("set-range-btn").onclick = updateRange;

fetch("/range").then(r => r.json()).then(actual_range => {
    console.log("actual range", actual_range)
    document.getElementById("min-temperature").value = actual_range.min;
    document.getElementById("max-temperature").value = actual_range.max;
    setRange(actual_range.min, actual_range.max)
});

setInterval(() => {
    fetch("/temp").then(r => r.json()).then(newTempValue => {
        setTemperatureValue(newTempValue);
    })
}, 2000);
