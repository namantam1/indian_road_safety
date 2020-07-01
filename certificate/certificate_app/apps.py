from django.apps import AppConfig


class CertificateAppConfig(AppConfig):
    name = 'certificate_app'

    def ready(self):
        import certificate_app.signals
