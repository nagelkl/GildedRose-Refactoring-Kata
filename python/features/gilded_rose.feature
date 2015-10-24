# description of the gilded rose features for acceptance testing with behave


Feature: Goods degrade in quality dependen on their type
  Aged brie increases in Quality

  Scenario: Aged Brie
    Given The Item is a aged Brie
    When one day has passed
    Then increase the quality by one
    And decreas the sell to date one

  Scenario: Backstage Pass with sell in date greater than 5
    Given The Item is a Backstage Pass
    And the sell in date is greater then 5
    When one day has passed
    Then icrease the quality by one
    And decreas the sell to date by one
