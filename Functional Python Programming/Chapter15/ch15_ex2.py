#!/usr/bin/env python3
"""Python. Programowanie funkcyjne

Rozdział 15, zbiór przykładów 2
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler

def server_demo():
    running = True
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    while running:
        httpd.handle_request()
    httpd.shutdown()

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
    #server_demo()
