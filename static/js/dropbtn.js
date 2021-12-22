let myBtn = document.querySelector(".btn");
let drop = document.getElementById("dropdown");

myBtn.addEventListener('click', () => {
    drop.classList.toggle("show");

})