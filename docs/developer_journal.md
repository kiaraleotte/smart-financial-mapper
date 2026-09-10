# Developer Journal

## 5th July 2026 - Initial Design and Documentation

### Progress

- Began developing the Software Design Document (SDD).
- Started defining the purpose and scope of Smart Financial Mapper.
- Considered the core functionality required for Version 1.

### Decisions

- Version 1 will focus on CSV files.
- More advanced matching and additional formats will be considered for future versions.

### Notes 

This stage focused primarily on understanding the problem and planning the system before beginning the implementation.

---

## July - September 2026 - SDD Development

### Progress

- Defined the main and alternative user workflows.
- Created functional and non-functional requirements.
- Designed the high-level system architecture.
- Designed the data flow between components.
- Identified project and system risks.
- Defined potential future features.
- Completed the introductory sections of the SDD.

### Decisions

- Version 1 will use exact-name matching alongside manual mapping.
- Version 1 will produce mapping configurations rather than transform the underlying CSV data.
- Mapping reveiw logic will be separated from the User Interface to improve testability and extensibility.
- Future functionality such as intelligent matching, additional file formats, data transformation, and integrations will remain outside Version 1.

### Challenges/Learning

- Distinguishing between functional and non-functional requirements.
- Understanding the differences between system architecture, workflow, and data flow.
- Keeping Version 1 limited while designing the system so that it can be extended later and not getting carried away!
- Learning how to divide documentation changes into meaningful Git commits.

---

## 10th September 2026 - SDD Review

### Progress

- Reviewed the completed SDD
- Corrected spelling and grammar.

## Identified for Future Revision

- Move NFR02 to Appendix/Design Notes - needs testing later.
- Add impact and likelyhood ratings to Risks section.
- Review Mermaid diagram formatting.
- Refine the Mapping Reviewer data flow.

### Next Steps 

- Complete the remaining SDD refinements.
- Finish README.
- Finish project Roadmap.
- Begin Version 1 implementation.
