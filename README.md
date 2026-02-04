# Web Security Scanner – Execution-Based Demo

This repository is a **demonstration project** showcasing a web security
scanner that focuses on **confirming real vulnerabilities through execution**
instead of reporting raw reflections or theoretical issues.

The goal of this demo is to show **how modern AppSec tooling should behave**
when accuracy and actionability matter more than volume.

---

## ❗ What Problem Does This Solve?

Most security scanners report:
- reflected strings as XSS
- theoretical issues without proof
- large amounts of false positives

This demo shows a different approach:

- vulnerabilities are reported **only if execution is confirmed**
- results are confidence-based
- noise is intentionally reduced

This makes the findings **actionable**, not just informative.

---

## 🔍 What This Demo Shows

This repository demonstrates:

- Reflected XSS validation via real JavaScript execution
- Stored XSS confirmation using replay-based logic
- Runtime analysis instead of regex-based detection
- Confidence scoring to prioritize real risks

⚠️ This is **not a full scanner**.  
It is a **focused demo of core concepts**.

---

## 🧠 How the Scanner Works (Conceptual Overview)

The scanner follows this general workflow:

1. Inject a controlled payload
2. Observe the application response
3. Monitor runtime behavior in a browser context
4. Confirm JavaScript execution
5. Report a finding **only if execution occurs**

If no execution is detected, **no vulnerability is reported**.

---

## 🔁 Example Workflow

A typical scan flow looks like this:

1. Target page is loaded
2. Payload is injected
3. Browser context is monitored
4. JavaScript execution is observed
5. Confidence score is calculated
6. Result is returned only if confirmed

This avoids reporting issues that cannot be exploited in practice.

---

## 📊 Example Finding Output

```json
{
  "type": "xss",
  "execution_confirmed": true,
  "confidence": 91,
  "severity": "High",
  "description": "Reflected XSS with confirmed JavaScript execution"
}
