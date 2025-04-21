from behave import given, when, then

@when(u'jag klickar på knappen "Ta bort"')
def step_button_delete(context):
    delete_button = context.page.locator('button', has_text="Ta bort").first
    assert delete_button.is_visible()
    delete_button.click()


@then(u'ska vännens post försvinna från listan')
def step_friend_removed(context):
    # Försök hitta texten "Jean-Luc Picard"
    locator = context.page.locator("text=Jean-Luc Picard")

    # Kontrollera att den inte är synlig
    assert not locator.is_visible(), "'Jean-Luc Picard' finns fortfarande på sidan!"
