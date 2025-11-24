prototype_pages = {
    'P1': {'name': 'Home Page', 'flow': ['P2 (View Lists)', 'P3 (Create List)', 'P6 (Settings)']},
    'P2': {'name': 'Lists Directory', 'flow': ['P4 (Select List)', 'P1 (Go Back)']},
    'P3': {'name': 'New List Setup', 'flow': ['P4 (Save List)', 'P1 (Cancel)']},
    'P4': {'name': 'List Detail View', 'flow': ['P5 (Edit List)', 'P2 (Go Back)']},
    'P5': {'name': 'List Detail Edit', 'flow': ['P4 (Save)', 'P4 (Cancel)']},
    'P6': {'name': 'Settings', 'flow': ['P1 (Go Back)']}
}

total_pages = len(prototype_pages)
print("--- Mobile App Prototype Documentation ---")
print(f"Total number of prototype pages: {total_pages}\n")

print("--- Page Names and Sequence/Flow ---")

print("\n[Page Names]")
for page_key, data in prototype_pages.items():
    print(f"  - {page_key}: {data['name']}")

print("\n[Page Flow Sequence]")
for page_key, data in prototype_pages.items():
    flow_targets = " -> ".join(data['flow'])
    print(f"{page_key} ({data['name']}) -> Primary Transitions: {flow_targets}")

print("\n----------------------------------------")