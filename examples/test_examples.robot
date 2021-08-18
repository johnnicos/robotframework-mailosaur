*** Settings ***
Library           rfmailosaur    API_KEY=${api_key}    server_id=${server_id}    server_domain=${server_domain}
Library           Browser

*** Test Cases ***
Test email subject
    email subject should match    regex=[a-zA-Z0-9]

Test email links
    email should have links    2

Test email attachments number
    email should have attachments    0

Test email body text
    ### pippo paperino pluto
    email body should contain    matcher=pluto    case_insensitive=true

Test email links text
    email links should contain text    text=nasa
    email links should contain text    text=tesla

Delete mails
    delete all emails

Test email subject
    email subject should contain    matcher=Pa

Test email sender
    email sender should be    matcher=andrea.gubellini@prima.it
