*** Settings ***
Library           ../rfmailosaur/RFMailosaur.py    API_KEY=flqsMTAbtpXvAltI    server_id=fr537ggd    server_domain=fr537ggd.mailosaur.net
Library           Browser

*** Test Cases ***
Test email subject
    ## inserire match su regexp
    email subject should match    regex=[a-zA-Z0-9]

Test email links
    email_should_have_links    2

Test email attachments number
    email should have attachments    0

Test email body text
    email body should contain    matcher=tracciando    case_insensitive=true

Test email links text
    email links should contain text    text=nasa
    email links should contain text    text=tesla
# Delete mails
#    delete all emails

Test email subject
    email subject should contain    matcher=Pa

Test email sender
    email sender should be    matcher=andrea.gubellini@prima.it
