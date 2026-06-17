# AutoclickOnColor

> A tiny Python script that watches the pixel color under your cursor and auto-clicks when it matches a target color — originally used as a simple in-game fishing bot.

![Python](https://img.shields.io/badge/Python-pyautogui-3776AB?logo=python)
![Type](https://img.shields.io/badge/Type-Automation%20Script-orange)

---

## Overview

The script continuously reads the screen pixel at the current mouse position. When that pixel matches a specific RGB value, it clicks the spot, waits, and clicks again — a basic color-triggered auto-clicker. The in-code comments ("Get Fish" / "New fishing") show it was built to automate a game's fishing minigame.

## How it works

1. Loop forever, reading the cursor position with `pyautogui.position()`
2. Take a screenshot and read the pixel color at that position
3. If the color equals the target (`(199, 84, 80)` by default), click → wait 10s → click again
4. Press `Ctrl-C` to quit

## Requirements

- Python 3
- `pyautogui`:
  ```bash
  pip install pyautogui
  ```

## Usage

```bash
python main.py
```

Hover the mouse over the spot you want monitored. When the matching color appears there, the script clicks automatically.

## Configuration

Edit the values in `main.py`:

- **Target color** — change the RGB tuple in the `if str(rgb) == "(199, 84, 80)"` check to your own color
- **Wait time** — adjust the `time.sleep(10)` between clicks

> Tip: print the live `rgb` value (already in the script) to find the exact color you want to match.

## Notes / possible improvements

- The loop screenshots the whole screen every iteration with no delay, which is CPU-heavy. Add a small `time.sleep(...)` per loop, and consider `pyautogui.pixel(x, y)` or capturing a 1×1 region instead of a full screenshot.
- Comparing colors as strings is fragile; comparing the tuple directly (`rgb == (199, 84, 80)`) with a small tolerance is more reliable.
- ⚠️ Automating input in online games may violate their terms of service — use only where it's allowed.
