def on_received_number(receivedNumber):
    pins.servo_write_pin(AnalogPin.P0, 0)
    basic.pause(500)
    pins.servo_write_pin(AnalogPin.P0, 180)
    basic.pause(500)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

angle = 0
opened = 95
closed = 175

def on_forever():
    global angle
    led.plot_bar_graph(input.light_level(), 0)
    angle = pins.map(input.light_level(), 0, 255, opened, closed)
    pins.servo_write_pin(AnalogPin.P0, angle)
    music.play_melody("C5 F C5 F A D E G ", 120)
basic.forever(on_forever)
