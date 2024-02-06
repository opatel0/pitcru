const routebox = document.querySelector('#routebox');
let chars = '';
chars = `${routebox.innerHTML}`;
routebox.innerHTML = '';
for (let x = 0; x < chars.length; x++) {
    routebox.innerHTML += `<span class='routechar' style='animation: routename 5s linear ${0 + (0.05 * x)}s infinite'>${chars[x]}</span>`;
}