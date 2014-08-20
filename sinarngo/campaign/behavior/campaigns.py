from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.formwidget.autocomplete.widget import AutocompleteFieldWidget

from sinarngo.campaign.content.campaign import ICampaign
from sinarngo.campaign import MessageFactory as _

class ICampaigns(form.Schema):
    """
       Marker/Form interface for Campaigns
    """

    # -*- Your Zope schema definitions here ... -*-

    form.fieldset(
            'categorization',
            label=_(u'Categorization'),
            fields=('campaigns',),
            )

    #form.widget(campaigns=AutocompleteFieldWidget)
    campaigns = RelationChoice(
            title=_(u'Campaigns'),
            source=ObjPathSourceBinder(
                object_provides=ICampaign.__identifier__),
            required=False,
            )

alsoProvides(ICampaigns,IFormFieldProvider)
