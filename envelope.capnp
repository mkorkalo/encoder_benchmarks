@0xf2e39dfe2dfa12ad;

struct Envelope {
  id @0 :Int64;
  replyId @1 :Int64;
  dst @2 :Text;
  src @3 :Text;
  msgEncoding @4 :MessageEncodingType;
  msg @5 :Data;

  enum MessageEncodingType {
      bson @0;
      json @1;
      binary @2;
  }
  
}

