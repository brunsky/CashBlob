# -*- coding: utf-8 -*-
"""
    urls
    ~~~~

    URL definitions.

"""
from tipfy import Rule

def get_rules(app):
    rules = [
        Rule('/', endpoint='home', handler='apps.cashblob.handlers.HomeHandler'),
        Rule('/uploader', endpoint='cashblob/uploader', handler='apps.cashblob.handlers.UFormHandler'),
        Rule('/upload', endpoint='cashblob/upload', handler='apps.cashblob.handlers.UploadHandler'),
        Rule('/downloader', endpoint='cashblob/downloader', handler='apps.cashblob.handlers.DFormHandler'),
        Rule('/download', endpoint='cashblob/download', handler='apps.cashblob.handlers.DownloadHandler'),
        Rule('/serve/<resource>', endpoint='cashblob/serve', handler='apps.cashblob.handlers.ServeHandler'),
    ]

    return rules
