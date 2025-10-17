# Pogo-Automation
Automation of pogo.com to register, search, loginlogout

#Install requirements before running testcases
pip install -r requirements.txt

# NOTE:
While registration, captcha should be entered manually and OTP sent in email should be entered manually. 
20 seconds wait to enter captcha and OTP

# To run all testcases as per assignments
pytest tests/ -s

# To run particular test (run test_filename)
pytest tests/test_registration.py 