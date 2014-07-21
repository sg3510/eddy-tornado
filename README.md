eddy-tornado
============

Handles audio files upload to remote server for later analysis.

How to use
----------
Run tornado server from main.py, change the port used in the
```python
application.listen(8888)
```
line.

To start listening for and sending audio, run record.py

File uploading is handled by uploadfile.py

Audio processing and tagging happens in process_audio.py
