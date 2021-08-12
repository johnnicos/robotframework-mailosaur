*** Settings ***
Library           rfmailosaur    API_KEY=foo    server_id=baz    server_domain=foobaz.mailosaur.net
Library           Browser

*** Test Cases ***
Test email subject
    email subject should match    test

Test email links
    email_should_have_links    3

Test email attachments number
    email should have attachments    2

Test email body text
    email body should contain    matcher=test    case_insensitive=true

Test email links text
    email links should contain text    text=pluto
    email links should contain text    text=paperino
    email links should contain text    text=pippo

Delete mails
    delete all emails

Test email subject
    email subject should contain    matcher=pu

Test email sender
    email sender should match    matcher=foo@baz.com
