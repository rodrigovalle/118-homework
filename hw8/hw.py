from bitstring import BitArray

def HDLC(input):
    oseq = BitArray('0x7e')
    bits_in_a_row = 0

    for bit in input:
        oseq.append('0b1' if bit else '0b0')

        if bit:
            bits_in_a_row += 1
        else:
            bits_in_a_row = 0

        if bits_in_a_row == 5:
            oseq.append('0b0')
            bits_in_a_row = 0

    oseq.append('0x7e')
    return oseq

def as_bytes(lst):
    i = iter(lst)
    while True:
        x = next(i)
        y = next(i)
        yield '0x' + x + y

def PPP(input):
    oseq = BitArray('0x7e')
    
    for byte in as_bytes(input.hex):
        if byte == '0x7e':
            oseq.append('0x7d, 0x5e')
        elif byte == '0x7d':
            oseq.append('0x7d, 0x5d')
        else:
            oseq.append(byte)

    oseq.append('0x7e')
    return oseq

def COBS(input):
    oseq = BitArray('0x00')

    def next_nonzero(input):
        nonzero = []
        count = 1
        for byte in as_bytes(input.hex):
            if byte == '0x00':
                yield '0x{:02x}'.format(count)
                count = 1
            else:
                count += 1
        yield '0x{:02x}'.format(count)

    gen = next_nonzero(input)

    oseq.append(next(gen))
    for byte in as_bytes(input.hex):
        if byte == '0x00':
            oseq.append(next(gen))
        else:
            oseq.append(byte)

    oseq.append('0x00')
    return oseq

if __name__ == '__main__':
    test1 = BitArray('0x00, 0x01, 0x02, 0xFF, 0x7E, 0x7D, 0x00, 0x00, 0x7D, 0xFD, 0x7E')
    test2 = BitArray('0x02, 0x00, 0x01, 0x02, 0x7D, 0x00')

    print('test 1:', end=' ')
    for byte in as_bytes(test1.hex):
        print(byte, end=' ')
    print()
    print('test 2:', end=' ')
    for byte in as_bytes(test2.hex):
        print(byte, end=' ')
    print()

    print()

    print('HDLC:')
    print('test 1:', end=' ')
    for i, b in enumerate(HDLC(test1).bin, 1):
        print(b, end='')
        if i % 8 == 0:
            print('', end=' ')
    print()
    print('test 2:', end=' ')
    for i, b in enumerate(HDLC(test2).bin, 1):
        print(b, end='')
        if i % 8 == 0:
            print('', end=' ')

    print()

    print('PPP:')
    print('test 1:', end=' ')
    for byte in as_bytes(PPP(test1).hex):
        print(byte, end=' ')
    print()
    print('test 2:', end=' ')
    for byte in as_bytes(PPP(test2).hex):
        print(byte, end=' ')
    print()

    print()

    print('COBS:')
    print('test 1:', end=' ')
    for byte in as_bytes(COBS(test1).hex):
        print(byte, end=' ')
    print()
    print('test 2:', end=' ')
    for byte in as_bytes(COBS(test2).hex):
        print(byte, end=' ')
    print()
