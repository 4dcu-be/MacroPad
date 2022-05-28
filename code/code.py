import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

from macropad import Macropad

keyboard = Keyboard(usb_hid.devices)

macropad = Macropad()
buttons = macropad.buttons

button_mapping = [
    [Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW],
    [Keycode.WINDOWS, Keycode.TAB],
    [Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.RIGHT_ARROW],
    [Keycode.LEFT_CONTROL, Keycode.F4],
    [Keycode.LEFT_CONTROL, Keycode.F5],
    [Keycode.LEFT_CONTROL, Keycode.F6],
    [Keycode.LEFT_CONTROL, Keycode.F7],
    [Keycode.LEFT_CONTROL, Keycode.F8],
    [Keycode.LEFT_CONTROL, Keycode.F9]]

for btn in buttons:
    @macropad.on_press(btn)
    def press_button(button):
        print(f"pressed {button.number}")
        keyboard.press(*button_mapping[button.number])

    @macropad.on_release(btn)
    def release_button(button):
        print(f"released {button.number}")
        keyboard.release(*button_mapping[button.number])
    
while True:
    macropad.update()
