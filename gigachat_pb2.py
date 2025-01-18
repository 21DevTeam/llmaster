# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gigachat.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'gigachat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egigachat.proto\x12\x0bgigachat.v1\"o\n\x0b\x43hatRequest\x12)\n\x07options\x18\x01 \x01(\x0b\x32\x18.gigachat.v1.ChatOptions\x12\r\n\x05model\x18\x02 \x01(\t\x12&\n\x08messages\x18\x03 \x03(\x0b\x32\x14.gigachat.v1.Message\"\xa3\x01\n\x0b\x43hatOptions\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\r\n\x05top_p\x18\x02 \x01(\x02\x12\x18\n\x10max_alternatives\x18\x03 \x01(\x05\x12\x12\n\nmax_tokens\x18\x04 \x01(\x05\x12\x1a\n\x12repetition_penalty\x18\x05 \x01(\x02\x12\x17\n\x0fupdate_interval\x18\x06 \x01(\x02\x12\r\n\x05\x66lags\x18\x07 \x03(\t\"E\n\x07Message\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x1b\n\x13unprocessed_content\x18\x03 \x01(\t\"\xa0\x01\n\x0c\x43hatResponse\x12.\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x18.gigachat.v1.Alternative\x12!\n\x05usage\x18\x02 \x01(\x0b\x32\x12.gigachat.v1.Usage\x12*\n\nmodel_info\x18\x03 \x01(\x0b\x32\x16.gigachat.v1.ModelInfo\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"Z\n\x0b\x41lternative\x12%\n\x07message\x18\x01 \x01(\x0b\x32\x14.gigachat.v1.Message\x12\x15\n\rfinish_reason\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x05\"O\n\x05Usage\x12\x15\n\rprompt_tokens\x18\x01 \x01(\x05\x12\x19\n\x11\x63ompletion_tokens\x18\x02 \x01(\x05\x12\x14\n\x0ctotal_tokens\x18\x03 \x01(\x05\"*\n\tModelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\x13\n\x11ListModelsRequest\"8\n\x12ListModelsResponse\x12\"\n\x06models\x18\x01 \x03(\x0b\x32\x12.gigachat.v1.Model\"7\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x10\n\x08owned_by\x18\x03 \x01(\t\"$\n\x14RetrieveModelRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\":\n\x15RetrieveModelResponse\x12!\n\x05model\x18\x01 \x01(\x0b\x32\x12.gigachat.v1.Model2\x8f\x01\n\x0b\x43hatService\x12;\n\x04\x43hat\x12\x18.gigachat.v1.ChatRequest\x1a\x19.gigachat.v1.ChatResponse\x12\x43\n\nChatStream\x12\x18.gigachat.v1.ChatRequest\x1a\x19.gigachat.v1.ChatResponse0\x01\x32\xb6\x01\n\rModelsService\x12M\n\nListModels\x12\x1e.gigachat.v1.ListModelsRequest\x1a\x1f.gigachat.v1.ListModelsResponse\x12V\n\rRetrieveModel\x12!.gigachat.v1.RetrieveModelRequest\x1a\".gigachat.v1.RetrieveModelResponseB\rZ\x0b./;protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gigachat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\013./;protocol'
  _globals['_CHATREQUEST']._serialized_start=31
  _globals['_CHATREQUEST']._serialized_end=142
  _globals['_CHATOPTIONS']._serialized_start=145
  _globals['_CHATOPTIONS']._serialized_end=308
  _globals['_MESSAGE']._serialized_start=310
  _globals['_MESSAGE']._serialized_end=379
  _globals['_CHATRESPONSE']._serialized_start=382
  _globals['_CHATRESPONSE']._serialized_end=542
  _globals['_ALTERNATIVE']._serialized_start=544
  _globals['_ALTERNATIVE']._serialized_end=634
  _globals['_USAGE']._serialized_start=636
  _globals['_USAGE']._serialized_end=715
  _globals['_MODELINFO']._serialized_start=717
  _globals['_MODELINFO']._serialized_end=759
  _globals['_LISTMODELSREQUEST']._serialized_start=761
  _globals['_LISTMODELSREQUEST']._serialized_end=780
  _globals['_LISTMODELSRESPONSE']._serialized_start=782
  _globals['_LISTMODELSRESPONSE']._serialized_end=838
  _globals['_MODEL']._serialized_start=840
  _globals['_MODEL']._serialized_end=895
  _globals['_RETRIEVEMODELREQUEST']._serialized_start=897
  _globals['_RETRIEVEMODELREQUEST']._serialized_end=933
  _globals['_RETRIEVEMODELRESPONSE']._serialized_start=935
  _globals['_RETRIEVEMODELRESPONSE']._serialized_end=993
  _globals['_CHATSERVICE']._serialized_start=996
  _globals['_CHATSERVICE']._serialized_end=1139
  _globals['_MODELSSERVICE']._serialized_start=1142
  _globals['_MODELSSERVICE']._serialized_end=1324
# @@protoc_insertion_point(module_scope)
