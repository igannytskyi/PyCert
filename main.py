from ca.ca_manager import CAManager
from cert_deployment.deploy_manager import DeployManager
from monitoring.cert_monitor import CertMonitor
import argparse
from utils.config import ConfigLoader


def main():
    # Set up argument parser to accept environment as a parameter
    parser = argparse.ArgumentParser(description="Certificate Management Framework")
    parser.add_argument(
        '--env',
        type=str,
        required=True,
        help='Specify the environment (dev, test)'
    )

    # Parse the arguments
    args = parser.parse_args()
    environment = args.env

    # Initialize CA Manager
    ca_manager = CAManager()

    # Example: Create and track a certificate
    domain_name = "example.com"
    cert_data = {
        "domain": domain_name,
        "organization": "Example Org",
        "email": "admin@example.com"
    }
    ca_manager.create_and_track_certificate(cert_data)

    # Deploy the certificate
    deploy_manager = DeployManager()
    deploy_manager.deploy_certificate(domain_name)

    # Monitor certificates
    cert_monitor = CertMonitor()
    cert_monitor.monitor_expiry()


if __name__ == "__main__":
    main()