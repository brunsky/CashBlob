# -*- coding: utf-8 -*-

from google.appengine.ext import blobstore
from google.appengine.ext import db
from tipfy import redirect_to, RequestHandler, Response, url_for
from tipfy.ext.blobstore import BlobstoreDownloadMixin, BlobstoreUploadMixin
from tipfy.ext.jinja2 import render_response

class MyFile(db.Model):
    name = db.StringProperty(required=True)
    owner = db.StringProperty(required=True)
    timestamp = db.DateTimeProperty(auto_now=True)
    blob_key = blobstore.BlobReferenceProperty(required=True)

class HomeHandler(RequestHandler):
    def get(self):
        return render_response('hello_world.html', message='Hello, World!')

class DFormHandler(RequestHandler):
    def get(self):
    	download_url = url_for('cashblob/download')
        html = ''
        html += '<html><body>'
        html += '<form action="%s" method="POST">' % download_url
        html += """Account: <input type="text" name="account"><br> <input type="submit"
            name="submit" value="Submit"> </form></body></html>"""

        return Response(html, mimetype='text/html')

class DownloadHandler(RequestHandler):
    def post(self, **kwargs):
    	account = self.request.form.get('account')
    	#query = MyFile.gql("WHERE owner= :1", account)
    	#f = query.get()
        query = MyFile.all()
        query.filter('owner =', account).order('-timestamp')   
        f = query.get() 	
        if f == None:
    		return render_response('hello_world.html', message='None') 
    	response = redirect_to('cashblob/serve', resource=str(f.blob_key.key()))
    	response.data = ''
        return response

class UFormHandler(RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url(url_for('cashblob/upload'))
        html = ''
        html += '<html><body>'
        html += '<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url
        html += """Upload File: <input type="file" name="file"><br> <input type="submit"
            name="submit" value="Submit"> </form></body></html>"""

        return Response(html, mimetype='text/html')


class UploadHandler(RequestHandler, BlobstoreUploadMixin):
    def post(self):
        # 'file' is the name of the file upload field in the form.
        upload_files = self.get_uploads('file')
        blob_info = upload_files[0]
        f = MyFile(name=blob_info.filename, blob_key=blob_info.key(), owner='will.lien@gmail.com')
        f.put()
        # response = redirect_to('blobstore/serve', resource=blob_info.key())
        response = redirect_to('home')
        # Clear the response body.
        response.data = ''
        return response


class ServeHandler(RequestHandler, BlobstoreDownloadMixin):
    def get(self, **kwargs):
        blob_info = blobstore.BlobInfo.get(kwargs.get('resource'))
        return self.send_blob(blob_info)

class GetUPath(RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url(url_for('cashblob/upload'))
        return Response(upload_url)

