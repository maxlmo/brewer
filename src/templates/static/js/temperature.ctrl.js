const ctrl = document.getElementById("temperatureValue");
let min = 50;
let max = 100;
let currentValue = 0;

document.getElementById("min-temperature").value = min;
document.getElementById("max-temperature").value = max;

export const setTemperatureValue = (value) => {
    ctrl.textContent = value;
    currentValue = value;
    refreshView();
}

export const updateRange = () => {
    min = document.getElementById("min-temperature").value;
    max = document.getElementById("max-temperature").value;
    refreshView();
}

const refreshView = () => {
    if (currentValue < min) {
        setBackgroundColor("#275DAD");
    } else if (currentValue > max) {
        setBackgroundColor("#FF5E5B")
    } else {
        setBackgroundColor("#20BF55")
    }
}

const setBackgroundColor = (color) => {
    document.getElementsByClassName("temperature-card")[0].style.backgroundColor = color;
}

