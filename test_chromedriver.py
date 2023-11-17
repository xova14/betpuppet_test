# Python script to test chromedriver functionality

# Importing required dependencies
import undetected_chromedriver as uc
import time
from pyvirtualdisplay import Display


display = Display(visible=0, size=(1024, 768))
display.start()

def test():
	print("Starting testing")
	time.sleep(5)
	driver = uc.Chrome(headless=False, use_subprocess=False)
	driver.get('https://nowsecure.nl')
	driver.save_screenshot('/shared/nowsecure.png')	
	print("Ending testing")
if __name__ == "__main__":
	test()
