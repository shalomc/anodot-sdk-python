import requests
import datetime
import calendar
import json

class Anodot:
	response = {}
	http_status=0

	
# define some functions
	
# Helper function to build an Anodot metric name out of a dimensions dictionary
	def build_graphite_name( self, dimensions ) :
		dot = "."
		graphite_name = ''
		for key, value in dimensions.iteritems(): 
			if ( graphite_name == '' ):
				graphite_name = graphite_name + key + "=" + str(value)
			else:
				graphite_name = graphite_name + dot + key + "=" + str(value )
		return graphite_name
		
####################################################################################################
# Helper function to build an Anodot compatible object
# @name - string - metric name. Use build_graphite_name to build it, or build your own
# @value - number
# @timestamp - Unix timestamp. Default is now in UTC
# @target_type - string. gauge or counter
# @return_dict - boolean. If true (default), returns a dictionary. If false - returns a JSON string
	def build_payload( self, name,  value, timestamp= None , target_type=None, return_dict=None) :
		if ( timestamp == None):
			now = datetime.datetime.utcnow() 
			timestamp =  calendar.timegm(now.utctimetuple())
		anodot_array_elem= {
			"name" : name,
			"timestamp" : timestamp,
			"value" : value
			}
		if (target_type!=None) : 
			anodot_array_elem["tags"] = {"target_type": target_type}
		if (return_dict==None or return_dict == True ):
			return [ anodot_array_elem ]
		else:
			return json.dumps( [ anodot_array_elem ] )
			
			
####################################################################################################
# Function to send metrics to Anodot
# @payload - string/dict Currently string is not supported. Use build_payload helper function 
#			to create the payload
# @token - string - Account id
	def sendMetrics(self, payload, token): 
		# method is not yet implemented
		def executeAPI( anodot_command, anodot_payload , token, method=None):
			anodot_base_url = "https://api.anodot.com/api/v1/"
			action = anodot_command
			url =   anodot_base_url + action + '?token=' + token
			# url =  'http://dynamic.fastly.cdn.test.danidin.net/method.php'+ '?token=' + token
			headers = { 
					'Content-Type' : 'application/json',
					'Accept' : 'application/json'
					}
			r = requests.post(url,headers=headers, json=anodot_payload)
			# Print the result
			self.http_status = r.status_code
			return (r.content)
					
		result = executeAPI( 'metrics',  payload, token, 'POST' ) 
		return result
		
		
		