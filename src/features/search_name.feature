#Söka baserat på namn, oberoende av stora eller små bokstäver

#Som en användare vill jag kunna söka på namn så att jag lättare kan hitta kontaktinformation till mina vänner

Feature: Söka baserat på namn, oberoende av stora eller små bokstäver
  Scenario: Som en användare vill jag kunna söka på namn så att jag lättare kan hitta kontaktinformation till mina vänner
    Given jag har sedan tidigare lagt till vänner i "Mina vänner"
    When jag klickar på knappen "Vänlista"
    Then visas en lista med mina vänner
    And en sökruta som jag kan söka efter namn
    And jag ska kunna verifiera sökt namn