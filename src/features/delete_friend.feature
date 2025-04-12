# Som en användare vill jag kunna ta bort en vän för att rensa i min vänlista

Feature: Ta bort en vän

  Scenario: Ta bort en vän
    Given jag har sedan tidigare lagt till vänner i "Mina vänner"
    When jag klickar på knappen "Vänlista"
    Then visas en lista med mina vänner
    When jag klickar på knappen "Ta bort"
    Then ska vännens post försvinna från listan