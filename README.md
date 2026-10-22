# AI Governance Helper for HR

A Streamlit **prototype** that guides nontechnical teams through AI-tool registration, risk review, ownership assignment, and a summary of their recorded use cases.

> **Status: demonstration / work in progress.** The current local demo uses Streamlit session state; entries are not durable records. Do not enter real employee, candidate, client, or confidential information.

## Workflow

1. **Home:** See the workflow and high-level counts.
2. **Add a Tool:** Register an AI use case.
3. **My Tools:** Review registered entries.
4. **Assess Risks:** Record risk information.
5. **Assign Owners:** Document responsibility.
6. **Summary:** Review the recorded entries.

The accompanying implementation methodology describes seven risk categories (Accuracy, Privacy, Bias, Security, Legal, Dependency, Reputation), a highest-category risk rule, named accountability, and quarterly review cadence. **Those methodology requirements must be separately verified against the running app; this README does not claim the prototype implements all of them.**

## Run locally

Use Python 3 and a dedicated virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Visit the local URL printed by Streamlit (often http://localhost:8501).

## Limitations

- Prototype for education and demonstration, **not a production governance system**.
- Session-only data may disappear on restart, refresh, or session expiry.
- No claim of legal compliance, certification, independent model testing, or audit-grade persistence.
- Use fictional/synthetic examples for demonstrations.
- Do not treat any output as a substitute for legal, compliance, security, or professional risk review.

## Roadmap / verification gates

- Validate the entire tool → risk assessment → ownership → summary workflow.
- Check all seven risk categories, completeness rules, HIGH flags, RACI constraints, and review cadence against the documented methodology.
- Add secure persistence, authentication, audit trail, export, and tests before considering real client use.

## Author

Tracy Anne Griffin Manning · AI Platform Engineering | Enterprise Cloud Architecture | AI Strategy & Consulting

MIT License. See [LICENSE](LICENSE).
