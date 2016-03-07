# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vrep_common/simRosSetObjectQuaternionRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class simRosSetObjectQuaternionRequest(genpy.Message):
  _md5sum = "9d74781e3cdb8dd84f786051a3a1c90b"
  _type = "vrep_common/simRosSetObjectQuaternionRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """



int32 handle
int32 relativeToObjectHandle
geometry_msgs/Quaternion quaternion

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['handle','relativeToObjectHandle','quaternion']
  _slot_types = ['int32','int32','geometry_msgs/Quaternion']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       handle,relativeToObjectHandle,quaternion

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(simRosSetObjectQuaternionRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.handle is None:
        self.handle = 0
      if self.relativeToObjectHandle is None:
        self.relativeToObjectHandle = 0
      if self.quaternion is None:
        self.quaternion = geometry_msgs.msg.Quaternion()
    else:
      self.handle = 0
      self.relativeToObjectHandle = 0
      self.quaternion = geometry_msgs.msg.Quaternion()

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
      _x = self
      buff.write(_struct_2i4d.pack(_x.handle, _x.relativeToObjectHandle, _x.quaternion.x, _x.quaternion.y, _x.quaternion.z, _x.quaternion.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.quaternion is None:
        self.quaternion = geometry_msgs.msg.Quaternion()
      end = 0
      _x = self
      start = end
      end += 40
      (_x.handle, _x.relativeToObjectHandle, _x.quaternion.x, _x.quaternion.y, _x.quaternion.z, _x.quaternion.w,) = _struct_2i4d.unpack(str[start:end])
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
      _x = self
      buff.write(_struct_2i4d.pack(_x.handle, _x.relativeToObjectHandle, _x.quaternion.x, _x.quaternion.y, _x.quaternion.z, _x.quaternion.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.quaternion is None:
        self.quaternion = geometry_msgs.msg.Quaternion()
      end = 0
      _x = self
      start = end
      end += 40
      (_x.handle, _x.relativeToObjectHandle, _x.quaternion.x, _x.quaternion.y, _x.quaternion.z, _x.quaternion.w,) = _struct_2i4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2i4d = struct.Struct("<2i4d")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vrep_common/simRosSetObjectQuaternionResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class simRosSetObjectQuaternionResponse(genpy.Message):
  _md5sum = "034a8e20d6a306665e3a5b340fab3f09"
  _type = "vrep_common/simRosSetObjectQuaternionResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 result


"""
  __slots__ = ['result']
  _slot_types = ['int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(simRosSetObjectQuaternionResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.result is None:
        self.result = 0
    else:
      self.result = 0

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
      buff.write(_struct_i.pack(self.result))
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
      (self.result,) = _struct_i.unpack(str[start:end])
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
      buff.write(_struct_i.pack(self.result))
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
      (self.result,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
class simRosSetObjectQuaternion(object):
  _type          = 'vrep_common/simRosSetObjectQuaternion'
  _md5sum = 'f5fe7b4813e58c37e0cb1c1585da009e'
  _request_class  = simRosSetObjectQuaternionRequest
  _response_class = simRosSetObjectQuaternionResponse
