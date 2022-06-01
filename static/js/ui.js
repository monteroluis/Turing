const Vacio = 'λ';
var Tick = undefined;
ID = 4;
var MaquinaTuring = {
    4 : new Array()
}
borrarTabla(4);

$(function() {
    Clear();
    $('#info').click(function(){
        $('#instrucciones' + ID).modal('show');
    });
});

function ScrollToID(id, time, table){

    container = $('#tabla' + table);
    item = $('#' + id);
    $('body').animate({ scrollTop: item.offset().top - container.offset().top + container.scrollTop() }, time >= 0 ? time:600, 'swing');
}

function ScrollLeftToID(id, time, table){

    container = $('#tabla' + table);
    item = $('#' + id);
    $('#tabla' + table).animate({ scrollLeft: item.offset().left - 1.5 * container.offset().left + container.scrollLeft() }, time >= 0 ? time:600, 'swing');
}

function AddRow(value, id_value, class_value, table){

    container = $('#tabla' + table + " tbody")
    item = `<td id='${id_value}' class='${class_value}'>
                ${value}
            </td>`
    container.append(item);
    return true
}

function borrarTabla(table){

    $('#tabla' + table + " tbody td").remove();
    return true
}

function ChangeActiveRow(table, time) { // This method requieres that 'the caller' sets row's id as 'new-row' before call this. 

    /* Remove old active row*/
    oldRow = $('#active-row');
    oldRow.attr('id', '');
    oldRow.attr('class', '');

    /* Set new active row*/
    newRow = $('#new-row');
    newRow.attr('id', 'active-row');    
    ScrollLeftToID('active-row', time, table);
    newRow.attr('class', 'bg-danger text-light');
}

function Clear(){
    // Popups
    $('[data-toggle="popover1"]').popover();
    $('#myModal').modal('hide');
    $('#instrucciones').modal('hide');

    // SET MATCHINE
    Turing();
    // SET COUNT
    $('#contador').text(MaquinaTuring[ID].Count);
    // SET STATE TO MACHINE'S HEAD
    $('#estado').text(MaquinaTuring[ID].Count);
}

function Update(){
       // SET COUNT
       $('#contador').text(MaquinaTuring[ID].Count);
       // SET STATE TO MACHINE'S HEAD
       $('#estado').text(MaquinaTuring[ID].State);
}

