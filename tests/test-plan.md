# Phase 1 Test Plan
**Team:** Power Testers  
**Date:** November 5, 2025

## Team Members and Roles

1. Team Manager: Eyasu Abreha  
   * Coordinates the test plan and schedule  
   * Tracks team progress and metrics  
   * Leads by doing and actively tests with the team

2. Risk Analyst: Wycklife Okello  
   * Identifies and prioritizes potential risks  
   * Designs challenging test cases and edge case coverage

3. Test Executor: Eric Kimuya  
   * Executes test cases and logs results  
   * Reports detailed bug reports and verifies fixes

4. Documentation Owner: Wycklife Okello  
   * Maintains test plans, test case documentation, and logs in markdown

5. Jira Admin: Eric Kimuya  
   * Sets up and manages the Jira board  
   * Creates issues and ensures traceability

6. Communications Coordinator: Eyasu Abreha  
   * Shares updates and maintains meeting notes  
   * Facilitates team communication

## Communication Plan

1. Primary Channels  
   * WhatsApp for quick updates  
   * Jira for task coordination and issue tracking

2. Sync Cadence  
   * Daily short check in for progress updates  
   * Weekly sync meeting for status review and blocker discussion

3. Documentation Sharing  
   * All project files kept under the tests folder in the repository  
   * Version control via GitHub

## Repository and Project Setup

1. Repository runs locally for testing and development  
2. Project board on Jira created and shared with team members  
3. Test plan and other artifacts committed to the repository  
4. Team roles and communication plan documented and distributed

## Phase 2 Test Plan Overview

### 1 Test Scope

1. In Scope  
   * Functional testing of catalog and discovery features  
   * Cart operations and checkout wizard  
   * Payment simulation using Paystack test mode  
   * Orders, returns and refunds workflows  
   * Reviews and community features  
   * Admin console basic operations  
   * Basic accessibility checks and performance spot checks

2. Out of Scope  
   * Live payments with real money  
   * Full load and stress performance testing  
   * Extensive cross browser coverage beyond Chrome for Phase 2  
   * External shipping carrier integrations

### 2 Test Objectives

1. Validate that core user flows work as intended  
2. Detect and log defects early with clear reproducible steps  
3. Verify persistence and state management for cart and checkout wizard  
4. Confirm sanitization for user generated content and reviews  
5. Demonstrate initial automation for key flows using Selenium and Pytest

### 3 Test Approach

1. Manual testing for core flows and edge cases  
2. Exploratory testing to find unexpected behaviors  
3. Positive and negative test cases for form validations and business rules  
4. Early automation for smoke tests and repeatable flows  
5. Traceability via RTM linking FR codes to test cases and defects

## Risk Analysis

### High Level Risks and Mitigations

1. R1 Payment failures or currency mismatch  
   * Likelihood: Medium  
   * Impact: High  
   * Mitigation: Validate currency preflight, test Paystack flows in test mode, log gateway errors

2. R2 Stock calculation and quantity enforcement errors  
   * Likelihood: High  
   * Impact: High  
   * Mitigation: Create tests that attempt quantity edge cases, enforce stock checks in UI and API

3. R3 Search and filter inaccuracies including diacritic issues  
   * Likelihood: Medium  
   * Impact: Medium  
   * Mitigation: Test exact, partial and misspelled queries, cover filter combinations

4. R4 Unauthorized admin access risk  
   * Likelihood: Low  
   * Impact: High  
   * Mitigation: Verify admin guard behavior using localStorage user role checks

5. R5 Data loss after refresh for cart and checkout wizard  
   * Likelihood: Medium  
   * Impact: High  
   * Mitigation: Verify localStorage persistence and recovery flows

6. R6 XSS risk in reviews and Q and A input  
   * Likelihood: Medium  
   * Impact: High  
   * Mitigation: Test sanitization of user content and block unsafe URL schemes

7. R7 CSV export formatting issues for orders  
   * Likelihood: Medium  
   * Impact: Medium  
   * Mitigation: Validate CSV in Excel and Google Sheets, check decimal and encoding

8. R8 Intentional defects being missed during tests  
   * Likelihood: Low  
   * Impact: Medium  
   * Mitigation: Include known planted defects as explicit test cases and log expected failures

9. R9 Notifications badge not updating after mark all read  
   * Likelihood: High  
   * Impact: Low  
   * Mitigation: Document the behavior as known issue and include in defect log

10. R10 Coupon bypass and validation issues  
    * Likelihood: Medium  
    * Impact: Medium  
    * Mitigation: Execute positive and negative coupon scenarios and combinability checks

## Entry and Exit Criteria

1. Entry Criteria  
   * Repository cloned and app runs locally with npm start  
   * Jira board available and team members added  
   * Test data and environment prepared

2. Exit Criteria for Phase 2  
   * Minimum test cases drafted as required by the brief and executed where applicable  
   * Initial automation scripts committed to the repository  
   * Defects logged in tests defect log with evidence links  
   * RTM updated to map executed test cases to requirements

## Test Environment

1. Operating System  
   * Ubuntu Linux or Windows as available for testers

2. Browser  
   * Chrome latest version for Phase 2

3. Tools  
   * Jira for issue tracking  
   * GitHub for version control  
   * Selenium and Pytest for automation samples  
   * axe DevTools for a11y checks and Lighthouse for performance spot checks

4. Test Data Examples  
   * Sample book seed data from src data or mock seed file  
   * Test coupon codes such as SAVE10 and EXPIRED10 for negative testing  
   * Sample shipping addresses to validate checkout form

## Deliverables

1. Test Plan document committed to tests folder  
2. Test Cases file with required minimum and expanded cases committed to tests folder  
3. Defect Log with reproducible steps and attachments committed to tests folder  
4. Requirements Traceability Matrix committed to tests folder  
5. Early automation scripts using Selenium and Pytest committed to tests automation folder  
6. Evidence screenshots for core flows and defect reproduction

## Approval

1. Team Manager Approver  
   * Eyasu Abreha

2. QA Team Acknowledgement  
   * Power Testers team members have reviewed and agreed on the plan

