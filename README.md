# Walk through to my submission
#Open main.py file
- Input file path of sample json to read
- Input output file path of result filename
- Run program using python3 main.py
- Result can be located in given output file path.

# Requirement
simplejson 

- Installation: pip install simplejson


# Rules followed  
- I have written a generic program that:
- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file 
- Dumps the output in (./schema/)

# Additional information for test cases
- I have padded all attributes in the JSON schema with "tag" and "description" keys
- I have captured ONLY the attributes within the "MESSAGE" key of the input JSON source data (Script would need adjusting to serve other unique purposes). All attributes within the key "attributes" have been excluded
- I have set all properties "required": false
- For data types of the JSON schema i have:
STRING: INTEGER: ENUM: ARRAY: 

# Output results 
- ./schema/schema_1.json
- ./schema/schema_2.json

# Additional Resources
- Here is a github link of repo used for this: https://github.com/gonvaled/jskemator.git