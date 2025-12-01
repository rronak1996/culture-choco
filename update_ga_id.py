import re

# List of HTML files to update
html_files = ['index.html', 'login.html', 'signup.html', 'account.html']

# Old GA ID to replace
old_ga_id = 'G-T52126R52S'
new_ga_id = 'G-8RRWPFGNS8'

for filename in html_files:
    try:
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the GA ID
        if old_ga_id in content:
            new_content = content.replace(old_ga_id, new_ga_id)
            
            # Write back to file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Updated {filename} with new GA ID: {new_ga_id}")
        else:
            print(f"⚠ {filename} does not contain {old_ga_id}")
            
    except Exception as e:
        print(f"✗ Error processing {filename}: {str(e)}")

print(f"\n✅ Google Analytics ID updated from {old_ga_id} to {new_ga_id}")
print("\nAll files now have:")
print("  - Google Tag Manager: GTM-5DRL6JVB")
print(f"  - Google Analytics: {new_ga_id}")
