let block = document.createElement('div');

block.classList.add('main');
document.querySelector('.container').appendChild(block);


block.setAttribute('style', "width:200px; height:100px; background-color:orange; margin:0 auto;");


let blo = document.children('div*4')

console.log(li.parentElement)
console.log(li.nextElementSibling)
let ul = document.querySelector('ul');
console.log(ul)
console.log(ul.children)
console.log(ul.firstElementChild);
console.log(ul.lastElementChild);
console.log(li.hasChildNodes())

let block = document.createElement('div');
block.classList.add('main')

for (let i = 0; i < 3; i++) {
    let miniblock = document.createElement('div');
    miniblock.classList.add('miniblock');
    block.appendChild(miniblock);
}

document.querySelector('.container').appendChild(block);

block.style.backgroundColor = 'red'
block.setAttribute('style', "width:200px;height:100px;background-color:purple;margin:0 auto;display:flex;")

console.log(block.getAttribute('class'))
block.onclick = function(event) {
    console.log(event.target)
}

block.addEventListener('class', (event) => {
    console.log(event.target)
    event.target.classList.add('bomba-oglan')
})