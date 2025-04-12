
Feature: som en användare vill jag kunna uppdatera information om mina vänner och se ett felmeddelande om något fält inte är ifyllt

  Scenario: Uppdatera information om en vän
    Given jag har sedan tidigare lagt till vänner i "Mina vänner"
    When jag klickar på knappen "Vänlista"
    Then visas en lista med mina vänner
    And klickar jag på knappen "Ändra"
    Then ändrar jag information i första fältet, namn
    Then ändrar jag information i andra fältet, mailadress
    Then klicka på knappen "spara"

  Scenario: Visa felmeddelande om någon information saknas
    Given jag har sedan tidigare lagt till vänner i "Mina vänner"
    When jag klickar på knappen "Vänlista"
    Then visas en lista med mina vänner
    And klickar jag på knappen "Ändra"
    Then ändrar jag information i första fältet, namn
    Then tar jag bort information i andra textfältet, mailadress
    Then ska felmeddelandet "Fyll i båda fälten för att ändra vännens uppgifter"
    Then knappen "Spara" ska inte går att trycka på