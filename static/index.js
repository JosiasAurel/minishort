
const formEl = document.getElementById("form");

function createAndAppendUrl(url, shortUrl) {

    // create elementss
    let span = document.createElement("span");
    let p1 = document.createElement("a");
    let p2 = document.createElement("a");

    // set element text values
    p1.innerText = shortUrl;
    p2.innerText = url;

    // set element href values
    p1.href = shortUrl;
    p2.href = url;

    // add a as child of span
    span.appendChild(p1);
    span.appendChild(p2);

    // add style class to span
    span.classList.add("short");

    // get parent URLs container
    const urlsContainer = document.getElementById("shorts");

    urlsContainer.appendChild(span);
}

async function shortenUrl(url) {
    let res = await fetch(`shorten?url=${url}`, {method: "POST"});
    let data = await res.json();

    createAndAppendUrl(url, `${location.href}${data.url}`);
}

formEl.addEventListener("submit", (event) => {
    event.preventDefault();

    let inputUrl = document.getElementById("inputUrl").value;

    shortenUrl(inputUrl);
})