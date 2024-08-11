def http_status_code(response):
    match response:
        case 200:
            return "Success"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case 501:
            return "Not Implemented"
        case 503:
            return "Service Unavailable"
        case 504:
            return "Gateway Timeout"
        case 505:
            return "HTTP Version Not Supported"
        case _:
            return "Unknown Status Code"
        
print(http_status_code(200))