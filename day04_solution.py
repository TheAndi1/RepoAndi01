import hashlib
import itertools

def find_hash_for(secret_key, count_of_zeros):
    zero_string = '0' * int(count_of_zeros)
    for secret_decimal in itertools.count():
        # key und dezimalzahl zu einem string umwandeln
        secret_value = f"{secret_key}{secret_decimal}"
        # secret_value encodieren und an hash-funktion übergeben
        result = hashlib.md5(secret_value.encode())
        # prüfen, ob hash-wert mit 5 nullen beginnt
        if result.hexdigest().startswith(zero_string):
            return secret_decimal

#print(find_hash_for('yzbqklnj', 5))
#print(find_hash_for('yzbqklnj', 6))

#5 Nullen
#assert find_hash_for('abcdef', 5) == 609043
#assert find_hash_for('pqrstuv', 5) == 1048970
#assert find_hash_for('yzbqklnj', 5) == 282749

#6 Nullen
#assert find_hash_for('yzbqklnj', 6) == 9962624