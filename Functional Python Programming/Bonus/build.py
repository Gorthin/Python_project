#!/usr/bin/env python3.3

# Skrypt budowania
# -------------------

# ..  sectnum::
#
# ..  contents::
#

# Projekt 
# ===============

# Jest to narzędzie przypominające ant lub scons, które będzie śledzić zależności
# wśród plików i odbudowywać zależne pliki, gdy źródła 
# się zmienią.

# Musimy zamodelować dwa rodzaje zależności.
#
# -   Ogólne ``*.txt`` zależy od ``*.py``, a także ``*.html`` zalezy od ``*.txt``.
#
# -   Konkretne ``index.rst`` zależy od ``[*.py]``.
#
# Różnica polega na tym, że zasada ogólna jest szablonem,
# który dotyczy wielu plików w relacji 1-1.
#
# Reguła konkretna jest nieco bardziej ogólną relacją pomiędzy źródłem, a formatem docelowym.
#
# W razie potrzeby zdefiniujemy funkcję do zbudowania. Będzie to funkcja wyższego rzędu,
# wymagająca mechanizmu budowania, który potrafi odbudować cel, jeśli
# zmienił się którykolwiek z plików źródłowych.
#
# Zdefiniujemy wiele mechanizmów budowania dla różnych narzędzi, które będziemy automatyzować.

# Koszty ogólne modułu
# =================

# Docstring modułu
# ::

"""Buduje wszystkie przykładowe pliki kodu do nieco bardziej czytelnych stron HTML.

1. Uruchom narzędzie pylit, aby zbudować pliki RST *.txt z kodu w plikach *.py.
2. Utwórz stronę index.rst jako dodatkowy plik.
3. Uruchom plik rst2html.py, aby zbudować wersje *.html plików *.txt.

Wymaga pakietów pylit3 i docutils.

::

    python3 -m pip install pylit3 docutils
"""

# Importy
# ::

from pathlib import Path
import os
import subprocess
import datetime
import sys
import logging
from functools import partial

# Ustawienia logowania
# ==================

# Globalny logger, z którego może korzystać cały moduł

logger = logging.getLogger("build")

# Oto konfiguracja logowania wykonana jako mechanizm zarządzania kontekstem.
# Zainicjujemy również logowanie i wyłączanie logowania.

# ::

class Logging_Config:
    def __enter__(self, filename="logging.config"):
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    def __exit__(self, *exc):
        logging.shutdown()

# Funkcje podstawowe
# ===================

# Podstawową funkcją jest ``build_if_needed()``. Funkcja ta
# sprawdza czasy modyfikacji podanych plików. Funkcja
# ma prostą treść:
#
# -  Jeśli plik docelowy jest nowszy od źródła, nie rób nic.
#
# -  Jeśli plik docelowy jest starszy niż źródło, zastosuj funkcję budowania.
#
# Aby ustalić, czy powinniśmy budować, musimy porównać 
# czasy modyfikacji plików docelowych i wszystkich źródeł.
# Do tego celu wykorzystamy funkcję ``target_ok()``, która sprawdza znaczniki czasu.

# ::

def target_ok(target_file, *source_list):
    """Czy plik docelowy został utworzony po wszystkich plikach źródłowych?
    Jeśli tak, to jest OK.
    Jeśli nie ma pliku docelowego lub jest nieaktualny,
    to nie jest OK.
    """
    try:
        mtime_target = datetime.datetime.fromtimestamp(
            target_file.stat().st_mtime)
    except FileNotFoundError:
        logger.debug("Nie znaleziono pliku %s", target_file)
        return False

    logger.debug("Porównywanie %s %s >WSZYSTKIE %s",
                 target_file, mtime_target, source_list)

    # Jeśli plik źródłowy nie istnieje, to mamy większe problemy.
    times = (
        datetime.datetime.fromtimestamp(source_file.stat().st_mtime)
        for source_file in source_list
    )

    return all(mtime_target > mtime_source for mtime_source in times)

# Funkcja ``build_if_needed()`` wymaga mechanizmu budowania, celu i 
# jednego lub więcej źródeł. Stosuje funkcję ``target_ok()``
# do pliku docelowego i plików źródłowych. W razie potrzeby zastosuje 
# mechanizm budowania.

# ::

def build_if_needed(builder, target_file, *source):
    """Buduje plik docelowy ze źródłowego z wykorzystaniem mechanimu budowania (builder)."""
    logger.debug("Sprawdzanie %s", target_file)
    if target_ok(target_file, *source):
        return f"ok({target_file}, *{source})"
    builder(target_file, *source)
    return f"builder({target_file}. *{source})"

# Moglibyśmy podejść do tego inaczej: napisać 
# funkcję ``build_if_needed()`` tak, aby zwracała jedną z dwóch rzeczy:
#
# - funkcję częściową ``builder(target, \*source)`` do późniejszej ewaluacji.
#
# - ``ok(target, \*source)`` funkcję częściową będącą namiastką funkcji budowania, która niczego nie robi.
#
# Chodzi o to, że wyjście z powyższej byłoby  
# skryptem, który wyraźnie pokazuje, co należy zrobić.

# Funkcje budowania (buildery)
# =============

# Każda funkcja budowania pobiera docelową nazwę pliku 
# oraz listę nazw plików źródłowych. Jej zadaniem jest stworzenie pliku docelowego
# na podstawie źródeł.
#
# Ponieważ polegamy na funkcji ``subprocess.run()``, każda
# funkcja budowania jest prawidłową kompozycją funkcji ``run()`` oraz
# innej funkcji, która buduje wywoływane polecenie.
#
# Istnieje kilka sposobów implementacji kompozycji funkcyjnej:
# poprzez definicję podklasy, dekoratory lub funkcję wyższego rzędu
# łączącej dwie inne funkcje.
#
# Wybieramy generyczną funkcję wyższego rzędu i tworzymy funkcję częściową,  
# podczas wiązania argumentów.

# ::

def subprocess_builder(make_command, target_file, *source_list):
    command = make_command(target_file, *source_list)
    logger.debug("Polecenie {0}".format(command))
    subprocess.run(command)

# Funkcja PyLit subprocess_builder tworzy polecenie do uruchomienia PyLit.

# ::

def command_pylit(output, *input):
    return ["python3", "-m", "pylit", input[0]]

pylit = partial(subprocess_builder, command_pylit)

# Funkcja rst2html subprocess_builder tworzy polecennie do uruchomienia rst2html.
# Zawiera dwa ogólne argumenty wymagane do uzyskania akceptowalnie wyglądającej
# zawartości.

# ::

def command_rst2html(output, *input):
    return ["rst2html.py", "--syntax-highlight=long", "--input-encoding=utf-8", input[0], output]

rst2html = partial(subprocess_builder, command_rst2html)

# Funkcja budowania, która utworzy stronę indeksu. Będzie to obejmowało trzy funkcje wewnętrzne
# aby utworzyć nagłówek, treść oraz stopkę.
#
# Można by to zrobić lepiej przy pomocy szablonu Jinja2. Jednak złożoność 
# formatu RST jest niska, dzięki czemu zbudowanie nagłówka i stopki
# dla podanej listy elementów w środku  jest stosunkowo proste.

# ::

header = lambda : """
#############################################
Python. Programowanie funkcyjne. Kod premium
#############################################

© 2018, Steven F. Lott

..  raw:: html

    <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>
    <br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Materiały premiu.
"""

footer = lambda : "Zaktualizowano {0}".format(datetime.datetime.now())

def body(source_list):
    return "\n".join(
        "-   `{0} <{0}>`_".format(source.with_suffix(".html").name)
        for source in source_list)

def make_index(target_file, *source_list):
    with open(target_file, "w") as target:
        print(header(), file=target)
        print('\n', file=target)
        print(body(source_list), file=target)
        print('\n', file=target)
        print(footer(), file=target)

# Główny skrypt 
# ===========================

# Oto wysokopoziomowa definicja zależności.
# Istnieją trzy zestawy reguł.
#
# -  Stwórz ``*.txt`` na podstawie plików ``*.py`` dla plików ``*.py``.
#
# -  Stwórz ``index.txt`` na podstawie plików ``*.txt`` zbudowany dla nazw z grupy``*.py``.
#
# -  Stwórz ``*.html`` na podstawie plików ``*.txt`` dla plików ``*.txt``.
#
# Reguły zostały opisane poniżej na dwa sposoby. Jedna zawiera listę 
# wartości funkcji zależności. Druga jako pętla **for** .
# Obie wersje wydają się dość jasne.

# ::

def make_files():
    files_py = list(Path.cwd().glob("*.py"))
    txt_builds = [
        build_if_needed(pylit, f.with_suffix(f.suffix+'.txt'), f)
        for f in files_py
    ]
    for item in txt_builds:
        logger.info(item)

    index_build = build_if_needed(
        make_index, Path("index.txt"),
        *[f.with_suffix(f.suffix+'.txt') for f in files_py]
    )
    logger.info(index_build)

    files_txt = Path.cwd().glob("*.txt")
    for f in files_txt:
        html_build = build_if_needed(rst2html, f.with_suffix('.html'), f)
        logger.info(html_build)

# Główny skrypt, który wykonuje całą pracę.
# Tworzymy kontekst logowania. Stosujemy reguły buduj-jeśli-trzeba.

# ::

if __name__ == "__main__":
    with Logging_Config():
        os.chdir(Path("Bonus"))
        make_files()
