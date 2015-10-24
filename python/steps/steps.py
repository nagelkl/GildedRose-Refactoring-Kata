#@PydevCodeAnalysisIgnore
from gilded_rose import GildedRose, Item


@given(u'The Item is a aged Brie')
def step_impl(context):
    context.items = [Item(name="Aged Brie", quality=10, sell_in=5)]

@when(u'one day has passed')
def step_impl(context):
    GildedRose(context.items).update_quality()

@then(u'increase the quality by one')
def step_impl(context):
    assert context.items[0].quality == 11 

@then(u'decreas the sell to date one')
def step_impl(context):
    assert context.items[0].sell_in == 4
    
@given(u'The Item is a Backstage Pass')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The Item is a Backstage Pass')

@given(u'the sell in date is greater then 5')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the sell in date is greater then 5')

@then(u'icrease the quality by one')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then icrease the quality by one')

@then(u'decreas the sell to date by one')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then decreas the sell to date by one')

    