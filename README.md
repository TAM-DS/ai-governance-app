# AI Governance Toolkit
### Your organization has an AI strategy. Can it prove who's accountable for the AI already in use?

**Inventory the tools. Identify the risks. Name the owners. Make oversight visible.**

AI adoption is not the same as AI governance. A policy alone cannot tell an organization which tools are in use, what information they process, where human approval is required, or who is accountable when something goes wrong.

**AI Governance Toolkit** is a free, open-source, practical starting point for answering those questions—with a guided Streamlit prototype and an accompanying governance methodology.

> **Public Edition · Prototype / work in progress**
>
> Built for exploration, education, and demonstration. **Not a production-ready compliance or audit system.** Use synthetic records only. The app currently stores data in Streamlit session state, not in durable storage.

---

## The executive question

Before giving another AI system access to a consequential workflow, can your organization answer these questions?

| Question | What operational governance needs |
|---|---|
| **What AI is actually in use?** | A consistent inventory, including shadow-AI discovery practices |
| **What could go wrong?** | Repeatable risk categories, rationale, mitigations, and visible HIGH flags |
| **Who owns the outcome?** | Named owners and explicit Responsible / Accountable assignments |
| **What can be demonstrated?** | Evidence of review, current status, and documented decisions |
| **What needs attention next?** | A practical assessment and operating cadence |

**Capability is not authority.** A tool can generate an answer without being authorized to make the decision.

## What you'll find here

### 🖥️ Guided Streamlit experience

A friendly interface oriented toward nontechnical teams:

`Home → Add a Tool → My Tools → Assess Risks → Assign Owners → Summary`

The current app is a **session-based demonstration** of this workflow. Its calculations and enforcement of the complete methodology have **not yet been independently verified**.

### 📘 Governance methodology

The accompanying implementation approach defines:

- **Seven risk categories:** Accuracy, Privacy, Bias, Security, Legal, Dependency, Reputation.
- **Explicit triage:** LOW, MEDIUM, HIGH, using the **highest category score** for overall risk.
- **Assessment completeness:** all seven categories require score, rationale, mitigation, owner, and date.
- **Early HIGH visibility:** recorded HIGH flags should remain visible even if an assessment is incomplete.
- **Named accountability:** exactly one Accountable (A), at least one Responsible (R), and a named accountable individual.
- **Review cadence:** an assessment becomes overdue after three calendar months.
- **Maturity assessment:** 20 questions scored 1–5, with no maturity level on partial or invalid responses.

These are **documented methodology rules**, not blanket claims about features already implemented in the Streamlit code.

### 📊 Supporting toolkit and public documentation

A companion Excel governance workbook, an executive presentation, and an implementation guide form the broader **AI Governance Toolkit — Public Edition**. Public copies will be linked here **after they are finalized and published**. No dead download links.

## Who it's for

- **Business and HR teams:** understand the tools being used and surface ownership and review questions.
- **Risk, security, and compliance teams:** establish a structured conversation around evidence, controls, and gaps.
- **Cloud and AI platform engineers:** demonstrate where governance boundaries need to meet implementation.
- **Consultants and transformation leaders:** use a concise, repeatable starting point for discovery workshops.

This toolkit is **vendor-neutral** and does not require purchasing an enterprise governance platform to explore the methodology.

## Run the Streamlit prototype locally

The Python app files are **not yet committed to this repository**. Once `app.py` and `requirements.txt` are uploaded, the local workflow is:

```bash
git clone https://github.com/TAM-DS/ai-governance-app.git
cd ai-governance-app

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL reported by Streamlit (typically `http://localhost:8501`). On Windows, activate with `.venv\Scripts\activate`.

**Do not upload local virtual environments, passwords, client files, employee records, or applicant information.** The repository includes a `.gitignore` for common local artifacts.

## Suggested demo: an AI resume-screening tool

Use entirely fictional names and synthetic data:

1. Register a hypothetical resume-screening application and describe its proposed use.
2. Consider the risk of incorrect rejection, bias, personal-data exposure, and security failures.
3. Record the mitigation and who must review decisions before any action is taken.
4. Assign a named accountable owner and examine the summary.
5. Restart the session to observe the prototype's current persistence limitation.

**Important:** An AI-generated recommendation to reject a candidate is **not authorization** to do so. Actual employment-related use requires appropriate human review, legal analysis, technical validation, and organizational controls.

## Implementation roadmap

| Stage | Focus | Evidence of completion |
|---|---|---|
| **1. Discover** | Tool inventory, data, users, stable IDs | Reconciled list of use cases |
| **2. Assess** | Seven risk categories and mitigations | Complete, reviewed risk records |
| **3. Assign** | Named owners and responsibility | Accountable owner + responsible roles |
| **4. Operate** | Review cadence and escalation | Dated decisions and tracked actions |
| **5. Improve** | Governance maturity and control gaps | Prioritized improvement plan |

The broader methodology offers an illustrative phased rollout; real scope depends on the organization.

## Trust boundaries and limitations

**This project does not:**

- certify compliance with NIST AI RMF, ISO/IEC 42001, the EU AI Act, or any law;
- replace legal advice, security reviews, bias testing, red teaming, or enterprise model evaluation;
- provide authentication, secure multi-user persistence, tamper-resistant audit trails, or production-grade access controls in the current app;
- prove that the Streamlit prototype enforces every rule in the accompanying governance methodology;
- authorize an AI tool to make consequential decisions about people, customers, finances, or operations.

**Standards alignment** means the methodology can *support* governance activities; it is not a certification or regulatory determination.

## Before wider deployment

Current engineering priorities:

- [ ] Commit and inspect the actual Streamlit source and dependencies.
- [ ] Test the end-to-end registration → risk → ownership → summary path.
- [ ] Implement and test all seven-category completeness and severity rules.
- [ ] Validate RACI constraints, HIGH risk visibility, and overdue-review calculations.
- [ ] Add appropriate durable storage, authentication, authorization, and audit history.
- [ ] Publish tested, clearly labeled Public Edition supporting materials.
- [ ] Add reproducible automated tests and a guided synthetic-data demonstration.

Issues and thoughtful contributions are welcome—especially around usability, trustworthy governance boundaries, testing, accessibility, and maintainability.

## Why this exists

Enterprise AI governance should be **understandable to the people responsible for using it**, not confined to a policy document.

Start with the workflow. Make decisions explicit. Preserve human authority. Document the evidence.

**Clarity over cleverness. Correctness over speed. Evidence over hype.**

---

**Created by Tracy Anne Griffin Manning**  
AI Platform Engineer | Enterprise Cloud Architecture | AI Strategy & Consulting  
[Professional site](https://tam-ds.github.io/) · [LinkedIn](https://www.linkedin.com/in/tracymanning/) · [GitHub](https://github.com/TAM-DS)

**License:** [MIT](LICENSE). Free to use, modify, and share under the license terms.
