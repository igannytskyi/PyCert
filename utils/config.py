import json
import os


class ConfigLoader:
    def __init__(self, environment):
        self.environment = environment
        self.config_path = os.path.join('config', self.environment)

    def load_certificate_data(self):
        cert_data_path = os.path.join(self.config_path, 'certificate_data.json')
        with open(cert_data_path, 'r') as file:
            return json.load(file)

    def load_hosts_data(self):
        hosts_data_path = os.path.join(self.config_path, 'hosts.json')
        with open(hosts_data_path, 'r') as file:
            return json.load(file)


# Example usage:
# Set the environment to load configuration for the respective environment
environment = os.getenv('CERT_ENV', 'test')  # Default to 'test' if not set

config_loader = ConfigLoader(environment)

# Load environment-specific certificate data
cert_data = config_loader.load_certificate_data()

# Load environment-specific hosts data
hosts_data = config_loader.load_hosts_data()

# Example of accessing configuration details
common_name = cert_data['common_name']
hosts = hosts_data['hosts']

for host in hosts:
    print(f"Deploying certificate to host: {host['host_name']} with IP: {host['ip']}")