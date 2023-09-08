import rans

symbols = [1, 0, 1, 1]
indexes = [0, 0, 0, 0]
cdf = [[0, 10000, 65536]]
cdf_length=[3]
cdf_offset = [0]

encoder = rans.BufferedRansEncoder()
encoder.encode_with_indexes(symbols, indexes, cdf, cdf_length, cdf_offset)
b = encoder.flush()
decoder = rans.RansDecoder()
decoder.set_stream(b)
recon = decoder.decode_stream(indexes, cdf, cdf_length, cdf_offset)
print("bytes =", b, "num_bits =", len(b)*8, symbols, recon)