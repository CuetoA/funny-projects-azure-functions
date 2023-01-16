const azureFunctionLink = "https://funnyprojectssms.azurewebsites.net/api/HttpTrigger1?code=iV-8drJgflIrYqMP_WHQmJZ5z9FFpyTCsxicBqDVFuJPAzFuP1MieQ=="
                           
function animate_card_trans(id_num){
    console.log("this is my other test");
    element = document.getElementsByClassName("back-slices-container");
    console.log(element[id_num]);
    element[id_num].classList.add("test-back-slices");
}

function send_to_assure(id_num){
    console.group("test send to assure console log")

    let [name_v, phone_v] = getMyElementValues();
    let response = validatePhone(phone_v);
    if (response){
        animate_card_trans(id_num); 

        setTimeout( ()=> {sendMessage(name_v, phone_v, id_num)}, 1500);
    } 
    else{
        alert("Algo salió mal")
    } 

    console.groupEnd()
}


function sendMessage(name_v, phone_v, id_num){
    var data_str = `&data={"name":"${name_v}","phone":"${phone_v}","msg":${parseInt(id_num)}}`;
    let req_link = azureFunctionLink + data_str;

    alert("Check your phone!")
    httpGetAsync(req_link, () => {console.log("I think we sent it")})

    console.log(`The resulting string is: \n ${data_str} \n and its type is: \n ${typeof data_str}`)
}


function getMyElementValues(){
    let name_i = document.getElementById("name_i");
    let phone_i = document.getElementById("phone_i");
    // let selector_i = document.getElementById("selector");

    return [name_i.value, phone_i.value]
}


function validatePhone(phone){
    let flag = false;
    let message = "Verify that your phone number: ";
    let number = 1;

    phone = phone.replaceAll(' ','');
    phone = phone.replaceAll('-','');

    if (phone[0] !== "+"){
        message += `\n${number}.- Includes country code: \"+14373730503\" including \"+\" `;
        number += 1;
        flag = true;
    } 
    if (!(phone.length >= 10)){
        message += `\n${number}.- Is 10 digits length (plus country code)`;
        flag = true;
    }

    if (flag){
        alert(message);
        return false;
    }

    return true
}

function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}