import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class DocumentFormTests(unittest.TestCase):

    # this part is for cross browser testing please Download and add the webdriver in your PATH.
    # Partially Covered: The test setup allows running tests across multiple browsers and supports switching between them easily.
    # However, documenting inconsistencies and implementing browser-specific workarounds would require additional steps based on the actual test results and observed issues.
    def setUp(self):
        # Set up Chrome WebDriver (you can change this to Firefox/Edge)
        self.browser = "chrome"  # You can change this to "firefox" or "edge"
        if self.browser == "chrome":
            self.driver = webdriver.Chrome()
        elif self.browser == "firefox":
            self.driver = webdriver.Firefox()
        elif self.browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise Exception("Browser not supported")
        self.driver.get("https://your-application-url.com")
        self.driver.maximize_window()

    # test for upload document with valid format and size
    def test_upload_valid_pdf_document(self):
        driver = self.driver

        # Step 1: PDF Document Upload with valid format and size
        upload_button = driver.find_element(By.ID, "upload-btn")
        upload_button.send_keys(os.path.abspath("path/to/valid_document.pdf"))

        # Validate successful upload
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "success-msg"))
        )
        self.assertIn("Upload Successful", success_message.text)

    def test_upload_valid_docx_document(self):
        driver = self.driver

        # Step 1: DOCX Document Upload with valid format and size
        upload_button = driver.find_element(By.ID, "upload-btn")
        upload_button.send_keys(os.path.abspath("path/to/valid_document.docx"))

        # Validate successful upload
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "success-msg"))
        )
        self.assertIn("Upload Successful", success_message.text)

    # test for upload document with invalid format
    def test_upload_invalid_format(self):
        driver = self.driver

        # Step 1: Document Upload with invalid format
        upload_button = driver.find_element(By.ID, "upload-btn")
        upload_button.send_keys(os.path.abspath("path/to/invalid_document.exe"))

        # Validate error message
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error-msg"))
        )
        self.assertIn("Invalid file format", error_message.text)

    # test for upload document with invalid size => 10mb.
    def test_upload_oversized_document(self):
        driver = self.driver

        # Step 1: Document Upload with oversized document
        upload_button = driver.find_element(By.ID, "upload-btn")
        upload_button.send_keys(os.path.abspath("path/to/oversized_document.pdf"))

        # Validate error message
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error-msg"))
        )
        self.assertIn("File size exceeds limit", error_message.text)


    # test for upload document with valid Metadata
    def test_enter_metadata(self):
        driver = self.driver

        # Step 1: Document Upload with valid document
        upload_button = driver.find_element(By.ID, "upload-btn")
        upload_button.send_keys(os.path.abspath("path/to/valid_document.pdf"))

        # Proceed to Step 2: Metadata Entry
        next_button = driver.find_element(By.ID, "next-btn")
        next_button.click()

        # Enter valid metadata
        title_input = driver.find_element(By.ID, "title")
        title_input.send_keys("Valid Title")

        description_input = driver.find_element(By.ID, "description")
        description_input.send_keys("Valid Description")

        category_input = driver.find_element(By.ID, "category")
        category_input.send_keys("Valid Category")

        # Validate the fields and move to next step
        next_button.click()

        # Validate successful navigation to Step 3
        step3_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "step3-msg"))
        )
        self.assertIn("Review your submission", step3_message.text)

    # test for upload document with invalid Metadata
    def test_invalid_metadata_submission(self):
        driver = self.driver

        # Step 1: Document Upload with valid document
        upload_button = driver.find_element(By.ID, "upload-btn")
        upload_button.send_keys(os.path.abspath("path/to/valid_document.pdf"))

        # Proceed to Step 2: Metadata Entry
        next_button = driver.find_element(By.ID, "next-btn")
        next_button.click()

        # Enter invalid metadata (e.g., missing title)
        description_input = driver.find_element(By.ID, "description")
        description_input.send_keys("Valid Description")

        category_input = driver.find_element(By.ID, "category")
        category_input.send_keys("Valid Category")

        # Attempt to proceed to next step
        next_button.click()

        # Validate error message due to missing title
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error-msg"))
        )
        self.assertIn("Title is required", error_message.text)

    # test for upload document with network fails
    def test_form_submission_with_network_failure(self):
        driver = self.driver

        # Step 1: Document Upload with valid document
        upload_button = driver.find_element(By.ID, "upload-btn")
        upload_button.send_keys(os.path.abspath("path/to/valid_document.pdf"))

        # Proceed to Step 2: Metadata Entry
        next_button = driver.find_element(By.ID, "next-btn")
        next_button.click()

        # Enter valid metadata
        title_input = driver.find_element(By.ID, "title")
        title_input.send_keys("Valid Title")

        description_input = driver.find_element(By.ID, "description")
        description_input.send_keys("Valid Description")

        category_input = driver.find_element(By.ID, "category")
        category_input.send_keys("Valid Category")

        # Move to Step 3: Submission Confirmation
        next_button.click()

        # Simulate network failure by disconnecting from the network
        # This part would be environment-specific. Here, we simulate by stopping the WebDriver.
        driver.set_network_conditions(
            offline=True,
            latency=5,  # in milliseconds
            throughput=500 * 1024,  # 500 kbps
        )

        # Try submitting the form
        submit_button = driver.find_element(By.ID, "submit-btn")
        submit_button.click()

        # Validate handling of network failure
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "network-error-msg"))
        )
        self.assertIn("Network error", error_message.text)

        # Restore network connection
        driver.set_network_conditions(
            offline=False,
            latency=0,
            throughput=5000 * 1024,  # 5 Mbps
        )

    # test of document that triggers dynamic elements
    def test_dynamic_element_loading(self):
        driver = self.driver

        # Step 1: Select a document type that triggers dynamic elements
        document_type_dropdown = driver.find_element(By.ID, "document-type")
        document_type_dropdown.click()

        # Select a type that causes additional fields to appear
        specific_type = driver.find_element(By.XPATH, "//option[text()='Specific Type']")
        specific_type.click()

        # Wait for dynamic elements to load
        dynamic_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "dynamic-field"))
        )

        # Validate the dynamic field is present and interactable
        self.assertTrue(dynamic_field.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
