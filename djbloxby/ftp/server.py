from django.contrib.sites.models import Site
from pyftpdlib.servers import FTPServer

from djbloxby.ftp.authorizers import APIAuth
from djbloxby.ftp.filesystems import CustomFileSystem
from djbloxby.ftp.handlers import Handler


def get_ftp_server(host, port=21):
    authorizer = APIAuth()
    handler = Handler
    handler.authorizer = authorizer
    handler.abstracted_fs = CustomFileSystem
    handler.masquerade_address = Site.objects.get_current().domain
    address = (host, port)
    server = FTPServer(address, handler)
    return server