from driver_setup import create_driver
import time

def run_example_login_flow():
    """
    Non-functional example of how a login flow could be structured.
    This does NOT target a specific site and does NOT perform real login.
    """

    driver = create_driver(headless=False)
    try:
        # Placeholder URL (generic example site)
        driver.get("https://example.com/login")

        # In a real flow, you would:
        # - locate username field
        # - locate password field
        # - locate submit button
        # - apply waits and checks

        time.sleep(2)
        print("Loaded login page (demo).")

        # Example of how structure might look:
        # username_input = driver.find_element(...)
        # password_input = driver.find_element(...)
        # username_input.send_keys("demo_user")
        # password_input.send_keys("demo_pass")
        # submit_button.click()

        time.sleep(2)
        print("Finished demo flow (no real login performed).")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_example_login_flow()
