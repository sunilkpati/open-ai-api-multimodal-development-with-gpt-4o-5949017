import json
from utils.openai_init import openai_init
from utils.encode_image import encode_image
from utils.manage_data_eob import add_rows
from utils.function_call_eob import function_call_eob

client = openai_init()


def process_eob(eob_df, image_path):
    """
    Process a claims image using a completion model.

    Parameters:
    client: The client object to interact with the completion model.
    image_path (str): The path to the claims image file to be processed.

    Returns:
    dict: The processed eob data.
    """

    # Encode the image
    print(f"Encoding image: {image_path}")
    base64_image = encode_image(image_path)

    # Create the completion request
    print(f"Passing image data to GPT-4o for processing...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a processor of explaination of benefits(eob). If the provided image is not a insurance eob, DON'T DESCRIBE IT! Ask for a valid eob image."},
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"}
                 }
            ]},
        ],
        tools=function_call_eob,
        tool_choice="auto",
        temperature=0.0,
    )

    if response:
        print(f"Response received from GPT-4o: {response}")

        # If the image is a eob, process the data
        if (response.choices[0].message.tool_calls is not None and
            len(response.choices[0].message.tool_calls) > 0 and
                response.choices[0].message.tool_calls[0].function.name == "itemize_eob"):

            # Extract eob data from the response
            eob_data = json.loads(
                response.choices[0].message.tool_calls[0].function.arguments)

            # print(eob_data)
            print(
                f"\nRetrieved eob data from {eob_data['DocumentID']} at {eob_data['patient']}")

            # Add the eob data to the expenses DataFrame
            eob_df = add_rows(eob_df, eob_data)

        else:
            print(f"\nWARNING:\n{response.choices[0].message.content}")

    else:
        print("No response received from GPT-4o.")

    return eob_df
