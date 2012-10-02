import zim.monitor.interfaces
import zope.interface

class IBaseMonitor(zope.interface.Interface):

    name = zope.schema.ASCIILine(
        title=u'name',
        description=u'Name of the monitor',
        required=True,
        )

    interval = zope.schema.Int(
        title=u'interval',
        description=u'Polling interval (seconds)',
        required=False,
        default = 300,
        )

class BaseMonitor:

    zope.interface.implements(zim.monitor.interfaces.IMonitor)

    schema = IBaseMonitor

    def __init__(self):
        self.__dict__.update(
            dict((name, self.schema[name].default) for name in self.schema)
            )

    def expose_config(self):
        return [self.schema[name] for name in sorted(self.schema)]

    def setup(self, configs):
        missing = sorted(
            name for name in self.schema
            if (self.schema[name].required and
                name not in configs and
                getattr(self, name) is None))
        if missing:
            raise TypeError("Required field %r ommitted." % missing)
        self.__dict__.update(
            dict(
                (name, self.schema[name].fromUnicode(configs[name]))
                for name in self.schema
                if name in configs
                ))

    def get_config(self):
        return dict((name, getattr(self, name)) for name in self.schema)
