{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Manage school infrastructure, schedules, teachers, students, payments, grades, and reports',
    'description': """
        This module allows you to manage the entire infrastructure of a school including:
        - Classrooms
        - Courses
        - Cycles (Bimester, Trimester, etc.)
        - Schedules
        - Subjects
        - Parallels
        - Teacher assignments and loads
        - Student enrollments
        - Payment plans and payments
        - Necessary reports
        - Payment receipts for accounting
    """,
    'author': 'sw1',
    'website': 'http://www.yourwebsite.com',
    'category': 'Education',
    'depends': ['base', 'mail', 'hr','hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'security/school_management_groups.xml',
        'security/school_management_security.xml',
        'views/school_management_menus.xml',
        'views/school_infrastructure_views.xml',
        'views/school_schedule_views.xml',
        'views/teacher_management_views.xml',
        'views/student_management_views.xml',
        'views/payment_management_views.xml',
        'views/school_activity.xml',
        'views/activity_calendar_view.xml',
        'data/infrastructure/course_data.xml', 
        'data/infrastructure/classroom_data.xml', 
        'data/infrastructure/subject_data.xml',
        'data/infrastructure/cycle_data.xml',
        'data/students/tutor_data.xml', 
        'data/students/students_data.xml',
        'data/teachers/teachers_data.xml',   
        'data/teachers/teachingload_data.xml',  # Carga después de teachers_data.xml
        'data/infrastructure/schedule_data.xml',           
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
