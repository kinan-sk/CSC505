def print_model_documentation():
    "Prints the documentation for the Web-based PHTRS Use Case Diagram."

    # Brief Diagram Description
    print("UML Use Case Diagram Description: Web-based Pothole Tracking and Repair System (PHTRS)")

    description = (
        "This Use Case Diagram models the functional requirements of the Web-based PHTRS. "
        "It defines four key actors and twelve use cases, illustrating the scope of the web-based system. "
        "Key relationships include 'Assign Repair Priority' including 'Log/Review Pothole Report' "
        "and 'Create Work Order' including 'Assign Repair Priority,' indicating mandatory steps in the workflow. "
        "The diagram shows 'Update Repair Status' optionally extending to 'Record Repair Costs/Materials.'"
    )
    print("\nDiagram Description:\n")
    print(description)


    # Actors
    print("\nActors:\n")

    actors = [
        "Citizen: Initiates reporting of potholes and damage claims.",
        "Public Works Staff: Manages reports, assigns priority, and processes claims.",
        "Repair Crew: Executes and records details of the repair work.",
        "System Administrator: Manages user accounts and system configuration."
    ]
    for actor in actors:
        print(f"{actor}")



    # Use Cases
    print("\nUse Cases:")
    use_cases = {
        "Citizen Interactions": [
            "Report Pothole",
            "Report Damage Claim",
            "View Pothole Status"
        ],
        "Public Works Staff Management": [
            "Log/Review Pothole Report",
            "Assign Repair Priority",
            "Create Work Order",
            "Process Damage Claim",
            "Query Report Data"
        ],
        "Repair Crew Workflow": [
            "View Assigned Work Order",
            "Update Repair Status",
            "Record Repair Costs/Materials"
        ],
        "System Administrator Maintenance": [
            "User Management",
            "General System Configuration"
        ]
    }

    for category, cases in use_cases.items():
        print(f"\n{category}:")
        for case in cases:
            print(f"- {case}")


# Execute the function to print the documentation
if __name__ == "__main__":
    print_model_documentation()