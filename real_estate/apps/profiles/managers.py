from django.db import models


class AgentProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_agent=True)

class TopAgentProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(top_agent=True)