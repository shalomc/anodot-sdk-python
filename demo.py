from anodot import Anodot

anodot = Anodot()
token='xxxxxxxxxxxxxxxxx'

# single metric
payload={"x":56, "what": "revenue"}
# set timestamp to None to automatically assign from system time
timestamp=None
event_payload_name = anodot.build_graphite_name(payload) 
event= anodot.build_payload(event_payload_name, 123, timestamp, 'gauge' ) 

print anodot.sendMetrics( event, token)
print anodot.http_status

# multiple metrics batch
# event a
payload_a={"x":56, "what": "revenue"}
revenue=123
event_payload_name = anodot.build_graphite_name(payload_a) 
event_a= anodot.build_payload(event_payload_name, revenue, timestamp, 'gauge' ) 
# event b
payload_b={"x":77, "what": "profit"}
event_payload_name = anodot.build_graphite_name(payload_b) 
profit=666
event_b= anodot.build_payload(event_payload_name, profit, timestamp, 'counter' ) 

# Send combined events
print anodot.sendMetrics( event_a+event_b, token)
print anodot.http_status