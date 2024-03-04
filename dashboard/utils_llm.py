from dashboard.utils import (read_md_file, get_text_between_comments)


def display_llm_insight_helper(string_data):
    # we display an input with some preloaded text
    markdown_text = read_md_file(f"./llm_prompts.md")

    product_titles_prompt = get_text_between_comments(markdown_text, "<!-- Competitors: Product titles analysis -->", "<!")


