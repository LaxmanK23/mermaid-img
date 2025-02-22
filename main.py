import subprocess
import os

# Mermaid code for the flowchart
mermaid_code = """
flowchart TD;
    A[Requirement Inspection] --> B[Design Inspection];
    B --> C[Code Review & Static Analysis];
    C --> D[Integration & System Testing];
    D --> E{Non-Compliance or Issues Found?};
    E -- Yes --> F[Implement Corrections & Retest];
    E -- No --> G[Prepare Final Compliance Report];
    F --> D;
    G --> H[Approval & Certification Readiness];
"""

# Output file name (the image)
output_image = "flowchart.png"

# Step 1: Save the Mermaid code to a temporary file
mermaid_file = "flowchart.mmd"
with open(mermaid_file, "w") as f:
    f.write(mermaid_code)

# Step 2: Define the full path to `mmdc` (update this with your actual path)
# Example path: C:\Users\<YourUsername>\AppData\Roaming\npm\mmdc.cmd
mmdc_path = r"C:/Users/laxman/AppData/Roaming/npm/mmdc.cmd"

# Step 3: Run the Mermaid CLI command to generate the image
try:
    subprocess.run([mmdc_path, "-i", mermaid_file, "-o", output_image], check=True)
    print(f"Flowchart successfully saved as {output_image}")
except subprocess.CalledProcessError as e:
    print(f"Error generating the flowchart: {e}")
except FileNotFoundError as e:
    print(f"FileNotFoundError: Could not find mmdc. Ensure it is installed and its path is correct.")
finally:
    # Clean up the temporary Mermaid file
    if os.path.exists(mermaid_file):
        os.remove(mermaid_file)
