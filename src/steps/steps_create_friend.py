from behave import given, when, then

@given(u'Jag har en väns kontaktuppgifter som jag vill lägga till i min vänlista')
def step_given_start(context):
    context.page.goto(context.base_url)

@when(u'jag klickar på knappen "Ny vän"')
def step_when_click_new_friend(context):
    new_friend_button = context.page.locator('a[href="#/add"]')
    new_friend_button.click()

@then(u'Jag fyller i fältet "Namn" på sidan "Ny vän" korrekt')
def step_then_add_name(context):
    first_input = context.page.query_selector("input")
    first_input.fill("Anna Andersson")
    #add_name = context.page.get_by_label("Namn")
    #add_name.click(timeout=800)
    #add_name.fill("Anna")

@then(u'Jag fyller i fältet "E-post" på sidan "Ny vän"  korrekt')
def step_then_add_epost(context):
    input_fields = context.page.query_selector_all("input")
    input_fields[1].fill("anna.andersson@test.com")
    #epost = context.page.get_by_label("E-post")
    #epost.click(timeout=500)
    #epost.fill("anna.andersson@test.com")

#@then(u'Jag klickar på knappen "Spara" på sidan "Ny vän"')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Then Jag klickar på knappen "Spara" på sidan "Ny vän"')



@then(u'jag klickar på knappen "Vänlista"')
def step_when_click_friends(context):
    friend_button = context.page.locator('a[href="#/friends"]')
    friend_button.click()


@then(u'jag verifierar att min nya vän finns i listan')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then jag verifierar att min nya vän finns i listan')
