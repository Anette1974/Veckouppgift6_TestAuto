from behave import then
from playwright.sync_api import expect


@then(u'klickar jag på knappen "Ändra"')
def step_then_update_button(context):
    update_button = context.page.locator('a[href="#/edit/1"]')
    update_button.click(timeout=500)


@then(u'kan jag ändra namn och mailadress')
def step_then_update_friend(context):
    update_name = context.page.locator('input[value="Jean-Luc Picard"]').fill("Godzilla")
    # Verifiera att värdet är "Godzilla"

@then(u'klicka på knappen "Spara"')
def step_then_button_save(context):
    save_button = context.page.get_by_role("button").get_by_text("Spara")
    save_button.click()
