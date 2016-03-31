// SocketIO functions when the document is ready
$(document).ready(function(){
    vec = Object.seal({
    x: 0,
    y: 0
    });

    var DURATION = 30;
    namespace = '/MCHE201'; // change to an empty string to use the global namespace

    // the socket.io documentation recommends sending an explicit package upon connection
    // this is specially important when using the global namespace
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    // event handler for server sent data
    // the data is displayed in the "Received" section of the page
    socket.on('my response', function(msg) {
        //$('#log').append('<br>Received #' + msg.count + ': ' + msg.data);
        console.log(msg.data);
        
        if (msg.data == "0") {
            $('#timer').text("");
            }
        else if (msg.data == "I\'m connected!" || msg.data == "Connected") {
            $('#timer').text(msg.data);
        }
        else {
            $('#timer').text(msg.data);
            $('#start_button').html("Stop");
        }
    });


    // handlers for the different forms in the page
    // these send data to the server in a variety of ways
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
    $('form#broadcast').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
        return false;
    });
    $('form#join').submit(function(event) {
        socket.emit('join', {room: $('#join_room').val()});
        return false;
    });
    $('form#leave').submit(function(event) {
        socket.emit('leave', {room: $('#leave_room').val()});
        return false;
    });
    $('form#send_room').submit(function(event) {
        socket.emit('my room event', {room: $('#room_name').val(), data: $('#room_data').val()});
        return false;
    });
    $('form#close').submit(function(event) {
        socket.emit('close room', {room: $('#close_room').val()});
        return false;
    });
    $('form#disconnect').submit(function(event) {
        socket.emit('disconnect request');
        return false;
    });
    
    
    var clock = $('.countdown_clock').FlipClock(DURATION, {
        clockFace: 'Counter'
    });
    
    var start = 0;
    var count = DURATION;
    
    function countdown(){
        countdown_Timer = setInterval(function() {
            clock.decrement();
            count = count - 1;
            console.log(count);
            
            if (count <= 0) {
                clearInterval(countdown_Timer);
                
                count = DURATION;
                setTimeout(function(){
                                      clock.setTime(DURATION); 
                                      $('#start_button').html("Start");}, 
                                      5000);
                
            };
        }, 1000);
        

    };

    $('.start_button').mousedown(function (){
        socket.emit('my broadcast event', {data: 1});
        if (count == DURATION){
            countdown();
            $('#start_button').html("Stop");
        }
        else { 
            socket.emit('my broadcast event', {data: 0});
            clearInterval(countdown_Timer);
                
            count = DURATION;
            clock.setTime(DURATION);
            $('#start_button').html("Start");
            
        }
        });
//         
//     // Start button - touch events
//     $(".start_button").bind('touchstart', function(){
//         socket.emit('my broadcast event', {data: 1});
//         if (count == DURATION){
//             countdown();
//             $('#start_button').html("Stop");
//         }
//         else { 
//             socket.emit('my broadcast event', {data: 0});
//             clearInterval(countdown_Timer);
//                 
//             count = DURATION;
//             clock.setTime(DURATION);
//             $('#start_button').html("Start");
//             
//         }
//         });

});

 


