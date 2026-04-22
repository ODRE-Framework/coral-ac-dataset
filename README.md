# CORAL-AC: ODRL Hospital Access Control Policy Dataset

This repository contains the **CORAL-AC dataset**, a curated collection of hospital access control policies originally implemented using **Row-Level Security (RLS) in PostgreSQL** and manually translated into the **Open Digital Rights Language (ODRL)**.

The dataset was created to support **reproducible research on semantic policy modelling, policy evaluation, policy recommendation, and policy engine validation**, particularly in regulated domains such as healthcare where transparency, interoperability, and auditability are essential.

Each policy is provided in **four aligned representations**:

- Natural language description
- PostgreSQL Row-Level Security (RLS) rule
- ODRL policy expressed in JSON-LD
- ODRL+ODRE policy expressed in JSON-LD

Additionally, the dataset includes **evaluation artefacts** following the conceptual model proposed in the **ODRL formal semantics**, including:

- evaluation requests
- contextual states of the world
- expected evaluation outcomes

The repository is intended to facilitate benchmarking, formal analysis, and comparative evaluation of policy enforcement mechanisms. These artefacts allow **independent validation of ODRL policy evaluators without requiring the original relational infrastructure**. 


The dataset accompanies the scientific article:

> **CORAL-AC: A Dataset of Hospital Access Control Policies for ODRL Evaluation**  
> OPAL Workshop 2026 — ODRL and beyond: practical applications and challenges for policy-base access and usage control



---

## Dataset Structure

Each policy is contained in its own directory organized as follows:

````
PXX_<Policy_Title>/
├── rls.sql
├── odrl.jsonld
├── odre.jsonld
├── policy.txt
├── evaluation_requests/
│ ├── PXX-n.jsonld
│ └── ...
├── sow/
│ ├── statePXX-n.jsonld
│ └── ...
├── evaluation_requests_index.json
├── state_of_world.json (optional)
````


- `rls.sql` — PostgreSQL RLS rules corresponding to the policy.
- `odrl.jsonld` — ODRL policy encoded in JSON-LD.
- `odre.json` — ODRL policy encoded in JSON-LD using ODRE.
- `policy.txt` — Natural language description of the policy.
- `evaluation_requests/` — One evaluation request per test case in JSON-LD.
- `evaluation_requests_index.json` — Mapping from case identifiers (e.g., `P01-1`) to individual evaluation request files.
- `state_of_world.json` — Contextual state definitions for cases where the state is non-empty.
- `dataset_description.json` — Dataset metadata at the repository root.

---

## CORAL-AC Ontology concepts

* **sch:Physician** extends **sch:Person**. A medical professional responsible for diagnosing patients, prescribing treatments, and accessing the clinical information required for patient care.
* **coral:NurseStaff** extends **sch:Person**. Represents nursing personnel responsible for monitoring patients, updating clinical observations, and assisting physicians during treatment.
* **sch:Patient** extends **sch:Person**. Represents an individual receiving medical care whose personal and clinical information is stored in the hospital information system.
* **coral:MedicalRecord**. Represents the digital record containing the medical history, diagnoses, treatments, and clinical observations associated with a patient.
* **coral:SystemAdministrator** extends **sch:Person**. A technical role responsible for maintaining the hospital information system infrastructure, including database management and system configuration.
* **coral:Auditor** extends **sch:Person**. A role responsible for reviewing and verifying access to medical records and system operations to ensure compliance with regulatory and organisational policies.
* **coral:DepartmentPhysicianHead** extends **sch:Person**. A senior physician responsible for supervising clinical staff within a department and overseeing medical decisions and operational procedures.
* **coral:EmergencyPhysician** extends **sch:Physician**. A specialist emergency physician who is authorised to access critical patient information during emergency medical situations.
* **coral:HospitalResearchMember** extends **sch:Person**. Represents hospital-affiliated researchers who can access anonymised or aggregated clinical data for research purposes.
* **coral:AdministrativeMember** extends **sch:Person**. Administrative staff responsible for operational tasks such as appointment scheduling, patient registration, and administrative management.
* **coral:Pharmacist** extends **sch:Person**. Healthcare professional responsible for dispensing medications, verifying prescriptions, and managing pharmaceutical records.
* **coral:LegalGuardian** extends **sch:Person**. Represents a person legally responsible for a patient, typically in the case of minors or individuals requiring legal representation.
* **coral:LaboratoryTechnician** extends **sch:Person**. Technical staff responsible for performing laboratory analyses and managing diagnostic test results associated with patients.
* **coral:SpecialistPhysician** extends **sch:Physician**. A physician with specialised expertise who may be granted temporary access to patient records for consultation or specialised treatment.

---

## Coral Relational Tables


* **db:PatientsRegistry** is a table containing all the patient personal information, containing columns such **as name**, **surname**, **address**.
    
* **db:EmployeeRecords** is a table that holds all the information of the hospital staff. The table contains columns such **as name**, **surname**, **address**, and **position** which indicate whether a person is hired as a physician, nurse, administrator, etc. 
    
* **db:ClinicalRecords** is the table that contains their clinical records for each patient. It contains a foreign key to the **db:PatientsRegistry** to know who is the patient, and another to the **db:EmployeeRecords** to know which doctor created the record. In addition, it contains a column **record** with the information.
    
* **db:BillingInformation** is the table that contains the financial information associated with each patient, including the billing status and payment records related to medical services.
    
* **db:AppointmentScheduling** is the table containing for each patient their appointments with doctors. It contains a foreign key to the **db:PatientsRegistry** to know who is the patient, and another to the **db:EmployeeRecords** to know with which doctor is the appointment. In addition, it contains the column **date** with the appointment day and time. 
    
* **db:MedicationPrescriptions** is the table containing the prescriptions for medications issued by physicians and the records of medication administration associated with patients.
    
* **db:LaboratoryTestResults** is the table containing the diagnostic test results generated by laboratory analyses associated with patients.


--- 
## Evaluation Setting

Each policy is accompanied by explicitly defined evaluation requests and expected outcomes. The dataset therefore supports:

- Benchmarking of ODRL evaluators,
- Formal semantic analysis,
- Compliance verification experiments,
- Cross-language policy translation (RLS ↔ ODRL ↔ Natural Language),
- Policy recommendation and synthesis research.

The inclusion of contextual state definitions where applicable enables reproducible testing under controlled conditions.


## Acknowledgements

### This project have been partially funded by:

 | Project       | Grant |
 |   :---:      |      :---      |
 | <img src="https://github.com/user-attachments/assets/152dc6f1-e418-41bc-9c50-88cc88b33525" height="80"/>| The Madrid Government (Comunidad de Madrid-Spain) under the Multiannual Agreement with the Universidad Politécnica de Madrid in the Excellence Programme for University Teaching Staff, in the context of the V PRICIT (Regional Programme of Research and Technological Innovation) through the project GUIA (M230020126A-AJCA). |
 | <img src="https://malta.linkeddata.es/malta.png" height="80"/> | The [MALTA](https://malta.linkeddata.es/) project, PID2024-159504OB-I00 funded by MICIU/AEI/10.13039/501100011033 |


