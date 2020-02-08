def int32_to_ip(int32):
    binary = bin(int32)[2:]
    binary = binary.zfill(32)
    bin_dots = binary[:8] + '.' + binary[8:16] + '.' + binary[16:24] + '.' + binary[24:]
    bin_parts = bin_dots.split('.')
    dec_parts = []
    for part in bin_parts:
        dec_parts.append(str(int(part, 2)))
    return '.'.join(dec_parts)
