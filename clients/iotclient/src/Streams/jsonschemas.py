UUID_REG = "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"

STREAM_SCHEMA = {
    "type": "object",
    "properties": {
        "schema": {"type": "string"},
        "stream": {"type": "string"},
        "flushing": {
            "type": "object",
            "oneOf": [{
                "properties": {
                    "base": {"type": "string", "enum": ["time"]},
                    "interval": {"type": "integer", "minimum": 1},
                    "unit": {"type": "string", "enum": ["s", "m", "h"]}
                },
                "required": ["base", "interval", "unit"],
                "additionalProperties": False
            }, {
                "properties": {
                    "base": {"type": "string", "enum": ["tuple"]},
                    "number": {"type": "integer", "minimum": 1}
                },
                "required": ["base", "number"],
                "additionalProperties": False
            }]
        },
        "columns": {
            "type": "array",
            "minItems": 1,
            "additionalItems": False,
            "items": {
                "type": "object",
                "anyOf": [{
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["char", "varchar", "character varying"]},
                        "nullable": {"type": "boolean"},
                        "limit": {"type": "integer", "minimum": 1},
                        "default": {"type": "string"}
                    },
                    "required": ["name", "type", "limit"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["text", "string", "character large object"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "string"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string",
                                 "enum": ["tinyint", "smallint", "int", "integer", "bigint", "hugeint"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "integer"},
                        "minimum": {"type": "integer"},
                        "maximum": {"type": "integer"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["real", "float", "double"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "number"},
                        "minimum": {"type": "number"},
                        "maximum": {"type": "number"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["decimal", "numeric"]},
                        "nullable": {"type": "boolean"},
                        "precision": {"type": "integer", "minimum": 1, "maximum": 38},
                        "scale": {"type": "integer", "minimum": 0},
                        "default": {"type": "number"},
                        "minimum": {"type": "number"},
                        "maximum": {"type": "number"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["boolean"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "boolean"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["date"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "string", "format": "date"},
                        "minimum": {"type": "string", "format": "date"},
                        "maximum": {"type": "string", "format": "date"},
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["time"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "string", "format": "time"},
                        "minimum": {"type": "string", "format": "time"},
                        "maximum": {"type": "string", "format": "time"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["timestamp"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "string", "format": "date-time"},
                        "minimum": {"type": "string", "format": "date-time"},
                        "maximum": {"type": "string", "format": "date-time"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["uuid"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "string", "pattern": UUID_REG}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["inet"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "string", "format": "ipv4"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["url"]},
                        "nullable": {"type": "boolean"},
                        "default": {"type": "string", "format": "uri"}
                    },
                    "required": ["name", "type"],
                    "additionalProperties": False
                }, {
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string", "enum": ["enum"]},
                        "nullable": {"type": "boolean"},
                        "values": {"type": "array", "minItems": 1, "uniqueItems": False, "items": {"type": "string"}},
                        "default": {"type": "string"}
                    },
                    "required": ["name", "type", "values"],
                    "additionalProperties": False
                }]
            }
        }
    },
    "required": ["schema", "stream", "flushing", "columns"],
    "additionalProperties": False
}

CONFIG_FILE_SCHEMA = {
    "title": "JSON schema to load configuration file",
    "description": "Validate the inserted properties",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": STREAM_SCHEMA
}

CREATE_STREAMS_SCHEMA = {
    "title": "JSON schema to create a stream",
    "description": "Validate the inserted properties",
    "$schema": "http://json-schema.org/draft-04/schema#",
}

CREATE_STREAMS_SCHEMA.update(STREAM_SCHEMA)

DELETE_STREAMS_SCHEMA = {
    "title": "JSON schema to delete a stream",
    "description": "Validate the inserted properties",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",

    "properties": {
        "schema": {"type": "string"},
        "stream": {"type": "string"}
    },
    "required": ["schema", "stream"],
    "additionalProperties": False
}
