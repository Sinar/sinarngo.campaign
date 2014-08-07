from collective.grok import gs
from sinarngo.campaign import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.campaign', 
    title=_('sinarngo.campaign import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.campaign.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
