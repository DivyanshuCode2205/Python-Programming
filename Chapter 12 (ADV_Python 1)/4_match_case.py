def website_status(status):
    match status:

        case 200:
            return 'OK'
        
        case 404:
            return 'Not found'
        
        case 500:
            return 'Error'
        
        case _:
            return 'Unknown Status'

print(website_status(200))
print(website_status(404))
print(website_status(500))
print(website_status(2100))
