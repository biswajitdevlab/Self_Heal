# test_script.py

from framework import SelfHealingAutomationFramework
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    global driver
    # Instantiate the framework
    framework = SelfHealingAutomationFramework()

    # Define the URL for the Facebook login page
    facebook_login_url = "https://www.facebook.com"

    try:
        # Start the browser session
        driver = framework.driver

        # Extract locators and save to Excel file
        framework.extract_locators_to_excel(facebook_login_url)

        # Define test cases
        test_cases = [
            {
                'name': 'Facebook Login Test',
                'steps': [
                    {'action': 'input_text', 'element': 'mail', 'text': 'abc123@gmail.com'},
                    {'action': 'input_text', 'element': 'pass', 'text': 'rama3456'},
                    {'action': 'click', 'element': 'Log in'}
                ]
            }
        ]

        # Run the test cases
        framework.run(test_cases)

    finally:
        # Quit the browser session
        try:
            if driver:
                driver.quit()
        except Exception as e:
            print(f"Error while quitting the browser session: {str(e)}")
