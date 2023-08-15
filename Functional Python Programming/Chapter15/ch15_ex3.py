#!/usr/bin/env python3
"""Python. Programowanie funkcyjne

Rozdział 15, zbiór przykładów 3
"""

from wsgiref.simple_server import make_server, demo_app
import wsgiref.util
import urllib
import urllib.parse
from pathlib import Path
import sys

from typing import (
    Dict, Callable, List, Tuple, Iterator, Union, Optional
)
from mypy_extensions import DefaultArg

# Aby poprawnie zadeklarować wywołanie zwrotne start_response wymaga mypy_extensions.
SR_Func = Callable[[str, List[Tuple[str, str]], DefaultArg(Tuple)], None]

TEST_TEMPLATE = """<html>
<head><title>Uruchom testy</title></head>
<body>
<h1>Testy</h1>
<p>Wyniki</p>
<pre><code>{0}
</code></pre>
<form method="POST" action="">
<hr/>
<input type="submit" value="Uruchom testy"/>
</form>
</body>
</html>"""

def test_app(
        environ: Dict,
        start_response: SR_Func
    ) -> Union[Iterator[bytes], List[bytes]]:
    """Uruchamia pakiet testów jednostkowych."""
    if environ['REQUEST_METHOD'] == "GET":
        # wysyła formularz i poprzednie wyniki (jeśli istnieją)
        if environ['QUERY_STRING']:
            query = urllib.parse.parse_qs(environ['QUERY_STRING'])
            file_path = Path(environ['TMPDIR']) / query['filename'][0]
            with file_path.open() as result_file:
                results = result_file.read()
        else:
            results = ""
        page = TEST_TEMPLATE.format(results)
        content = page.encode("utf-8")
        headers = [
            ("Content-Type", 'text/html; charset="utf-8"'),
            ("Content-Length", str(len(content))),
            ]
        start_response('200 OK', headers)
        return [content]
    elif environ['REQUEST_METHOD'] == "POST":
        # Uruchamia testy, zbiera dane w pliku pamięci podręcznej
        import test_all
        file_path = Path(environ['TMPDIR']) / "results"
        file_list = sorted(
            Path.cwd().glob("Chapter_*"),
            key=lambda p: test_all.chap_key(p.name))
        with file_path.open("w") as result_file:
            sys.stderr = result_file
            local_names = [
                str(item.relative_to(Path.cwd())) for item in file_list
            ]
            test_all.master_test_suite(
                test_all.package_module_iter(*local_names))
            sys.stderr = sys.__stderr__
        #Może za każdym razem obliczyć unikatową nazwę pliku
        filename = {"filename": "results"}
        encoded_filename = urllib.parse.urlencode(filename)
        headers = [
            ("Lokalizacja", "/test?{0}".format(encoded_filename))
        ]
        start_response("302 FOUND", headers)
        return []
    start_response("400 NOT ALLOWED", [])
    return []

INDEX_TEMPLATE_HEAD = """<html>
<head><title>Rozdział 15</title></head>
<body><h1>Pliki w {0}</h1>
"""

INDEX_TEMPLATE_FOOT = """
</body></html>
"""

def index_app(
        environ: Dict,
        start_response: SR_Func
    ) -> Union[Iterator[bytes], List[bytes]]:
    """Wyświetla indeks dostępnych plików. """
    log = environ['wsgi.errors']
    print("PATH_INFO '{0}'".format(environ['PATH_INFO']), file=log)
    page = INDEX_TEMPLATE_HEAD.format(environ.get('PATH_INFO', '.'))
    for entry in (Path.cwd()/environ['PATH_INFO'][1:]).glob('*'):
        if entry.name.startswith('.'): continue
        rel_path = entry.relative_to(Path.cwd())
        page += '<p><a href="/static/{0}">{1}</a></p>'.format(rel_path, entry.name)
    page += INDEX_TEMPLATE_FOOT
    content = page.encode("utf-8")
    headers = [
        ("Content-Type", 'text/html; charset="utf-8"'),
        ("Content-Length", str(len(content))),
    ]
    start_response('200 OK', headers)
    return [content]

def static_app(
        environ: Dict,
        start_response: SR_Func
    ) -> Union[Iterator[bytes], List[bytes]]:
    """Wyświetla pojedynczy, statyczny plik. """
    log = environ['wsgi.errors']
    try:
        print(f"CWD={Path.cwd()}", file=log)
        static_path = Path.cwd()/environ['PATH_INFO'][1:]
        with static_path.open() as static_file:
            content = static_file.read().encode("utf-8")
            headers = [
                ("Content-Type", 'text/plain; charset="utf-8"'),
                ("Content-Length", str(len(content))),
            ]
            start_response('200 OK', headers)
            return [content]
    except IsADirectoryError as e:
        return index_app(environ, start_response)
    except FileNotFoundError as e:
        start_response('404 NOT FOUND', [])
        return [f"Not Found {static_path}\n{e!r}".encode("utf-8")]

WELCOME_TEMPLATE = """<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<title>Chapter 15</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
<div class="container">
<h1>Rzodział 15</h1>
<p><a href="demo" class="btn btn-default" role="button">Aplikacja WSGI Demo</a></p>
<p><a href="static" class="btn btn-default" role="button">Cały kod</a></p>
<p><a href="test" class="btn btn-default" role="button">Uruchom zbiór testów</a></p>
<p><a href="static/Chapter_15/ch15_ex3.py" class="btn btn-default" role="button">Ten kod</a></p>
</div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>
</html>"""

def welcome_app(
        environ: Dict,
        start_response: SR_Func
    ) -> Union[Iterator[bytes], List[bytes]]:
    """Wyświetla stronę z informacjami powitalnymi."""
    content = WELCOME_TEMPLATE.encode("utf-8")
    headers = [
        ("Content-Type", "text/html; charset=utf-8"),
        ("Content-Length", str(len(content))),
    ]
    start_response('200 OK', headers)
    return [content]

SCRIPT_MAP = {
    "demo": demo_app,
    "static": static_app,
    "test": test_app,
    "": welcome_app,
}

def routing(
        environ: Dict,
        start_response: SR_Func
    ) -> Union[Iterator[bytes], List[bytes]]:
    """Routing po aplikacjach przy użyciu informacji ze skryptu. """
    top_level = wsgiref.util.shift_path_info(environ)
    app = SCRIPT_MAP.get(top_level, SCRIPT_MAP[''])
    content = app(environ, start_response)
    return content

def server_demo():
    httpd = make_server('', 8080, routing)
    print("Serving HTTP on port 8080...")

    # Odpowiadaj na żądania, aż proces zostanie zabity
    httpd.serve_forever()

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
    server_demo()
