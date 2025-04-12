import re
from behave import then
from playwright.sync_api import expect


@then(u'klickar jag på knappen "Ändra"')
def step_then_update_button(context):
    update_button = context.page.locator('a[href="#/edit/1"]')
    update_button.click(timeout=500)


@then(u'ändrar jag information i första fältet, namn')
def step_then_update_name(context):
    update_name = context.page.locator('input[value="Jean-Luc Picard"]').fill("Godzilla")
    # TO DO - Verifiera att värdet är "Godzilla"

@then(u'ändrar jag information i andra fältet, mailadress')
def step_then_update_email(context):
    update_email = context.page.locator('input[value="captain.picard@starfleet.com"]').fill("godzilla.monster@film.com")
    # TO DO - Verifiera att värdet är en giltigt e-mailadress

@then(u'klicka på knappen "Spara"')
def step_then_button_save(context):
    save_button = context.page.get_by_role("button").get_by_text("Spara")
    save_button.click()


@then(u'tar jag bort information i andra textfältet, mailadress')
def step_remove_email(context):
    remove_email = context.page.locator('input[value="captain.picard@starfleet.com"]').fill("")


@then(u'ska felmeddelandet "Fyll i båda fälten för att ändra vännens uppgifter"')
def step_show_error(context):
    error = context.page.get_by_role("text").get_by_text(re.compile("Fyll i båda fälten för att ändra vännens uppgifter"))


@then(u'knappen "Spara" ska inte går att trycka på')
def step_button_save(context):
    save_button = context.page.get_by_role("button").get_by_text(re.compile("Spara"))
    expect(save_button).to_be_disabled()


