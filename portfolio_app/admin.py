from django.contrib import admin
from .models import Home, About, Skill, Project, ContactInfo, ContactMessage

class HomeAdmin(admin.ModelAdmin):
    list_display = ("name", "role","photo","resume") 
admin.site.register(Home,HomeAdmin)



class AboutAdmin(admin.ModelAdmin):
    list_display=("heading","content","skills_heading")
admin.site.register(About,AboutAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display=("name",)
admin.site.register(Skill,SkillAdmin)



class ProjectAdmin(admin.ModelAdmin):
    list_display=("title","description","image","link")
admin.site.register(Project,ProjectAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display=("address","phone","email")
admin.site.register(ContactInfo,ContactInfoAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=("name","email","subject","message","created_at")
admin.site.register(ContactMessage,ContactMessageAdmin)