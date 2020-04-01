from django.contrib import admin
from .models import institute_information
from .models import course_detail
from .models import faculty_detail
from .models import Images
from .models import Inst_review
from .models import institute_result
from .models import rating_detail


admin.site.site_header='Learncess Admin Dashboard'
admin.site.site_title='Admin|Learncess'

admin.site.register(institute_information)
admin.site.register(course_detail)
admin.site.register(Images)
admin.site.register(Inst_review)
admin.site.register(faculty_detail)
admin.site.register(institute_result)
admin.site.register(rating_detail)
