# smart-financial-mapper
## Overview
Smart Financial Mapper is a tool designed to make mapping columns between different accounting systems easier during financial data migrations.

Companies often use different accounting systems, and when data is migrated into a new system, the columns must first be matched correctly. Company mergers are just one example; upgrading, replacing, consolidating, and moving to cloud systems all require data mapping. The problem is that different systems may use different column headers (e.g. Acc_Num vs Account_Number), meaning someone has to tell the software which columns correspond to each other. The long term aim of this project is to reduce the time spent manually mapping columns, minimise human error, and eventually automate much of the mapping process.

This project is inspired by a real-world problem experienced by an accountant during company acquisitions, where significant time was spent manually mapping financial data between different systems alongside normal day-to-day responsibilities.

Version 1 will focus on understanding CSV file structures and assisting users with the mapping process. Future versions aim to introduce increasingly intelligent mapping suggestions to further reduce manual effort while allowing users to remain in control of the final mappings.

## Current Status

This project is currently in the planning and design phase. No implementation has started yet.

- Repository Structure Established.
- README in progress.
- Software Design Document in progress.

## Planned Features

- Upload source and destination CSV files.
- Validate uploaded files.
- Extract and display column headers.
- Automatically map columns with identical names.
- Manually map remaining unmatched columns.
- Review and edit mappings before saving or exporting.
- Save and export mapping configurations.

## Technologies

- **Python** - Core programming language.
- **FastAPI** - backend API.
- **Pandas** - CSV processing and data handling.
- **Pydantic** - Data validation and structured data models.
- **React** - Frontend user interface.
- **PostgreSQL** - Storage for mapping configurations.
- **Pytest** - Automated testing.

## Installation

Installation instructions will be added once Version 1 implementation begins.

## Usage

Once implemented, the application will allow users to: 

1. Upload a source CSV file and a destination CSV file.
2. Validate the uploaded files.
3. View the column headers from both files.
4. Review automatically created mappings for identical headers.
5. Manually map any remaining unmatched columns.
6. Review and edit the completed mappings.
7. Save or export the mapping configuration.

## Project Structure

```text
smart-financial-mapper/
├── doc/
|   ├── software_design_document.md
|   ├── developer_journal.md
|   ├── research.md
|   └── roadmap.md
├── src/
|   └── main.py
└── README.md
```

## Roadmap

1. Complete project documentation.
2. Implement core Version 1 functionality (file handling, exact matching, manual mapping, review, save/export).
3. Testing and refinement.
4. Begin working on intelligent matching and support for additional file formats.

## License