#!/usr/bin/env python3
"""
combination_engine.py

CLI for the Combination Engine framework: a five-step method for finding
non-obvious innovation opportunities via cross-domain patent search.

Usage:
    python combination_engine.py                           # interactive walkthrough
    python combination_engine.py --step friction \
        --input "sensors drain too fast" --domain IoT      # single step, print prompt
    python combination_engine.py --auto --output out.json  # call Anthropic API automatically
"""

import os
import sys
import json
import argparse
import textwrap
from datetime import datetime
from pathlib import Path

try:
    import anthropic
    _HAS_ANTHROPIC = True
except ImportError:
    _HAS_ANTHROPIC = False

STEPS = ["friction", "contradiction", "cross-domain", "expired-patents", "filter"]

_PROMPTS = {
    "friction": (
        "I'm trying to solve a problem in {domain}.\n\n"
        "The friction is: {input}\n\n"
        "Help me restate this as a single friction point: one sentence, no buzzwords, "
        "no solution embedded in the problem statement. The sentence should be "
        "falsifiable — a reader should be able to tell whether it is solved or not.\n\n"
        "Then tell me what this friction point is NOT, so I can bound the search space."
    ),
    "contradiction": (
        "My friction point is: {input}\n\n"
        "Help me identify the core contradiction: what two things must simultaneously "
        "be true for this problem to be solved, but cannot both be true given current "
        "constraints?\n\n"
        "Format it as:\n"
        "- The system must be [PROPERTY A] — because [REASON]\n"
        "- The system must also be [PROPERTY B] — because [REASON]\n"
        "- These conflict because [WHY THEY CANNOT BOTH BE TRUE TODAY]\n\n"
        "Then identify which TRIZ engineering parameters this maps to. "
        "List the top 2-3 candidate parameter pairs and the inventive principles "
        "most commonly associated with them."
    ),
    "cross-domain": (
        "My contradiction is: {input}\n\n"
        "Ignore my specific domain ({domain}) entirely.\n\n"
        "Search your knowledge of patents, engineering history, and product development "
        "across all other fields for cases where this same structural tension was resolved.\n\n"
        "For each example:\n"
        "1. Name the domain and approximate decade\n"
        "2. Describe how the contradiction was resolved (the mechanism, not the product name)\n"
        "3. Identify what enabling condition made the solution possible\n"
        "4. Rate transferability to my domain: High / Medium / Low, "
        "with one sentence of reasoning\n\n"
        "Return 5-8 examples. Prioritize diversity of domain."
    ),
    "expired-patents": (
        "My friction point: {input}\n"
        "My domain: {domain}\n\n"
        "I want to find expired patents — filed more than 20 years ago — that attempted "
        "to solve this problem or a structurally similar one.\n\n"
        "For each candidate mechanism:\n"
        "1. Plain-language description of the mechanism\n"
        "2. Original application domain\n"
        "3. Why it likely failed or stalled commercially\n"
        "4. What has changed since filing — materials, regulation, computing, "
        "manufacturing, market — that changes the viability calculus\n"
        "5. Relevance to my friction point: High / Medium / Low\n\n"
        "Return 4-6 candidates."
    ),
    "filter": (
        "I have the following candidate mechanisms for solving: {input}\n\n"
        "Apply these kill tests to each, stopping at first failure:\n\n"
        "1. Physics: Does this violate any physical constraint in the application environment?\n"
        "2. Regulatory: Does applying this trigger a prohibitive regulatory burden?\n"
        "3. Economics: Do unit economics make sense at realistic scale?\n"
        "4. Moat: Is there anything durable here if this works?\n"
        "5. Keystone dependency: Does this depend on a single withdrawable input?\n\n"
        "Return Pass/Fail at each test with one-sentence reason for any failure. "
        "For each candidate that passes all five tests, write one paragraph "
        "on what makes it defensible."
    ),
}


def _wrap(text: str, width: int = 76) -> str:
    return "\n".join(
        textwrap.fill(line, width) if line.strip() else line
        for line in text.splitlines()
    )


def _header(title: str) -> None:
    bar = "\u2500" * 60
    print(f"\n{bar}\n  {title}\n{bar}\n")


def _build_prompt(step: str, user_input: str, domain: str) -> str:
    return _PROMPTS[step].format(input=user_input, domain=domain or "unspecified")


def _call_api(prompt: str, model: str) -> str:
    if not _HAS_ANTHROPIC:
        return "[anthropic package not installed — run: pip install anthropic]"
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return "[ANTHROPIC_API_KEY not set — showing prompt only]"
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=model,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def _run_interactive(args: argparse.Namespace) -> None:
    session: dict = {
        "created": datetime.now().isoformat(),
        "domain": "",
        "steps": {},
    }

    _header("THE COMBINATION ENGINE")
    print("A five-step framework for combinatorial innovation.\n")
    print("Each step generates a structured prompt. Paste it into any LLM,")
    print("or set ANTHROPIC_API_KEY to call the Anthropic API automatically.\n")

    domain = input("What domain are you working in? -> ").strip()
    session["domain"] = domain
    carry = ""

    for step in STEPS:
        _header(f"STEP: {step.upper().replace('-', ' ')}")

        if carry:
            preview = carry[:120] + ("..." if len(carry) > 120 else "")
            print(f"Previous step output:\n  {preview}\n")
            use = input("Use this as input for this step? [Y/n] -> ").strip().lower()
            user_input = carry if use in ("", "y", "yes") else input("Enter input -> ").strip()
        else:
            user_input = input("Describe the problem -> ").strip()

        prompt = _build_prompt(step, user_input, domain)
        print(f"\n--- Generated Prompt ---\n\n{_wrap(prompt)}\n")

        if args.auto:
            print("Calling API...\n")
            response = _call_api(prompt, args.model)
            print(f"--- Response ---\n\n{_wrap(response)}\n")
            carry = response
        else:
            carry = input(
                "Paste the LLM response to carry forward (or press Enter to skip) -> "
            ).strip()

        session["steps"][step] = {
            "input": user_input,
            "prompt": prompt,
            "response": carry,
        }

        again = input("\nContinue to next step? [Y/n] -> ").strip().lower()
        if again in ("n", "no"):
            break

    if args.output:
        Path(args.output).write_text(json.dumps(session, indent=2))
        print(f"\nSession saved to {args.output}")

    _header("SESSION COMPLETE")
    print("Review outputs above. Candidates that survived Step 5 filtering")
    print("are your starting points for prototyping or further patent research.\n")


def _run_single(args: argparse.Namespace) -> None:
    prompt = _build_prompt(args.step, args.input, args.domain or "")
    print(prompt)
    if args.auto:
        print(f"\n{_call_api(prompt, args.model)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="The Combination Engine -- combinatorial innovation framework CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            examples:
              python combination_engine.py

              python combination_engine.py --step friction \\
                --input "field sensors drain batteries in 6 months, need 5-year deployment" \\
                --domain "industrial IoT"

              export ANTHROPIC_API_KEY=sk-...
              python combination_engine.py --auto --output session.json
        """),
    )
    parser.add_argument(
        "--step", choices=STEPS,
        help="Run a single step instead of the full walkthrough",
    )
    parser.add_argument(
        "--input",
        help="Input text for the step (required with --step)",
    )
    parser.add_argument(
        "--domain",
        help="Application domain",
    )
    parser.add_argument(
        "--auto", action="store_true",
        help="Call Anthropic API automatically (requires ANTHROPIC_API_KEY)",
    )
    parser.add_argument(
        "--output", metavar="FILE",
        help="Save the session as a JSON file",
    )
    parser.add_argument(
        "--model", default="claude-opus-4-7",
        help="Model ID for --auto mode (default: claude-opus-4-7)",
    )
    args = parser.parse_args()

    if args.step:
        if not args.input:
            parser.error("--input is required when --step is specified")
        _run_single(args)
    else:
        _run_interactive(args)


if __name__ == "__main__":
    main()
