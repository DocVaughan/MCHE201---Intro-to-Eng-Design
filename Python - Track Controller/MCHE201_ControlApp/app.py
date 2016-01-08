from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
import logging
import threading
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect
    

    
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None

start = False
ON_RASPI = True

if ON_RASPI:
    import pifacedigitalio


@app.route('/')
def full():
    return render_template('index.html')


@socketio.on('my event', namespace='/MCHE201')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})



@socketio.on('my broadcast event', namespace='/MCHE201')
def test_broadcast_message(message):
    global start
    
    session['receive_count'] = session.get('receive_count', 0) + 1
    
    logging.debug('Message data = {}'.format(message['data']))
    
    if message['data'] == 1:
        logging.debug('Message data = {}'.format(message['data']))
        
        with lock:
            start = True
            
    elif message['data'] == 0:
        logging.debug('Message data = {}'.format(message['data']))
        
        with lock:
            start = False


@socketio.on('join', namespace='/MCHE201')
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('leave', namespace='/MCHE201')
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})


@socketio.on('close room', namespace='/MCHE201')
def close(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         room=message['room'])
    close_room(message['room'])


@socketio.on('my room event', namespace='/MCHE201')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('disconnect request', namespace='/MCHE201')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('connect', namespace='/MCHE201')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/MCHE201')
def test_disconnect():
    print('Client disconnected')


class hardware_loop(threading.Thread):
    """
    Class to control the threaded hardware loop
    """
    def __init__(self):
        threading.Thread.__init__(self, name = 'Hardware')
        logging.debug('Hardware thread starting...')
        self.running = True
    
    def run(self):
        """
        Main control loop
        """
        global start
        global pfd
        
        logging.debug('Hardware thread running...')
        
        while self.running:
            if start:
                logging.debug('Starting Countdown...')
                
                if ON_RASPI:
                    # Close all the relays
                    pfd.relays[0].value = 1 
                    pfd.relays[1].value = 1
                    pfd.output_pins[2].value = 1
                    pfd.output_pins[3].value = 1
    
                    # Turn on the LEDS
                    pfd.output_pins[7].value = 1
                    pfd.output_pins[6].value = 1
                    pfd.output_pins[5].value = 1
                    pfd.output_pins[4].value = 1
            
                start_time = time.time()
                while time.time() - start_time < 30:
                    elapsed_time = time.time() - start_time
                    
                    if start:
                        logging.debug('Elapsed Time {:0.2f}'.format(elapsed_time))
                    else:
                        if ON_RASPI:
                            # Open all the relays
                            pfd.relays[0].value = 0 
                            pfd.relays[1].value = 0
                            pfd.output_pins[2].value = 0
                            pfd.output_pins[3].value = 0
    
                            # Turn off the LEDS
                            pfd.output_pins[7].value = 0
                            pfd.output_pins[6].value = 0
                            pfd.output_pins[5].value = 0
                            pfd.output_pins[4].value = 0
                        break
                    
                    time.sleep(0.1)
                else:
                    if ON_RASPI:
                        # Open all the relays
                        pfd.relays[0].value = 0 
                        pfd.relays[1].value = 0
                        pfd.output_pins[2].value = 0
                        pfd.output_pins[3].value = 0

                        # Turn off the LEDS
                        pfd.output_pins[7].value = 0
                        pfd.output_pins[6].value = 0
                        pfd.output_pins[5].value = 0
                        pfd.output_pins[4].value = 0
                    
        
            with lock:
                start = False
                
            time.sleep(0.1)
                     
    def stop(self):
        self.running = False


if __name__ == '__main__':
    # creates a PiFace Digtal object
    if ON_RASPI:
        pfd = pifacedigitalio.PiFaceDigital() 


    # Create a lock
    lock = threading.Lock()
    
    #     hardware_thread = threading.Thread(name = 'Hardware', target = hardware_loop)
    hardware_thread = hardware_loop()
    hardware_thread.daemon = True
    hardware_thread.start()
    
    try:  
        logging.debug('Starting Flask app')
        socketio.run(app, host='0.0.0.0', port=5000)
        #socketio.run(app)
        
    except (KeyboardInterrupt, SystemExit):
        hardware_thread.stop()
        hardware_thread.join()
        logging.debug('KeyboardInterrupt or SystemExit exception. Exiting.\n\n')
