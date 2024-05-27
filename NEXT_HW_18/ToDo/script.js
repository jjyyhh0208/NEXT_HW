const lucks = [
    '오늘은 운명같은 사람을 만날 수 있는 날입니다. 마음의 준비를 해두세요.',
    '오늘은 코딩하기에 머리가 돌아가지 않는 날입니다. 조금 쉬세요.',
    '오늘은 누군가 당신에게 야식을 사주는 날입니다. 메뉴를 생각해두세요.',
    '오늘은 모든 일이 술술 풀리는 날입니다. 새로운 도전을 해보세요.',
    '오늘은 조금씩 어긋나는 날입니다. 중요한 일을 나중으로 미뤄보세요.',
    '오늘은 주량이 일시적으로 늘어난 날입니다. 술배틀에 참여해보세요.',
];

const luck = document.querySelector('#luck p');
const luckToday = lucks[Math.floor(Math.random() * lucks.length)];
luck.innerText = luckToday;

const username = document.querySelector('.username');
const userWrapper = document.querySelector('.usernameWrapper');
const header = document.querySelector('#header');
const list = document.querySelector('#todo-list');

const checkUsername = () => {
    const checkName = window.localStorage.getItem('username');
    console.log(checkName);

    if (checkName) {
        userWrapper.classList.add('hidden');
        header.innerHTML = `<h1>${checkName}의 TODO LIST</h1> <button onclick = resetUsername()>초기화</button>`;
    } else {
        userWrapper.classList.remove('hidden');
        header.innerHTML = '';
    }
};

const setUsername = () => {
    const inputValue = username.value;
    window.localStorage.setItem('username', inputValue);
    console.log(window.localStorage);
    checkUsername();
};

const resetUsername = () => {
    window.localStorage.removeItem('username');
    window.localStorage.removeItem('task');
    list.innerHTML = '';
    checkUsername();
};

const resetTask = (index) => {
    let taskArray = JSON.parse(window.localStorage.getItem('task')) || [];
    taskArray.splice(index, 1);
    window.localStorage.setItem('task', JSON.stringify(taskArray));
    checkTask();
};

const task = document.querySelector('#content');
const addButton = document.querySelector('.submitBtn');

const checkTask = () => {
    const taskArray = JSON.parse(window.localStorage.getItem('task')) || [];
    console.log(taskArray);

    if (userWrapper.classList.contains('hidden')) {
        list.innerHTML = '';
        taskArray.forEach((task, index) => {
            list.insertAdjacentHTML(
                'beforeend',
                `<li>${task} <button onclick="resetTask(${index})">삭제하기</button></li>`
            );
        });
    }
};

const setTask = () => {
    const inputTask = task.value;
    let taskArray = JSON.parse(window.localStorage.getItem('task')) || [];

    if (userWrapper.classList.contains('hidden')) {
        taskArray.push(inputTask);
        window.localStorage.setItem('task', JSON.stringify(taskArray));
    }
    console.log(window.localStorage);
    checkTask();
};

addButton.addEventListener('click', setTask);
console.log(task);

checkUsername();
checkTask();
