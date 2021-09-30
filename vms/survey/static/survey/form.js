
$("#id_emergency_first_name").parents('div').hide()
$("#id_emergency_last_name").parents('div').hide()
$("#id_emergency_phone").parents('div').hide()
$("#id_emergency_relation").parents('div').hide()
$("#id_role").parents('div').hide()
var chosen_role = document.getElementById("id_role_dropdown")
var role_text = chosen_role.options[chosen_role.selectedIndex].text
document.getElementById("id_role").value = role_text

$("#id_nightstay").click(function(){
    var checkBox = document.getElementById("id_nightstay");
    if(checkBox.checked === true) {
        $("#id_emergency_first_name").parents('div').show()
        $("#id_emergency_last_name").parents('div').show()
        $("#id_emergency_phone").parents('div').show()
        $("#id_emergency_relation").parents('div').show()
    } 
    if(checkBox.checked === false) {
        $("#id_emergency_first_name").parents('div').hide()
        $("#id_emergency_last_name").parents('div').hide()
        $("#id_emergency_phone").parents('div').hide()
        $("#id_emergency_relation").parents('div').hide()
    }
})

$("#id_role_dropdown").change(function(){
    role_text = chosen_role.options[chosen_role.selectedIndex].text
    document.getElementById("id_role").value = role_text
    if(chosen_role.value === 'other'){
        $("#id_role").parents('div').show()
        document.getElementById("id_role").value = ''
        document.getElementById("id_role").placeholder = 'Please Key in Role'
    }
    else{
        $("#id_role").parents('div').hide()
    }
    
})
