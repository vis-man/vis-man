
$("#id_role").parents('div').hide()

var checkBox = document.getElementById("id_nightstay");
var chosen_role = document.getElementById("id_role_dropdown")
var role_text = chosen_role.options[chosen_role.selectedIndex].text
document.getElementById("id_role").value = role_text

$("#id_role_dropdown").change(function () {
    role_text = chosen_role.options[chosen_role.selectedIndex].text
    document.getElementById("id_role").value = role_text
    if (chosen_role.value === 'other') {
        $("#id_role").parents('div').show()
        document.getElementById("id_role").value = ''
        document.getElementById("id_role").placeholder = 'Please Key in Role'
    }
    else {
        $("#id_role").parents('div').hide()
    }

})

var today = new Date();
var day = today.getDate()
if (today.getHours() >= 17) {
    day = today.getDate() + 1
}
var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + day;
var time = "17" + ":" + "00" + ":" + "0";
var dateTime = date + ' ' + time;

let f = navigator.userAgent.search("Firefox");
let s = navigator.userAgent.search("Safari");
let c = navigator.userAgent.search("Chrome");

if (c > -1) {
    c = 1
}
else if (f > -1) {
    config = {
        enableTime: true,
        enableSeconds: false,
        dateFormat: "Y-m-d H:i:s",
        defaultDate: dateTime,
    }
    flatpickr("input[type=datetime-local]", config);
}
else if (s > -1) {
    config = {
        enableTime: true,
        enableSeconds: false,
        dateFormat: "Y-m-d H:i:s",
        defaultDate: dateTime,
    }
    flatpickr("input[type=datetime-local]", config);
}

$("#id_nightstay").click(function () {
    var checkBox = document.getElementById("id_nightstay");
    if (checkBox.checked === true) {
        $("#id_emergency_first_name").parents('div').show()
        $("#id_emergency_last_name").parents('div').show()
        $("#id_emergency_phone").parents('div').show()
        $("#id_emergency_relation").parents('div').show()
    }
    if (checkBox.checked === false) {
        $("#id_emergency_first_name").parents('div').hide()
        $("#id_emergency_last_name").parents('div').hide()
        $("#id_emergency_phone").parents('div').hide()
        $("#id_emergency_relation").parents('div').hide()
    }
})

if (chosen_role.value === 'other') {
    $("#id_role").parents('div').show()
    document.getElementById("id_role").value = ''
    document.getElementById("id_role").placeholder = 'Please Key in Role'
}

if (checkBox.checked === false) {
    $("#id_emergency_first_name").parents('div').hide()
    $("#id_emergency_last_name").parents('div').hide()
    $("#id_emergency_phone").parents('div').hide()
    $("#id_emergency_relation").parents('div').hide()
}



