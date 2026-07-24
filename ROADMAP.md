# Roadmap

This roadmap records approved product outcomes and implementation milestones. Approved technical direction is documented in `docs/PRODUCT.md`; detailed architecture still requires explicit approval.

## Phase 0 - Repository and Product Foundation

Status: Complete

- [x] Create the local Git repository.
- [x] Create and connect the public GitHub repository.
- [x] Add reusable AI collaboration documentation.
- [x] Define the initial product baseline.
- [x] Review and commit the initial documentation.
- [x] Document the proven GitHub CLI project-creation workflow in the Developer Playbook.

## Phase 1 - Application Bootstrap

Status: Complete

- [x] Approve Python, Django 5.2 LTS, SQLite, Django templates, HTML, CSS, and limited JavaScript.
- [x] Create and activate the local virtual environment.
- [x] Record Django 5.2.16 in `requirements.txt`.
- [x] Generate the Django project configuration.
- [x] Create the local SQLite database and apply built-in migrations.
- [x] Establish the initial run and verification commands.
- [x] Run the development server and verify the default Django page in a browser.
- [x] Create the `dashboard` app as the first vertical slice.
- [x] Replace the default page with a custom Recipe Dashboard page.
- [x] Add and run the first focused Django test.

## Phase 2 - First Usable Workflow

Status: Planned

Deliver the approved end-to-end Version 1 workflow documented in `docs/PRODUCT.md`, from an explainable complete-meal suggestion through ingredient review, cooking-session completion, and cooking history.

Build this phase as small vertical slices. Resolve remaining product and architectural decisions before implementing the behavior they affect.

## Phase 3 - Pantry Tracking

Status: Approved for later

Add basic pantry tracking after the first usable recipe-discovery version.

Detailed requirements have not been defined.

## Phase 4 - Food-Waste Guidance

Status: Approved for later

After pantry tracking exists, help the operator identify ingredients that should be used soon.

Detailed requirements have not been defined.

## Parking Lot

Parking-lot ideas and their non-commitment boundary are maintained in `docs/PRODUCT.md`.
