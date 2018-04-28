var mainInnerHTML = document.getElementById('main').innerHTML;

function EnableLodgerEdit() {
    document.getElementById('lodger_edit').style.display = "flex";
    document.getElementById('lodger_display').style.display = "none";
}

function SaveLodgerEdit() {
    document.getElementById('lodger_edit_form').submit();
}

function CancelLodgerEdit() {
    document.getElementById('lodger_edit').style.display = "none";
    document.getElementById('lodger_display').style.display = "flex";
}
