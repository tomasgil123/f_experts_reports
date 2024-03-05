import streamlit as st
from openai import OpenAI
import re
import os

from dashboard.utils import (read_md_file, get_text_between_comments)
class OpenaiInsights():
    def __init__(self):
        self.client = OpenAI()

    def display_llm_insight_helper(self, data):
        # we display an input with some preloaded text
        markdown_text = read_md_file("./dashboard/llm_prompts.md")

        prompt = get_text_between_comments(markdown_text, data['section'], "<!")

        system_message = st.text_area("System Message", value=prompt)

        if st.button("Ask Chat GPT"):
            try:
                delimiter = "####"
                
                messages =  [  
                    {'role':'system', 
                    'content': system_message},    
                    {'role':'user', 
                    'content': f"{delimiter}{data['string_data']}{delimiter}"},  
                ]
                response = self.client.chat.completions.create(
                    model="gpt-4-0125-preview",
                    messages=messages,
                    temperature=0, 
                    max_tokens=1000, 
                )
                
                st.write(response.choices[0].message.content.strip())
            except Exception as err:
                st.write(err)
