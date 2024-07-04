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
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "claim_number": {
                                    "type": "string",
                                    "description": "Claim Number",
                                },
                                "claimdate": {
                                    "type": "string",
                                    "format": "date",
                                    "description": "Claim Date",
                                },
                                "paid_on": {
                                    "type": "string",
                                    "format": "date",
                                    "description": "Paid On",
                                },
                                "items": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "servicedate": {
                                                "type": "string",
                                                "format": "date",
                                                "description": "Service Date",
                                            },
                                            "service_description": {
                                                "type": "string",
                                                "description": "Service Description",
                                            },
                                            "provider_billed": {
                                                "type": "number",
                                                "description": "Provider billed",
                                            },
                                            "member_discount": {
                                                "type": "number",
                                                "description": "Member discount",
                                            },
                                            "net_charged": {
                                                "type": "number",
                                                "description": "Net charged",
                                            },
                                            "your_plan_paid": {
                                                "type": "number",
                                                "description": "Plan Paid",
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
                                                "enum": ["Office Visit", "Diagnostic", "Telehealth", "other"],
                                            },
                                        },
                                    },
                                    "description": "List of services in eob",
                                },
                            },
                        },
                        "description": "List of claims in eob",
                    },
                },
                "required": ["patient", "provider", "DocumentID", "items"],
            },
        }
    }
]
