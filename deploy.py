#!/usr/bin/env python3
"""
Deployment Script for Anurag Mishra's Portfolio Website
This script helps with deployment tasks and site optimization
"""

import os
import subprocess
import json
from datetime import datetime

def check_files():
    """
    Check if all required files are present for deployment
    """
    required_files = [
        'index.html',
        'styles.css',
        'script.js',
        'README.md'
    ]
    
    print("🔍 Checking required files...")
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            file_size = os.path.getsize(file)
            print(f"✅ {file} - {file_size} bytes")
        else:
            missing_files.append(file)
            print(f"❌ {file} - Missing")
    
    if missing_files:
        print(f"\n⚠️  Missing files: {', '.join(missing_files)}")
        return False
    
    print("\n✅ All required files are present!")
    return True

def generate_resume():
    """
    Generate the resume PDF if the script exists
    """
    if os.path.exists('generate_resume.py'):
        print("\n📄 Generating resume PDF...")
        try:
            # Try to run the resume generation script
            result = subprocess.run(['python', 'generate_resume.py'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Resume generated successfully!")
                return True
            else:
                print(f"❌ Resume generation failed: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Error running resume generator: {str(e)}")
            return False
    else:
        print("\n⚠️  Resume generator not found. Skipping PDF generation.")
        return True

def validate_html():
    """
    Basic HTML validation checks
    """
    print("\n🔍 Validating HTML structure...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Basic checks
        checks = [
            ('DOCTYPE declaration', '<!DOCTYPE html>' in html_content),
            ('HTML lang attribute', 'lang="en"' in html_content),
            ('Meta charset', 'charset="UTF-8"' in html_content),
            ('Meta viewport', 'viewport' in html_content),
            ('Title tag', '<title>' in html_content),
            ('CSS link', 'styles.css' in html_content),
            ('JavaScript link', 'script.js' in html_content),
        ]
        
        all_passed = True
        for check_name, passed in checks:
            if passed:
                print(f"✅ {check_name}")
            else:
                print(f"❌ {check_name}")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"❌ Error validating HTML: {str(e)}")
        return False

def check_links():
    """
    Check for placeholder links that need to be updated
    """
    print("\n🔗 Checking for placeholder links...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Look for placeholder links
        placeholder_patterns = [
            'href="#"',
            'https://linkedin.com/in/anurag-mishra',
            'https://github.com/anuragmishra',
            'anurag.mishra@email.com',
            '+91 98765 43210'
        ]
        
        placeholders_found = []
        for pattern in placeholder_patterns:
            if pattern in html_content:
                placeholders_found.append(pattern)
        
        if placeholders_found:
            print("⚠️  Placeholder links found (update these with real information):")
            for placeholder in placeholders_found:
                print(f"   • {placeholder}")
            return False
        else:
            print("✅ No placeholder links found!")
            return True
            
    except Exception as e:
        print(f"❌ Error checking links: {str(e)}")
        return False

def optimize_images():
    """
    Check for image optimization opportunities
    """
    print("\n🖼️  Checking image optimization...")
    
    # Look for image references in HTML
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Count placeholder images
        placeholder_count = html_content.count('via.placeholder.com')
        
        if placeholder_count > 0:
            print(f"⚠️  Found {placeholder_count} placeholder images")
            print("   Consider replacing with actual optimized images")
            return False
        else:
            print("✅ No placeholder images found!")
            return True
            
    except Exception as e:
        print(f"❌ Error checking images: {str(e)}")
        return False

def create_deployment_info():
    """
    Create a deployment information file
    """
    deployment_info = {
        "deployment_date": datetime.now().isoformat(),
        "version": "1.0.0",
        "status": "ready",
        "files": {
            "html": os.path.exists('index.html'),
            "css": os.path.exists('styles.css'),
            "js": os.path.exists('script.js'),
            "readme": os.path.exists('README.md'),
            "resume": os.path.exists('resume.pdf')
        },
        "notes": [
            "Portfolio website for Anurag Mishra",
            "Data Science graduate from VIT",
            "Optimized for global recruitment"
        ]
    }
    
    try:
        with open('deployment-info.json', 'w') as f:
            json.dump(deployment_info, f, indent=2)
        print("\n📋 Deployment info created: deployment-info.json")
        return True
    except Exception as e:
        print(f"❌ Error creating deployment info: {str(e)}")
        return False

def print_deployment_instructions():
    """
    Print deployment instructions for different platforms
    """
    print("\n🚀 DEPLOYMENT INSTRUCTIONS")
    print("=" * 50)
    
    print("\n📌 GitHub Pages:")
    print("1. Push all files to your GitHub repository")
    print("2. Go to Settings > Pages in your repository")
    print("3. Select source branch (main/master)")
    print("4. Your site will be live at: https://yourusername.github.io/repository-name")
    
    print("\n📌 Netlify:")
    print("1. Drag and drop the project folder to netlify.com/drop")
    print("2. Or connect your GitHub repository for continuous deployment")
    print("3. Custom domain can be configured in site settings")
    
    print("\n📌 Vercel:")
    print("1. Install Vercel CLI: npm i -g vercel")
    print("2. Run 'vercel' in the project directory")
    print("3. Follow the prompts for deployment")
    
    print("\n📌 Traditional Hosting:")
    print("1. Upload all files to your web hosting via FTP")
    print("2. Ensure index.html is in the root directory")
    print("3. Test all links and functionality")

def main():
    """
    Main deployment preparation function
    """
    print("🚀 PORTFOLIO DEPLOYMENT PREPARATION")
    print("=" * 50)
    print("Preparing Anurag Mishra's Data Science Portfolio for deployment...")
    
    # Run all checks
    checks_passed = 0
    total_checks = 6
    
    if check_files():
        checks_passed += 1
    
    if generate_resume():
        checks_passed += 1
    
    if validate_html():
        checks_passed += 1
    
    if check_links():
        checks_passed += 1
    else:
        print("   ℹ️  Update placeholder links with real contact information")
    
    if optimize_images():
        checks_passed += 1
    else:
        print("   ℹ️  Consider adding real profile and project images")
    
    if create_deployment_info():
        checks_passed += 1
    
    # Summary
    print(f"\n📊 DEPLOYMENT READINESS: {checks_passed}/{total_checks} checks passed")
    
    if checks_passed == total_checks:
        print("🎉 Portfolio is ready for deployment!")
    elif checks_passed >= 4:
        print("⚠️  Portfolio is mostly ready. Address the warnings above.")
    else:
        print("❌ Portfolio needs more work before deployment.")
    
    # Always show deployment instructions
    print_deployment_instructions()
    
    print(f"\n✨ Portfolio prepared on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
    print("💼 Ready to showcase Anurag's data science skills to global recruiters!")

if __name__ == "__main__":
    main()