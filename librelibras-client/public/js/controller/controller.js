let v = document.getElementById("myVideo");

// Cria uma tela para capturar uma imagem para upload
let imageCanvas = document.createElement('canvas');
let imageCtx = imageCanvas.getContext("2d");

// Adiciona o blob do arquivo a um formulário e completa o "post"
function postFile(file) {
    let formdata = new FormData();
    formdata.append("image", file);
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:5000/image', true);
    xhr.onload = function () {
        if (this.status === 200)
            console.log(this.response);
        else
            console.error(xhr);
    };
    xhr.send(formdata);
}

// Obtém a imagem da tela
function sendImagefromCanvas() {

    // Verifica se a tela está definida para o tamanho atual do vídeo
    imageCanvas.width = v.videoWidth;
    imageCanvas.height = v.videoHeight;

    imageCtx.drawImage(v, 0, 0, v.videoWidth, v.videoHeight);

    // Converta a tela para blob e postar o arquivo
    imageCanvas.toBlob(postFile, 'image/jpeg');
}

// Tire uma foto ao clicar
var enviar = function () {
    console.log('click');
    sendImagefromCanvas();
};

window.onload = function () {

    //Pega a camera do vídeo
    navigator.mediaDevices.getUserMedia({ video: { width: 1280, height: 720 }, audio: false })
        .then(stream => {
            v.srcObject = stream;
        })
        .catch(err => {
            console.log('navigator.getUserMedia error: ', err)
        });
};