import requests, zipfile
from io import BytesIO

link = 'https://cdn.cs50.net/ai/2020/x/projects/0/tictactoe.zip'


req =requests.get(link)

zipfile = zipfile.ZipFile(BytesIO(req.content))

zipfile.extractall()

