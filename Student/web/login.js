function check() {

    var x = document.getElementById("username").value;
    var y = document.getElementById("password").value;
    var z = document.getElementById("code").value;
    if (x != "" & y != "" & z != "") {
        eel.login(x, y, z)(change)
        function change(ret) {
            if (ret) {
                location.replace("exam.html");
            }
        }
    }
    else {
        alert("Not Successul")
    }

}