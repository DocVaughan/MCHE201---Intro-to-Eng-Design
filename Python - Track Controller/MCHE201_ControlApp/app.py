import time
import logging
import serial
import threading
from threading import Thread

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


start = False
ON_RASPPI = True
HARDWARE_CONNECTED = True
ROUND_DURATION = 30.0


@app.route('/')
def full():
    return render_template('index.html')

@app.route('/')
def sections():
    return render_template('sections.html')


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
    
    if message['data'] == 1111:
        logging.debug('Message data = {}'.format(message['data']))
        
        with lock:
            start = True
            
    elif message['data'] == 0:
        logging.debug('Message data = {}'.format(message['data']))
        
        with lock:
            start = False


# @socketio.on('join', namespace='/MCHE201')
# def join(message):
#     join_room(message['room'])
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
#           'count': session['receive_count']})
# 
# 
# @socketio.on('leave', namespace='/MCHE201')
# def leave(message):
#     leave_room(message['room'])
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
#           'count': session['receive_count']})
# 
# 
# @socketio.on('close room', namespace='/MCHE201')
# def close(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response', {'data': 'Room ' + message['room'] + ' is closing.',
#                          'count': session['receive_count']},
#          room=message['room'])
#     close_room(message['room'])
# 
# 
# @socketio.on('my room event', namespace='/MCHE201')
# def send_room_message(message):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my response',
#          {'data': message['data'], 'count': session['receive_count']},
#          room=message['room'])


@socketio.on('disconnect request', namespace='/MCHE201')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('connect', namespace='/MCHE201')
def test_connect():
    emit('my response', {'data': 'Connected', 'duration': ROUND_DURATION})


@socketio.on('disconnect', namespace='/MCHE201')
def test_disconnect():
    print('Client disconnected')


class oceanControls(object):
    """ Class to wrap the ASCII protocol for controlling the Ocean Controls
    Relay module"""
    
    def __init__(self, port, baudrate = 9600, address = 00):
        self.ser = serial.Serial(port, baudrate, 
                                 bytesize=8, parity='N', 
                                 stopbits=1, timeout=0.1)
        
        self.address = address
        
                                 
    def turnRelayOn(self, relay_number):
        """ Method to turn on an individual relay 
        
        Input arguments:
            relay_number = The relay number to control
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.ser.write('@{:02d} ON {}\r'.format(self.address, relay_number).encode('utf-8'))
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
        
    def turnRelayOff(self, relay_number):
        """ Method to turn off an individual relay 
        
        Input arguments:
            relay_number = The relay number to control
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            self.ser.write('@{:02d} OFF {}\r'.format(self.address, relay_number).encode('utf-8'))
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
    
    
    def timedRelayOn(self, relay_number, time_on):
        """ Method to turn on an individual relay for a set time
        
        Input arguments:
            relay_number = The relay number to control
            time_on = the time the relay should remain on (s)
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            # Convert the time input (s) to the number of ms the relay should be on
            time_tenths = int(time_on * 10)
        
            if time_tenths < 1 or time_tenths > 255:
                raise ValueError('The time must be between 0.1s and 25.5s')
            
            if not np.isclose((time_on / 0.1) % 1, 0):
                raise ValueError('The resolution of this command is only 0.1s.\n\
                Please enter a value that is a multiple of 0.1s.')
        
            self.ser.write('@{:02d} TR {} {:03d}\r'.format(self.address, relay_number, time_tenths).encode('utf-8'))
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
        
    
    def turnAllOn(self):
        """ Method to turn on all relays 
        
        Input arguments:
            nothing
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        self.ser.write('@{:02d} ON {}\r'.format(self.address, 0).encode('utf-8'))
    
    
    def turnAllOff(self):
        """ Method to turn off all relays 
        
        Input arguments:
            nothing
    
        Returns:
            nothing
            
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        self.ser.write('@{:02d} OFF {}\r'.format(self.address, 0).encode('utf-8'))

    def isDigitalInputOn(self, digital_input_number):
        """ Method that checks the status of an individual digital input 
        
        Input Arugments:
            digital_input_number = The input number to check
        
        Returns:
            Boolean indicating if input is High/On (True) or Low/Ooff (False)
        
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/16/16
        """
        
        if digital_input_number in [1, 2, 3, 4]:
            self.ser.flushInput()
            # May need to change to below in versions of PySerial >= 3.0
            # self.ser.reset_input_buffer()
        
            self.ser.write('@{:02d} IS {:02d}\r'.format(self.address, digital_input_number).encode('utf-8'))
        
            # TODO: Be more elegant about this
            status_string = self.ser.readlines()[-1]
        
            status = int(status_string.split()[-1])
        
            if status:
                return True
            else:
                return False
        else:
            raise ValueError('Please enter a digital input number between 1 and 4.')
    
    def isRelayOn(self, relay_number):
        """ Method that checks the status of an individual relay 
        
        Input Arugments:
            relay_number = The relay number to control
        
        Returns:
            Boolean indicating if relay is on (True) or off (False)
        
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            # self.ser.flushInput()
            # May need to change to below in versions of PySerial >= 3.0
            # self.ser.reset_input_buffer()
        
            self.ser.write('@{:02d} RS {:02d}\r'.format(self.address, relay_number).encode('utf-8'))
            
            # TODO: Be more elegant about this
            status_string = self.ser.readlines()[-1]
        
            status = int(status_string.split()[-1])
        
            if status:
                return True
            else:
                return False
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
    
    def printRelayStatus(self, relay_number):
        """ Method to print the status of an individual relay 
        
        Input Arugments:
            relay_number = The relay number to control
        
        Returns:
            nothing
        
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/15/16
        """
        
        if relay_number in [1, 2, 3, 4, 5, 6, 7, 8]:
            if controller.isRelayOn(relay_number):
                print('Relay {} is on.'.format(relay_number))
            else:
                print('Relay {} is off.'.format(relay_number))
        else:
            raise ValueError('Please enter a relay number between 1 and 8.')
    
    def printDigitalInputStatus(self, digital_input_number):
        """ Method to print the status of an individual digital input 
        
        Input Arugments:
            relay_number = The digital input number to check
        
        Returns:
            nothing
        
        Created: Joshua Vaughan - joshua.vaughan@louisiana.edu - 03/16/16
        """
        
        if digital_input_number in [1, 2, 3, 4]:
            if controller.isDigitalInputOn(digital_input_number):
                print('Input {} is High/On.'.format(digital_input_number))
            else:
                print('Input {} is Low/Off.'.format(digital_input_number))
        else:
            raise ValueError('Please enter a digital input number between 1 and 4.')


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
        
        logging.debug('Hardware thread running...')
        
        while self.running:
            if start:
                logging.info('Starting Countdown...')
                
                # Close all the relays
                if HARDWARE_CONNECTED:
                    # Open all the relays
                    controller.turnAllOn()
                    
                logging.info('Turning all on.')
            
                start_time = time.time()
                while time.time() - start_time < ROUND_DURATION:
                    elapsed_time = time.time() - start_time
                    
#                     if start:
#                         logging.debug('Elapsed Time {:0.2f}'.format(elapsed_time))
#                     else:
#                         if HARDWARE_CONNECTED:
#                             # Open all the relays
#                             controller.turnAllOff()
# 
#                         logging.info('Turning all off.')
#                         break
                    
                    socketio.emit('my response',
                      {'data': 'time', 'elapsed_time': '{:0f}'.format(elapsed_time)},
                      namespace='/MCHE201')
                      
                    time.sleep(0.2)
                    
                else:
                    if HARDWARE_CONNECTED:
                        controller.turnAllOff()

                    logging.info('Turning all off.')
                    socketio.emit('my response',
                      {'data': '0000'},
                      namespace='/MCHE201')
                    
            with lock:
                start = False
                
            time.sleep(0.5)
                     
    def stop(self):
        self.running = False


if __name__ == '__main__':

    if HARDWARE_CONNECTED:
        if ON_RASPPI:
         #   Define an instance of the oceanControls class for use on Rasp Pi
            controller = oceanControls('/dev/ttyUSB0')
        else:
            # Define an instance of the oceanControls class on Dr. Vaughan's MacBook
            controller = oceanControls('/dev/tty.usbserial-AL01H195')
    
    # Now the relationship between the Ocean Controller outputs and the track
    # Define the values for red then increment around the track CW
    # Red - Blue - Black - Yellow
    # Should allow easier changing in the future
    red_relay = 1
    red_LED = 5
    
    blue_relay = red_relay + 1    
    blue_LED = red_LED + 1
    
    black_relay = blue_relay + 1
    black_LED = blue_LED + 1
    
    yellow_relay = black_relay + 1
    yellow_LED = black_LED + 1
    
    # Define the digital input position of the hardware switch
    hardware_start_switch = 4

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
