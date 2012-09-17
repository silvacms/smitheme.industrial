
from megrok.pagetemplate import PageTemplate
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from silva.core import conf as silvaconf
from silva.ui.smi import SMI
from five import grok


class ISMIIndustrialSkin(IDefaultBrowserLayer):
    pass


# Customize SMI template
# class SMITemplate(PageTemplate):
#     grok.view(SMI)
#     grok.layer(ISMIIndustrialSkin)

