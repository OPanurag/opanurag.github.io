#!/usr/bin/env python3
"""
Resume Generator Script for Anurag Mishra
This script generates a professional PDF resume using Python libraries.
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
    This function generates a comprehensive resume with all sections
    """
    
    # Define file path for the resume
    filename = "resume.pdf"
    
    # Create document with letter size and margins
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Define custom styles for different sections
    styles = getSampleStyleSheet()
    
    # Custom style for name/header
    name_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=HexColor('#4f46e5'),
        fontName='Helvetica-Bold'
    )
    
    # Custom style for section headers
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
    
    # Custom style for contact info
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_CENTER,
        spaceAfter=20
    )
    
    # Custom style for job titles
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=12,
        fontName='Helvetica-Bold',
        spaceAfter=6
    )
    
    # Custom style for company/institution names
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Helvetica-Bold',
        textColor=HexColor('#6b7280'),
        spaceAfter=4
    )
    
    # Custom style for dates
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#9ca3af'),
        spaceAfter=8
    )
    
    # Custom style for bullet points
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=4,
        bulletIndent=10
    )
    
    # Story list to hold all content
    story = []
    
    # Header Section with Name and Contact Information
    story.append(Paragraph("ANURAG MISHRA", name_style))
    
    contact_info = """
    <b>Data Science Graduate | Machine Learning Enthusiast</b><br/>
    📧 officiallyanurag1@gmail.com | 📱 +91 9911210461<br/>
    🔗 linkedin.com/in/anuragmishra02 | 💻 github.com/OPanurag<br/>
    📍 Gurgaon, Haryan, India
    """
    story.append(Paragraph(contact_info, contact_style))
    
    # Professional Summary Section
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    summary_text = """
    Recent Computer Science graduate from VIT with specialization in Data Science and Machine Learning. 
    Passionate about transforming complex data into actionable insights through statistical analysis, 
    predictive modeling, and data visualization. Proficient in Python, R, SQL, and modern ML frameworks 
    including TensorFlow and PyTorch. Seeking to leverage analytical skills and technical expertise 
    in a challenging data science role to drive business growth and innovation.
    """
    story.append(Paragraph(summary_text, styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Education Section
    story.append(Paragraph("EDUCATION", section_style))
    
    # Education details
    story.append(Paragraph("Bachelor of Technology in Computer Science & Engineering Specialisation in Artificial Intelligence and Machine Learning", job_title_style))
    story.append(Paragraph("Vellore Institute of Technology (VIT)", company_style))
    story.append(Paragraph("2021 - 2025 | Percentage: 83.5%", date_style))
    
    education_details = [
        "Specialized in Data Science and Machine Learning with focus on statistical analysis and LLM",
        "Relevant Coursework: Data Structures, Algorithms, Database Management, Machine Learning, Deep Learning, Big Data Analytics",
        "Final Year Project: Lane Detection System using Deep Learning",
        "Active member of Omdena Contributors Club, Data Science Club and participated in multiple technical workshops"
    ]
    
    for detail in education_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 12))
    
    # Technical Skills Section
    story.append(Paragraph("TECHNICAL SKILLS", section_style))
    
    # Create skills table for better organization
    skills_data = [
        ['Programming Languages:', 'Python, R, SQL, JavaScript, Java, C++'],
        ['Data Science Libraries:', 'Pandas, NumPy, Scikit-learn, TensorFlow, PyTorch, Keras'],
        ['Data Visualization:', 'Matplotlib, Seaborn, Plotly, Tableau, Power BI'],
        ['Databases:', 'MySQL, PostgreSQL, MongoDB, SQLite'],
        ['Cloud & Tools:', 'AWS, Google Cloud Platform, Docker, Git, Jupyter Notebook'],
        ['Machine Learning:', 'Supervised Learning, Unsupervised Learning, Deep Learning, NLP, Computer Vision'],
        ['Statistical Analysis:', 'Hypothesis Testing, Regression Analysis, Time Series Analysis, A/B Testing']
    ]
    
    skills_table = Table(skills_data, colWidths=[2*inch, 4.5*inch])
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    
    story.append(skills_table)
    story.append(Spacer(1, 12))
    
    # Projects Section
    story.append(Paragraph("KEY PROJECTS", section_style))
    
    # Project 1
    story.append(Paragraph("Customer Churn Prediction Model", job_title_style))
    story.append(Paragraph("Technologies: Python, Scikit-learn, XGBoost, Pandas, Matplotlib", company_style))
    story.append(Paragraph("Jan 2024 - Mar 2024", date_style))
    
    project1_details = [
        "Developed machine learning model to predict customer churn with 92% accuracy using ensemble methods",
        "Implemented feature engineering techniques and hyperparameter tuning for optimal performance",
        "Created comprehensive data visualization dashboard for stakeholder presentation",
        "Deployed model using Flask API with real-time prediction capabilities"
    ]
    
    for detail in project1_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 8))
    
    # Project 2
    story.append(Paragraph("Social Media Sentiment Analysis System", job_title_style))
    story.append(Paragraph("Technologies: Python, BERT, TensorFlow, Flask, BeautifulSoup", company_style))
    story.append(Paragraph("Sep 2023 - Dec 2023", date_style))
    
    project2_details = [
        "Built real-time sentiment analysis system for social media posts using BERT and LSTM models",
        "Implemented web scraping techniques to collect and preprocess social media data",
        "Achieved 89% accuracy in sentiment classification across multiple social platforms",
        "Developed RESTful API for integration with external applications"
    ]
    
    for detail in project2_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 8))
    
    # Project 3
    story.append(Paragraph("Medical Image Classification using Deep Learning", job_title_style))
    story.append(Paragraph("Technologies: Python, PyTorch, OpenCV, ResNet, CNN", company_style))
    story.append(Paragraph("May 2023 - Aug 2023", date_style))
    
    project3_details = [
        "Developed CNN-based system for medical image classification with 95% accuracy",
        "Implemented transfer learning using ResNet50 architecture for improved performance",
        "Applied data augmentation techniques to enhance model robustness",
        "Created user-friendly interface for medical professionals to upload and analyze images"
    ]
    
    for detail in project3_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 12))
    
    # Experience Section
    story.append(Paragraph("EXPERIENCE", section_style))
    
    # Internship Experience
    story.append(Paragraph("Data Analytics Intern", job_title_style))
    story.append(Paragraph("Tech Startup (Remote)", company_style))
    story.append(Paragraph("Jun 2023 - Aug 2023", date_style))
    
    internship_details = [
        "Analyzed customer behavior patterns and market segmentation using statistical methods",
        "Developed automated ETL pipelines processing 50GB+ of customer data daily",
        "Created interactive dashboards for stakeholder reporting using Plotly and Streamlit",
        "Contributed to data-driven decision making that improved customer retention by 15%",
        "Collaborated with cross-functional teams in agile development environment"
    ]
    
    for detail in internship_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 8))
    
    # Research Experience
    story.append(Paragraph("Data Science Research Assistant", job_title_style))
    story.append(Paragraph("VIT University", company_style))
    story.append(Paragraph("Jan 2024 - May 2024", date_style))
    
    research_details = [
        "Led team of 4 students in developing ML solution for predicting academic performance",
        "Analyzed dataset of 10,000+ student records using advanced statistical techniques",
        "Implemented and compared 5 different machine learning algorithms for optimal results",
        "Presented research findings at university symposium and documented methodology in research paper"
    ]
    
    for detail in research_details:
        story.append(Paragraph(f"• {detail}", bullet_style))
    
    story.append(Spacer(1, 12))
    
    # Achievements Section
    story.append(Paragraph("ACHIEVEMENTS & CERTIFICATIONS", section_style))
    
    achievements = [
        "<b>2nd Place Winner</b> - National Data Science Hackathon (200+ participants) - Developed fraud detection system",
        "<b>Google Data Analytics Professional Certificate</b> - Completed comprehensive data analytics program",
        "<b>Deep Learning Specialization</b> - Coursera (Andrew Ng) - 5-course specialization completed",
        "<b>AWS Machine Learning Specialty</b> - Currently pursuing cloud ML certification",
        "<b>Kaggle Competitions</b> - Participated in 10+ competitions with top 25% rankings",
        "<b>Technical Publications</b> - Co-authored 2 research papers on machine learning applications"
    ]
    
    for achievement in achievements:
        story.append(Paragraph(f"• {achievement}", bullet_style))
    
    story.append(Spacer(1, 12))
    
    # Additional Information Section
    story.append(Paragraph("ADDITIONAL INFORMATION", section_style))
    
    additional_info = [
        "<b>Languages:</b> English (Fluent), Hindi (Native), Tamil (Conversational)",
        "<b>Interests:</b> Machine Learning Research, Data Visualization, Open Source Contributions",
        "<b>Volunteer Work:</b> Data Science Mentor for junior students, Technical Workshop Organizer",
        "<b>Availability:</b> Immediately available for full-time positions globally",
        "<b>Work Authorization:</b> Indian citizen, open to relocation and visa sponsorship"
    ]
    
    for info in additional_info:
        story.append(Paragraph(f"• {info}", bullet_style))
    
    # Footer with generation date
    story.append(Spacer(1, 20))
    footer_text = f"<i>Resume generated on {datetime.now().strftime('%B %d, %Y')}</i>"
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        alignment=TA_CENTER,
        textColor=HexColor('#9ca3af')
    )
    story.append(Paragraph(footer_text, footer_style))
    
    # Build the PDF document
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
    """
    print("🚀 Starting resume generation for Anurag Mishra...")
    print("📝 Creating professional PDF resume...")
    
    # Check if required library is available
    try:
        from reportlab.lib.pagesizes import letter
        print("✅ ReportLab library found")
    except ImportError:
        print("❌ ReportLab library not found. Please install it using:")
        print("   pip install reportlab")
        return
    
    # Generate the resume
    success = create_resume()
    
    if success:
        print("\n🎉 Resume generation completed successfully!")
        print("📋 The resume includes:")
        print("   • Professional summary and contact information")
        print("   • Educational background from VIT")
        print("   • Comprehensive technical skills")
        print("   • Detailed project descriptions with technologies")
        print("   • Work experience and internships")
        print("   • Achievements and certifications")
        print("   • Additional information for recruiters")
        print("\n💼 Ready to share with potential employers worldwide!")
    else:
        print("\n❌ Resume generation failed. Please check the error messages above.")

if __name__ == "__main__":
    main()