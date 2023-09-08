# Python ANS library
Codes are detached from: [CompressAI](https://github.com/InterDigitalInc/CompressAI/tree/master) and [ryg_ans](https://github.com/rygorous/ryg_rans)
## Install
```
python setup.py build
python setup.py install
```
## Uninstall
```
pip uninstall pyans
```
## Usage
```
import rans
encoder = rans.BufferedRansEncoder()
encoder.encode_with_indexes(symbols, indexes, cdf, cdf_length, cdf_offset)
b = encoder.flush()
decoder = rans.RansDecoder()
decoder.set_stream(b)
recon = decoder.decode_stream(indexes, cdf, cdf_length, cdf_offset)
```
Other usages may follow `cpp_exts/rans/rans_interface.hpp`
## Verify installation
```
python test.py
```