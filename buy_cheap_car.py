import pyautogui
import time
import sys
pyautogui.FAILSAFE = False

nav_to_20k_car = [
    'x', 'down', 'down', 'down', '\n', 'backspace', 'up', '\n',
]
buy_car = [
    '\n', 'y',
]
buy_car_2 = [
    '\n', '\n', '\n'
]
reset = [
    'Esc', '\n'
]
def main():
    time.sleep(3) #3 seconds to nav back to forza's autoshop after kicking off script
    num_cars = 100
    if len(sys.argv) > 1:       
        num_cars = sys.argv[1]
    purchase(num_cars)

def purchase(cars):
    for car in range(int(cars)):
        print('starting to buy car#', car+1)
        pyautogui.typewrite(nav_to_20k_car, interval=.85)
        print('naved to')
        pyautogui.typewrite(buy_car, interval=2.5)
        pyautogui.typewrite(buy_car_2, interval=1)
        print('sleeping 14 seconds to to wait for car to load')
        for i in range(14):
            print("slept ", i+1)
            time.sleep(1)
        pyautogui.typewrite(reset, interval=1.4)
        print('finished purchasing car #', car+1, 'reset and buying next unless this is the last one')
main()