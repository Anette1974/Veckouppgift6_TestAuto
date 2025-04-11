# Som en användare vill jag kunna visa en lista med alla mina vänner

Feature: Lista alla mina vänner

  Scenario: Lista alla mina vänner
    Given jag har sedan tidigare lagt till vänner i "Mina vänner"
    When jag klickar på knappen "Vänlista"
    Then visas en lista med mina vänner