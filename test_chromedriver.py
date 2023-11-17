# Python script to test chromedriver functionality

# Importing required dependencies
import undetected_chromedriver as uc

def test():
	print("Starting testing")
	driver = uc.Chrome(headless=True,use_subprocess=False)
	driver.get('https://nowsecure.nl')
	driver.save_screenshot('nowsecure.png')	
	print("Ending testing")
if __name__ == "__main__":
	test()
