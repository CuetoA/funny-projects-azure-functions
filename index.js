function test(){
    console.group("test")
    console.log("hello there testers");

    let [name_v, phone_v, selector_v] = getMyElementValues();
    validatePhone(phone_v);

    console.log(`name_i value: ${name_v}`);
    console.log(`phone_v value: ${phone_v}`);
    console.log(`selector_v value: ${selector_v}`);
    console.groupEnd()
}


function getMyElementValues(){
    let name_i = document.getElementById("name_i");
    let phone_i = document.getElementById("phone_i");
    let selector_i = document.getElementById("selector");

    return [name_i.value, phone_i.value, selector_i.value]
}


function validatePhone(phone){
    console.log(`primer posición: ${phone[0]}`)

    let flag = false;
    let message = "Verifique que su celular: ";
    let number = 1;

    if (phone[0] !== "+"){
        message += `\n${number}.- contenga la lada ejemplo: \"+525585311900\" incluyendo el \"+\" `
        number += 1
        flag = true;
    } 
    if (!(phone.length >= 10)){
        message += `\n${number}.- contenga todos los dígitos`
        flag = true;
    }

    if (flag){
        alert(message)
        return false
    }

    return true
}