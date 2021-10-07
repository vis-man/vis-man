
$("#id_emergency_first_name").parents('div').hide()
$("#id_emergency_last_name").parents('div').hide()
$("#id_emergency_phone").parents('div').hide()
$("#id_emergency_relation").parents('div').hide()
$("#id_role").parents('div').hide()
var chosen_role = document.getElementById("id_role_dropdown")
var role_text = chosen_role.options[chosen_role.selectedIndex].text
document.getElementById("id_role").value = role_text

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
let f = navigator.userAgent.search("Firefox");
let s = navigator.userAgent.search("Safari");
let c = navigator.userAgent.search("Chrome");

if (c > -1) {
    c = 1
}
else if (f > -1) {
    config = {
        enableTime: true,
        enableSeconds: true,
        dateFormat: "Y-m-d H:i:s",
    }
    flatpickr("input[type=datetime-local]", config);
}
else if (s > -1) {
    config = {
        enableTime: true,
        enableSeconds: true,
        dateFormat: "Y-m-d H:i:s",
    }
    flatpickr("input[type=datetime-local]", config);
}

// const Toast = Swal.mixin({
//     toast: true,
//     position: 'top',
//     showConfirmButton: false,
//     timer: 3000,
//     timerProgressBar: true,
//     didOpen: (toast) => {
//         toast.addEventListener('mouseenter', Swal.stopTimer)
//         toast.addEventListener('mouseleave', Swal.resumeTimer)
//     }
// })

// Toast.fire({
//     icon: 'success',
//     title: 'Signed in successfully'
//     })

// $("#in_form").onsubmit = function() {myFunction()}
// $("#out_form").onsubmit = function() {myFunction()}
// function myFunction() {
//     console.log("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOO");
//     alert("The form was submitted");
//   }



// $("#in_form").onsubmit(function(){
//     console.log("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOO");
//     Toast.fire({
//         icon: 'success',
//         title: 'Signed in successfully'
//       })
// })



// document.getElementById("#in_form").addEventListener("submit", myFunction2);
// document.getElementById("#out_form").addEventListener("submit", myFunction2);

// function myFunction2() {
//     alert("The form was submitted");
//     console.log("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOO");
// }


