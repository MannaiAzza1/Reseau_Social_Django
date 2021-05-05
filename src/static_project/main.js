$(document).ready(function (){
    console.log('hello')
    $('#modal-btn').click(function (){
        console.log('working')
        $('.ui.modal')
        .modal('show')
        ;
    })
    $('.ui.dropdown').dropdown()
})