# tracks the status and information of issued certificates

class CertificateTracker:
    def __init__(self):
        self.tracked_certificates = {}

    def track_certificate(self, domain, certificate):
        # Track issued certificate details
        self.tracked_certificates[domain] = certificate
        print(f"Tracking certificate for {domain}")

    def update_certificate(self, domain, certificate):
        # Update the tracked certificate after renewal
        if domain in self.tracked_certificates:
            self.tracked_certificates[domain] = certificate
            print(f"Updated tracking for {domain}")
        else:
            print(f"Domain {domain} not found in tracked certificates.")

    def get_certificate(self, domain):
        # Retrieve the tracked certificate details
        return self.tracked_certificates.get(domain, None)