Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help()

Welcome to Python 3.12's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> modeles
No Python documentation found for 'modeles'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> modules

Please wait a moment while I gather a list of all available modules...

test_sqlite3: testing with SQLite version 3.42.0

Warning (from warnings module):
  File "C:\Python\Lib\site-packages\vboxapi-1.0-py3.12.egg\vboxapi\__init__.py", line 73
SyntaxWarning: invalid escape sequence '\P'

Warning (from warnings module):
  File "C:\Python\Lib\site-packages\vboxapi-1.0-py3.12.egg\vboxapi\__init__.py", line 73
SyntaxWarning: invalid escape sequence '\P'
PyInstaller         aifc                idle                searchbase
__future__          altgraph            idle_test           searchengine
__hello__           antigravity         idlelib             secrets
__main__            argparse            imaplib             select
__phello__          array               imghdr              selectors
_abc                ast                 importlib           setuptools
_aix_support        asyncio             importlib_metadata  shelve
_ast                atexit              inflect             shlex
_asyncio            audioop             inspect             shutil
_bisect             autocommand         io                  sidebar
_blake2             autocomplete        iomenu              signal
_bz2                autocomplete_w      ipaddress           site
_codecs             autoexpand          itertools           six
_codecs_cn          backports           json                smtplib
_codecs_hk          base64              keyword             sndhdr
_codecs_iso2022     bdb                 lib2to3             socket
_codecs_jp          binascii            linecache           socketserver
_codecs_kr          bisect              locale              sqlite3
_codecs_tw          browser             logging             squeezer
_collections        builtins            lzma                sre_compile
_collections_abc    bz2                 macosx              sre_constants
_compat_pickle      cProfile            mailbox             sre_parse
_compression        calendar            mailcap             ssl
_contextvars        calltip             mainmenu            stackviewer
_csv                calltip_w           marshal             stat
_ctypes             cgi                 math                statistics
_ctypes_test        cgitb               mimetypes           statusbar
_datetime           chunk               mmap                string
_decimal            cmath               modulefinder        stringprep
_distutils_hack     cmd                 more_itertools      struct
_elementtree        code                msilib              subprocess
_functools          codecontext         msvcrt              sunau
_hashlib            codecs              multicall           symtable
_heapq              codeop              multiprocessing     sys
_imp                collections         mysql               sysconfig
_io                 colorizer           mysqlx              tabnanny
_json               colorsys            netrc               tarfile
_locale             compileall          nntplib             telnetlib
_lsprof             concurrent          nt                  tempfile
_lzma               config              ntpath              test
_markupbase         config_key          nturl2path          textview
_md5                configdialog        numbers             textwrap
_msi                configparser        numpy               this
_multibytecodec     contextlib          opcode              threading
_multiprocessing    contextvars         operator            time
_mysql_connector    copy                optparse            timeit
_opcode             copyreg             ordlookup           tkinter
_operator           crypt               os                  token
_osx_support        csv                 outwin              tokenize
_overlapped         ctypes              packaging           tomli
_pickle             curses              pandas              tomllib
_py_abc             dataclasses         parenmatch          tooltip
_pydatetime         datetime            pathbrowser         trace
_pydecimal          dateutil            pathlib             traceback
_pyinstaller_hooks_contrib dbm                 pdb                 tracemalloc
_pyio               debugger            pefile              tree
_pylong             debugger_r          percolator          tty
_queue              debugobj            peutils             turtle
_random             debugobj_r          pickle              turtledemo
_sha1               decimal             pickletools         typeguard
_sha2               delegator           pip                 types
_sha3               difflib             pipes               typing
_signal             dis                 pkg_resources       typing_extensions
_sitebuiltins       doctest             pkgutil             tzdata
_socket             dynoption           platform            undo
_sqlite3            editor              platformdirs        unicodedata
_sre                email               plistlib            unittest
_ssl                encodings           poplib              urllib
_stat               ensurepip           posixpath           util
_statistics         enum                pprint              uu
_string             errno               profile             uuid
_strptime           faulthandler        pstats              vboxapi
_struct             filecmp             pty                 vboxapisetup
_symtable           fileinput           py_compile          venv
_testbuffer         filelist            pyclbr              warnings
_testcapi           fnmatch             pydoc               wave
_testclinic         format              pydoc_data          weakref
_testconsole        fractions           pyexpat             webbrowser
_testimportmultiple ftplib              pymysql             wheel
_testinternalcapi   functools           pyparse             win32ctypes
_testmultiphase     gc                  pyshell             window
_testsinglephase    genericpath         pytz                winreg
_thread             getopt              query               winsound
_threading_local    getpass             queue               wsgiref
_tkinter            gettext             quopri              xdrlib
_tokenize           glob                random              xml
_tracemalloc        graphlib            re                  xmlrpc
_typing             grep                redirector          xxsubtype
_uuid               gzip                replace             zipapp
_warnings           hashlib             reprlib             zipfile
_weakref            heapq               rlcompleter         zipimport
_weakrefset         help                rpc                 zipp
_winapi             help_about          run                 zlib
_wmi                history             runpy               zoneinfo
_xxinterpchannels   hmac                runscript           zoomheight
_xxsubinterpreters  html                sched               zzdummy
_zoneinfo           http                scrolledlist        
abc                 hyperparser         search              

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.

import mysql.connector
myDB =mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
    )














type(myDB)
<class 'mysql.connector.connection.MySQLConnection'>


myDB
<mysql.connector.connection.MySQLConnection object at 0x0000010FBBB655E0>
comando = myDB.cursor()
comando.execute("CREATE DATABASE BDPYN2_EDGAR")
comando.execute("SHOW DATABASE LIKE '%bdpyn2%'")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    comando.execute("SHOW DATABASE LIKE '%bdpyn2%'")
  File "C:\Python\Lib\site-packages\mysql\connector\cursor.py", line 551, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 490, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 395, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'DATABASE LIKE '%bdpyn2%'' at line 1
comando.execute("SHOW DATABASES LIKE '%bdpyn2%'")
for bd in comando:
    bd

    
('bdpyn2_david',)
('bdpyn2_edgar',)
('bdpyn2_efrenyer',)
('bdpyn2_henry',)
('bdpyn2_martindlr',)

myDB = mysql.connector.connect ( host = "localhost",
                                 user = "root",
                                 passwd = "",
                                 database = "bdpyn2_edgar")
comando = myDB.cursor()
comando.execute("CREATE TABLE PERSONAS (cedula varchar(10), nombre varchar(30), apellido varchar(30), direccion text(30), fechanac date)")

comando.execute("ALTER TABLE personas ADD COLUMN id integer auto_increment  PRIMARY KEY")

comando.execute("ALTER TABLE personas ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST")
sql = "INSERT INTO personas(cedula, nombre, apellido, fechanac) VALUES(%S %s %s %s %s)"
sql
'INSERT INTO personas(cedula, nombre, apellido, fechanac) VALUES(%S %s %s %s %s)'
valores = ('v123456789', 'ANA', 'VASQUEZ', 'SANTA FE', '1960-08-25')
comando.execute(sql, valores)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    comando.execute(sql, valores)
  File "C:\Python\Lib\site-packages\mysql\connector\cursor.py", line 542, in execute
    raise errors.ProgrammingError(
mysql.connector.errors.ProgrammingError: Not all parameters were used in the SQL statement
sql = "INSERT INTO personas(cedula, nombre, apellido, fechanac) VALUES(%s %s %s %s %s)"
sql
'INSERT INTO personas(cedula, nombre, apellido, fechanac) VALUES(%s %s %s %s %s)'
valores = ('v123456789', 'ANA', 'VASQUEZ', 'SANTA FE', '1960-08-25')

comando.execute(sql, valores)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    comando.execute(sql, valores)
  File "C:\Python\Lib\site-packages\mysql\connector\cursor.py", line 551, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 490, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 395, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.DataError: 1136 (21S01): Column count doesn't match value count at row 1
sql
'INSERT INTO personas(cedula, nombre, apellido, fechanac) VALUES(%s %s %s %s %s)'
comando.execute(sql, valores)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    comando.execute(sql, valores)
  File "C:\Python\Lib\site-packages\mysql\connector\cursor.py", line 551, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 490, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 395, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.DataError: 1136 (21S01): Column count doesn't match value count at row 1
sql = "INSERT INTO personas(cedula, nombre, apellido, fechanac) VALUES(%s, %s, %s, %s, %s)"
sql
'INSERT INTO personas(cedula, nombre, apellido, fechanac) VALUES(%s, %s, %s, %s, %s)'
valores = ('v123456789', 'ANA', 'VASQUEZ', 'SANTA FE', '1960-08-25')
comando.execute(sql, valores)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    comando.execute(sql, valores)
  File "C:\Python\Lib\site-packages\mysql\connector\cursor.py", line 551, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 490, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 395, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.DataError: 1136 (21S01): Column count doesn't match value count at row 1
sql = "INSERT INTO personas (cedula, nombre, apellido, fechanac) VALUES(%s, %s, %s, %s, %s)"
sql
'INSERT INTO personas (cedula, nombre, apellido, fechanac) VALUES(%s, %s, %s, %s, %s)'
comando.execute(sql, valores)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    comando.execute(sql, valores)
  File "C:\Python\Lib\site-packages\mysql\connector\cursor.py", line 551, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 490, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Python\Lib\site-packages\mysql\connector\connection.py", line 395, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.DataError: 1136 (21S01): Column count doesn't match value count at row 1
>>> sql = "INSERT INTO personas (cedula, nombre, apellido, direccion, fechanac) VALUES(%s, %s, %s, %s, %s)"
>>> comando.execute(sql, valores)
>>> valores = ('v123456789', 'ANA', 'VASQUEZ', 'SANTA FE', '1960-08-25')
>>> comando.execute(sql, valores)
>>> sql
'INSERT INTO personas (cedula, nombre, apellido, direccion, fechanac) VALUES(%s, %s, %s, %s, %s)'
>>> sql = "INSERT INTO personas (cedula, nombre, apellido, direccion, fechanac) VALUES(%s, %s, %s, %s, %s)"
>>> valores = ('v123456789', 'ANA', 'VASQUEZ', 'SANTA FE', '1960-08-25')
>>> comando.execute(sql, valores)
>>> myDB.commit()
>>> comando.lastrowid
3
>>> valores1 = [('v123456789', 'ANA', 'VASQUEZ', 'SANTA FE', '1960-08-25'), ('v123456789', 'PEDRO', 'VASQUEZ', 'GUARENAS', '1960-08-25'), ('v123456789', 'JUAN', 'VASQUEZ', 'CARACAS', '1960-08-25')]
>>> valores1
[('v123456789', 'ANA', 'VASQUEZ', 'SANTA FE', '1960-08-25'), ('v123456789', 'PEDRO', 'VASQUEZ', 'GUARENAS', '1960-08-25'), ('v123456789', 'JUAN', 'VASQUEZ', 'CARACAS', '1960-08-25')]
>>> comando.executemany(sql, valores1)
>>> myDB.commit()
>>> comando.rowcount
3
>>> 
================================== RESTART: C:\PYTHON_NIVEL2_SAB_20241123\EdgarGil\ingresar.py ==================================
Por favor ingrese los siguientes datos.
Cédula:29908675
Nombre:edgar
Apellido:gil
Dirección:guarenas
Fecha nacimiento (AAAA-MM-DD):2003-06-30
¿Desea ingresar los datos de otra persona (S/N)?N
