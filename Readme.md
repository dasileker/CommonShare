# Automation Test Suite for test_commonShare
### Overview
This repository contains an automation test suite designed to validate the document upload and metadata entry process for the test_commonShare project. The test suite is developed using Selenium and Python, and it is configured to run in a continuous integration environment using GitHub Actions.

### Deliverables
1. Well-Documented Automation Test Suite
   The automation test suite includes the following key components:

- Test Scripts: Located in the tests/ directory, the test scripts cover various scenarios, including valid and invalid document uploads, metadata validation, and network failure handling.
Cross-Browser Testing: The test suite is configured to run on multiple browsers (Chrome, Firefox, Edge) to ensure cross-browser compatibility.
Dynamic Element Handling: Special attention has been given to handling dynamic elements that load based on user input.
2. Comprehensive Test Report with Analysis and Recommendations
   After running the tests, a detailed test report is generated, highlighting:

- Test Results: Success and failure of each test case.
Failed Cases: Detailed logs and screenshots for failed test cases to assist in debugging.
Analysis and Recommendations: Insights into potential issues and suggestions for improving the application’s stability and user experience.
The report is automatically generated and can be found in the GitHub Actions artifacts section after each run.

3. Brief Write-Up on Challenges and Solutions (500 words max)
   Challenges Faced
   Dynamic Elements: One of the primary challenges was dealing with dynamic elements that load based on previous user inputs. These elements required careful handling to ensure that the tests did not fail due to timing issues.
   Cross-Browser Compatibility: Ensuring that the tests run consistently across different browsers was another challenge. Browser-specific quirks sometimes caused tests to fail, which required implementing conditional logic and workarounds.
   Network Failure Simulation: Simulating a network failure during form submission was complex, as it required mimicking real-world conditions without causing false positives in the test results.
   Solutions Implemented
   WebDriverWait: Used WebDriverWait to handle dynamic elements, ensuring that the tests wait for elements to be fully loaded before interacting with them.
   Conditional Logic: Implemented conditional checks to handle browser-specific issues, ensuring the test suite is robust across different environments.
   Network Simulation: Leveraged Selenium’s ability to set network conditions, allowing for accurate simulation of network failures and validating that the application handles these scenarios gracefully.
   These solutions ensured that the automation test suite is reliable, maintainable, and scalable, providing comprehensive coverage of the application’s key functionalities.

- Getting Started
- Prerequisites
- Python 3.x
- Selenium
- pytest
- Google Chrome, Mozilla Firefox, Microsoft Edge
Chromedriver, Geckodriver, and Edgedriver (Ensure these are available in your system's PATH)
### Installation
Clone the repository:


git clone https://github.com/your-username/test_commonShare.git
cd test_commonShare
Install the required Python packages:


pip install -r requirements.txt
Running the Tests
To run the tests locally:


pytest -n 4 --html=report.html
This command will execute the tests in parallel across 4 threads and generate an HTML report (report.html).

CI/CD Integration
The test suite is integrated with GitHub Actions. Tests are automatically run on every pull request to the main branch. Test reports and artifacts are available in the GitHub Actions tab of the repository.

License
This project is licensed under the MIT License. See the LICENSE file for details.