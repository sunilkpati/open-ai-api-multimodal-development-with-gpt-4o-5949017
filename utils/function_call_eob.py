function_call = [
    {
        "type": "function",
        "function": {
            "name": "itemize_eob",
            "description": "Itemize a eob from an image",
            "parameters": {
                "type": "object",
                "properties": {
                    "provider": {
                        "type": "string",
                        "description": "Name of provider",
                    },
                    "date": {
                        "type": "string",
                        "format": "date",
                        "description": "Service Date",
                    },
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "Service Name",
                                },
                                "billed": {
                                    "type": "number",
                                    "description": "Provider billed",
                                },
                                "discount": {
                                    "type": "number",
                                    "description": "Member discount",
                                },
                                "charged": {
                                    "type": "number",
                                    "description": "Net charged",
                                },
                                "copay": {
                                    "type": "number",
                                    "description": "Member Copay",
                                },
                                "total": {
                                    "type": "number",
                                    "description": "Total Pay",
                                },
                                "category": {
                                    "type": "string",
                                    "description": "Category of item",
                                    "enum": ["OfficeVisit", "Diagnostic", "Telehealth", "other"],
                                },
                            },
                        },
                        "description": "List of services in eob",
                    },
                },
                "required": ["provider", "date", "items"],
            },
        }
    }
]
