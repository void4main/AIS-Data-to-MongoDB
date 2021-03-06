# AIS-Data-to-MongoDB
Read AIS data from UDP broadcast and write to MongoDB (quick and dirty)

Looks like that in the database (redundant data are intentional):

<pre>
{"_id":{"$oid":"5f25d51fcef27e42d0937b19"},
"nmea":{"ais_id":1,"raw":"!AIVDM,1,1,,B,139a8jPP030ea5PN`ovM;?vt0@BC,0*72","talker":"AI","msg_type":"VDM","count":1,"index":1,"seq_id":"","channel":"B","data":"139a8jPP030ea5PN`ovM;?vt0@BC","checksum":114,"bit_array":"000001000011001001101001001000110010100000100000000000000011000000101101101001000101100000011110101000110111111110011101001011001111111110111100000000010000010010010011"},
"decoded":{"type":1,"repeat":0,"mmsi":211437770,"status":0,"turn":-128,"speed":0.3,"accuracy":false,"lon":9.97064,"lat":53.54494833333333,"course":337.20000000000005,"heading":511,"second":30,"maneuver":0,"raim":false,"radio":66707},
"date":"2020-08-01 20:48:31.272159"}
<pre>
