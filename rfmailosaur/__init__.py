from rfmailosaur.keywords import keywords
from rfmailosaur.version import VERSION
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria


class rfmailosaur(keywords):
    __version__ = VERSION
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, API_KEY, server_id, server_domain) -> None:
        """
        The library needs a few arguments in order to work properly:

        - API_KEY which you can retrieve from your mailosaur dashboard

        - server_id which you can retrieve from your mailosaur dashboard

        - server_domain which you can retrieve from your mailosaur dashboard

        Set these arguments when importing the library in the .robot file or set a __init__.robot file with the import and parameters.
        """
        self.mailosaur = MailosaurClient(API_KEY)
        self.server_id = server_id
        self.server_domain = server_domain
        self.criteria = SearchCriteria()
