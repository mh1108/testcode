testcode
========

The demo code is in demo branch.

Before run the demo, you need to setup below things:

<h2>Python environment:</h2>
-- Python 2.7

<h2>Python module:</h2>
-- Flask<br/>
The web Framework, which will create a local server and run the website and code<br/>
Link: http://flask.pocoo.org/docs/0.10/

--simple-json<br/>
The module for parse json<br/>
Link: https://pypi.python.org/pypi/simplejson/

-- Wikipedia<br/>
The module for wikipedia api.<br/>
packagename: wikipedia-1.3.1.tar.gz <br/>
Link: https://pypi.python.org/pypi/wikipedia/

--Spotify<br/>
The module for spotify web api<br/>
packagename: spotipy-master.zip <br/>
Link: https://github.com/plamere/spotipy

<b>For install module:</b><br/>
--on mac<br/>
open terminal<br/>
<code>$ sudo easy_install modulename</code><br/>
or<br/>
<code>$ cd modulefolder</code><br/>
<code>$ sudo python setup.py install</code><br/>
--on Linux<br/>
<code>$ sudo pip modulename</code>

<h2>How to run</h2>
<b>Serchhing engine python application</b><br/>
<code>$ cd wikipedia_spotify/test</code><br/>
<code>$ python main.py</code><br/>
Given a artist name, return a dict, key-value pair is {"suggest_artist_name":"brief_instruction"}

<b>Web application</b><br/>
<code>$ cd webdemo </code><br/>
<code>$ python app.py</code><br/>
You will see<br/>
<code>$  * Running on http://127.0.0.1:5000/</code><br/>
Open your browser, go to http://127.0.0.1:5000/signUp, you will see the demo<br/>
Input any artist name and click go button, you will see the random suggested artists<br/>
(The process will take a little time, please wait) <br/>







