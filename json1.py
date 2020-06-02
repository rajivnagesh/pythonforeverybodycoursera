import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data) #creates a structured object, dictionary
print('Name:', info["name"])
print('Hide:', info["email"]["hide"]) #dictipnary within a dictionary
