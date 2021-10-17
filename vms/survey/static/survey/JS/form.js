// textbox for manual entry of role must be hidden by default
$("#id_role").parents('div').hide()


var checkBox = document.getElementById("id_nightstay");
var chosen_role = document.getElementById("id_role_dropdown")
var role_text = chosen_role.options[chosen_role.selectedIndex].text
// id_role always has a copy of the data chosen from the dropdown
document.getElementById("id_role").value = role_text

// called each time there a different option in the role dropdown is chosen
$("#id_role_dropdown").change(function () {
    role_text = chosen_role.options[chosen_role.selectedIndex].text
    // id_role stores the data from the dropdown
    document.getElementById("id_role").value = role_text
    // id_role is made visible so user can manually enter their role
    if (chosen_role.value === 'other') {
        $("#id_role").parents('div').show()
        document.getElementById("id_role").value = ''
        document.getElementById("id_role").placeholder = 'Please Key in Role'
    }
    else {
        $("#id_role").parents('div').hide()
    }

})

// storing current date and time
var today = new Date();
var day = today.getDate()
// if it is after 5pm then set the default checkout date as the next day
if (today.getHours() >= 17) {
    day = today.getDate() + 1
}

// rearranging the date and time as per the required format
var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + day;
var time = "17" + ":" + "00" + ":" + "00"
var dateTime = date + 'T' + time;

document.getElementById("id_planned_checkout").value = dateTime

// detecting if the browser is chrome/firefox/safari
let f = navigator.userAgent.search("Firefox");
let s = navigator.userAgent.search("Safari");
let c = navigator.userAgent.search("Chrome");

// use default chrome datetime picker if chrome
if (c > -1) {
    c = 1
}
// use flatpicker custom datetime picker if firefox
else if (f > -1) {
    config = {
        enableTime: true,
        enableSeconds: false,
        dateFormat: "Y-m-d H:i:s",
    }
    flatpickr("input[type=datetime-local]", config);
}
// use flatpicker custom datetime picker if safari
else if (s > -1) {
    config = {
        enableTime: true,
        enableSeconds: false,
        dateFormat: "Y-m-d H:i:s",
    }
    flatpickr("input[type=datetime-local]", config);
}

// clicking of the nightstay checkbox hides/unhides the emergency section
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

// this is mainly to prevent page from resetting when it is reloaded
if (chosen_role.value === 'other') {
    $("#id_role").parents('div').show()
    document.getElementById("id_role").value = ''
    document.getElementById("id_role").placeholder = 'Please Key in Role'
}

// this is mainly to make sure page acts appropriately when reloaded
if (checkBox.checked === false) {
    $("#id_emergency_first_name").parents('div').hide()
    $("#id_emergency_last_name").parents('div').hide()
    $("#id_emergency_phone").parents('div').hide()
    $("#id_emergency_relation").parents('div').hide()
}



