const axios = require("axios");

const form = document.querySelector('form');

form.addEventListener('submit', listen());


function listen() {
    const url = document.getElementsByName("videoURL").value;
    const assembly = {
        "audio_url": url
    };
}

function func(){
    const get = axios.create({
        baseURL: "https://api.assemblyai.com/v2",
        headers: {
            authorization: "a30b0d235ea04ce5946b07f391afd504",
            "content-type": "application/json",
        },
    });

    get
    .post("/transcript", {
        audio_url: url
    })
    .then((res) => console.log(res.text))
    .catch((err) => console.error(err));
    

}


