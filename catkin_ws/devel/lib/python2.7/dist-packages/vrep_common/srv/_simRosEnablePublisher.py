# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vrep_common/simRosEnablePublisherRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class simRosEnablePublisherRequest(genpy.Message):
  _md5sum = "e7df7c248dc5801f9f5b98f61f3741b8"
  _type = "vrep_common/simRosEnablePublisherRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """



string topicName
int32 queueSize
int32 streamCmd
int32 auxInt1
int32 auxInt2
string auxString

"""
  __slots__ = ['topicName','queueSize','streamCmd','auxInt1','auxInt2','auxString']
  _slot_types = ['string','int32','int32','int32','int32','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       topicName,queueSize,streamCmd,auxInt1,auxInt2,auxString

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(simRosEnablePublisherRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.topicName is None:
        self.topicName = ''
      if self.queueSize is None:
        self.queueSize = 0
      if self.streamCmd is None:
        self.streamCmd = 0
      if self.auxInt1 is None:
        self.auxInt1 = 0
      if self.auxInt2 is None:
        self.auxInt2 = 0
      if self.auxString is None:
        self.auxString = ''
    else:
      self.topicName = ''
      self.queueSize = 0
      self.streamCmd = 0
      self.auxInt1 = 0
      self.auxInt2 = 0
      self.auxString = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.topicName
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4i.pack(_x.queueSize, _x.streamCmd, _x.auxInt1, _x.auxInt2))
      _x = self.auxString
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topicName = str[start:end].decode('utf-8')
      else:
        self.topicName = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.queueSize, _x.streamCmd, _x.auxInt1, _x.auxInt2,) = _struct_4i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.auxString = str[start:end].decode('utf-8')
      else:
        self.auxString = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.topicName
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4i.pack(_x.queueSize, _x.streamCmd, _x.auxInt1, _x.auxInt2))
      _x = self.auxString
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.topicName = str[start:end].decode('utf-8')
      else:
        self.topicName = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.queueSize, _x.streamCmd, _x.auxInt1, _x.auxInt2,) = _struct_4i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.auxString = str[start:end].decode('utf-8')
      else:
        self.auxString = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4i = struct.Struct("<4i")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vrep_common/simRosEnablePublisherResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class simRosEnablePublisherResponse(genpy.Message):
  _md5sum = "8280ce6c5ec203a92c1559486bea2e2e"
  _type = "vrep_common/simRosEnablePublisherResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string effectiveTopicName


"""
  __slots__ = ['effectiveTopicName']
  _slot_types = ['string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       effectiveTopicName

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(simRosEnablePublisherResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.effectiveTopicName is None:
        self.effectiveTopicName = ''
    else:
      self.effectiveTopicName = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.effectiveTopicName
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.effectiveTopicName = str[start:end].decode('utf-8')
      else:
        self.effectiveTopicName = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.effectiveTopicName
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.effectiveTopicName = str[start:end].decode('utf-8')
      else:
        self.effectiveTopicName = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
class simRosEnablePublisher(object):
  _type          = 'vrep_common/simRosEnablePublisher'
  _md5sum = '1656daea9e4b58b53b650fa39f39e74e'
  _request_class  = simRosEnablePublisherRequest
  _response_class = simRosEnablePublisherResponse
