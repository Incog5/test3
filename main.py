try:
    import ubinascii
    import uhashlib
    import uos
    import machine
    import ssd1306
    import time

    ord = lambda x: x
    ESP = True
except ImportError:
    import binascii as ubinascii
    import hashlib as uhashlib
    import os as uos
    ESP = False

int2bytes = lambda x: ubinascii.unhexlify("{:x}".format(x))
bytes2int = lambda x: int("".join(["{:02x}".format(ord(c)) for c in x]), 16)


def generate(entropy):
    entbytes = int2bytes(entropy)
    width_bytes = len(entbytes)
    width_bits = width_bytes * 8
    assert width_bits in range(128, 257, 32)
    sha = uhashlib.sha256(int2bytes(entropy)).digest()
    checksum = sha[0:1]
    final = bytes2int(entbytes + checksum)
    mnemonic = [((final & (2047 << (x * 11))) >> (x * 11)) for x in range(24)]
    return list(reversed(mnemonic))


def get_words(indices):
    wordict = {}
    counter = 0
    infile = open("english.txt")
    for line in infile:
        if counter in indices:
            wordict[counter] = line.strip()
        counter += 1
    infile.close()
    return [wordict[index] for index in indices]

def generate_words(entropy):
    return get_words(generate(entropy))

if __name__ == "__main__":
    entropy = bytes2int(uos.urandom(32))
    words = generate_words(entropy)

    if not ESP:
        print(entropy)
        print(" ".join(words))
    else:
        i2c = machine.I2C(-1, machine.Pin(2), machine.Pin(4))
        display = ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)

        words.insert(0, "START WRITING")
        while True:
            for word in words:
                display.fill(0)
                display.text(word, 0, 0)
                display.show()
                time.sleep(4)
