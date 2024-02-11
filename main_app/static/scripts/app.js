
const routebox = document.querySelector('#routebox');
const shadowbox = document.querySelector('#shadowbox');

let chars = '';
chars = `${routebox.innerHTML}`;
routebox.innerHTML = '';
shadowbox.innerHTML = '';
for (let x = 0; x < chars.length; x++) {
    routebox.innerHTML += `<span class='routechar' style='animation: routename 5s linear ${0 + (0.05 * x)}s infinite; bottom: ${x}px'>${chars[x]}</span>`;
}

for (let x = 0; x < chars.length; x++) {
    shadowbox.innerHTML += `<span class='shadowchar' style='animation: routeshadow 5s linear ${0 + (0.05 * x)}s infinite'>${chars[x]}</span>`;
}

const navparts = document.querySelectorAll('.navbit');
for (let x = 0; x < (navparts.length); x++) {
    navparts[x].style.height = '0%';
    navparts[x].style.animation  = `bitload .2s linear ${.4 + (x * 0.05)}s forwards`;
}

if (document.querySelector('.textscroll')){
const textscroll = document.querySelector('.textscroll');
}
let scrolls = '';
scrolls = `${textscroll.innerHTML}`;
textscroll.innerHTML = '';
for (let x = 0; x < scrolls.length; x++) {
    textscroll.innerHTML += `<span class='scrollchar' style='animation: scrolling .1s linear ${0 + (0.01 * x)}s forwards '>${scrolls[x]}</span>`;
}

