"""Email service."""

import os
import smtplib
from email.message import EmailMessage
from typing import Optional


class EmailService:
    """Service for sending emails."""

    def __init__(self):
        """Initialize email service with SMTP configuration."""
        self.smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
        self.smtp_port = int(os.environ.get("SMTP_PORT", "587"))
        self.smtp_user = os.environ.get("SMTP_USER", "")
        self.smtp_pass = os.environ.get("SMTP_PASS", "")

    def is_configured(self) -> bool:
        """Check if email service is properly configured."""
        return bool(self.smtp_user and self.smtp_pass)

    def send_email(
        self,
        to_email: str,
        subject: str,
        text_body: str,
        html_body: Optional[str] = None,
    ) -> bool:
        """Send email."""
        if not self.is_configured():
            return False

        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = self.smtp_user
            msg["To"] = to_email

            msg.set_content(text_body)

            if html_body:
                msg.add_alternative(html_body, subtype="html")

            with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
                smtp.starttls()
                smtp.login(self.smtp_user, self.smtp_pass)
                smtp.send_message(msg)

            return True
        except Exception:
            return False

    def send_reset_password_email(self, to_email: str, nombre: str, reset_url: str) -> bool:
        """Send password reset email."""
        subject = "Restablecer tu contraseña - Check-in Viajes"

        text_body = f"""
Hola {nombre},

Para restablecer tu contraseña, haz clic en el siguiente enlace:
{reset_url}

Si no solicitaste este cambio, ignora este correo.

Saludos,
Check-in Viajes
        """

        html_body = f"""
        <html>
            <body>
                <h2>Hola {nombre},</h2>
                <p>Para restablecer tu contraseña, haz clic en el siguiente enlace:</p>
                <p><a href="{reset_url}" style="background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">Restablecer Contraseña</a></p>
                <p>Si no solicitaste este cambio, ignora este correo.</p>
                <p>Saludos,<br/>Check-in Viajes</p>
            </body>
        </html>
        """

        return self.send_email(to_email, subject, text_body, html_body)

    def send_reservation_confirmation(self, to_email: str, nombre: str, viaje_nombre: str) -> bool:
        """Send reservation confirmation email."""
        subject = f"Confirmación de Reserva - {viaje_nombre}"

        text_body = f"""
Hola {nombre},

¡Gracias por tu reserva! Tu viaje '{viaje_nombre}' ha sido confirmado.

Pronto recibirás más informaciónes en tu correo.

Saludos,
Check-in Viajes
        """

        html_body = f"""
        <html>
            <body>
                <h2>Hola {nombre},</h2>
                <p>¡Gracias por tu reserva!</p>
                <p>Tu viaje <strong>{viaje_nombre}</strong> ha sido confirmado.</p>
                <p>Pronto recibirás más información en tu correo.</p>
                <p>Saludos,<br/>Check-in Viajes</p>
            </body>
        </html>
        """

        return self.send_email(to_email, subject, text_body, html_body)

    def send_welcome_email(self, to_email: str, nombre: str) -> bool:
        """Send welcome email to new user."""
        subject = "¡Bienvenido a Check-in Viajes!"

        text_body = f"""
Hola {nombre},

¡Bienvenido a Check-in Viajes!

Tu cuenta ha sido creada exitosamente. Ahora puedes explorar nuestros increíbles viajes y hacer reservas.

Saludos,
Check-in Viajes
        """

        html_body = f"""
        <html>
            <body>
                <h2>¡Hola {nombre}!</h2>
                <p>Bienvenido a <strong>Check-in Viajes</strong></p>
                <p>Tu cuenta ha sido creada exitosamente.</p>
                <p>Ahora puedes explorar nuestros increíbles viajes y hacer reservas.</p>
                <p>Saludos,<br/>Check-in Viajes</p>
            </body>
        </html>
        """

        return self.send_email(to_email, subject, text_body, html_body)
