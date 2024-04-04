import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID

def generate_csr_from_json(json_file):
    with open(json_file, 'r') as f:
        configurations = json.load(f)

    for config in configurations:
        common_name = config['common_name']
        country = config['country']
        state = config['state']
        locality = config['locality']
        organization = config['organization']
        organizational_unit = config['organizational_unit']

        # Generate a private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        # Generate a CSR
        csr_builder = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organizational_unit)
        ]))

        csr = csr_builder.sign(private_key, hashes.SHA256())

        # Serialize the CSR
        csr_bytes = csr.public_bytes(serialization.Encoding.PEM)

        # Serialize the private key
        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Write the CSR to a file
        with open(f"output/{common_name}.csr", "wb") as csr_file:
            csr_file.write(csr_bytes)

        # Write the private key to a file
        with open(f"output/{common_name}.key", "wb") as private_key_file:
            private_key_file.write(private_key_bytes)


# Example usage
generate_csr_from_json('conf/cert.json')
