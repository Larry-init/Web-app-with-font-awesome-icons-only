let btnOne = document.querySelector('.hamburger');
let btnTwo = document.querySelector('.times');
let divOne = document.querySelector('.navContainer');
let divTwo = document.querySelector('.timesButton');

btnOne.addEventListener('click', function () {
    if(btnOne.classList.contains('hamburger')){
        divOne.classList.toggle('removeNavContainer');
        divTwo.classList.toggle('displayTimesButton');
    }
});

btnTwo.addEventListener('click', function () {
    if(btnTwo.classList.contains('times')){
        divOne.classList.toggle('removeNavContainer');
        divTwo.classList.toggle('displayTimesButton');
    }
});