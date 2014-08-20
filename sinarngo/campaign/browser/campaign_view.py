from five import grok
from plone.directives import dexterity, form
from sinarngo.campaign.content.campaign import ICampaign

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ICampaign)
    grok.require('zope2.View')
    grok.template('campaign_view')
    grok.name('view')

