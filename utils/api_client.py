import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://api.example.com/certificates"  # Example API URL

    def create_certificate(self, cert_data):
        try:
            response = requests.post(f"{self.base_url}/create", json=cert_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating certificate: {e}")
            return None

    def renew_certificate(self, domain_name):
        try:
            response = requests.post(f"{self.base_url}/renew", json={"domain": domain_name})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error renewing certificate: {e}")
            return None

    def download_certificate(self, domain_name):
        try:
            response = requests.get(f"{self.base_url}/download", params={"domain": domain_name})
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error downloading certificate: {e}")
            return None