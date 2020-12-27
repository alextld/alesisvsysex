import mido
from alesisvsysex.protocol.sysex import SysexMessage

__all__ = ['AlesisV25Device']

class AlesisV25Device (object):

    mido.set_backend('mido.backends.portmidi')
    _PORT_PREFIX = "VMini"
    
    def __init__(self):
        for port in mido.get_input_names():
            if port.startswith(self._PORT_PREFIX):
                self._port = mido.open_input(port)
                break
        for port in mido.get_output_names():
            if port.startswith(self._PORT_PREFIX):
                self._outport = mido.open_output(port)
                break
        else:
            raise RuntimeError("Could not find a port named '%s'" % self._PORT_PREFIX)
    
    def __del__(self):
        try:
            self.port.close()
        except:
            pass

    def _send(self, message):
        if not isinstance(message, SysexMessage):
            raise ValueError("Can only send a SysexMessage")
        p = mido.Parser()
        p.feed(message.serialize())
        self._outport.send(p.get_message())

    def _recv(self):
        while True:
            r = self._port.receive()
            if r.type == 'sysex':
                break
        return SysexMessage.deserialize(r.bin())

    def get_config(self):
        self._send(SysexMessage('query'))
        return self._recv().model
    
    def set_config(self, model):
        model_bin = model.serialize()
        self._send(SysexMessage('update', model))
        if self.get_config().serialize() != model_bin:
            raise RuntimeError('Failed to update configuration')

