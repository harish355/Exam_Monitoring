
document.write('<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>');
$(document).on("keydown", function (e) {
    if (e.keyCode >= 112 && e.keyCode <= 123) {
        return false;
    }
    if (e.keyCode >= 17 && e.keyCode <= 18) {
        alert(0);
        return false;
    }
    if (e.keyCode == 91) {
        return false;
    }
});
document.addEventListener('contextmenu', event => event.preventDefault());