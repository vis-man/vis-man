
$("#id_emergency_first_name").parents('div').hide()
$("#id_emergency_last_name").parents('div').hide()
$("#id_emergency_phone_0").parents('div').hide()
$("#id_emergency_phone_1").parents('div').hide()
$("#id_emergency_relation").parents('div').hide()
// $("#id_role").parents('div').hide()
document.getElementById("id_role").value = "Hello"
// document.getElementById("role_dropdown").value
console.log(document.getElementById("role_dropdown").value)

$("#id_nightstay").click(function(){
    var checkBox = document.getElementById("id_nightstay");
    if(checkBox.checked == true) {
        $("#id_emergency_first_name").parents('div').show()
        $("#id_emergency_last_name").parents('div').show()
        $("#id_emergency_phone_0").parents('div').show()
        $("#id_emergency_phone_1").parents('div').show()
        $("#id_emergency_relation").parents('div').show()
    } 
    if(checkBox.checked == false) {
        $("#id_emergency_first_name").parents('div').hide()
        $("#id_emergency_last_name").parents('div').hide()
        $("#id_emergency_phone_0").parents('div').hide()
        $("#id_emergency_phone_1").parents('div').hide()
        $("#id_emergency_relation").parents('div').hide()
    }
})

// $("#role_dropdown").change(function(){
//     var role = document.getElementById("role_dropdown");
//     if(role) {
//         $("#id_emergency_first_name").parents('div').show()
//         $("#id_emergency_last_name").parents('div').show()
//         $("#id_emergency_phone_0").parents('div').show()
//         $("#id_emergency_phone_1").parents('div').show()
//         $("#id_emergency_relation").parents('div').show()
//     } 
//     if(checkBox.checked == false) {
//         $("#id_emergency_first_name").parents('div').hide()
//         $("#id_emergency_last_name").parents('div').hide()
//         $("#id_emergency_phone_0").parents('div').hide()
//         $("#id_emergency_phone_1").parents('div').hide()
//         $("#id_emergency_relation").parents('div').hide()
//     }
// })
