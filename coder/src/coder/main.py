#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from coder.crew import Coder


import os
from dotenv import load_dotenv


dotenv_path = r"C:\Users\joevi\TerraformCoderAgent_JV\.env"

print("🔍 Looking for .env at:", dotenv_path)
load_dotenv(dotenv_path=dotenv_path)
print("✅ OPENAI_API_KEY loaded:", os.getenv("OPENAI_API_KEY"))

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

assignment = 'Write a terraform template for aws that creates an s3 instance and creates 2 buckets called jv1 and jv2'


def run():
    """
    Run the crew.
    """
    inputs = {
        'assignment': assignment,
    }
    
    result = Coder().crew().kickoff(inputs=inputs)
    print(result.raw)




