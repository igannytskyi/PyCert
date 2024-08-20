# manages the creation, renewal, and downloading of certificates using an external API.

from .certificate_data import CertificateData
from .certificate_tracker import CertificateTracker
from utils.api_client import APIClient
from utils.logger import setup_logger


class CAManager:
    def __init__(self):
        self.logger = setup_logger(self.__class__.__name__)
        self.api_client = APIClient()
        self.certificate_data = CertificateData()
        self.certificate_tracker = CertificateTracker()

    def create_and_track_certificate(self, cert_data):
        # Store initial certificate data
        self.certificate_data.store_initial_data(cert_data)

        # Create certificate using external API
        cert = self.api_client.create_certificate(cert_data)

        if cert:
            # Track certificate
            self.certificate_tracker.track_certificate(cert_data["domain"], cert)
            self.logger.info(f"Certificate for {cert_data['domain']} created and tracked successfully.")
        else:
            self.logger.error(f"Failed to create certificate for {cert_data['domain']}.")

    def renew_certificate(self, domain_name):
        cert = self.api_client.renew_certificate(domain_name)
        if cert:
            self.certificate_tracker.update_certificate(domain_name, cert)
            self.logger.info(f"Certificate for {domain_name} renewed successfully.")
        else:
            self.logger.error(f"Failed to renew certificate for {domain_name}.")

    def download_certificate(self, domain_name):
        cert = self.api_client.download_certificate(domain_name)
        if cert:
            self.logger.info(f"Certificate for {domain_name} downloaded successfully.")
            return cert
        else:
            self.logger.error(f"Failed to download certificate for {domain_name}.")
            return None