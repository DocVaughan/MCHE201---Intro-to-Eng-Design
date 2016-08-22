// SocketIO functions when the document is ready
$(document).ready(function(){
    var DURATION = 30;
    var start = 0;
    var count = DURATION;
    var curr_time = DURATION;
    var elapsed_time = 0;
    var running = false;
    
    namespace = '/MCHE201'; // change to an empty string to use the global namespace

    // the socket.io documentation recommends sending an explicit package upon connection
    // this is specially important when using the global namespace
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    socket.on('disconnect', function() {
        $('#timer').text('Disconnected. Reload Page.');
    });

    // event handler for server sent data
    // the data is displayed in the "Received" section of the page
    socket.on('my response', function(msg) {
        //  $('#log').append('<br>Received #' + msg.count + ': ' + msg.data);
        console.log("Data from python ", msg.data);
        
        if (msg.data == "0000") {
            $('#start_button').html("Start");
            clock.setTime(DURATION);
        }
        else if (msg.data == "Connected") {
            $('#timer').text(msg.data);
            
            // Update the clock duration on connect
            DURATION = msg.duration;
            count = DURATION;
            clock.setTime(DURATION);
            
            // Logging
            console.log(msg.duration);
            console.log(DURATION); 
        }
        else if (msg.data == "time") {
            console.log("elapsed = ", msg.elapsed_time);
            curr_time = Math.floor(DURATION - msg.elapsed_time)
            console.log("current = ", curr_time);
            clock.setTime(curr_time);
        }
        else if (msg.data == "1111") {
            $('#start_button').html("Stop");
        }
    });


//     handlers for the different forms in the page
//     these send data to the server in a variety of ways
//     $('form#emit').submit(function(event) {
//         socket.emit('my event', {data: $('#emit_data').val()});
//         return false;
//     });
//     $('form#broadcast').submit(function(event) {
//         socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
//         return false;
//     });
//     $('form#join').submit(function(event) {
//         socket.emit('join', {room: $('#join_room').val()});
//         return false;
//     });
//     $('form#leave').submit(function(event) {
//         socket.emit('leave', {room: $('#leave_room').val()});
//         return false;
//     });
//     $('form#send_room').submit(function(event) {
//         socket.emit('my room event', {room: $('#room_name').val(), data: $('#room_data').val()});
//         return false;
//     });
//     $('form#close').submit(function(event) {
//         socket.emit('close room', {room: $('#close_room').val()});
//         return false;
//     });
//     $('form#disconnect').submit(function(event) {
//         socket.emit('disconnect request');
//         return false;
//     });
    
    // Define the flip clock
    var clock = $('.countdown_clock').FlipClock(DURATION, {
        clockFace: 'Counter'
    });
    
    // Define the button events
    $('.start_button').mousedown(function (){
        if (running == false) {
            console.log('Start button Pressed')
            running = true;

            // Send data to Python backend, close relays, light LEDS
            socket.emit('my broadcast event', {data: 1111});
            
            // Change the button text
            $('#start_button').html("Stop");
        }
        else { 
            console.log('Stop Pressed')
            running = false;
            
            // Send data to Python backend, open relays, turn off LEDS
            socket.emit('my broadcast event', {data: 0000});
            
            // Reset the clock to the final duration
            clock.setTime(DURATION);
            
            // Change the button text
            $('#start_button').html("Start");
        }
        });


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

 


