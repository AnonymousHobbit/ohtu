*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Start

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testero
    Set Password  kalle123
    Set Confirmation  kalle123
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  b
    Set Password  kalle456
    Set Confirmation  kalle456
    Submit Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  Jari
    Set Password  b
    Set Confirmation  b
    Submit Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  Jari
    Set Password  jari1234
    Set Confirmation  be
    Submit Register
    Register Should Fail With Message  Password and password confirmation must match

Login After Successful Registration
    Set Username  Jari
    Set Password  jari1234
    Set Confirmation  jari1234
    Submit Register
    Register Should Succeed
    Go To Login Page
    Set Username  Jari
    Set Password  jari1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  Jarib
    Set Password  jari1234
    Set Confirmation  b
    Submit Register
    Go To Login Page
    Set Username  Jarib
    Set Password  jari1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Set Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}
    
Go To Register Page And Start
    Go To Register Page
    Register Page Should Be Open