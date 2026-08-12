# Software Design Document
## 1. Project Overview
## 2. Problem Statement
## 3. Project Goals
## 4. Stakeholders
## 5. User Workflow 
### Main Workflow (Successful CSV Mapping)

1. **Upload source and destination CSV files**
- The user uploads the two CSV files they want to compare and map.
2. **Validate uploaded files**
- The system checks that:
 - Files are in a supported format
 - Files are not empty
 - Files can be read successfully
 - Required structure is present
3. **Extract column headers**
- The system reads both files and identifies their column names.
4. **Display column headers for comparison**
- The system dysplays the source and destination columns side by side so the user can compare their structures.
5. **Automatically match identical column names**
- The system identifies columns with exact matching names and suggests these as mappings.
6. **Manually map remaining unmatched columns**
- The user reviews unmatched columns and manually selects the corresponding destination column for each.
7. **Review mappings**
- The user reviews all automatic and manual mappings before saving.
8. **Save and export mapping configuration**
- The system saves the completed mapping configuration for future use, before being exported.

### Alternative Workflow (Invalid File Upload)

1. **Upload source and destination CSV files**
2. **Validate uploaded files**
- The system checks that the uploaded files are valid and can be processed.
3. **Validation fails**
- The system detects one or more validation errors:
 - Unsupported file type
 - Empty file
 - Corrupted file
 - Missing column headers
4. **Display an error message**
- The system explains why the file cannot be processed.
5. **Allow the user to upload another file**
- The user selects a replacement file.
6. **Repeat Validation**
- The system validates the newly uploaded file before continuing with the main worklow.
## 6. Functional Requirements
The following describes the functionality planned for Version 1 of Smart Financial Mapper.

**FR01 File Upload**
The system shall allow users to upload a source CSV file and a destination CSV file.
**FR02 File Validation**
The system shall validate uploaded files before processing.
**FR03 Invalid File Rejection**
The system shall reject unsupported, corrupted, unreadable, or empty files.
**FR04 Validation Error Message**
The system shall display an error message explaining why an uploaded file was rejected.
**FR05 File Replacement**
The system shall allow users to replace a rejected file and attempt to re-upload.
**FR06 Column Header Extraction**
The system shall identify and extract column headers from both CSV files.
**FR07 Column Header Display**
The system shall display the extracted source and destination column headers for comparison.
**FR08 Extract Header Comparison**
The system shall compare source and destination column headers to identify exact matches.
**FR09 Automatic Mapping**
The system shall automatically create mappings between columns with identical header.
**FR10 Complete Automatic Mapping**
The system shall inform the user when no unmatched columns remain and allow them to proceed directly to the review stage.
**FR11 Manual Mapping**
The system shall allow users to manually map remaining unmatched source and destination columns.
**FR12 Duplicate Destination Prevention**
The system shall prevent multiple source columns from being mapped to the same destination column.
**FR13 Invalid Mapping Feedback**
The system shall display an error message when a user attempts to map a destination column that has already been mapped.
**FR14 Mapping Review**
The system shall allow users to review all mappings before saving or exporting them.
**FR15 Mapping Modification**
The system shall allow users to modify or remove automatically generated mappings during the review stage.
**FR16 Mapping Method Identification**
The system shall indicate whether each mapping was created automatically or manually.
**FR17 Save Mapping Configuration**
The system shall allow users to save a mapping configuration within the application for later use.
**FR18 Export Mapping Configuration**
The system shall allow users to export a completed mapping configuration to their computer.
## 7. Non-Functional Requirements
## 8. System Architecture
## 9. Data Flow
## 10. Risks
## 11. Future Features