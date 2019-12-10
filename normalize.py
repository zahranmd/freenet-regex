def strip_scheme(uri):
    if uri.startswith("http://"):
        uri = uri[len("http://"):]

    if(uri.startswith("https://")):
        uri = uri[len("https://"):]

    return uri


def strip_backslash(uri):
    if(uri[0]=='/'):
        uri = uri[1:]
    return uri

def normal(uri):
    uri = strip_scheme(uri)
    return strip_backslash(uri)