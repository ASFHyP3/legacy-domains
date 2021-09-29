def lambda_handler(event, context):
    domain_name = event['requestContext']['domainName']

    if domain_name == 'hyp3.asf.alaska.edu':
        response = {
            'statusCode': 308,
            'headers': {
                'Location': 'https://hyp3-docs.asf.alaska.edu/v2-transition',
            },
        }

    elif domain_name in ['hyp3-download.asf.alaska.edu', 'api.hyp3.asf.alaska.edu']:
        response = {
            'statusCode': 410,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n'
                    '<title>410 Gone</title>\n'
                    '<h1>Gone</h1>\n'
                    '<p>The requested URL is no longer available on this server and there is no forwarding address. If '
                    'you followed a link from a foreign page, please contact the author of this page.</p>\n',
        }

    else:
        response = {
            'statusCode': 404,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n'
                    '<title>404 Not Found</title>\n'
                    '<h1>Not Found</h1>\n'
                    '<p>The requested URL was not found on the server. If you entered the URL manually please check '
                    'your spelling and try again.</p>\n',
        }

    return response
