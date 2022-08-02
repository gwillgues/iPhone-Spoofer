# iPhone-Spoofer
iPhone spoofer that exploits the MIME Sub-Header Vulnerability

Attempted to report to Apple in March 2021. Unknown if its an issue with the way iPhone handles the messages or T mobile.

for a writeup on this, see https://willgu.es/?p=92

To use, create a valid email account with a provider that supports SMTP. Then change the SMTP server on the following line:
    server = smtplib.SMTP('mail.example.com', port=587)
Then, change the email and password to your credentials in the following line:
    server.login("testspoofiphone@example.com", "willgues_security_password")
Then, change the email in the "To" section of the MIME headers to the phone number and email to SMS gateway you want to use. The gateway used in the example will work for T Mobile phones:
    msg['To'] = "some-phone-number@tmomail.net"

Then, change the last sendmail line to have your actual sending email, and the destiniation phone + sms gateway, This line does NOT contain the spoofed email you want to send as:

    server.sendmail("testspoofiphone@example.com", "some-phone-number@tmomail.net", text)
