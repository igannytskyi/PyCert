#Manages the initial data required to create certificates.
class CertificateData:
    def __init__(self):
        self.certificates = {}

    def store_initial_data(self, cert_data):
        # Store the initial data needed for creating a certificate
        domain = cert_data["domain"]
        self.certificates[domain] = cert_data
        print(f"Initial certificate data stored for {domain}")

    def get_initial_data(self, domain):
        # Retrieve initial data for a certificate
        return self.certificates.get(domain, None)