const timeElement = document.querySelector(".real_time");
const recordList = document.querySelector(".recored_list");

let seconds = 0;
let interval = null;
let currentTime = `00:00`;

function startTime(){
    if(interval) return;
    interval = setInterval(timeFlow, 1000);
}
function timeFlow(){
    seconds ++;
    let mins = String(Math.floor(seconds / 60)).padStart(2, "0");
    let secs = String(Math.floor(seconds % 60)).padStart(2, "0");

    currentTime = `${mins}:${secs}`;
    timeElement.innerText = currentTime;
}

function stopTime(){
    clearInterval(interval);
    interval = null;
    recordTime();
}

function resetTime(){
    stopTime();
    seconds = 0;
    currentTime = `00:00`;
    timeElement.innerText = currentTime;
}

function recordTime(){
    recordList.innerHTML += `
    <li class="recorded_list_element">
        <label class="check-container">
            <input type="checkbox" class="list_check_box">
            <span class="mark"></span>
        </label>
        <div class="recorded_time">${currentTime}</div>
    </li>
    `
    attachCheckBoxListeners();
    updateAllCheckBox();
}

function deleteSelectedTime(){
    const checkedBoxes = document.querySelectorAll(".list_check_box:checked");

    checkedBoxes.forEach(box => {
        const li = box.closest(".recorded_list_element");
        if (li) li.remove();
    });
    updateAllCheckBox();
}

function checkAllBoxes(){
    const allBoxes = document.querySelectorAll(".list_check_box");
    allBoxes.forEach(box => box.checked = this.checked);

    updateAllCheckBox();
}

// 전체 체크박스 감지
function updateAllCheckBox() {
    const allBoxes = document.querySelectorAll(".list_check_box");
    const checkedBoxes = document.querySelectorAll(".list_check_box:checked");

    const allCheckBox = document.querySelector("#all_check_box");
    allCheckBox.checked = allBoxes.length > 0 && allBoxes.length === checkedBoxes.length;
}

function attachCheckBoxListeners() {
    const allBoxes = document.querySelectorAll(".list_check_box");
    allBoxes.forEach(box => {
        box.addEventListener("change", updateAllCheckBox);
    });
}

// 버튼 온클릭
document.querySelector(".start_button").onclick = startTime;
document.querySelector(".stop_button").onclick = stopTime;
document.querySelector(".reset_button").onclick = resetTime;

document.querySelector(".delete-icon").addEventListener("click", deleteSelectedTime);
document.querySelector("#all_check_box").addEventListener("change", checkAllBoxes);