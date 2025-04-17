#!/usr/bin/env python3
import re
import os
import shutil
import glob

def process_markdown_file(md_path):
    """
    Process a single markdown file:
    1. Extract image references
    2. Move images to essay-specific folder
    3. Update image references in the markdown
    """
    # Read the markdown file
    with open(md_path, 'r') as f:
        content = f.read()
    
    # Get the base directory name
    base_name = os.path.splitext(os.path.basename(md_path))[0]
    new_dir = os.path.join('essays', base_name)
    
    # Ensure target directory exists
    os.makedirs(new_dir, exist_ok=True)
    
    # Keep track of moved images for reporting
    moved_images = []
    
    # Find all image references using both patterns
    # Pattern 1: {% include figure.html src="images/filename.png" %}
    figure_matches = re.finditer(r'{%\s*include\s+figure\.html[^}]*src=["\'](images/[^"\']+)["\'][^}]*%}', content)
    
    # Process figure.html matches
    for match in figure_matches:
        old_path = match.group(1)  # images/filename.png
        filename = os.path.basename(old_path)
        old_full_path = os.path.join('essays', old_path)
        new_full_path = os.path.join(new_dir, filename)
        
        # Move the file if it exists
        if os.path.exists(old_full_path):
            print(f"Moving {old_full_path} to {new_full_path}")
            shutil.copy2(old_full_path, new_full_path)
            moved_images.append(filename)
        else:
            print(f"Warning: Image not found: {old_full_path}")
        
        # Update the reference in the content
        new_ref = f'{base_name}/{filename}'
        content = content.replace(old_path, new_ref)
    
    # Pattern 2: <img src="{{ site.baseurl }}/essays/images/filename.jpg"/>
    img_matches = re.finditer(r'<img\s+src="\{\{\s*site\.baseurl\s*\}\}/essays/images/([^"]+)"', content)
    
    # Process img matches
    for match in img_matches:
        filename = match.group(1)
        old_full_path = os.path.join('essays', 'images', filename)
        new_full_path = os.path.join(new_dir, filename)
        
        # Move the file if it exists
        if os.path.exists(old_full_path):
            print(f"Moving {old_full_path} to {new_full_path}")
            shutil.copy2(old_full_path, new_full_path)
            moved_images.append(filename)
        else:
            print(f"Warning: Image not found: {old_full_path}")
        
        # Update the reference in the content
        old_ref = f'essays/images/{filename}'
        new_ref = f'essays/{base_name}/{filename}'
        content = content.replace(old_ref, new_ref)
    
    # Write the updated content back to the file
    with open(md_path, 'w') as f:
        f.write(content)
    
    # Return summary of what was moved
    return moved_images

def process_all_markdown_files():
    """Process all markdown files in the essays directory."""
    md_files = glob.glob('essays/*.md')
    print(f"Found {len(md_files)} markdown files to process")
    
    all_moved_images = {}
    
    for md_file in md_files:
        print(f"\nProcessing {md_file}...")
        moved = process_markdown_file(md_file)
        all_moved_images[md_file] = moved
        print(f"Moved {len(moved)} images for {md_file}")
    
    # After copying is complete, now we can remove the original images
    for md_file, images in all_moved_images.items():
        base_name = os.path.splitext(os.path.basename(md_file))[0]
        for img in images:
            original = os.path.join('essays', 'images', img)
            if os.path.exists(original):
                os.remove(original)
                print(f"Removed original image: {original}")
    
    return all_moved_images

if __name__ == "__main__":
    print("Starting to process markdown files and move images...")
    results = process_all_markdown_files()
    
    # Print summary
    total_images = sum(len(imgs) for imgs in results.values())
    print(f"\nSummary: Moved {total_images} images across {len(results)} markdown files")
    print("Done!")

