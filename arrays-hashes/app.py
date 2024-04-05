from medium.encodedecode import EncodeDecode


def main():

    cs = EncodeDecode()
    
    encoded = cs.encode(["tobi", "tope", "wa?le", "samu#el", "sam-?son"])
    print(encoded)

    decoded = cs.decode(encoded)
    print(decoded)

main()