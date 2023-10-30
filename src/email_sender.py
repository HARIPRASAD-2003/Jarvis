import pyautogui
import time
from PIL import ImageGrab
import webbrowser
import pygetwindow as gw

class EmailSend():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    def send_email(self, rec_email, sub, body):
        # Open your web browser and go to Gmail (or your preferred email provider).
        # pyautogui.hotkey('ctrl', 't')
        # time.sleep(1)
        # pyautogui.write("https://mail.google.com")
        # pyautogui.press("enter")
        webbrowser.open("https://mail.google.com")
        time.sleep(5)  # Adjust the time for page loading.
        chrome_window = gw.getWindowsWithTitle("Google Chrome")[0]

        # Get the window width and height
        window_width = chrome_window.width
        window_height = chrome_window.height

        # def find_and_click_compose_button(self):
        # Define the screenshot region where you expect to find the "Compose" button
        screenshot_region = (0, 0, window_width, window_height)

        # Take a screenshot of the defined region
        screenshot = ImageGrab.grab(bbox=screenshot_region)
        # screenshot.save("src/sample/screenshot.png")  # Save the screenshot for reference

        # Define the image file (a small portion of the "Compose" button) you want to find
        image_to_find = "src/sample/compose.png"

        # Use PyAutoGUI's image recognition to find the location of the "Compose" button
        button_location = pyautogui.locateOnScreen(image_to_find, region=screenshot_region, confidence=0.8)
        if button_location:
            # Get the center of the "Compose" button and click it
            button_x, button_y = pyautogui.center(button_location)
            pyautogui.click(button_x, button_y)
        else:
            print("Compose button not found.")

        time.sleep(5)
        # Address and send the email.
        pyautogui.write(rec_email) 
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.press("tab")
        pyautogui.write(sub) 
        time.sleep(2)
        pyautogui.press("tab")
        pyautogui.write(body)  # Enter the email body.

        # Send the email.
        pyautogui.hotkey('ctrl', 'enter')

        time.sleep(3)  # Adjust the time for the email to be sent.

        # Close the browser.
        # pyautogui.hotkey('ctrl', 'w')

    # def main(self):
    #     # print("Press 'S' to send an email using pyautogui.")
    #     # keyboard.wait("s")
    #     self.send_email()
