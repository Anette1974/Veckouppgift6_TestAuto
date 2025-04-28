#Lägga till ny vän
#Formuläret visar ett felmeddelande om inte båda fälten är ifyllda
@wip

Feature: Lägga till ny vän
  Som en användare vill jag kunna lägga till ny användare så att jag har alla mina vänners kontaktuppgifter på ett ställe.

  Scenario: Lägga till ny vän med båda fälten ifyllda
    Given Jag har en väns kontaktuppgifter som jag vill lägga till i min vänlista
    When jag klickar på knappen "Ny vän"
    Then  Jag fyller i fältet "Namn" på sidan "Ny vän" korrekt
    And Jag fyller i fältet "E-post" på sidan "Ny vän"  korrekt
    And klicka på knappen "spara"
    And jag klickar på knappen "Vänlista"
    And jag verifierar att min nya vän finns i listan
