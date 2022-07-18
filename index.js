const azureFunctionLink = "https://funnyprojectssms.azurewebsites.net/api/HttpTrigger1?code=iV-8drJgflIrYqMP_WHQmJZ5z9FFpyTCsxicBqDVFuJPAzFuP1MieQ=="


function test(){
    console.group("test")

    let [name_v, phone_v, selector_v] = getMyElementValues();
    let response = validatePhone(phone_v);
    response ? sendMessage(name_v, phone_v, selector_v) : alert("Algo salió mal")

    console.groupEnd()
}


function sendMessage(name_v, phone_v, selector_v){
    var data_str = `&data={"name":"${name_v}","phone":"${phone_v}","msg":${parseInt(selector_v)}}`;
    let req_link = azureFunctionLink + data_str;

    alert("¡Checa las notificaciones de tu Cel! :D")
    httpGetAsync(req_link, () => {console.log("I think we sent it")})

    console.log(`The resulting string is: \n ${data_str} \n and its type is: \n ${typeof data_str}`)
}


function getMyElementValues(){
    let name_i = document.getElementById("name_i");
    let phone_i = document.getElementById("phone_i");
    let selector_i = document.getElementById("selector");

    return [name_i.value, phone_i.value, selector_i.value]
}


function validatePhone(phone){
    let flag = false;
    let message = "Verifique que su celular: ";
    let number = 1;

    phone = phone.replaceAll(' ','');
    phone = phone.replaceAll('-','');

    if (phone[0] !== "+"){
        message += `\n${number}.- contenga la lada ejemplo: \"+525585311900\" incluyendo el \"+\" `;
        number += 1;
        flag = true;
    } 
    if (!(phone.length >= 10)){
        message += `\n${number}.- contenga todos los dígitos`;
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