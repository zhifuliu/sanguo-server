# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: character.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='character.proto',
  package='Sanguo.protocol.character',
  serialized_pb='\n\x0f\x63haracter.proto\x12\x19Sanguo.protocol.character\"y\n\tCharacter\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04gold\x18\x03 \x02(\x05\x12\x0b\n\x03gem\x18\x04 \x02(\x05\x12\r\n\x05level\x18\x05 \x02(\x05\x12\x15\n\rcurrent_honor\x18\x06 \x02(\x05\x12\x11\n\tmax_honor\x18\x07 \x02(\x05\"V\n\x0f\x43haracterNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x32\n\x04\x63har\x18\x02 \x02(\x0b\x32$.Sanguo.protocol.character.Character\"7\n\x16\x43reateCharacterRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0c\n\x04name\x18\x02 \x02(\t\"7\n\x17\x43reateCharacterResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c')




_CHARACTER = _descriptor.Descriptor(
  name='Character',
  full_name='Sanguo.protocol.character.Character',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Sanguo.protocol.character.Character.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Sanguo.protocol.character.Character.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='Sanguo.protocol.character.Character.gold', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gem', full_name='Sanguo.protocol.character.Character.gem', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Sanguo.protocol.character.Character.level', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_honor', full_name='Sanguo.protocol.character.Character.current_honor', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_honor', full_name='Sanguo.protocol.character.Character.max_honor', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=46,
  serialized_end=167,
)


_CHARACTERNOTIFY = _descriptor.Descriptor(
  name='CharacterNotify',
  full_name='Sanguo.protocol.character.CharacterNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.character.CharacterNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char', full_name='Sanguo.protocol.character.CharacterNotify.char', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=169,
  serialized_end=255,
)


_CREATECHARACTERREQUEST = _descriptor.Descriptor(
  name='CreateCharacterRequest',
  full_name='Sanguo.protocol.character.CreateCharacterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.character.CreateCharacterRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Sanguo.protocol.character.CreateCharacterRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=257,
  serialized_end=312,
)


_CREATECHARACTERRESPONSE = _descriptor.Descriptor(
  name='CreateCharacterResponse',
  full_name='Sanguo.protocol.character.CreateCharacterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Sanguo.protocol.character.CreateCharacterResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Sanguo.protocol.character.CreateCharacterResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=314,
  serialized_end=369,
)

_CHARACTERNOTIFY.fields_by_name['char'].message_type = _CHARACTER
DESCRIPTOR.message_types_by_name['Character'] = _CHARACTER
DESCRIPTOR.message_types_by_name['CharacterNotify'] = _CHARACTERNOTIFY
DESCRIPTOR.message_types_by_name['CreateCharacterRequest'] = _CREATECHARACTERREQUEST
DESCRIPTOR.message_types_by_name['CreateCharacterResponse'] = _CREATECHARACTERRESPONSE

class Character(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARACTER

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.character.Character)

class CharacterNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARACTERNOTIFY

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.character.CharacterNotify)

class CreateCharacterRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATECHARACTERREQUEST

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.character.CreateCharacterRequest)

class CreateCharacterResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATECHARACTERRESPONSE

  # @@protoc_insertion_point(class_scope:Sanguo.protocol.character.CreateCharacterResponse)


# @@protoc_insertion_point(module_scope)