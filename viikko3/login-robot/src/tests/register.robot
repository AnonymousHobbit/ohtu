*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  Jari  dkwao12431ok
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testero  dkwao12431ok
    Output Should Contain  User with username testero already exists

Register With Too Short Username And Valid Password
    Input Credentials  aa  dkwao12431ok
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  Jari  aa
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  Jari  aaaaaaaaaaaaaa
    Output Should Contain  Password must contain at least one number


*** Keywords ***
Create User And Input New Command
    Create User  testero  Test123test
    Input New Command
    