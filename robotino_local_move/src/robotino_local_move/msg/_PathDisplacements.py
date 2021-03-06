"""autogenerated by genpy from robotino_local_move/PathDisplacements.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PathDisplacements(genpy.Message):
  _md5sum = "9b998c7d1cd4ec3c3324c335d8cef150"
  _type = "robotino_local_move/PathDisplacements"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 move_x		# in meters
float32 move_y		# in meters
float32 rotation	# in degrees

uint8 movementType	
# 0 -> Translational Movement (move_phi should be equal to zero)
# 1 -> Rotational Movement (move_x and move_y should be equal to zero)
# 2 -> Translational and Rotational Moviment (at the same time)
# 3 -> Tangent Moviment (move_x must be iqual to move_y)

"""
  __slots__ = ['move_x','move_y','rotation','movementType']
  _slot_types = ['float32','float32','float32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       move_x,move_y,rotation,movementType

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PathDisplacements, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.move_x is None:
        self.move_x = 0.
      if self.move_y is None:
        self.move_y = 0.
      if self.rotation is None:
        self.rotation = 0.
      if self.movementType is None:
        self.movementType = 0
    else:
      self.move_x = 0.
      self.move_y = 0.
      self.rotation = 0.
      self.movementType = 0

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
      buff.write(_struct_3fB.pack(_x.move_x, _x.move_y, _x.rotation, _x.movementType))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 13
      (_x.move_x, _x.move_y, _x.rotation, _x.movementType,) = _struct_3fB.unpack(str[start:end])
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
      buff.write(_struct_3fB.pack(_x.move_x, _x.move_y, _x.rotation, _x.movementType))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 13
      (_x.move_x, _x.move_y, _x.rotation, _x.movementType,) = _struct_3fB.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3fB = struct.Struct("<3fB")
