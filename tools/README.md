# CLI Tool

`combination_engine.py` is a command-line interface for the five-step Combination Engine method. It generates a structured prompt for each step, carries outputs between steps, and optionally calls the Anthropic API automatically.

---

## Installation

```bash
pip install -r requirements.txt
```

Requires Python 3.9+. The Anthropic SDK is optional — without it the tool prints prompts for manual copy-paste into any LLM.

---

## Usage

### Interactive mode (recommended for first use)

```bash
python combination_engine.py
```

Walks through all five steps in sequence. At each step you can paste the output from the previous step or type a new input. The tool carries outputs forward automatically.

### Single step

```bash
python combination_engine.py \
  --step friction \
  --input "field sensors drain batteries in 6 months but need 5-year deployment" \
  --domain "industrial IoT"
```

Prints the generated prompt and exits. Available steps: `friction`, `contradiction`, `cross-domain`, `expired-patents`, `filter`.

### Automatic mode (Anthropic API)

```bash
export ANTHROPIC_API_KEY=your_key_here
python combination_engine.py --auto --output session.json
```

With `--auto`, the tool calls the API at each step and carries the response forward automatically. The full session is saved as JSON if `--output` is specified.

---

## Options

| Flag | Description |
|------|-------------|
| `--step` | Run a single step instead of the full walkthrough |
| `--input TEXT` | Input text (required with `--step`) |
| `--domain TEXT` | Application domain |
| `--auto` | Call Anthropic API automatically |
| `--output FILE` | Save session as JSON |
| `--model ID` | Model for `--auto` mode (default: `claude-opus-4-7`) |

---

## Session Output Format

When `--output` is specified, the session is saved as:

```json
{
  "created": "2026-04-22T10:00:00",
  "domain": "industrial IoT",
  "steps": {
    "friction": {
      "input": "sensors drain batteries in 6 months",
      "prompt": "...",
      "response": "..."
    },
    "contradiction": { ... },
    ...
  }
}
```
