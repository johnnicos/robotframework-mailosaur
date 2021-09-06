import re
from robot.api.deco import keyword, library
from robot.api import logger


class keywords(object):

    def email_subject_should_match(self, regex: str):
        """
        Checks the email subject of the last email received on the current server_domain matches the given regular expression.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(self.server_id, self.criteria)
        check = bool(re.match(r'{}'.format(regex), last_email.subject))
        if check is False:
            raise Exception(
                "The regexp does not match {}".format(last_email.subject))

    def email_subject_should_contain(self, matcher: str):
        """
        Checks the email subject of the last email received on the current server_domain contains the matcher.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(self.server_id, self.criteria)
        try:
            assert matcher in last_email.subject
        except AssertionError as e:
            raise Exception("AssertionError: '{0}' does not contain '{1}'".format(
                last_email.subject, matcher))

    def delete_all_emails(self):
        """
        deletes all emails contained in the currently selected server domain.
        """
        self.criteria.sent_to = self.server_domain
        try:
            self.mailosaur.messages.delete_all(self.server_id)
        except Exception as e:
            raise e

    def email_should_have_links(self, links_number: int):
        """
        Checks the last email contains X number of links where X == links_number.
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

    def email_should_have_attachments(self, attachments_number: int):
        """
        Checks the last email contains X number of attachments where X == attachments_number.
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

    def email_body_should_contain(self, matcher, case_insensitive: bool):
        """
        Checks the last email's body contains a specific string (matcher).

        If case_insensitive is set to True, then case is not checked in the substring.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        text = last_email.text.body
        if case_insensitive is True:
            text = text.lower()
            matcher = matcher.lower()
        try:
            assert matcher in text
        except AssertionError as e:
            raise Exception("AssertionError: {0} is not contained {1}".format(
                matcher, text))

    def email_links_should_contain_text(self, text: str):
        """
        Checks if atleast one of the links contained in the last email contains text.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        links = [link.text for link in last_email.text.links]
        assert any(map(lambda link: text in link, links))

    def email_sender_should_be(self, matcher: str):
        """
        Checks that last email sender matches the given matcher.
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        sender = last_email.sender[0].email
        try:
            assert sender == matcher
        except AssertionError as e:
            raise Exception("AssertionError: '{0}' does not match sender '{1}'".format(
                matcher, sender))

    def html_content_should_contain_text(self, matcher: str, case_insensitive):
        """
        Checks that last email's HTML content contains sub-string
        """
        self.criteria.sent_to = self.server_domain
        last_email = self.mailosaur.messages.get(
            self.server_id, self.criteria)
        html = last_email.html.body
        if case_insensitive is True:
            html = html.lower()
            matcher = matcher.lower()
        try:
            assert matcher in html
        except AssertionError as e:
            logger.error(last_email.html.body)
            raise Exception("AssertionError: '{0}' is not contained in '{1}'".format(
                matcher, html))
