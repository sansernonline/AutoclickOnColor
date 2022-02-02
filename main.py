import pyautogui,time

print('Press Ctrl-C to quit.')
try:
    while True:
        # Get position
        x, y = pyautogui.position()

        # Click
        # pyautogui.click(x, y)
        # time.sleep(2)

        # Print Position
        # positionStr = 'X: ' + str(x) + ' Y: ' + str(y)
        # print(positionStr)

        # Print Color
        img = pyautogui.screenshot()
        rgb = img.getpixel((x, y))
        print(rgb)

        # Check Color
        if str(rgb) == "(199, 84, 80)":
            print("Color match")

            # Get Fish
            pyautogui.click(x, y)

            # Wait to next round
            time.sleep(10)

            # New fishing
            pyautogui.click(x, y)
        else:
            print("Color not match")
except KeyboardInterrupt:
    print('\n')

