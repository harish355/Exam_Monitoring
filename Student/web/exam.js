
eel.exam()(change)
function change(ret) {
    if (ret) {
        var data = ret;
        var data = ret.split(" ");
        document.getElementById("title").innerHTML = data[0] + " " + data[1];
        document.getElementById("time").innerHTML = data[4] + " " + data[6];
        document.getElementById("Subject").innerHTML = data[3];
        // location.replace("studentguide.html");
    }
}



function fm() {
	eel.fm()
}