
from flask import Flask, send_from_directory, jsonify
import subprocess
import sys
from pathlib import Path
import re

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/generate")
def generate():
    try:
        result = subprocess.run(
            [
                sys.executable,
                "sample.py",
                "--out_dir=out_movies2",
                "--device=cpu",
                "--compile=False",
                "--num_samples=1",
                "--max_new_tokens=300"
            ],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120
        )

        if result.returncode != 0:
            return jsonify({
                "error": "Text generation failed. Check the Flask terminal."
            }), 500

        
        # Remove nanoGPT configuration and model-loading logs
        output_lines = result.stdout.splitlines()

        log_prefixes = (
            "Overriding:",
            "number of parameters:",
            "Loading meta from",
            )

        clean_lines = [
            line for line in output_lines
            if not line.strip().startswith(log_prefixes)
            ]   

        output = "\n".join(clean_lines).strip()
        # Remove leftover HTML tags from generated text
        output = re.sub(r"</?[^>]+>", "", output)
        # Keep only complete sentences at the end
        last_end = max(
            output.rfind("."),
            output.rfind("?"),
            output.rfind("!")
        )

        if last_end != -1:
            output = output[:last_end + 1].strip()


        # Keep the generated text after the last separator, if present.
        if "---------------" in output:
            output = output.split("---------------")[-1].strip()

        if not output:
            return jsonify({"error": "No text was generated."}), 500

        return jsonify({"text": output})

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Generation timed out."}), 504
    except Exception:
        app.logger.exception("Generation failed")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == "__main__":
    app.run(debug=True)
