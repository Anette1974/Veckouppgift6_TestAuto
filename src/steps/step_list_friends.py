from behave import given, when, then


@given(u'jag har sedan tidigare lagt till vänner i "Mina vänner"')
def step_given_start(context):
    context.page.goto(context.base_url)


@when(u'jag klickar på knappen "Vänlista"')
def step_when_click_friends(context):
    friend_button = context.page.locator('a[href="#/friends"]')
    friend_button.click()


@then(u'visas en lista med mina vänner')
def step_then_list_friends(context):
    search_name = context.page.locator('input[placeholder="Sök namn"]')
