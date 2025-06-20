#!/usr/bin/env python3
"""
Resume Generator Script for Anurag Mishra
This script generates a professional PDF resume using Python libraries.
Updated with actual professional details and experience.
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.platypus import PageBreak, KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from datetime import datetime
import os

def create_resume():
    """
    Create a professional PDF resume for Anurag Mishra
    This function generates a comprehensive resume with all sections using actual professional details
    """
    
    # Define file path for the resume PDF output
    filename = "resume.pdf"
    
    # Create document with letter size and standard margins for professional appearance
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Define custom styles for different sections to ensure consistent formatting
    styles = getSampleStyleSheet()
    
    # Custom style for name/header - large, bold, centered with brand color
    name_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=HexColor('#4f46e5'),
        fontName='Helvetica-Bold'
    )
    
    # Custom style for section headers - consistent branding with borders
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        spaceBefore=20,
        textColor=HexColor('#4f46e5'),
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=HexColor('#4f46e5'),
        borderPadding=5
    )
    
    # Custom style for contact information - centered and readable
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_CENTER,
        spaceAfter=20
    )
    
    # Custom style for job titles and project names - bold and prominent
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=12,
        fontName='Helvetica-Bold',
        spaceAfter=6
    )
    
    # Custom style for company/institution names - distinguishable from job titles
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Helvetica-Bold',
        textColor=HexColor('#6b7280'),
        spaceAfter=4
    )
    
    # Custom style for dates - subtle but clear
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#9ca3af'),
        spaceAfter=8
    )
    
    # Custom style for bullet points - proper indentation and spacing
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=4,
        bulletIndent=10
    )
    
    # Story list to hold all content elements for PDF generation
    story = []
    
    # Header Section with Name and Contact Information
    story.append(Paragraph("ANURAG MISHRA", name_style))
    
    # Contact information with actual details and professional title
    contact_info = """
    <b>Data Scientist & ML Engineer | LLM Specialist</b><br/>
    📧 officiallyanurag1@gmail.com | 📱 +91-9911210461<br/>
    🔗 linkedin.com/in/anuragmishra02/ | 💻 github.com/OPanurag<br/>
    📍 California, US (Open to Global Opportunities)
    """
    story.append(Paragraph(contact_info, contact_style))
    
    # Professional Summary Section - Updated with actual experience and skills
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    summary_text = """
    Data Scientist and ML Engineer with hands-on experience developing and deploying scalable LLM-based 
    solutions & ML models in production environments. Skilled in designing sustainable ML pipelines, optimizing 
    model performance, & translating complex data into strategic insights. Adept with modern NLP frameworks, 
    cloud platforms (GCP) & MLOps best practices to drive data-driven decision-making & automation at scale.
    """
    story.append(Paragraph(summary_text, styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Technical Skills Section - Updated with actual technology stack
    story.append(Paragraph("TECHNICAL STACK AND SKILLS", section_style))
    
    # Create skills table for better organization with actual skills
    skills_data = [
        ['Programming Languages:', 'Python, R, Bash, Git, HTML'],
        ['Data Science:', 'Pandas, Scikit-Learn, Transformers, LLM, Flask, PyTorch, TensorFlow, MLOps'],
        ['Tools:', 'JIRA, Notion, Jupyter, Power BI, Tableau, Git, Docker, Kubernetes, NLTK, ZenML'],
        ['Cloud Platforms:', 'Google Cloud Platform (GCP), Amazon Web Services (AWS)'],
        ['Databases:', 'SQL, Milvus Vector DB'],
        ['Data Analytics:', 'Seaborn, Dask, Matplotlib, Plotly, Bokeh, SciPy, Spacy']
    ]
    
    # Configure skills table layout and styling
    skills_table = Table(skills_data, colWidths=[2*inch, 4.5*inch])
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Bold labels
        ('FONTSIZE', (0, 0), (-1, -1), 10),               # Consistent font size
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),              # Top alignment
        ('LEFTPADDING', (0, 0), (-1, -1), 0),             # No left padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),            # Right padding for spacing
        ('TOPPADDING', (0, 0), (-1, -1), 3),              # Top padding
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),           # Bottom padding
    ]))
    
    story.append(skills_table)
    story.append(Spacer(1, 12))
    
    # Professional Experience Section - Updated with actual work experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))
    
    # Current Position - Kounsel
    story.append(Paragraph("Graduate Data Scientist", job_title_style))
    story.append(Paragraph("Kounsel – https://kounsel.io | California, US", company_style))
    story.append(Paragraph("Oct 2024 – Present", date_style))
    
    # Kounsel experience details
    kounsel_details = [
        "Utilized GCP and specialized NLP libraries to scale and optimize the LLM development process",
        "Developing a Large Language Model (LLM) focused on medical benefits, especially in recipe and diet generation",
        "Extracting and structuring nutritional data from diverse sources to build a large-scale ingredient nutrition dataset",
        "Collaborated with medical professionals & researchers ensuring accuracy & relevance of dietary recommendations"
    ]
    
    # Add each detail as a bullet point
    for detail in kounsel_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 8))
    
    # Previous Position - Omdena
    story.append(Paragraph("Machine Learning Engineer – Intern", job_title_style))
    story.append(Paragraph("Omdena – https://www.omdena.com | California, US", company_style))
    story.append(Paragraph("Jul 2024 – Sep 2024", date_style))
    
    # Omdena experience details
    omdena_details = [
        "Worked on 'AudioShield' project to distinguish deepfake audio from original audio samples",
        "Utilized XGBoost to optimize audio threat detection, reducing false positives by 25%",
        "Enhanced audio classification model with a 20% accuracy improvement through feature engineering and tuning"
    ]
    
    # Add each detail as a bullet point
    for detail in omdena_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 12))
    
    # Hands-On Projects Section - Updated with actual projects
    story.append(Paragraph("HANDS-ON PROJECTS", section_style))
    
    # Project 1 - AudioShield
    story.append(Paragraph("AudioShield: Deepfake Audio Detection", job_title_style))
    story.append(Paragraph("Technologies: Python, XGBoost, Audio Processing, Hugging Face", company_style))
    story.append(Paragraph("Deployed: https://huggingface.co/spaces/savinshynu/audioshield-hugg", date_style))
    
    # AudioShield project details
    audioshield_details = [
        "Developed an audio classification model to detect deepfake audio, deployed on Hugging Face",
        "Deepfake audio classification model through feature engineering and model tuning",
        "Fine-tuned XGBoost for better threat detection with improved accuracy metrics"
    ]
    
    for detail in audioshield_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 8))
    
    # Project 2 - Singapore Energy Analysis
    story.append(Paragraph("Singapore: Recycled Energy Saved", job_title_style))
    story.append(Paragraph("Technologies: Python, Data Analytics, Visualization, Statistical Analysis", company_style))
    story.append(Paragraph("GitHub: https://github.com/OPanurag/Singapore_Recycled_Energy_Saved.git", date_style))
    
    # Singapore project details
    singapore_details = [
        "Analyzed 18+ years of recycling and waste data to quantify energy savings and trends",
        "Revealed energy savings of up to 500 GWh annually from five waste types, supporting sustainability decisions",
        "Recommended a strategy that could reduce landfill dependency by 30%"
    ]
    
    for detail in singapore_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 8))
    
    # Project 3 - AI Chatbot
    story.append(Paragraph("Generative AI Chat Bot", job_title_style))
    story.append(Paragraph("Technologies: Python, NLP, Generative AI, Web Integration", company_style))
    story.append(Paragraph("GitHub: https://github.com/OPanurag/AI_ChatBot_System", date_style))
    
    # Chatbot project details
    chatbot_details = [
        "Developed a chatbot using NLP that handles 1,000+ monthly interactions with environment-personalized responses",
        "Boosted engagement by 35% through personalization based on 5 environmental and historical data factors",
        "Integrated chatbot into web platforms for seamless deployment"
    ]
    
    for detail in chatbot_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 8))
    
    # Additional projects mention
    story.append(Paragraph("Additional Portfolio", job_title_style))
    story.append(Paragraph("12+ Projects covering AI Engineer, ML Engineer, Data Analyst & Data Scientist roles", bullet_style))
    
    story.append(Spacer(1, 12))
    
    # Education Section - Updated with actual education details
    story.append(Paragraph("EDUCATION", section_style))
    
    # Education details
    story.append(Paragraph("Bachelor's of Technology - Computer Science Engineering", job_title_style))
    story.append(Paragraph("Specialization in Artificial Intelligence and Machine Learning", job_title_style))
    story.append(Paragraph("Vellore Institute of Technology", company_style))
    story.append(Paragraph("Percentage: 83.5%", date_style))
    
    story.append(Spacer(1, 12))
    
    # Certifications and Training Section - Updated with actual certifications
    story.append(Paragraph("CERTIFICATIONS AND TRAININGS", section_style))
    
    # List of actual certifications
    certifications = [
        "<b>Data Science</b> – IBM",
        "<b>Python</b> – Google",
        "<b>Applied Machine Learning in Python</b> – University of Michigan",
        "<b>SQL</b> – Kaggle"
    ]
    
    # Add each certification as a bullet point
    for cert in certifications:
        story.append(Paragraph(f"• {cert}", bullet_style))
    
    # Footer with generation date and professional note
    story.append(Spacer(1, 20))
    footer_text = f"<i>Resume generated on {datetime.now().strftime('%B %d, %Y')} | Available for immediate opportunities globally</i>"
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        alignment=TA_CENTER,
        textColor=HexColor('#9ca3af')
    )
    story.append(Paragraph(footer_text, footer_style))
    
    # Build the PDF document with error handling
    try:
        doc.build(story)
        print(f"✅ Resume successfully generated: {filename}")
        print(f"📄 File size: {os.path.getsize(filename)} bytes")
        return True
    except Exception as e:
        print(f"❌ Error generating resume: {str(e)}")
        return False

def main():
    """
    Main function to execute resume generation
    Includes dependency checking and success reporting
    """
    print("🚀 Starting resume generation for Anurag Mishra...")
    print("📝 Creating professional PDF resume with actual experience and projects...")
    
    # Check if required ReportLab library is available
    try:
        from reportlab.lib.pagesizes import letter
        print("✅ ReportLab library found")
    except ImportError:
        print("❌ ReportLab library not found. Please install it using:")
        print("   pip install reportlab")
        return
    
    # Generate the resume with actual professional details
    success = create_resume()
    
    # Provide detailed feedback on generation results
    if success:
        print("\n🎉 Resume generation completed successfully!")
        print("📋 The resume includes:")
        print("   • Current professional summary as Data Scientist & ML Engineer")
        print("   • Actual work experience at Kounsel and Omdena")
        print("   • Real technical skills and technology stack")
        print("   • Deployed projects with GitHub and live demo links")
        print("   • VIT education details with actual percentage")
        print("   • Verified certifications from IBM, Google, University of Michigan, and Kaggle")
        print("\n💼 Ready to share with potential employers worldwide!")
        print("🌍 Updated with current California location and global availability!")
    else:
        print("\n❌ Resume generation failed. Please check the error messages above.")

# Execute the script when run directly
if __name__ == "__main__":
    main()