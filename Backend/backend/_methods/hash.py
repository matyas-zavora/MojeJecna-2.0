import hashlib

def sha256_hash(input_string):
    # Vytvoříme objekt pro SHA-256 hash
    sha256 = hashlib.sha256()

    # Převedeme vstupní řetězec na bajty, protože hashlib očekává bajty
    input_bytes = input_string.encode('utf-8')

    # Aktualizujeme hash s vstupními daty
    sha256.update(input_bytes)

    # Získáme hash v hexadecimálním formátu
    hashed_string = sha256.hexdigest()

    return hashed_string