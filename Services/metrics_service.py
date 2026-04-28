import subprocess
import json

def get_metrics():
    try:
        result = subprocess.check_output(
            ["../agent/health_agent"],
            stderr=subprocess.STDOUT
        )

        result_str = result.decode("utf-8")
        data = json.loads(result_str)

        return data

    except subprocess.CalledProcessError as e:
        raise Exception(f"Subprocess failed: {e.output.decode('utf-8')}")

    except FileNotFoundError:
        raise Exception("Agent executable not found")

    except json.JSONDecodeError:
        raise Exception("Invalid JSON output from agent")
