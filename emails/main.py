import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import abort
from dotenv import load_dotenv


def get_bearer_token(request):

    bearer_token = request.headers.get('Authorization', None)
    if not bearer_token:
        abort(401)
    parts = bearer_token.split()
    if parts[0].lower() != 'bearer': # header must start with bearer
        abort(401)
    elif len(parts) == 1: # token not found
        abort(401)
    elif len(parts) > 2: # header must be of the form bearer_token
        abort(401)
        print(bearer_token)
    bearer_token = parts[1]

    return bearer_token


def send_mail(request):

    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python

    # dotenv_path = os.path.join(os.path.dirname(__file__), './../.env')
    # load_dotenv(dotenv_path)
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

    if request.method != 'POST':
        abort(405)

    bearer_token = get_bearer_token(request)
    secret_key = os.environ.get("ACCESS_TOKEN")
    if bearer_token != secret_key:
        abort(401)

    request_json = request.get_json(silent=True)
    parameters = ("sender", "receiver", "subject", "html_content")
    sender = receiver = subject = html_content = ""

    if request_json and all(k in request_json for k in parameters):
        sender = request_json["sender"]
        receiver = request_json["receiver"]
        subject = request_json["subject"]
        html_content = request_json["html_content"]
    else:
        abort(400)

    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=html_content
        )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        # response = sg.send(message)
        sg.send(message)
        return 'OK', 200
    except Exception as e:
        return e, 400