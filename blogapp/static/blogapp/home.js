let e = document.getElementById('formLogin')
try {
    let ie = e.getElementsByTagName('input')
    for(i=0;i<ie.length; i++){
        if(i == 1){
            ie[i].setAttribute('placeholder', 'Username')
        }else if(i == 2){
            ie[i].setAttribute('placeholder', 'Password')
        }else{
            ie[i].setAttribute('placeholder', 'Re-enter password')
        }
    }

} catch (error) {
    // console.log(error) 
}

try {
    let divEle = document.getElementsByClassName('dbContent')[0].getElementsByTagName('img')
    for (let i=0; i<divEle.length; i++) {
        divEle[i].removeAttribute("width");
        divEle[i].removeAttribute("height");
        divEle[i].removeAttribute("style");
        divEle[i].setAttribute("alt", "Image Loading...");

    }
} catch (error) {
    // console.log(error)
}


try {
    let divEle = document.getElementsByClassName('dbContent')[0].getElementsByTagName('table')
    for (let i=0; i<divEle.length; i++) {
        divEle[i].removeAttribute("width");
        divEle[i].removeAttribute("style");
    }
} catch (error) {
    // console.log(error)
}

try {
    let divEle = document.getElementsByClassName('indbloglists')
    for(let i=0; i<divEle.length; i++){
        for(j=0; j<divEle[i].children.length; j++){
            if(divEle[i].children[j].getAttribute('id') == 'uniqDiv'){
                if(divEle[i].children[j].innerHTML.includes("&lt;table") || divEle[i].children[j].innerHTML.includes("&lt;a") || divEle[i].children[j].innerHTML.includes("&lt;img")){
                    divEle[i].children[j].innerHTML = "Please click on article name above to read the full article."
                }
                divEle[i].children[j].innerHTML = divEle[i].children[j].innerText
            }
        }
        
    }
} catch (error) {
    console.log(error)
}