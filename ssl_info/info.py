import socket
import argparse
from datetime import datetime, UTC
import ssl


def get_cert_info(hostname="reddit.com"):
    context = ssl.create_default_context()
    cert_info = dict()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert_info = ssock.getpeercert()
    return cert_info


def get_expiration_date(cert_info):

    ssl.cert_time_to_seconds(cert_info["notAfter"])
    timestamp = ssl.cert_time_to_seconds(cert_info["notAfter"])

    cert_info_list = [item[0] for item in list(cert_info["subject"])]
    cert_info_dict = {k: v for k, v in cert_info_list}

    print(cert_info_dict["commonName"])
    print(datetime.fromtimestamp(timestamp, UTC))


def parse_args():
    parser = argparse.ArgumentParser(description="Retrieves TLS/SSL certificate information from a given endpoint")
    parser.add_argument("-e", "--endpoint", help="endpoint to check", default="reddit.com", type=str)
    args = parser.parse_args()
    return args.endpoint


def main():
    endpoint = parse_args()
    cert_info = get_cert_info(endpoint)
    get_expiration_date(cert_info)


if __name__ == "__main__":
    main()
