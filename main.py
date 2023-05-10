#!/usr/bin/env python3
import openai
import textwrap
import json
import logging
import sys
import argparse
import os

from pygments import highlight
from pygments.lexers import RustLexer
from pygments.formatters import TerminalFormatter

def main():
    logging.basicConfig(
    # stream=sys.stdout,
    level=logging.CRITICAL,
    format='%(asctime)s %(levelname)s %(message)s'
    )
    if 'OPENAI_API_KEY' in os.environ:
        logging.info("The OPENAI_API_KEY is set")
    else:
        logging.error("Must set OPENAI_API_KEY in env")
        exit()

    logging.info("Starting tool")
    logging.info("Parsing tool")

    parser = argparse.ArgumentParser(description="Fast track API to Chat GTP - requires a payment plan")
    parser.add_argument('-q', '--question', type=str, required=False, help='Question to ask ChatGPT api')
    args = parser.parse_args()

    if args.question:
        logging.info("Asking GPT3 a question")
        completion=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": args.question}])

        """text=json.dumps(completion["choices"][0].message["content"], indent=4)"""
        text = completion["choices"][0].message["content"]
        highlighted_code = highlight(text, RustLexer(), TerminalFormatter())
        print("\n")
        print("CHAPGPT3 RESPONSE")
        print("\n")
        print(highlighted_code)

    logging.error("Failed to input chat GPT3 question flag -q or --question")

if __name__ == "__main__":
    main()
