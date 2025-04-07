from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

from constants import FILE_NAME, SECRET_KEY

class Utils:
    def __init__(self):
        # Convert the SECRET_KEY string to bytes
        self.password = SECRET_KEY.encode()

        # Derive a key using PBKDF2HMAC
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'Navya20B!#%&(_',  # You can generate a random salt or use a fixed one
            iterations=100000,
            backend=default_backend()
        )
        self.key = kdf.derive(self.password)

        # Encode the key in URL-safe base64 format
        url_safe_key = base64.urlsafe_b64encode(self.key)
        self.filename = FILE_NAME
        self.cipher = Fernet(url_safe_key)
    
    def encrypt_token_and_save(self, token):
        # Encrypt the data
        encrypted_data = self.cipher.encrypt(token.encode())

        # Write the encrypted data to a file
        with open(self.filename, "wb") as file:
            file.write(encrypted_data)

    def decrypt_token(self):
        try:
            # Read the encrypted data from the file
            with open(self.filename, "rb") as file:
                encrypted_data = file.read()

            # Decrypt the data
            decrypted_data = self.cipher.decrypt(encrypted_data)
            token = decrypted_data.decode()
            return True, token
        except FileNotFoundError:
            print("Exception decrypt_token: FileNotFoundError")
            return False, ''
        except Exception as e:
            print("Exception decrypt_token: ",str(e))
            return False, ''

    def greet_user(self):
        current_time = datetime.now()
        hour = current_time.hour

        if 6 <= hour < 12:
            return "Good morning!"
        elif 12 <= hour < 18:
            return "Good afternoon!"
        elif 18 <= hour < 22:
            return "Good evening!"
        else:
            return "Good night!"