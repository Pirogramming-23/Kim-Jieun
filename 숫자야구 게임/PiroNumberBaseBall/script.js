let attempts = 0; // 변경 가능한 숫자 값
let answer_numbers=[];

const game_result_container = document.getElementById('game-result-img');
const attempts_container = document.getElementById('attempts');
const results_container = document.getElementById('results');
const input_container = document.getElementsByClassName("input-field");

// 1. 게임 초기화

function newGameStart(){
    attempts = 9; // 변경 가능한 숫자 값
    answer_numbers = getRandomNumber();
    console.log("정답 :", answer_numbers.join(''));

    // ==== 초기화 ====
    // 버튼 활성화
    document.querySelector(".submit-button").disabled = false;
    // 게임 결과 화면
    game_result_container.src = ""

    // 남은 횟수
    attempts_container.textContent = attempts;

    // 결과 출력 창
    results_container.innerHTML = "";

    // input 필드
    Array.from(input_container).forEach(input => input.value = "");
    input_container[0].focus();

}

/// 중복되지 않는 랜덤 숫자 3개 생성 함수 - getRandomNumber
function getRandomNumber(){
    const numbers = new Set();
    while (numbers.size < 3){
        numbers.add(Math.floor(Math.random()*10));
    }
    const answer = Array.from(numbers);
    return answer
}



// 2. 숫자 확인

function check_numbers(){
    //input 필드 확인
    const input_answer = Array.from(input_container).map(input => input.value);
    /// 빈 필드가 있다면 입력창 비우기
    if (input_answer.some(val => val === "")) {
        Array.from(input_container).forEach(input => input.value = "");
        return;
    }
    /// 없을 때
    checkTheAnswer(input_answer);
}

/// 정답 비교 함수 - checkTheAnswer
function checkTheAnswer(input_answer){
    let strike = 0;
    let ball = 0;

    // strike 계산
    for (let i = 0; i < answer_numbers.length; i++){
        if ((Number(input_answer[i])) == Number(answer_numbers[i])){
            strike ++;
        }
    }

    // ball 계산
    for (let i = 0; i < answer_numbers.length; i++){
        if(Number(input_answer[i]) != Number(answer_numbers[i]) && answer_numbers.includes(Number(input_answer[i]))){
            ball ++;
        }

    }

    results_container.innerHTML += createHTMLResult(input_answer, strike, ball);
    resultHTMLCSS();
    results_container.scrollTop = results_container.scrollHeight;
    attempts -= 1;
    attempts_container.textContent = attempts;


    /// 게임 종료 조건 확인
    if (strike == 3 || attempts == 0){
        gameOver(strike, attempts);
    }
}
/// 게임 종료 함수
function gameOver(strike, attempts){
    document.querySelector(".submit-button").disabled = true;
    if (strike == 3){
        game_result_container.src = "./success.png"
    }
    else if(attempts == 0){
        game_result_container.src = "./fail.png";
    }
}
/// 정답 영역 추가 createHTMLResult(strike, ball)
function createHTMLResult(input_answer, strike, ball){
    if (strike == 0 && ball == 0){
        return `
        <div class="result_item">
            <div class = "num-result">${input_answer.join(" ")}</div>
            <div>:</div>
            <div class = "score_space">
                <div class = "out num-result">O</div>
            </div>
        </div>
    `;
    }
    else{
        return `
        <div class="result_item">
            <div class = "num-result">${input_answer.join(" ")}</div>
            <div>:</div>
            <div class = "score_space">
                <div class = "num-result">${strike}</div>
                <div class = "strike num-result">S</div>
                <div class = "num-result">${ball}</div>
                <div class = "ball num-result">B</div>
            </div>
        </div>
    `;
    }
}

//// innerHTML css 속성
function resultHTMLCSS(){
    results_container.style.display = "flex";
    results_container.style.flexDirection = "column";
    results_container.style.width = "100%";

    const lastItem = results_container.lastElementChild;

    lastItem.style.display = "flex";
    lastItem.style.justifyContent = "space-between";
    lastItem.style.alignItems = "center";
    lastItem.style.width = "100%";

    const children = Array.from(lastItem.children);

    children[0].style.display = "flex";
    children[0].style.flex = "1"; 
    children[0].style.justifyContent = "flex-start";
    children[0].style.textAlign = "left";

    //children[1].style.flex = "0 0 20px"; // 고정 20px 폭
    children[1].style.display = "flex";
    children[1].style.flex = "1"; 
    children[1].style.justifyContent = "center";
    children[1].style.alignItems = "center";

    children[2].style.display = "flex";
    children[2].style.flex = "1";
    children[2].style.justifyContent = "flex-end";
    children[2].style.alignItems = "center";
    children[2].style.gap = "8px";

}



// main
newGameStart(); // 게임 초기화 함수 실행

