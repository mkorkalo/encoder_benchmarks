# encoder_benchmarks
Ad-hoc python encoder benchmarking tool: supports JSON, BSON, MsgPack, Cap'n'Proto
# Results from run
```
(venv) Mikkos-MacBook-Pro:encoder_benchmarks keitsi$ python speed.py
Encoder JsonEncoder, payload length 14 bytes, elapsed 1.255 seconds for 100000 encode/decode cycles, rate 79698.619/sec, encoded length 112 bytes
Encoder CapEncoder, payload length 14 bytes, elapsed 0.563 seconds for 100000 encode/decode cycles, rate 177571.553/sec, encoded length 80 bytes
Encoder BsonEncoder, payload length 14 bytes, elapsed 4.3 seconds for 100000 encode/decode cycles, rate 23255.267/sec, encoded length 104 bytes
Encoder MsgPackEncoder, payload length 14 bytes, elapsed 0.628 seconds for 100000 encode/decode cycles, rate 159359.205/sec, encoded length 74 bytes
Encoder JsonEncoder, payload length 1000000 bytes, elapsed 1.157 seconds for 100 encode/decode cycles, rate 86.434/sec, encoded length 1333430 bytes
Encoder CapEncoder, payload length 1000000 bytes, elapsed 0.033 seconds for 100 encode/decode cycles, rate 3030.61/sec, encoded length 1000080 bytes
Encoder BsonEncoder, payload length 1000000 bytes, elapsed 0.049 seconds for 100 encode/decode cycles, rate 2036.871/sec, encoded length 1000090 bytes
Encoder MsgPackEncoder, payload length 1000000 bytes, elapsed 0.022 seconds for 100 encode/decode cycles, rate 4537.817/sec, encoded length 1000064 bytes
```
