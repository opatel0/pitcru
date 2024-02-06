const routebox = document.querySelector('#routebox');
const shadowbox = document.querySelector('#shadowbox');
const textscroll = document.querySelector('#textscroll');
let chars = '';
let scrolls = '';
chars = `${routebox.innerHTML}`;
scrolls = `${textscroll.innerHTML}`;
routebox.innerHTML = '';
shadowbox.innerHTML = '';
textscroll.innerHTML = '';
for (let x = 0; x < chars.length; x++) {
    routebox.innerHTML += `<span class='routechar' style='animation: routename 5s linear ${0 + (0.05 * x)}s infinite; bottom: ${x}px'>${chars[x]}</span>`;
}

for (let x = 0; x < chars.length; x++) {
    shadowbox.innerHTML += `<span class='shadowchar' style='animation: routeshadow 5s linear ${0 + (0.05 * x)}s infinite'>${chars[x]}</span>`;
}

for (let x = 0; x < scrolls.length; x++) {
    textscroll.innerHTML += `<span class='scrollchar' style='animation: scrolling .1s linear ${0 + (0.01 * x)}s forwards '>${scrolls[x]}</span>`;
}
