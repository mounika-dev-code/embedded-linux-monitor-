import subprocess
import json
import logging

# create logger
logger = logging.getLogger(__name__)

def get_metrics():
    """
    Executes external health agent,
    parses JSON response,
    and returns metrics data.
    """
    try:
        logger.info("Executing health agent")

        result = subprocess.check_output(
            ["../agent/health_agent"],
            stderr=subprocess.STDOUT
        )

        result_str = result.decode("utf-8")
        data = json.loads(result_str)

        logger.info("Successfully fetched metrics")
        return data

    except subprocess.CalledProcessError as e:
        logger.error("Subprocess failed")
        raise Exception(f"Subprocess failed: {e.output.decode('utf-8')}")

    except FileNotFoundError:
        logger.error("Agent executable not found")
        raise Exception("Agent executable not found")

    except json.JSONDecodeError:
        logger.error("Invalid JSON output from agent")
        raise Exception("Invalid JSON output from agent")
