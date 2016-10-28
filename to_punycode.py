# coding by Denis Khabarov - admin@saymon21-root.pro
class FilterModule(object):
    def filters(self):
        return {
            'to_punycode': self.to_punycode,
        }
    def to_punycode(self, value):
        return value.encode('idna')
