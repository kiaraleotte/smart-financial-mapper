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
## 7. Non-Functional Requirements
## 8. System Architecture
## 9. Data Flow
## 10. Risks
## 11. Future Features