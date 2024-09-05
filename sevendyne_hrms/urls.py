from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from main import views as general_views
from sevendyne_hrms import settings
from main.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap



sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt/', general_views.robots_txt,name='robots_txt'),
    path('admin/', admin.site.urls),
    path('app/',include(('user.urls','user'),namespace='user')),
    path('',general_views.job_portal,name='job_portal'),
    path('app/hrms/dashboard/',general_views.hrms_dashboard,name='hrms_dashboard'),
    path('',include(('main.urls','main'),namespace='main')),
    path('app/hrms/',include(('hrms.urls','hrms'),namespace='hrms')),
    path('app/candidate/',include(('candidate.urls','candidate'),namespace='candidate')),
    path('app/employee/',include(('employee.urls','employee'),namespace='employee')),
    path('app/client/',include(('client.urls','client'),namespace='client')),
    path('app/job/',include(('job.urls','job'),namespace='job')),
    path('app/payroll/',include(('payroll.urls','payroll'),namespace='payroll')),
    # path('app/task-board/',include(('taskboard.urls','taskboard'),namespace='taskboard')),
    path('app/asset/',include(('asset.urls','asset'),namespace='asset'))
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add the custom 404 handler
handler404 = "main.views.custom_404"

# Add the custom 500 handler
handler500 = "main.views.custom_500"