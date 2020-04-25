from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hola():
    return 'Hello world'

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    msg = request.form.get('Body')
    print(msg)
    resp = MessagingResponse()

    # Add a message
    resp.message("Hola soy un bot")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)