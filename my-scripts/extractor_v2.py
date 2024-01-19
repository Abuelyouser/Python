import re
import os
from docx import Document

directory_path = input("Enter a folder location to remove all time stamps! : ")


def remove_timestamps(input_text):
    # Define a regular expression pattern to match timestamps
    timestamp_pattern = re.compile(r'\d+\n(?:\d{2}:\d{2}:\d{2},\d+ --> \d{2}:\d{2}:\d{2},\d+\n)?')
    # Use re.sub to replace the timestamp lines with an empty string
    text_without_timestamps = re.sub(timestamp_pattern, '', input_text)
    # Remove tabs and line breaks
    formatted_text = re.sub(r'\t|\n', ' ', text_without_timestamps)
    return formatted_text


for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith(".srt"):
            text_file_path = os.path.join(root, file)
            with open(text_file_path, 'r') as opened_file:
                content = opened_file.read()
                script = remove_timestamps(content)
                # Save the content to a DOCX file
                doc = Document()
                doc.add_paragraph(script)
                # Replace '.srt' with '.docx' in the output file name
                output_docx_path = os.path.splitext(text_file_path)[0] + '.docx'
                doc.save(output_docx_path)

                print(f"Script saved to: {output_docx_path}")
