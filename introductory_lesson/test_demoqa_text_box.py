from selene import browser, have


def test_fill_the_text_box_form():
    # GIVEN
    browser.open('https://demoqa.com/text-box')

    # WHEN
    browser.element('input#userName').type('Konstantin Varvarkin')
    browser.element('input#userEmail').type('KonstantinVarvarkin@gmail.com')
    browser.element('textarea#currentAddress').type('Saint-Petersburg')
    browser.element('textarea#permanentAddress').type('Saint-Petersburg')
    browser.element('button#submit').click()

    # THEN
    browser.element('p#name').should(have.text('Konstantin Varvarkin'))
    browser.element('p#email').should(have.text('KonstantinVarvarkin@gmail.com'))
    browser.element('p#currentAddress').should(have.text('Saint-Petersburg'))
    browser.element('p#permanentAddress').should(have.text('Saint-Petersburg'))
