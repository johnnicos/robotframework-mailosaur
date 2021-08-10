# python3.8

from os import tcgetpgrp
from mailosaur import MailosaurClient, mailosaur_client
from mailosaur.models import SearchCriteria
from robot.api.deco import keyword, library
from robot.api import logger


@library
class rfmailosaur:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '0.1'
    ROBOT_AUTO_KEYWORDS = False

    def __init__(self, API_KEY, server_id, server_domain) -> None:
        self.mailosaur = MailosaurClient(API_KEY)
        self.server_id = server_id
        self.server_domain = server_domain
        self.criteria = SearchCriteria()

    @keyword
    def email_subject_should_match(self, matcher: str):
        """
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(self.server_id, self.criteria)
        try:
            assert last_email.subject == matcher
        except AssertionError as e:
            raise Exception("AssertionError: {0} does not equal {1}".format(
                last_email.subject, matcher))

    @keyword
    def delete_all_emails(self):
        """
        deletes all emails contained in the currently selected server domain.
        """
        self.criteria.sent_to = self.server_domain
        try:
            self.mailosaur.messages.delete_all(self.server_id)
        except Exception as e:
            raise e

    @keyword
    def email_should_have_links(self, links_number: int):
        """
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        links = len(last_email.html.links)
        try:
            assert links == links_number
        except AssertionError as e:
            raise Exception("AssertionError: {0} does not equal {1}".format(
                links, links_number))

    @keyword
    def email_should_have_attachments(self, attachments_number: int):
        """
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        attachments = len(last_email.attachments)
        try:
            assert attachments == attachments_number
        except AssertionError as e:
            raise Exception("AssertionError: {0} does not equal {1}".format(
                attachments, attachments_number))
