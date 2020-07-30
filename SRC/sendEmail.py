import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


def enviaMail(receptor):
    
    """
        This function takes care of sending the email with the PDF report.
    """
    # Setting all the necessary passes and emails
    key = os.getenv("REPASS")
    message = MIMEMultipart('alternative')
    message['Subject'] = "Surf report: STAY RIDIN'!"
    message['From'] = 'letsgosurfingapp@gmail.com'

    # Sending the attached file
    nombre_adjunto = "Report"
    archivo_adjunto = open("OUTPUT/forecastPDF.pdf", 'rb')
    # Creating a MIME object to later on add the attached file
    message.attach(MIMEText("Hi, please find attached the PDF report with the surf forecast. STAY RIDIN'!", 'plain'))
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    text = "Hi, please find attached the PDF report with the surf forecast. STAY RIDIN'!"
    # Adding the attached file
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codifiying the object to base64
    encoders.encode_base64(adjunto_MIME)
    # Adding a content description to the email
    adjunto_MIME.add_header('Content-Disposition', f"attachment; filename= {nombre_adjunto}.pdf",)
    # We finally add it to the message and send it
    message.attach(adjunto_MIME)
    text = message.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('letsgosurfingapp@gmail.com', f'{key}')
    server.sendmail('uscoburgo@gmail.com', f'{receptor}', text)
    server.quit()

