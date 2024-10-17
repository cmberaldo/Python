# Cristiano Martins Beraldo

'''
 Import all required libraries and functions
'''

import os
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import streamlit as st


def generate_rsa_key_pair():
    """
    Generate RSA key pair (public and private keys)
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def save_private_key(private_key, filename):

    """
    Save Private key in a file to preserve
    """
    with open(os.path.join(os.path.dirname(__file__), filename), "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

def save_public_key(public_key, filename):

    """
    Save Public key in a file to preserve
    """
    with open(os.path.join(os.path.dirname(__file__), filename), "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def load_private_key(filename):

    """
    Load private key from a file
    """
    with open(os.path.join(os.path.dirname(__file__), filename), "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

def load_public_key(filename):

    """
    Load public key from a file
    """
    with open(os.path.join(os.path.dirname(__file__), filename), "rb") as f:
        return serialization.load_pem_public_key(f.read(), backend=default_backend())

def encrypt_file(public_key, input_file, encrypted_file_path):

    """
    Function to encrypt a file with public key
    """
    # reading the content of the file
    data = input_file.getvalue()
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # write the encrypt file
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt_file(private_key, encrypted_file_path, decrypted_file_path):

    """
    Function to decrypt a file with private key
    """
    # reading the content of the file
    encrypted_data = encrypted_file_path.getvalue()
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # write the decrypt file
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def generate_hash(file_path):

    """
    Generate a hash of the original file using SHA-256
    """
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65537)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def verify_integrity(original_file_path, received_file_path):

    """
    Verify the integrity of the received file by comparing its hash with the original hash
    """
    # create a hash from original and received files
    original_hash = generate_hash(original_file_path)
    received_hash = generate_hash(received_file_path)
    return original_hash == received_hash


if __name__ == "__main__":
    # title of webpage
    st.title("Secure File Transfer System")
    # box of selection with 3 options
    option = st.selectbox("Select an option", ["Encrypt File", "Decrypt File", "Verify Integrity"])

    # test if file keys exists
    # If yes, read the keys from files
    # If no generate new keys and files
    if os.path.exists(os.path.join(os.path.dirname(__file__), "private_key.pem")) and os.path.exists(os.path.join(os.path.dirname(__file__), "public_key.pem")):
        private_key = load_private_key("private_key.pem")
        public_key = load_public_key("public_key.pem")
        st.write("RSA key pair loaded.")
    else:
        private_key, public_key = generate_rsa_key_pair()
        save_private_key(private_key, "private_key.pem")
        save_public_key(public_key, "public_key.pem")
        st.write("RSA key pair generated and saved.")

    # first option
    if option == "Encrypt File":
        st.header("File Encryption")
        # user choose the file to encrypt
        file_to_encrypt = st.file_uploader("Upload file to encrypt:")
        if file_to_encrypt is not None:
            # create a file path
            encrypted_file_path = os.path.join(os.path.dirname(__file__), file_to_encrypt.name + '.enc')
            # wait the button to encrypt the file
            if st.button("Encrypt"):
                encrypt_file(public_key, file_to_encrypt, encrypted_file_path)
                st.success("File encrypted successfully.")
    # second option
    elif option == "Decrypt File":
        st.header("File Decryption")
        # user choose the file to decrypt
        encrypted_file = st.file_uploader("Upload encrypted file:")
        if encrypted_file is not None:
            # user type the decrypt file name
            decrypted_name = st.text_input("Type the name of decrypted file")
            if decrypted_name:
                # create a file path
                decrypted_file_path = os.path.join(os.path.dirname(__file__), decrypted_name + '.dec.txt')
                # wait the button to decrypt the file
                if st.button("Decrypt"):
                    decrypt_file(private_key, encrypted_file, decrypted_file_path)
                    st.success("File decrypted successfully.")
    # third option
    elif option == "Verify Integrity":
        st.header("Integrity Verification")
        # user choose the files to verify
        original_file = st.file_uploader("Upload original file:")
        received_file = st.file_uploader("Upload received file:")

        if original_file is not None and received_file is not None:
            # create a file paths
            original_file_path = os.path.join(os.path.dirname(__file__), original_file.name)
            received_file_path = os.path.join(os.path.dirname(__file__), received_file.name)
            is_integrity_verified = verify_integrity(original_file_path, received_file_path)
            if is_integrity_verified:
                st.success("Integrity verified: The received file matches the original file.")
            else:
                st.error("Integrity verification failed: The received file has been tampered with.")

