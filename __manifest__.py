{
    'name': 'College ERP Custom Module',
    'version': '18.0.1.0.0',
    'category': 'Education',
    'sequence': 1,
    'summary': 'College Management System',
    'description': """
        College ERP Custom Module for managing:
        - Students
        - Courses
        - Faculty
        - Departments
        - Attendance
        - Examinations
        - Fees
        - Library
        - Hostel
        - Transport
    """,
    'author': 'College ERP Team',
    'website': 'https://www.college-erp.com',
    'images': ['static/description/logo1.webp'],
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/erp_view.xml',        'data/student_sequence.xml',

        'views/college_student_views_enhanced.xml',
        'views/college_course_views.xml',
        'views/college_faculty_views.xml',
        'views/college_department_views.xml',
        # 'data/ir_sequence_data.xml',  #If you have sequence data


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
