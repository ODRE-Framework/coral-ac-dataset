# Hospital Access Control Policy Dataset (RLS ↔ ODRL)

This repository hosts a curated dataset of hospital access control policies originally implemented using Row-Level Security (RLS) in PostgreSQL and manually translated into the Open Digital Rights Language (ODRL). The dataset was developed to support reproducible research on policy representation, enforcement, and evaluation in regulated domains such as healthcare.

The dataset is published alongside the scientific article:

> *Title*  
> Conference.

The repository is intended to facilitate benchmarking, formal analysis, and comparative evaluation of policy enforcement mechanisms.

---

## Dataset Structure

Each policy is contained in its own directory organized as follows:

````
PXX_<Policy_Title>/
├── rls.sql
├── odrl.jsonld
├── policy.txt
├── evaluation_requests/
│ ├── PXX-n.jsonld
│ └── ...
├── evaluation_requests_index.json
├── state_of_world.json (optional)
````


- `rls.sql` — PostgreSQL RLS rules corresponding to the policy.
- `odrl.jsonld` — ODRL policy encoded in JSON-LD.
- `policy.txt` — Natural language description of the policy.
- `evaluation_requests/` — One evaluation request per test case in JSON-LD.
- `evaluation_requests_index.json` — Mapping from case identifiers (e.g., `P01-1`) to individual evaluation request files.
- `state_of_world.json` — Contextual state definitions for cases where the state is non-empty.
- `dataset_description.json` — Dataset metadata at the repository root.

---

## Policy Index

The table below provides direct links to each policy in its different representations. This structure allows reviewers to inspect the alignment between:

- Database-native enforcement (RLS),
- Semantic policy representation (ODRL),
- Natural language description,
- Contextual states, and
- Evaluation requests.

| Policy ID | Title | RLS | ODRL | Natural Language | State of World | Evaluation Requests |
|-----------|-------|-----|------|------------------|----------------|--------------------|
| **P01** | Global Reading of Patients | [rls.sql](./P01_Global_Reading_of_Patients/rls.sql) | [odrl.jsonld](./P01_Global_Reading_of_Patients/odrl.jsonld) | [policy.txt](./P01_Global_Reading_of_Patients/policy.txt) | — | [Index](./P01_Global_Reading_of_Patients/evaluation_requests_index.json) |
| **P02** | Employee Management by Admin | [rls.sql](./P02_Employee_Management_by_Admin/rls.sql) | [odrl.jsonld](./P02_Employee_Management_by_Admin/odrl.jsonld) | [policy.txt](./P02_Employee_Management_by_Admin/policy.txt) | — | [Index](./P02_Employee_Management_by_Admin/evaluation_requests_index.json) |
| **P03** | Read-Only Audit | [rls.sql](./P03_Read-Only_Audit/rls.sql) | [odrl.jsonld](./P03_Read-Only_Audit/odrl.jsonld) | [policy.txt](./P03_Read-Only_Audit/policy.txt) | — | [Index](./P03_Read-Only_Audit/evaluation_requests_index.json) |
| **P04** | Patient: Access to Own Record | [rls.sql](./P04_Patient_Access_to_Own_Record/rls.sql) | [odrl.jsonld](./P04_Patient_Access_to_Own_Record/odrl.jsonld) | [policy.txt](./P04_Patient_Access_to_Own_Record/policy.txt) | — | [Index](./P04_Patient_Access_to_Own_Record/evaluation_requests_index.json) |
| **P05** | Assigned Physician: Can Write/Edit Notes | [rls.sql](./P05_Assigned_Physician_Can_WriteEdit_Notes/rls.sql) | [odrl.jsonld](./P05_Assigned_Physician_Can_WriteEdit_Notes/odrl.jsonld) | [policy.txt](./P05_Assigned_Physician_Can_WriteEdit_Notes/policy.txt) | — | [Index](./P05_Assigned_Physician_Can_WriteEdit_Notes/evaluation_requests_index.json) |
| **P06** | Department Head: Reading by Ward Membership | [rls.sql](./P06_Department_Head_Reading_by_Ward_Membership/rls.sql) | [odrl.jsonld](./P06_Department_Head_Reading_by_Ward_Membership/odrl.jsonld) | [policy.txt](./P06_Department_Head_Reading_by_Ward_Membership/policy.txt) | — | [Index](./P06_Department_Head_Reading_by_Ward_Membership/evaluation_requests_index.json) |
| **P07** | Emergency: Access by Emergency (Break-the-Glass) | [rls.sql](./P07_Emergency_Access_by_Emergency_Break-the-Glass/rls.sql) | [odrl.jsonld](./P07_Emergency_Access_by_Emergency_Break-the-Glass/odrl.jsonld) | [policy.txt](./P07_Emergency_Access_by_Emergency_Break-the-Glass/policy.txt) | [state](./P07_Emergency_Access_by_Emergency_Break-the-Glass/state_of_world.json) | [Index](./P07_Emergency_Access_by_Emergency_Break-the-Glass/evaluation_requests_index.json) |
| **P08** | Research: Anonymized Data Only | [rls.sql](./P08_Research_Anonymized_Data_Only/rls.sql) | [odrl.jsonld](./P08_Research_Anonymized_Data_Only/odrl.jsonld) | [policy.txt](./P08_Research_Anonymized_Data_Only/policy.txt) | [state](./P08_Research_Anonymized_Data_Only/state_of_world.json) | [Index](./P08_Research_Anonymized_Data_Only/evaluation_requests_index.json) |
| **P09** | Administrative: Forbidden to Create Appointment if Debtor | [rls.sql](./P09_Administrative_Forbidden_to_Create_Appointment_if_Debtor/rls.sql) | [odrl.jsonld](./P09_Administrative_Forbidden_to_Create_Appointment_if_Debtor/odrl.jsonld) | [policy.txt](./P09_Administrative_Forbidden_to_Create_Appointment_if_Debtor/policy.txt) | [state](./P09_Administrative_Forbidden_to_Create_Appointment_if_Debtor/state_of_world.json) | [Index](./P09_Administrative_Forbidden_to_Create_Appointment_if_Debtor/evaluation_requests_index.json) |
| **P10** | Nursing: Access During Shift Window | [rls.sql](./P10_Nursing_Access_During_Shift_Window/rls.sql) | [odrl.jsonld](./P10_Nursing_Access_During_Shift_Window/odrl.jsonld) | [policy.txt](./P10_Nursing_Access_During_Shift_Window/policy.txt) | [state](./P10_Nursing_Access_During_Shift_Window/state_of_world.json) | [Index](./P10_Nursing_Access_During_Shift_Window/evaluation_requests_index.json) |
| **P11** | Prescription of Medications | [rls.sql](./P11_Prescription_of_Medications/rls.sql) | [odrl.jsonld](./P11_Prescription_of_Medications/odrl.jsonld) | [policy.txt](./P11_Prescription_of_Medications/policy.txt) | — | [Index](./P11_Prescription_of_Medications/evaluation_requests_index.json) |
| **P12** | Pharmaceutical Dispensing | [rls.sql](./P12_Pharmaceutical_Dispensing/rls.sql) | [odrl.jsonld](./P12_Pharmaceutical_Dispensing/odrl.jsonld) | [policy.txt](./P12_Pharmaceutical_Dispensing/policy.txt) | [state](./P12_Pharmaceutical_Dispensing/state_of_world.json) | [Index](./P12_Pharmaceutical_Dispensing/evaluation_requests_index.json) |
| **P13** | External Consultation | [rls.sql](./P13_External_Consultation/rls.sql) | [odrl.jsonld](./P13_External_Consultation/odrl.jsonld) | [policy.txt](./P13_External_Consultation/policy.txt) | [state](./P13_External_Consultation/state_of_world.json) | [Index](./P13_External_Consultation/evaluation_requests_index.json) |
| **P14** | Legal Guardian / Parent: Access to Minors | [rls.sql](./P14_Legal_Guardian_Parent_Access_to_Minors/rls.sql) | [odrl.jsonld](./P14_Legal_Guardian_Parent_Access_to_Minors/odrl.jsonld) | [policy.txt](./P14_Legal_Guardian_Parent_Access_to_Minors/policy.txt) | [state](./P14_Legal_Guardian_Parent_Access_to_Minors/state_of_world.json) | [Index](./P14_Legal_Guardian_Parent_Access_to_Minors/evaluation_requests_index.json) |
| **P15** | Laboratory: Entry of Results | [rls.sql](./P15_Laboratory_Entry_of_Results/rls.sql) | [odrl.jsonld](./P15_Laboratory_Entry_of_Results/odrl.jsonld) | [policy.txt](./P15_Laboratory_Entry_of_Results/policy.txt) | — | [Index](./P15_Laboratory_Entry_of_Results/evaluation_requests_index.json) |

---

## Evaluation Setting

Each policy is accompanied by explicitly defined evaluation requests and expected outcomes. The dataset therefore supports:

- Benchmarking of ODRL evaluators,
- Formal semantic analysis,
- Compliance verification experiments,
- Cross-language policy translation (RLS ↔ ODRL ↔ Natural Language),
- Policy recommendation and synthesis research.

The inclusion of contextual state definitions where applicable enables reproducible testing under controlled conditions.




