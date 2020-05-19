const temperatureElement = document.getElementById("temperatureValue");
let min = 50;
let max = 100;
let currentValue = 0;

const headers = {
    'Content-Type': 'application/json'
};

document.getElementById("min-temperature").value = min;
document.getElementById("max-temperature").value = max;

export const setTemperatureValue = (value) => {
    temperatureElement.textContent = value;
    currentValue = value;
    refreshView();
}

export function setRange(newMin, newMax) {
    min = newMin;
    max = newMax;
    document.getElementById("min-temperature").value = min;
    document.getElementById("max-temperature").value = max;
    refreshView();
}

export const updateRange = () => {
    const potentialNewMin = document.getElementById("min-temperature").value;
    const potentialNewMax = document.getElementById("max-temperature").value;

    if (!isValidInput(potentialNewMin) || !isValidInput(potentialNewMax)) {
        alert("Min and max must be between 0 and 100");
        return;
    }
    if (potentialNewMax < potentialNewMin) {
        alert("Your min value is higher than your max value!");
        return
    }

    min = potentialNewMin;
    max = potentialNewMax;
    fetch("/range", {method: 'post', headers: headers, body: JSON.stringify({"min": min, "max": max})}).then(() => {
        console.log("done")
    })
    refreshView();
}

function isValidInput(value) {
    return 0 < value && value < 100;
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

