import capnp
import envelope_capnp
import json
import bson
import time, os
import base64
import msgpack

class DictEncoder:
	def encode(self, testData):
		ev = {
			"id" : 6000,
			"src" : "lahde",
			"dst" : "kohde",
			"msg_type" : "test",
			"msg_encoding" : 1,
		}
		if isinstance(testData, str):
			ev["msg_encoding"] = 2
			ev["msg"] = testData
		else:
			ev["msg_encoding"] = 1
			ev["msg"] = self.encodeInner(testData)

		return self.dumps(ev)
		
	def decode(self, d):
		msg = self.loads(d)
		try:
			if msg["id"] != 6000:
				print("Invalid id")
		except:
			print(str(msg))
			raise
		if msg["msg_encoding"] == 1:
			return self.decodeInner(msg["msg"])
		else:
			return msg["msg"]

class MsgPackEncoder(DictEncoder):
	def encodeInner(self, x):
		return x
	def decodeInner(self, x):
		return x
	def dumps(self, x):
		return msgpack.packb(x, use_bin_type=True)
	def loads(self, x):
		return msgpack.unpackb(x, raw=False)

class JsonEncoder(DictEncoder):
	def encodeInner(self, x):
		return base64.b64encode(x).decode("utf-8")
	def decodeInner(self, x):
		return base64.b64decode(x)
	def dumps(self, x):
		return json.dumps(x)
	def loads(self, x):
		return json.loads(x)
class BsonEncoder(DictEncoder):
	def encodeInner(self, x):
		return x
	def decodeInner(self, x):
		return x
	def dumps(self, x):
		return bson.dumps(x)
	def loads(self, x):
		return bson.loads(x)

class CapEncoder():
	def encode(self, testData):
		ev = envelope_capnp.Envelope.new_message()
		ev.msgEncoding = 'json'
		ev.msg = testData
		return ev.to_bytes()

	def decode(self, d):
		ev = envelope_capnp.Envelope.from_bytes(d)
		return ev.msg

class Test:
	def run(self):
		encoders = [ JsonEncoder(), CapEncoder(), BsonEncoder(), MsgPackEncoder() ]
		shortData = json.dumps({"foo":"bar"})
		bigData = os.urandom(1000000)

		tests = [
			{ "iterations" : 100000, "data" : shortData },
			{ "iterations" : 100, "data" : bigData },
			]
		for test in tests:
			for enc in encoders:
				self.bench(enc, test["data"], test["iterations"])
	def bench(self, enc, testData, times):
		encoderName = type(enc).__name__
		#print("Testing encoder {} with test data length {}".format(encoderName, len(testData)))
		start = time.time()
		encodedSize = None
		for i in range(times):
			ev = enc.encode(testData)
			encodedSize = len(ev)
			d = enc.decode(ev)
			if len(d) != len(testData):
				print("Test data different: {} vs {}".format(d, testData))
				raise Exception()
		end = time.time()
		elapsed = end - start
		print("Encoder {}, payload length {} bytes, elapsed {} seconds for {} encode/decode cycles, rate {}/sec, encoded length {} bytes".format(
			encoderName, len(testData), round(elapsed, 3), times, round(times/elapsed, 3), encodedSize))

if __name__ == '__main__':
	p = Test()
	p.run()
