# REQUIREMENTS.md

## 1. Overview

**Project:** *idea‑flow*  
**Goal:** Deliver a lightweight, offline‑first application that lets users create boards, add ideas, and sync changes with a remote server when connectivity is restored. The solution must be reliable, secure, and performant while remaining easy to maintain and extend.

---

## 2. Functional Requirements

| ID | Description | Acceptance Criteria |
|----|-------------|---------------------|
| **FR‑1** | **Create a Board** | User can create a new board with a unique title. The board appears immediately in the UI and is stored locally. |
| **FR‑2** | **Delete a Board** | User can delete a board. Deletion is marked locally and removed from the server during the next sync. |
| **FR‑3** | **Add an Idea** | User can add an idea to a board. The idea contains a title, optional description, and timestamp. It is stored locally and queued for sync. |
| **FR‑4** | **Edit an Idea** | User can edit an existing idea’s title or description. Changes are stored locally and queued for sync. |
| **FR‑5** | **Delete an Idea** | User can delete an idea. Deletion is stored locally and propagated to the server on sync. |
| **FR‑6** | **View Boards & Ideas** | User can list all boards and view the ideas within each board. Data is loaded from local storage first. |
| **FR‑7** | **Offline Status Indicator** | UI shows a clear indicator when the device is offline. |
| **FR‑8** | **Sync Progress Indicator** | UI shows a progress bar or spinner during sync, including number of items queued and synced. |
| **FR‑9** | **Automatic Sync** | When connectivity is restored, the app automatically initiates a sync of all pending changes. |
| **FR‑10** | **Conflict Resolution** | In case of conflicting changes (e.g., same idea edited on two devices), the system uses *last‑write‑wins* based on server timestamps. |
| **FR‑11** | **Data Persistence** | All boards and ideas are persisted locally in a SQLite database. |
| **FR‑12** | **API Integration** | The app communicates with a RESTful API (`/boards`, `/ideas`) using JSON over HTTPS. |
| **FR‑13** | **Authentication** | Users authenticate via OAuth2 token (passed in `Authorization: Bearer <token>` header). Token is stored securely in the OS keychain. |
| **FR‑14** | **Unit & Integration Tests** | All functional requirements are covered by automated tests (pytest). |

---

## 3. Non‑Functional Requirements

| ID | Category | Requirement | Acceptance Criteria |
|----|----------|-------------|---------------------|
| **NF‑1** | **Performance** | Sync latency < 5 s for up to 10 k ideas. | Benchmark shows average sync time ≤ 5 s under simulated 3 Mbps network. |
| **NF‑2** | **Responsiveness** | UI interactions (create, edit, delete) < 100 ms on a mid‑range laptop. | End‑to‑end latency measured with Chrome DevTools ≤ 100 ms. |
| **NF‑3** | **Scalability** | Handle up to 10 k ideas per board without degradation. | Stress test with 10 k ideas passes without crashes. |
| **NF‑4** | **Security** | • Data at rest encrypted with AES‑256. <br>• All network traffic over TLS 1.2+. <br>• OAuth2 tokens stored in OS keychain. | Security audit confirms encryption and TLS usage. |
| **NF‑5** | **Reliability** | • Crash‑free recovery: app restores to last consistent state. <br>• No data loss on
