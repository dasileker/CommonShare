# Automation Test Suite for test_commonShare
# Overview
Welcome to the test_commonShare automation test suite. This suite is designed to thoroughly test the document upload and metadata entry process for the commonShare project. Built with Selenium and Python, this suite ensures that all critical functions are tested across multiple browsers, providing reliable feedback for continuous integration.

# Key Components
## 1. Comprehensive Test Suite
   This repository includes a set of well-structured test scripts that cover a wide range of scenarios, ensuring the robustness of the commonShare platform. The key features of the test suite include:

Diverse Test Scenarios: From valid and invalid document uploads to network failure simulations, each script is tailored to test specific functionalities of the platform.
Cross-Browser Compatibility: The suite runs seamlessly on Chrome, Firefox, and Edge, ensuring consistent user experiences across different browsers.
Dynamic Element Handling: The tests are equipped to interact with elements that change dynamically based on user inputs.
## 2. Detailed Test Reporting
   After executing the tests, a comprehensive report is generated, which includes:

Test Outcomes: A clear overview of which tests passed and which failed, along with detailed reasons for any failures.
Error Analysis: Logs and screenshots of failed cases to help identify and troubleshoot issues quickly.
Recommendations: Insights on potential improvements to enhance the stability and performance of the platform.
These reports are available in the GitHub Actions artifacts section after each test run, providing easy access for review.

## 3. Insights and Solutions
   Overcoming Challenges
   During the development of this test suite, several challenges were encountered:

Handling Dynamic Elements: Some elements in the application load based on previous user inputs, requiring careful handling to avoid test failures.
Ensuring Cross-Browser Compatibility: Each browser has its quirks, and ensuring that tests run smoothly across Chrome, Firefox, and Edge was a key focus.
Simulating Network Failures: Accurately simulating network disruptions and ensuring the application’s resilience was a complex task.
Solutions Implemented
To address these challenges:

Dynamic Waits: Implemented WebDriverWait to ensure that tests wait for dynamic elements to fully load before interacting with them.
Browser-Specific Adjustments: Used conditional logic to handle browser-specific issues, ensuring robust and consistent test results.
Network Simulation: Leveraged Selenium’s network condition settings to simulate real-world scenarios like network failures, ensuring the application handles them gracefully.
These solutions have made the test suite highly reliable, maintainable, and scalable, providing thorough coverage of the application’s critical functionalities.

## Getting Started
### Prerequisites
Before running the tests, ensure you have the following installed:

- Python 3.x
- Google Chrome, Mozilla Firefox, Microsoft Edge
- WebDriver Executables: Chromedriver, Geckodriver, and Edgedriver (added to your system's PATH)
## Installation
Clone the repository:

`bash
Copy code
git clone https://github.com/your-username/test_commonShare.git
cd test_commonShare`
Set up Python environment and install dependencies:

Create a virtual environment (optional but recommended):

`bash
Copy code
python -m venv venv
source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
### Install required Python packages:

`bash
Copy code
pip install -r requirements.txt`
### Install Selenium:

If Selenium is not included in your requirements.txt, you can install it separately:

`bash
Copy code
pip install selenium`
This will install the Selenium WebDriver library, which is essential for running the browser automation scripts.

### Running the Tests
To execute the tests:

`bash
Copy code
pytest -n 4 --html=report.html`
This command will run the tests in parallel using 4 threads and generate an HTML report named report.html.

## Continuous Integration with GitHub Actions
The test suite is integrated with GitHub Actions, ensuring that tests are automatically executed on every pull request to the main branch. Test reports and artifacts are generated and accessible via the GitHub Actions tab in the repository.

## License
This project is licensed under the MIT License. For more details, see the LICENSE file in the repository.