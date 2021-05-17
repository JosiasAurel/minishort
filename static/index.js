
const formEl = document.getElementById("form");

function createAndAppendUrl(url, shortUrl) {

    // create elementss
    let span = document.createElement("span");
    let p1 = document.createElement("p");
    let p2 = document.createElement("p");

    // set element values
    p1.innerText = shortUrl;
    p2.innerText = url;

    // add p as child of span
    span.appendChild(p1);
    span.appendChild(p2);

    // get parent URLs container

    const urlsContainer = document.getElementById("shorts");

    urlsContainer.appendChild(span);
}

async function shortenUrl(url) {
    let res = await fetch(`shorten?url=${url}`, {method: "POST"});
    let data = await res.json();
    console.log(data);
}

formEl.addEventListener("submit", (event) => {
    event.preventDefault();

    let inputUrl = document.getElementById("inputUrl").value;

    shortenUrl(inputUrl);
})