
# Retrieving key from keyvault for OpenAI

This file describes the steps to retrieve the openAI key from keyvault. **Please make sure you are connected to JHU VPN.**

## Install the Required libraries
- pip install azure-keyvault-secrets azure-identity
- brew tap azure/azd && brew install azd

## VS Code
- extensions > search for Azure account > install
- extensions > search for Azure Developer CLI > install
- extensions > search for Azure Tools > install
- restart vs code
- go to A icon on the left side
	- sign in to azure using JHU credentials
	- open terminal
        - azd auth login 

- If you have SSL warning you can try
pip install urllib3==1.26.6

### Python code
Please check test_azure.py
