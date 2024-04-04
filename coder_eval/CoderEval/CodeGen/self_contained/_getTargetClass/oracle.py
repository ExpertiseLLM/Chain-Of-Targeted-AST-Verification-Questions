def _getTargetClass(self):
    from zope.interface.declarations import getObjectSpecification
    return getObjectSpecification
