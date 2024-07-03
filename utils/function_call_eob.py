function_call_eob = [
    {
        "type": "function",
        "function": {
            "name": "itemize_eob",
            "description": "Itemize a eob from an image",
            "parameters": {
                "type": "object",
                "properties": {
                    "patient": {
                        "type": "string",
                        "description": "Name of patient",
                    },
                    "provider": {
                        "type": "string",
                        "description": "Name of provider",
                    },
                    "DocumentID": {
                        "type": "string",
                        "description": "DocumentID",
                    },
                    "servicedate": {
                        "type": "string",
                        "format": "date",
                        "description": "Service Date",
                    },
                    "claimdate": {
                        "type": "string",
                        "format": "date",
                        "description": "Claim Date",
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
                                    "description": "Copay",
                                },
                                "total": {
                                    "type": "number",
                                    "description": "Total",
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
                "required": ["patient", "claimdate", "provider", "servicedate", "DocumentID", "items"],
            },
        }
    }
]
