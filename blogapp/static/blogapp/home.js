let e = document.getElementById('formLogin')
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