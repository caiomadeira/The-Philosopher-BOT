function CapturaParametrosUrl() {
    urlchat = window.location.href;
    let parametrosUrl;
    let res = urlchat.split('?'); 
    if (res[1] === undefined) {

    }
    if (res[1] !== undefined) {
        let parametros = res[1].split('&');
        parametrosUrl = parametros;
    }
    return parametrosUrl;
} 

function validarLog(value){
    if (value[0] === 'loro6995caga0120mousepad'){
        let x = document.getElementById('logTxt');
        x.style.display = 'block'
    }
}

window.onload=function(){
    CapturaParametrosUrl()
    let y = document.getElementById('send-message')
    if (CapturaParametrosUrl() === undefined){

    } else {
        validarLog(CapturaParametrosUrl())
    }

    // document.querySelector('#send-message').onclick = function() {
    //     msg = document.querySelector('#input-text-chat').value;
    //     // appendDIV(msg)
    // }
}

function appendDIV(event) {
    // let repeat = event.length;
    console.log(event)
    const chatContainer = document.querySelector('.chat-output');
    const span = document.createElement('span');
    span.tabIndex = 0;
    span.classList.add("text-chat2");
    let a = event.log.replace(/-/g,'<br>');
    span.innerHTML = a; 
    chatContainer.insertBefore(span, chatContainer.firstChild);
    // for(i = 0; i < repeat; i++){
    //     const chatContainer = document.querySelector('.chat-output');
    //     const span = document.createElement('span');
    //     span.tabIndex = 0;
    //     span.classList.add("text-chat2");
    //     let a = event[0].log.replace(/-/g,'<br>');
    //     span.innerHTML = a; 
    //     chatContainer.insertBefore(span, chatContainer.firstChild);
    //     event.shift();
    // }  
}

function ajax(config){
    const xhr = new XMLHttpRequest()
    xhr.open(config.metodo, config.url, true)

    xhr.onload = e => {
        if (xhr.status === 200) {
            config.sucesso(xhr.response)
        } else if (xhr.status >= 400){
            config.erro({
                codigo: xhr.status,
                texto: xhr.statusText
            })
        }
    }

    xhr.send()
}

ajax({
    url: "./js/dados.json",
    metodo: "get",
    sucesso(resposta){
        const estados = JSON.parse(resposta)
        console.log(estados)
        appendDIV(estados)
    },
    erro(e){
        const msg = document.createTextNode(`${e.codi}: ${e.texto}`)
        document.body.appendChild(msg)
    }
})