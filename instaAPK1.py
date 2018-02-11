#importing modules
from bs4 import BeautifulSoup
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from bs4 import BeautifulSoup
import requests
import json
import os

from flask import Flask
app = Flask(__name__)

@app.route("/download/<app_name>")

def download_apk(app_name):
	root = 'https://apkpure.com'
	url = 'https://apkpure.com/search?q=' + app_name #Making the URl to scrap
	html = requests.get(url) #getting Url
	soup = BeautifulSoup(html.text) #Making soup

	for i in  soup.find('p'):
		rest_url = i['href']
		print rest_url #debugging purpose
		app_url = root + rest_url + '/download?from=details' # app-download page
		return get_download_link(app_url,app_name)

def get_download_link(app_link,app_name):
	html2 = requests.get(app_link)
	soup2 = BeautifulSoup(html2.text)
	for link in soup2.find_all('a',id='download_link'):
		print link['href']
		download_link = link['href']
	return json.dumps({"app_name": app_name,"download_link":download_link})


if __name__ == "__main__":
    app.run()
