# module imports --------------------------------------------------------------------------------------

import ast
import re
import string
import urllib


# HTTP parameters -------------------------------------------------------------------------------------

url = 'https://redcap.partners.org/redcap/api/'

headers = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Accept' : 'application/json'
}

HTTP_responses = {
    200 : 'REDCap says: "OK"',
    400 : 'REDCap says: "Bad Request"',
    401 : 'REDCap says: "Unauthorized"',
    403 : 'REDCap says: "Forbidden"',
    404 : 'REDCap says: "Not Found"',
    406 : 'REDCap says: "Not Acceptable"',
    500 : 'REDCap says: "Internal Server Error"',
    501 : 'REDCap says: "Not Implemented"'
}


# REDCap Methods --------------------------------------------------------------------------------------

def export_records(tkn, frmt = 'xml', typ = 'flat', **options):
	
	'''
	Returns a LIST of DICTs. Please visit the "API Playground"
	file in your REDCap project, as well as the REDCap API docs
	file for usage information
	'''
    
    # method requires REDCap token
    if not tkn:
        raise RuntimeError('No token specified. No records returned.')
        pass
    
    # required parameters
    data = [
        'token={0}'.format(tkn),
        'content=record',
        'format={0}'.format(frmt),
        'type={0}'.format(typ)
    ]
    
    # format optional parameters for HTTP post
    if len(options) > 0:
        options_list = []
        options_keys = [
			'records[0-9]*',
            'fields[0-9]*',
            'forms[0-9]*'
        ]
        for key, value in options.items():
            for regex in iter(options_keys):
                if re.match(regex, key):
                    temp_key = key
                    key_left = temp_key.rstrip(string.digits)
                    key_right = temp_key.lstrip(string.ascii_lowercase)
                    key = key_left + '[]' + key_right
                    options_list.append(key + '=' + value)
                else:
                    options_list.append(key + '=' + value)
        data = '&'.join(data) + '&' + '&'.join(options_list)
    else:
        data = '&'.join(data)
    
    # fetch and return records
    records_request = urllib.request.Request(url, data.encode('ascii'), headers)
    try:
        with urllib.request.urlopen(records_request) as response:
            records = response.read().decode('ascii')
        return ast.literal_eval(records)
    except urllib.error.HTTPError as e:
        raise RuntimeError(str(e.code) + ' --> ' + str(HTTP_responses[e.code]))



def export_metadata(tkn, frmt = 'xml', **options):
	
	'''
	Returns a LIST of DICTs. Please visit the "API Playground"
	file in your REDCap project, as well as the REDCap API docs
	file for usage information
	'''
    
    # method requires REDCap token
    if not tkn:
        raise RuntimeError('No token specified. No records returned.')
        pass
    
    # required parameters
    data = [
        'token={0}'.format(tkn),
        'content=metadata',
        'format={0}'.format(frmt)
    ]
    
    # format optional parameters for HTTP post
    if len(options) > 0:
        options_list = []
        options_keys = [
			'fields[0-9]*',
            'forms[0-9]*'
        ]
        for key, value in options.items():
            for regex in iter(options_keys):
                if re.match(regex, key):
                    temp_key = key
                    key_left = temp_key.rstrip(string.digits)
                    key_right = temp_key.lstrip(string.ascii_lowercase)
                    key = key_left + '[]' + key_right
                    options_list.append(key + '=' + value)
                else:
                    options_list.append(key + '=' + value)
        data = '&'.join(data) + '&' + '&'.join(options_list)
    else:
        data = '&'.join(data)
    
    # fetch and return records
    records_request = urllib.request.Request(url, data.encode('ascii'), headers)
    try:
        with urllib.request.urlopen(records_request) as response:
            metadata = response.read().decode('ascii')
        return ast.literal_eval(metadata)
    except urllib.error.HTTPError as e:
        raise RuntimeError(str(e.code) + ' --> ' + str(HTTP_responses[e.code]))


