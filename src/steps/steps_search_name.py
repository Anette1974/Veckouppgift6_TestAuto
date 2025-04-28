import re
from behave import given, when, then

@then(u'en sökruta som jag kan söka efter namn')
def step_search_name(context):
    textbox = context.page.get_by_placeholder("Sök namn")
    textbox.click(timeout=500)
    textbox.fill("JAMES")

@then(u'jag ska kunna verifiera sökt namn')
def step_verify_name(context):
    content = context.page.content()
    pattern = re.compile(r"\bJames\w*\b", re.IGNORECASE)
    assert  pattern.search(content)

