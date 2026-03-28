# Cloud Architecture: Home Assignment

**Topic:** Cloud Services Knowledge - System Design & Architecture

**Estimated Time:** 30-45 minutes

## Assignment Prompt

### Scenario

You are joining XYZ Inc., a logistics company managing warehousing and inventory for multiple partner brands. They currently rely on an on-premise PostgreSQL setup and batch uploads from warehouses via CSV files.

The company is now migrating to the cloud and is choosing between AWS, Azure, and Google Cloud Platform (GCP). You are tasked with designing the new cloud-native data architecture. The company prefers GCP, but any single-provider architecture is acceptable as long as all services belong to the same cloud provider.

### Business Constraints

1. Enable near real-time inventory tracking with 15-minute latency acceptable.
2. Keep the solution cost-aware and efficient.
3. The team has limited Python experience and is new to the cloud.
4. Dashboards must be mobile-friendly and auto-refreshable.
5. Manual Excel-based reporting should be phased out.

### Standardized Assumptions

- There are 10 warehouses, each uploading CSV files of approximately 5 MB.
- Daily data volume is approximately 500,000 records.
- Uploads occur hourly.
- Total monthly storage needed is about 30 GB.
- The data team has SQL knowledge and limited Python experience.
- Executives access dashboards on mobile devices and require hourly updates.

### Task

#### A. Propose a cloud-based architecture

- Show the end-to-end flow: ingestion -> processing -> storage -> visualization.
- Use only AWS-native, Azure-native, or GCP-native tools.

#### B. Explain your tool choices

- For each tool, explain why it was chosen.
- For each tool, explain the tradeoffs of choosing it.
- Consider cost, ease of use, learning curve, and team experience.

#### C. Draw the proposed data flow architecture

- Show how each service connects and how data flows between them.

#### D. Provide a Bash or similar script

- Show what a script could look like for automating the order requests.

#### E. Bonus

- Show what a script could look like for checking whether files are available and moving files from the third party.

---

## Answer (Cowork with Codex)

**Provider Chosen:** GCP

## A. Proposed Cloud-Based Architecture

### Recommendation

I recommend a **GCP-native micro-batch architecture on GCP**:

`Warehouses upload CSV files -> Cloud Storage -> Cloud Run -> BigQuery -> Looker Studio`

This is the best fit because:

- the company already prefers GCP
- 15-minute latency is acceptable, so full streaming is unnecessary
- the team knows SQL better than Python
- the company wants a low-cost and low-maintenance solution
- dashboards need to replace manual Excel reporting

### End-to-End Flow

1. Each warehouse uploads hourly CSV files to **Google Cloud Storage**.
2. **Cloud Scheduler** runs every 15 minutes.
3. The scheduler triggers **Cloud Run**.
4. Cloud Run checks whether new files exist.
5. If a file is valid, Cloud Run loads it into a **BigQuery raw table**.
6. If a file is invalid, Cloud Run moves it to a **quarantine** path in Cloud Storage.
7. **BigQuery scheduled queries** transform raw data into clean reporting tables.
8. **Looker Studio** reads the curated BigQuery tables and refreshes dashboards hourly.

### Why This Design Fits the Business Constraints

| Business Constraint | How the Design Responds |
| --- | --- |
| 15-minute latency is acceptable | Cloud Scheduler runs every 15 minutes |
| Cost-aware | Uses serverless tools and avoids always-on servers |
| Team is new to cloud and weak in Python | Most logic stays in BigQuery SQL |
| Dashboards must work on mobile | Looker Studio is browser/mobile friendly |
| Excel reporting should be phased out | Curated BigQuery tables feed dashboards directly |

### Why I Did Not Choose a More Complex Design

I did **not** choose Pub/Sub + Dataflow streaming because the assignment does not need that level of complexity:

- files arrive hourly, not continuously every second
- 500,000 records per day is moderate volume
- 15-minute delay is allowed
- the team would support SQL-based processing more easily than code-heavy pipelines

---

## B. Explain Tool Choices

| Stage | GCP Tool | Why It Is Used | Tradeoff |
| --- | --- | --- | --- |
| Ingestion | Cloud Storage | Cheap and simple place to receive CSV files | Only stores files; does not validate or transform data |
| Scheduling | Cloud Scheduler | Easy way to run every 15 minutes | Polling is less real-time than event-driven design |
| Validation / Load | Cloud Run | Serverless processing for file checks and load orchestration | Requires container setup |
| Analytics Storage | BigQuery | SQL-first, low ops, good for reporting | Query cost must be managed carefully |
| Dashboard | Looker Studio | Fast, mobile-friendly, native BigQuery integration | Less advanced than enterprise BI tools |
| Monitoring | Cloud Logging / Monitoring | Tracks failures and missing files | Needs alert rules to be configured well |

---

## C. Data Flow Architecture Diagram

### High-Level Flow

![Data Flow Architecture Diagram](./Cloud_Data_flow.png)

The diagram shows a simple micro-batch pipeline: warehouse and third-party CSV files land in **Cloud Storage**, **Cloud Scheduler** triggers processing every 15 minutes, **Cloud Run** validates and ingests the files, invalid files move to **quarantine**, valid records load into **BigQuery raw tables**, **BigQuery scheduled queries** create curated reporting tables, and **Looker Studio** reads those curated tables for mobile dashboards. Historical files are kept in archive storage, while **Cloud Logging / Monitoring** tracks failures and pipeline health.

In practice, the main data layers are: landing files in Cloud Storage, quarantine/archive paths in Cloud Storage, raw tables in BigQuery, and curated reporting tables in BigQuery.

---

## D. Bash Script for Automating Order Requests

The script is now stored separately here:

- [request_orders.sh](/Users/huangjunyi/Documents/Github/Python_JAVA_Business_Simulation/TCXR_HW/Cloud_Architecture/scripts/request_orders.sh)

This script automates order retrieval from a partner API. It calls the API, downloads the CSV file, verifies that the file is not empty, and uploads it to Cloud Storage. This replaces a manual process where someone downloads a file from a partner system and uploads it by hand.

### Example

```bash
chmod +x TCXR_HW/Cloud_Architecture/scripts/request_orders.sh
TCXR_HW/Cloud_Architecture/scripts/request_orders.sh
```

---

## E. Bonus: Check Whether Files Exist and Move Them from a 3rd Party

The bonus script is stored separately here:

- [check_and_transfer_partner_file.sh](/Users/huangjunyi/Documents/Github/Python_JAVA_Business_Simulation/TCXR_HW/Cloud_Architecture/scripts/check_and_transfer_partner_file.sh)

This script automates file pickup from a third-party SFTP location. It checks for the expected file, downloads it, verifies that it exists and is not empty, and then moves it into Cloud Storage. This is useful when a partner delivers files over SFTP instead of exposing an API.

### Recommended Production Improvements

For production, I would add:

- retry logic
- checksum validation
- duplicate detection
- alerting if a file is late or missing
- secrets management instead of hardcoded credentials

### Example

```bash
chmod +x TCXR_HW/Cloud_Architecture/scripts/check_and_transfer_partner_file.sh
TCXR_HW/Cloud_Architecture/scripts/check_and_transfer_partner_file.sh
```
