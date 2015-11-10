# -*- coding: utf-8 -*-

from django.test.client import Client

from lettuce import step, world, before
from lettuce.django import django_url


@before.all
def set_browser():
    world.browser = Client()

@step(u'Given I navigate to url "(.*)"')
def given_i_navigate_to_url(step, url):
    full_url = django_url(url)
    world.browser.get(full_url)
    assert False

@step(u'When I fill in the "([^"]*)"')
def when_i_fill_in_the_group1(step, group1):
    assert False, 'This step must be implemented'

@step(u'And I click "([^"]*)"')
def and_i_click_group1(step, group1):
    assert False, 'This step must be implemented'

@step(u'Then I new expense add to database')
def then_i_new_expense_add_to_database(step):
    assert False, 'This step must be implemented'
