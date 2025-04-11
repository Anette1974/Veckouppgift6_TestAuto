
Feature: Uppdatera information för en vän

  Scenario: Uppdatera information för en vän
    Given jag har sedan tidigare lagt till vänner i "Mina vänner"
    When jag klickar på knappen "Vänlista"
    Then visas en lista med mina vänner
    And klickar jag på knappen "Ändra"
    Then kan jag ändra namn och mailadress
    Then klicka på knappen "spara"
