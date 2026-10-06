# sdd-kit — the SDD method's skills for the service design course

This plugin is the toolset of the method that the service design course, *Designing Digital
Government Services using a Building Block Approach*, teaches: specification-driven development (SDD). In it, a service is
written down as twelve documents, each accepted before the next is begun, and the last of them is
turned into the running service by a program. The course's subtopic 6.4 says that for each document a
person writes there is an assisting tool that walks that person through the document's standard,
part by part. These are those tools.

The plugin is for the team that writes the documents: the staff of the public body, its supplier,
or an AI assistant working for either. A manager who only accepts the documents does not need it;
the course pages and their prompts serve the manager.

## What is inside

| Folder | What it holds |
|---|---|
| `skills/` | Twelve skills. Eleven help a person write one document of the method, each under its own standard; `sdd-specify` drives the whole specification and says which skill comes next. `ux-enterprise-ruleset` applies the standard for what a person sees to every screen. |
| `standards/` | The thirteen standards the skills read, as Markdown text: SDD-01 to SDD-11, UX-01 and UX-02, with their figures in `standards/figures/`. Also the one ruling the skills read (`standards/rulings/`) and the one working paper the kit's register check reads (`standards/_working/`). |
| `kit/` | The programs the skills run, reached as `python3 tools/kit.py <verb>` in `kit/`: the register of the twelve documents (`templates/spec/slots.yaml`), the templates and checklists each standard produces, the schema of the application model, and the screen patterns (`patterns/ux/`). `kit/README.md` lists the verbs this copy carries. |
| `references/SKILL-form.md` | The one form every skill of the method is written from. |
| `scripts/sync-skills.sh` | Copies `kit/` and the text of `standards/` into every skill's folder. |

Every path a skill names is in the skill's own folder: its `standards/` and `kit/` are copies of the
plugin's `standards/` (the text, without the figures) and `kit/`, made by `scripts/sync-skills.sh`.
So one skill works when it is installed on its own. Edit the plugin's own `standards/` and `kit/`,
never a skill's copy, then run the script; `sync-skills.sh --check` fails on any copy that differs.
Nothing in the plugin names a path on the author's machine, so the folder works wherever it is
placed.

## Which module of the course each skill serves

| Skill | Standard | The document it helps write | Course |
|---|---|---|---|
| `sdd-specify` | SDD-01 | The specification as a whole: the tree of twelve documents, the order, the handovers, the claim of conformance, and what a change made stale | Module 1 (1.4, 1.5); module 6 (6.2, 6.3, 6.4) |
| `sector-services-catalogue` | SDD-10 | The catalogue of the services of a sector | 2.1 |
| `requirements-catalogue` | SDD-02 | The register of what the client asked for | 2.2 |
| `entity-model` | SDD-03 | The records the service keeps, with the glossary and the business rules | 2.3 |
| `use-case-model` | SDD-05 | Every goal, named and tied to what was asked | 2.4 |
| `shared-registers` | SDD-04 | Who writes each fact, the states a record moves through, and the shared lists, events and settings every goal may use | 2.3, 2.5 |
| `architecture-document` | SDD-08 | What the service is built on, and what crosses its boundary | 2.6 |
| `use-case-description` | SDD-06 | One goal written out in full, with every way it can go wrong | 3.1, 3.2 |
| `use-case-screens` | SDD-07 | The screens of one goal, every value with its source, and the walk-through officials click | 3.3, 3.5, 3.6 |
| `ux-enterprise-ruleset` | UX-01, UX-02 | Screens officers can use: the rules every screen is generated and reviewed under | 3.4 |
| `interaction-design` | SDD-11 | The four questions decided once for every screen: pick, find, move, act | 4.1, 4.2, 4.3 |
| `application-model` | SDD-09 | The one file a program reads, and the review of what it assumed and could not express | 4.4, 4.5, 4.6 |

Module 5, generating the service on a low-code platform, is the kit's work and no skill's: the
verbs `kit validate`, `kit gen` and `kit deploy` in `kit/`, which need a Joget DX installation to
deploy to (`kit/GETTING-STARTED.md`, `kit/DEPLOY.md`).

## Before you start

- **An assistant that runs skills and programs.** Claude Code, or the Claude app with code
  execution turned on. The skills run Python programs; a chat without code execution can read the
  skills and the standards but cannot run the checks.
- **Python 3.10 or later**, with `pyyaml` and `jsonschema` (`pip install pyyaml jsonschema`).
- **pandoc**, to build the Word edition a reviewer reads. `use-case-model` builds its edition
  with `python-docx`, LibreOffice and `pdftoppm` (poppler) instead.
- **A Joget DX installation** only for `kit gen` and `kit deploy`.

## How to install it

**Claude Code, for one session.** Point Claude Code at this folder:

    claude --plugin-dir /path/to/sdd-kit

**Claude Code, to keep it.** Add the kit's marketplace once, then install the plugin from it:

    /plugin marketplace add alaponin/ea-plays-kit
    /plugin install sdd-kit@ea-plays-kit

**Any agent, one skill at a time.** The skills are also published through the ITU Skills
Marketplace, and the skills CLI installs one of them into Claude Code, Codex and other agents:

    npx skills add alaponin/ea-plays-kit --skill entity-model

**The Claude app.** Upload the whole folder as one plugin, where your plan allows plugins, or one
skill's folder on its own: each skill carries its own copy of the standards' text and of the kit.

**Check that it works.** In `kit/`, at the plugin's root or in any skill's folder:

    python3 tools/kit.py skills --check
    python3 tools/kit.py slot --check

The first prints each skill it finds as `current` (twelve at the plugin's root, one in a skill's
folder); the second prints `nothing to report`.

## Alone, or beside ea-plays

sdd-kit works alone. It also works beside `ea-plays`, the learner kit of the series: the two share
no skill name and neither calls the other. ea-plays carries the helpers for the AI usage tips of
the courses, written for the manager; sdd-kit carries the method's skills, written for the team
that writes the documents.

## How this copy was made

On 6 October 2026, from the method's own sources, for the learners of the service design course:

- **The skills** are the method's twelve skills, with every path made relative to the skill's own
  folder, which carries its copy of the kit and of the standards' text.
- **The standards** are the editions of record of the method's standards, carried as Markdown.
  Ten were taken from their own text sources and one, SDD-01, converted from its Word edition with
  pandoc; UX-01 and UX-02 were already Markdown. Each states the same edition, sections and rules as
  its Word edition. Because the kit compares each skill's pin with the document in the standards
  root by checksum, the pins, the checklists' heads and the register name the Markdown files and
  their checksums; each checklist records the Word edition it came from under `converted_from`.
- **The examples.** Where a standard drew an example from the method's author's own client work, this
  copy carries an example set in Progressa in its place, and says so where it does. No other text
  of the standards was changed beyond the paths and the names this copy needs.
- **The kit** is the part of the method's delivery kit the skills run, with the programs it
  imports and the files they read.

The editions keep the standing their first pages state: SDD-02, SDD-10 and SDD-11 are drafts.
The skills are published under CC BY 4.0 (`LICENSE-CONTENT`) and the programs under MIT
(`LICENSE-CODE`), with FiscalAdmin OÜ as their provider, as the rest of this repository is.
